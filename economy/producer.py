from basics import *


#following class represents an entity with rational production and an unlimited budget
#possible inheritance structure with Consumer from some base class
#IMPLEMENT A CHANGING PRICE SYSTEM
#IMPLEMENT MULTIPLE TRADEABLES AS WELL
class Producer:

    def __init__(self, name, factor_list, tradeable, p_function, factor_p_dict): #factors of production are Tradeables
        #argument name expected to be of class str
        #argument factor_list expected to be list of Tradeable
        #argument tradeable is the Tradeable the Producer is selling
        #argument p_function is the amount a Producer may produce, given certain factors of production
        #factor_p_dict links factors to Sympy symbols in p_function

        self.name = name
        self.factor_list = factor_list
        self.tradeable = tradeable
        self.p_function = p_function
        self.factor_p_dict = factor_p_dict
        self.decision = collections.Counter()
        self.strat_list = []
        self.payoff_mat = []

    def find_mp(self, added_factor = None, subtracted_factor = None):

        #following code creates a new list of factor amounts to substitute into the p_function
        #with added_factor incremented and subtracted_factor decremented
        #CONSIDER INTEGRATING get_total_production FOR CONCISENESS
        old_subs_list = []
        new_subs_list = []
        for factor in self.factor_list:
            var = self.factor_p_dict[factor]
            current_level = self.decision[factor]
            old_subs_list.append([var, current_level])
            if factor == added_factor:
                new_subs_list.append([var, current_level + 1])
            elif factor == subtracted_factor:
                new_subs_list.append([var, current_level - 1])
            else:
                new_subs_list.append([var, current_level])
        #end

        return float(self.p_function.subs(new_subs_list) - self.p_function.subs(old_subs_list))

    def get_total_production(self):

        #following code creates a list (effetively a dict) that links each Tradeable with
        #how much it is being bought, to substitute into the p_function
        #CONSIDER JUST USING A COMPREHENSION
        subs_list = []
        for factor in self.factor_list:
            var = self.factor_p_dict[factor]
            current_level = self.decision[factor]
            subs_list.append([var, current_level])
        #end

        return float(self.p_function.subs(subs_list))

    def get_total_spending(self):

        return sum([factor.cost*self.decision[factor] for factor in self.factor_list])

    def find_increment_payoff(self, factor, demand):
        
        profit = self.find_mp(factor)*self.tradeable.cost - factor.cost #profict from increasing factor
        return profit

    def find_decrement_payoff(self, factor, demand):
        
        if self.decision[factor] == 0:
            return ILLEGAL

        loss = self.find_mp(subtracted_factor = factor)*self.tradeable.cost + factor.cost
        return loss

    def find_interchange_payoff(self, factor, other_factor, demand):
        
        if self.decision[factor] == 0:
            return ILLEGAL
        
        loss = self.find_mp(subtracted_factor = factor)*self.tradeable.cost + factor.cost #loss from decreasing factor
        profit = self.find_mp(other_factor)*self.tradeable.cost - other_factor.cost #profict from increasing other_factor
        return profit + loss

    def update_game_lists(self, factor_list, demand = None):

        #following code makes a list (payoff_mat) of payoffs with a one-to-one correspondence with strat_list, to link
        #each Strat to its payoff (games are one player, so even if payoff_mat is a matrix, each strategy only has
        #one payoff)

        if demand == None:
            demand = INFINITY    #assume infinite demand
        
        strat_list = []
        payoff_mat = []
        
        for factor in factor_list:

            strat_list.append(Strat(INCREMENT + factor.name))
            payoff_mat.append([self.find_increment_payoff(factor, demand)])

            decrement_payoff = self.find_decrement_payoff(factor, demand)
            if decrement_payoff != ILLEGAL:
                strat_list.append(Strat(DECREMENT + factor.name))
                payoff_mat.append([decrement_payoff])
            
            for other_factor in factor_list:
                if other_factor == factor:
                    continue
                interchange_payoff = self.find_interchange_payoff(factor, other_factor, demand)
                if interchange_payoff != ILLEGAL:
                    strat_list.append(Strat(factor.name + INTERCHANGE + other_factor.name))  #change factor out for other_factor
                    payoff_mat.append([interchange_payoff])  
        #end

        strat_list.append(Strat(INACTIVE))
        payoff_mat.append([0])
        self.strat_list = strat_list
        self.payoff_mat = payoff_mat

    def make_strat_factor_dict(self, factor_list):

        return {factor.name: factor for factor in factor_list}

    def change_decision(self, factor_list, demand = None):

        strat_factor_dict = self.make_strat_factor_dict(factor_list)
        self.update_game_lists(factor_list, demand)

        #print(self.strat_list)
        #print(self.payoff_mat)

        #following code creates game from strat_list and payoff_mat, and retrieves ne
        decision_tree = Tree_Single([self.name], self.strat_list, self.payoff_mat)
        ne = decision_tree.ne_list[0]    #eventually, find a way to consider all nash equilibria
        #end

        #following code evaluates ne of game and acts accordingly
        if INCREMENT in ne.name:
            self.decision[strat_factor_dict[ne.name[2:]]] += 1  
        elif DECREMENT in ne.name:
            self.decision[strat_factor_dict[ne.name[2:]]] -= 1 
        elif INTERCHANGE in ne.name:
            interchange_list = ne.name.split(INTERCHANGE)
            self.decision[strat_factor_dict[interchange_list[0]]] -= 1
            self.decision[strat_factor_dict[interchange_list[1]]] += 1
        #end

        print(self.decision)
        #print()
