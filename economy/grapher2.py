import plotly.plotly as py
from plotly.graph_objs import *
from market import *


#xylo yacht consumer graphing, this time 2D
#let x be the number of xylos bought by the consumer
#let y be the number of yachts bought by the consumer
#let z be the number of iterations
"""
tracex_list = []
trace0y_list = []
trace1y_list = []

x, y = symbols("x y")
xylo = Tradeable("xylo", 1)
yacht = Tradeable("yacht", 2)
u = Consumer("u", 120, [xylo, yacht], (x**2)*(y**3),
             {xylo: x, yacht: y})
for x in range(100):
    trace0y_list.append(u.decision[xylo])
    trace1y_list.append(u.decision[yacht])
    tracex_list.append(x)
    u.change_decision([xylo, yacht])

trace0 = Scatter(x = tracex_list, y = trace0y_list)
trace1 = Scatter(x = tracex_list, y = trace1y_list)
classical0 = Scatter(x = [0,99], y = [48, 48])
classical1 = Scatter(x = [0,99], y = [36, 36])

data = [trace0, trace1, classical0, classical1]
py.iplot(data, filename = '2d_xylo_yact_consumer_graph')
"""

#super producer graphing, this time 2D
#let c be the number of capital bought by the producer
#let l be the number of labor bought by the producer
#let z be the number of iterations
"""
tracex_list = []
trace0y_list = []
trace1y_list = []

super_good = Tradeable("super good", 9)
capital = Tradeable("capital", 20)
labor = Tradeable("labor", 5)
c, l = symbols("c l")
graph_producer = Producer("graph producer", [capital, labor], super_good, 5*sqrt(c)*sqrt(l), {capital: c, labor: l})
graph_producer.decision[capital] += 1
graph_producer.decision[labor] += 1

for x in range(80):
    trace0y_list.append(graph_producer.decision[capital])
    trace1y_list.append(graph_producer.decision[labor])
    tracex_list.append(x)
    graph_producer.change_decision([capital, labor], 177)


trace0 = Scatter(x = tracex_list, y = trace0y_list)
trace1 = Scatter(x = tracex_list, y = trace1y_list)
classical0 = Scatter(x = [0,79], y = [25, 25])
classical1 = Scatter(x = [0,79], y = [50, 50])


data = [trace0, trace1, classical0, classical1]
py.iplot(data, filename = '2D_graph_producer_graph')
"""


#2d economy graphing
total_supply_list = []
total_demand_list = []
price_level_list = []

g1 = Symbol('g1')
g2 = Symbol('g2')
f1 = Symbol('f1')
for a in range(1,16):
    price_level_list.append(a)
    good1 = Tradeable("good1", a)
    good2 = Tradeable("good2", a)
    factor1 = Tradeable("factor1", 1)
    producer1 = Producer("graph_producer1", [factor1], good1, sqrt(f1), {factor1: f1})
    producer2 = Producer("graph_producer2", [factor1], good2, sqrt(f1), {factor1: f1})
    consumer1 = Consumer("graph_consumer1", 100, [good1, good2], g1 + g2, {good1: g1, good2: g2})
    consumer2 = Consumer("graph_consumer2", 100, [good1, good2], g1 + g2, {good1: g1, good2: g2})
    market = Market("graph_market1", [producer1, producer2], [consumer1, consumer2])
    for x in range(200):
        market.change_decision()
    total_supply_list.append(sum([producer.get_total_production() for producer in market.producer_list]))
    total_demand_list.append(sum([sum(consumer.decision.values()) for consumer in market.consumer_list]))

trace0 = Scatter(x = price_level_list, y = total_supply_list)
trace1 = Scatter(x = price_level_list, y = total_demand_list)
classical0 = Scatter(x = [1,15], y = [1, 15])
classical1 = Scatter(x = [x/10 + 1 for x in range(1,150)], y = [200/(x/10 + 1) for x in range(1,150)])

data = [trace0, trace1, classical0, classical1]
py.iplot(data, filename = '2D_sample_market_graph')
