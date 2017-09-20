from market import *

"""
x, y = symbols("x y")
xylo = Tradeable("xylo", 1)
yacht = Tradeable("yacht", 2)
consumer1 = Consumer("consumer1", 20, [xylo, yacht], (x**2 + 1)*(y**3 + 1),
                    {xylo: x, yacht: y})

#for x in range(20):
#    consumer1.change_decision([xylo, yacht])
#print(consumer1.get_total_utility())


capital = Tradeable("capital", 100)
labor = Tradeable("labor", 0.2)
c, l = symbols("c l")

producer1 = Producer("producer1", [labor], xylo, -l*(l - 8), {capital: c, labor: l})


#for x in range(10):
#    print("production", producer1.get_total_production())
#    producer1.change_decision([labor],100)


print("SECOND PRODUCER")

producer2 = Producer("producer2", [labor], yacht, -l*(l - 8), {capital: c, labor: l})


#for x in range(10):
#    print("production", producer2.get_total_production())
#    producer2.change_decision([labor],100)


p_list = [producer1, producer2]
c_list = [consumer1]

print("yacht and xylo market testing")
m = Market("yacht and xylo market", p_list, c_list)
print(m.strat_mat)
print(m.payoff_mat)

for x in range(20):
    m.change_decision()



a = Symbol('a')
apple = Tradeable("apple", 2)
test_consumer = Consumer("test_consumer", 20, [apple], a, {apple: a})

l = Symbol('l')
labor = Tradeable("labor", 1)
test_producer = Producer("test_producer", [labor], apple, 0.1*(-l*(l - 16)), {labor: l})

m = Market("apple market", [test_producer], [test_consumer])
print(m.strat_mat)
print(m.payoff_mat)
for x in range(20):
    m.change_decision()

"""
"""
id_list = list(range(0, 4))

consumer_symbol_list = [Symbol('f' + str(i)) for i in id_list]
tradeable_list = [Tradeable("fish" + str(i), 1) for i in id_list]
u_function = sum(consumer_symbol_list)
trade_u_dict = {tradeable: consumer_symbol for tradeable, consumer_symbol in zip(tradeable_list, consumer_symbol_list)}
consumer_list = [Consumer("consumer" + str(i), i + 1, tradeable_list, u_function, trade_u_dict) for i in id_list]

l = Symbol('l')
labor = Tradeable('l', 1)
producer_list = [Producer("producer" + str(i), [labor], tradeable_list[i], l, {labor: l}) for i in id_list]

fish_market = Market("fish market", producer_list, consumer_list)
fish_market.change_decision()
"""
"""
g_good1 = Tradeable("graph_good1", 10*sqrt(2))
g_good2 = Tradeable("graph_good2", 10*sqrt(2))
g1 = Symbol('g1')
g2 = Symbol('g2')

g_factor1 = Tradeable("graph_factor1", 1)
f1 = Symbol('f1')

g_producer1 = Producer("graph_producer1", [g_factor1], g_good1, sqrt(f1), {g_factor1: f1})
g_producer2 = Producer("graph_producer2", [g_factor1], g_good2, sqrt(f1), {g_factor1: f1})

g_consumer1 = Consumer("graph_consumer1", 100, [g_good1, g_good2], g1 + g2, {g_good1: g1, g_good2: g2})
g_consumer2 = Consumer("graph_consumer2", 100, [g_good1, g_good2], g1 + g2, {g_good1: g1, g_good2: g2})

g_market1 = Market("graph_market1", [g_producer1, g_producer2], [g_consumer1, g_consumer2])

for x in range(65):
    print("total production", sum([producer.get_total_production() for producer in g_market1.producer_list]))
    print("supply list", g_market1.supply_list)
    print("demand list", g_market1.demand_list)
    g_market1.change_decision()
    
"""
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

