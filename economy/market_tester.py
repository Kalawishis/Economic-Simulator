from market import *
from random import *

#market testing testing
#consumer demand = 2i/g
#producer supply = sqrt(g^2/l^2)

g1 = Symbol('g1')
g2 = Symbol('g2')
f1 = Symbol('f1')
a=8
good1 = Tradeable("good1", a)
good2 = Tradeable("good2", a)
factor1 = Tradeable("factor1", 1)
producer1 = Producer("graph_producer1", [factor1], good1, sqrt(f1), {factor1: f1})
producer2 = Producer("graph_producer2", [factor1], good2, sqrt(f1), {factor1: f1})
consumer1 = Consumer("graph_consumer1", 100, [good1, good2], g1 + g2, {good1: g1, good2: g2})
consumer2 = Consumer("graph_consumer2", 100, [good1, good2], g1 + g2, {good1: g1, good2: g2})
market = Market("graph_market1", [producer1, producer2], [consumer1, consumer2])
for x in range(50):
    market.change_decision()

#for each arg:
#arg[0] = g
#arg[1] = f1
#arg[2] = i

classical_list = []
simulator_list = []

for x in range(100):
    
    g = uniform(1, 20)
    f = uniform(1, 5)
    i = uniform(50, 150)

    classical_demand = 2*i/g
    classical_supply = float(sqrt(g**2/f**2))
    
    g1 = Symbol('g1')
    g2 = Symbol('g2')
    f1 = Symbol('f1')
    good1 = Tradeable("good1", g)
    good2 = Tradeable("good2", g)
    factor1 = Tradeable("factor1", f)
    producer1 = Producer("graph_producer1", [factor1], good1, sqrt(f1), {factor1: f1})
    producer2 = Producer("graph_producer2", [factor1], good2, sqrt(f1), {factor1: f1})
    consumer1 = Consumer("graph_consumer1", i, [good1, good2], g1 + g2, {good1: g1, good2: g2})
    consumer2 = Consumer("graph_consumer2", i, [good1, good2], g1 + g2, {good1: g1, good2: g2})
    market = Market("graph_market1", [producer1, producer2], [consumer1, consumer2])
    for x in range(200):
        market.change_decision()
    
    print("classical", classical_supply, classical_demand)
    print("simulation",
          sum([producer.get_total_production() for producer in market.producer_list]),
          sum([sum(consumer.decision.values()) for consumer in market.consumer_list]))
    classical_list.append([classical_supply, classical_demand])
    simulator_list.append([sum([producer.get_total_production() for producer in market.producer_list]),
                           sum([sum(consumer.decision.values()) for consumer in market.consumer_list])])
    print()














    
#"""
