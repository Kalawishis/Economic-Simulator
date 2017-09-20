#module to model interactions between consumers and producers in a buyer/seller way

from producer import *
from consumer import *

class Market():

    def __init__(self, name, producer_list, consumer_list):
        #all producers must sell the same Tradeable, the argument tradeable
        #all consumer in consumer_list must have the exact same tradeable_list

        self.name = name
        self.producer_list = producer_list
        self.consumer_list = consumer_list
        self.player_list = producer_list[:]
        self.player_list.extend(consumer_list)  #producers first, then consumers
        self.consumer_option_list = [producer.tradeable for producer in producer_list]  #same tradeable, different prices
        self.supply_list = self.make_supply_list()
        self.demand_list = self.make_demand_list()
        self.strat_mat = []
        self.payoff_mat = []

    """
    def get_supply(self, tradeable):

        return sum([producer.get_total_production() for producer in self.producer_list])

    def get_demand(self, tradeable):

        return sum([sum(consumer.decision) for consumer in self.consumer_list])
    """

    def make_supply_list(self):

        return [producer.get_total_production() for producer in self.producer_list]

    def make_demand_list(self):

        demand_list = [0]*len(self.producer_list)
        for consumer in self.consumer_list:
            for tradeable_enum in enumerate(consumer.tradeable_list):
                demand_list[tradeable_enum[0]] += consumer.decision[tradeable_enum[1]]
                
        return demand_list

    """
    def make_strat_mat(self):   #All producers first, then consumers

        for producer in self.producer_list:
            producer
        for consumer in self.consumer_list:
            
        strat_mat = [producer.make_strat_list(producer.factor_list) for producer in self.producer_list]   #etc.
        strat_mat.extend([consumer.make_strat_list(self.consumer_option_list) for consumer in self.consumer_list])
        return strat_mat
    """
 
    #after you get this function to work, optimize it
    def update_game_lists(self):

        #print("CURRENT_SUPPLY_LIST", self.supply_list)
        #print("CURRENT_DEMAND_LIST", self.demand_list)
        for producer_enum in enumerate(self.producer_list):
            producer_enum[1].update_game_lists(producer_enum[1].factor_list)
        for consumer in self.consumer_list:
            consumer.update_game_lists(self.consumer_option_list)
        strat_mat = [producer.strat_list for producer in self.producer_list]   #etc.
        strat_mat.extend([consumer.strat_list for consumer in self.consumer_list])
        self.strat_mat = strat_mat
        payoff_mat = []
        strats_combined_list = combine(strat_mat)
        
        #for each strategy combination in the list of strategy combinations
        for strats_combined in strats_combined_list:
            payoff_list = []
            new_supply_list = self.supply_list[:]
            individual_supply_mat = []
            new_demand_list = self.demand_list[:]

            #for each strat in strats_combined
            for strat_enum in enumerate(strats_combined):
                strat_index = strat_enum[0]
                strat = strat_enum[1]
                if strat_index < len(self.producer_list):  #if going through producer strats
    
                    producer = self.producer_list[strat_index]
                    strat_factor_dict = producer.make_strat_factor_dict(producer.factor_list)
                    
                    if INCREMENT in strat.name:
                        changed_factor = strat_factor_dict[strat.name[2:]]
                        marginal_production = producer.find_mp(changed_factor)
                        new_supply_list[strat_index] += marginal_production  #strat index = producer index 
                    elif DECREMENT in strat.name:
                        changed_factor = strat_factor_dict[strat.name[2:]]
                        marginal_production = producer.find_mp(subtracted_factor = changed_factor)
                        new_supply_list[strat_index] += marginal_production  #strat index = producer index 
                    elif INTERCHANGE in strat.name:
                        interchange_list = strat.name.split(INTERCHANGE)
                        subtracted_factor = strat_factor_dict[interchange_list[0]]
                        added_factor = strat_factor_dict[interchange_list[1]]
                        marginal_production = producer.find_mp(added_factor, subtracted_factor)
                        new_supply_list[strat_index] += marginal_production  #strat index = producer index
                   
                else:   #if going through consumer strats
        
                    consumer = self.consumer_list[strat_index - len(self.producer_list)]
                    strat_tradeable_dict = consumer.make_strat_tradeable_dict(self.consumer_option_list)  #same for all consumers
                    
                    if INCREMENT in strat.name:
                        changed_tradeable = strat_tradeable_dict[strat.name[2:]]
                        changed_tradeable_index = consumer.tradeable_list.index(changed_tradeable)
                        new_demand_list[changed_tradeable_index] += 1
                    elif DECREMENT in strat.name:
                        changed_tradeable = strat_tradeable_dict[strat.name[2:]]
                        changed_tradeable_index = consumer.tradeable_list.index(changed_tradeable)
                        new_demand_list[changed_tradeable_index] -= 1
                    elif INTERCHANGE in strat.name:
                        interchange_list = strat.name.split(INTERCHANGE)
                        subtracted_tradeable = strat_tradeable_dict[interchange_list[0]]
                        added_tradeable = strat_tradeable_dict[interchange_list[1]]
                        new_demand_list[consumer.tradeable_list.index(subtracted_tradeable)] -= 1
                        new_demand_list[consumer.tradeable_list.index(added_tradeable)] += 1
                        
            #end for each strat in strats_combined

            #print("NEW_SUPPLY_LIST", new_supply_list)
            #print("NEW_DEMAND_LIST", new_demand_list)
            

            for producer_enum in enumerate(self.producer_list):
                producer = producer_enum[1]
                producer_strat = strats_combined[producer_enum[0]]
                strat_factor_dict = producer.make_strat_factor_dict(producer.factor_list)
                demand = new_demand_list[producer_enum[0]]                

                if INCREMENT in producer_strat.name:
                    factor = strat_factor_dict[producer_strat.name[2:]]
                    payoff_list.append(producer.find_increment_payoff(factor, demand))
                    
                elif DECREMENT in producer_strat.name:
                    factor = strat_factor_dict[producer_strat.name[2:]]
                    payoff_list.append(producer.find_decrement_payoff(factor, demand))
                    
                elif INTERCHANGE in producer_strat.name:
                    interchange_list = producer_strat.name.split(INTERCHANGE)
                    factor = strat_factor_dict[interchange_list[0]]
                    other_factor = strat_factor_dict[interchange_list[1]]
                    payoff_list.append(producer.find_interchange_payoff(factor, other_factor, demand))

                else:   #strategy is most probably a do nothing strategy
                    payoff_list.append(0)

            for consumer_enum in enumerate(self.consumer_list):
                consumer = consumer_enum[1]
                consumer_strat = strats_combined[consumer_enum[0] + len(self.producer_list)]
                strat_tradeable_dict = consumer.make_strat_tradeable_dict(consumer.tradeable_list)

                if INCREMENT in consumer_strat.name:
                    tradeable = strat_tradeable_dict[consumer_strat.name[2:]]
                    payoff_list.append(consumer.find_increment_payoff(tradeable, new_supply_list))
                    
                elif DECREMENT in consumer_strat.name:
                    tradeable = strat_tradeable_dict[consumer_strat.name[2:]]
                    payoff_list.append(consumer.find_mu(subtracted_tradeable = tradeable)/tradeable.cost)
                    
                elif INTERCHANGE in consumer_strat.name:
                    interchange_list = consumer_strat.name.split(INTERCHANGE)
                    tradeable = strat_tradeable_dict[interchange_list[0]]
                    other_tradeable = strat_tradeable_dict[interchange_list[1]]   
                    payoff_list.append(consumer.find_interchange_payoff(tradeable, other_tradeable, new_supply_list))

                elif consumer.get_total_spending() <= consumer.budget:   #strategy is most probably a do nothing strategy
                    payoff_list.append(0)
                                       
            payoff_mat.append(payoff_list)
        #end for each strategy combination in the list of strategy combinations
        
        self.payoff_mat = payoff_mat
    
    def change_decision(self):

        matrix_player_list = [player.name for player in self.player_list]
        self.update_game_lists()

        #print(self.strat_mat)
        #print(self.payoff_mat)

        #for x in zip(combine(self.strat_mat), self.payoff_mat):
            #print(x)
        
        decision_matrix = Matrix_Single(matrix_player_list, self.strat_mat, self.payoff_mat, calculate_mixed_ne = False)
        ne = decision_matrix.pure_ne_list[0]    #eventually, find a way to consider all nash equilibria (including mixed ones)


        #print("NE list", decision_matrix.pure_ne_list)
        #print("NE chosen", ne)
        #print("NE index", combine(self.strat_mat).index(ne))
        

        for strat_enum in enumerate(ne):
            strat = strat_enum[1]
            player = self.player_list[strat_enum[0]]
            
            if strat_enum[0] < len(self.producer_list):  #if current player is a producer
                strat_dict = player.make_strat_factor_dict(player.factor_list)
            else:   #if current player is a consumer
                strat_dict = player.make_strat_tradeable_dict(player.tradeable_list)
                
            if INCREMENT in strat.name:
                player.decision[strat_dict[strat.name[2:]]] += 1
            elif DECREMENT in strat.name:
                player.decision[strat_dict[strat.name[2:]]] -= 1 
            elif INTERCHANGE in strat.name:
                interchange_list = strat.name.split(INTERCHANGE)
                player.decision[strat_dict[interchange_list[0]]] -= 1
                player.decision[strat_dict[interchange_list[1]]] += 1

        #for player in self.player_list:
            #print(player.decision)
        #print()

        self.supply_list = self.make_supply_list()
        self.demand_list = self.make_demand_list()
