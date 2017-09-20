from basics import *

#following class represents an entity with rational preferences and a fixed budget
class Consumer:

    def __init__(self, name, budget, tradeable_list, u_function, trade_u_dict):
        #argument name expected to be of type str
        #argument budget expected to be of type int or float
        #argument tradeable_list expected to be a list of Tradeable
        #argument u_function expected to be Sympy expression, representing utility
        #argument trade_u_dict expected to be a dict of the form {Tradeable: Sympy symbol}
        #with the same len as tradeable_list
        
        self.name = name
        self.budget = budget
        self.tradeable_list = tradeable_list
        self.u_function = u_function
        self.trade_u_dict = trade_u_dict
        self.decision = collections.Counter()
        self.strat_list = []
        self.payoff_mat = []

    def find_mu(self, added_tradeable = None, subtracted_tradeable = None):

        #following code creates a new list of variables to substitute into the u_function
        #with added_tradeable incremented and subtracted_tradeble decremented
        #CONSIDER INTEGRATING get_total_utility FOR CONCISENESS
        old_subs_list = []
        new_subs_list = []
        for tradeable in self.tradeable_list:
            var = self.trade_u_dict[tradeable]
            current_level = self.decision[tradeable]
            old_subs_list.append([var, current_level])
            if tradeable == added_tradeable:
                new_subs_list.append([var, current_level + 1])
            elif tradeable == subtracted_tradeable:
                new_subs_list.append([var, current_level - 1])
            else:
                new_subs_list.append([var, current_level])
        #end

        return float(self.u_function.subs(new_subs_list) - self.u_function.subs(old_subs_list))

    def get_total_utility(self):

        #following code creates a list (effetively a dict) that links each Tradeable with
        #how much it is being bought, to substitute into the u_function
        #CONSIDER JUST USING A COMPREHENSION
        subs_list = []
        for tradeable in self.tradeable_list:
            var = self.trade_u_dict[tradeable]
            current_level = self.decision[tradeable]
            subs_list.append([var, current_level])
        #end

        return float(self.u_function.subs(subs_list))

    def get_total_spending(self):

        return sum([tradeable.cost*self.decision[tradeable] for tradeable in self.tradeable_list])

    def find_increment_payoff(self, tradeable, supply_list):
        
        if self.get_total_spending() + tradeable.cost > self.budget:
            return ILLEGAL
        return self.find_mu(tradeable)/tradeable.cost

    def find_decrement_payoff(self, tradeable, supply_list):

        if self.decision[tradeable] == 0:
            return ILLEGAL
        return self.find_mu(subtracted_tradeable = tradeable)/tradeable.cost

    def find_interchange_payoff(self, tradeable, other_tradeable, supply_list):

        if self.decision[tradeable] == 0 or \
           self.get_total_spending() + other_tradeable.cost - tradeable.cost > self.budget:
            return ILLEGAL
        return self.find_mu(other_tradeable)/other_tradeable.cost - self.find_mu(tradeable)

    def update_game_lists(self, tradeable_list, supply_list = None):

        #following code makes a list (payoff_mat) of payoffs with a one-to-one correspondence with strat_list, to link
        #each Strat to its payoff (games are one player, so even if payoff_mat is a matrix, each strategy only has
        #one payoff)

        if not supply_list:
            supply_list = [INFINITY]*len(tradeable_list)    #assume infinite supply
        
        strat_list = []
        payoff_mat = []
        for tradeable in tradeable_list:
            
            increment_payoff = self.find_increment_payoff(tradeable, supply_list)
            if increment_payoff != ILLEGAL:
                strat_list.append(Strat(INCREMENT + tradeable.name))
                payoff_mat.append([increment_payoff])

            decrement_payoff = self.find_decrement_payoff(tradeable, supply_list)
            if decrement_payoff != ILLEGAL:
                strat_list.append(Strat(DECREMENT + tradeable.name))
                payoff_mat.append([decrement_payoff])
            
            for other_tradeable in tradeable_list:
                if other_tradeable == tradeable:
                    continue
                interchange_payoff = self.find_interchange_payoff(tradeable, other_tradeable, supply_list)
                if interchange_payoff != ILLEGAL:
                    payoff_mat.append([interchange_payoff])
                    strat_list.append(Strat(tradeable.name + INTERCHANGE + other_tradeable.name))  #change tradeable out for other_tradeable

        if self.get_total_spending() <= self.budget:    #if underbudget, Consumer has the luxury of doing nothing
            strat_list.append(Strat(INACTIVE))
            payoff_mat.append([0])
            
        self.strat_list = strat_list
        self.payoff_mat = payoff_mat

    def make_strat_tradeable_dict(self, tradeable_list):

        return {tradeable.name: tradeable for tradeable in tradeable_list}

    def change_decision(self, tradeable_list, supply_list = None):
            
        strat_tradeable_dict = self.make_strat_tradeable_dict(tradeable_list)
        self.update_game_lists(tradeable_list, supply_list)
        
        #print(self.strat_list)
        #print(self.payoff_mat)
        
        #following code creates a game from strat_list and payoff_mat
        decision_tree = Tree_Single([self.name], self.strat_list, self.payoff_mat)
        ne = decision_tree.ne_list[0]    #eventually, find a way to consider all nash equilibria
        #end

        #following code detects nash equilibrium and acts according to Consumer's best interest
        if INCREMENT in ne.name:
            self.decision[strat_tradeable_dict[ne.name[2:]]] += 1  
        elif DECREMENT in ne.name:
            self.decision[strat_tradeable_dict[ne.name[2:]]] -= 1 
        elif INTERCHANGE in ne.name:
            interchange_list = ne.name.split(INTERCHANGE)
            self.decision[strat_tradeable_dict[interchange_list[0]]] -= 1
            self.decision[strat_tradeable_dict[interchange_list[1]]] += 1
        #end

        print(self.decision)
        #print()
