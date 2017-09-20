from consumer import *
from producer import *
"""
print("TEST_1")
i, s = symbols("i s")
inferior = Tradeable("inferior", 1)
superior = Tradeable("superior", 1.5)
test = Consumer("test", 1.5, [inferior, superior], 5*i + 6*s, {inferior: i, superior: s})
for x in range(10):
    test.change_decision([inferior, superior])
print(test.get_total_utility())
print(test.decision)

print("TEST_2")
i, s = symbols("i s")
inferior = Tradeable("inferior", 2)
superior = Tradeable("superior", 1)
test = Consumer("test2", 2, [inferior, superior], 5*s + 6*i, {inferior: i, superior: s})
for x in range(10):
    test.change_decision([inferior, superior])
print(test.get_total_utility())
print(test.decision)

print("TEST_3")
g = symbols("g")
good = Tradeable("good", 1)
test = Consumer("test3", 5, [good], g, {good: g})
for x in range(10):
    test.change_decision([good], [0])
print(test.get_total_utility())
print(test.decision)

software = Tradeable("software", 4)
clothes = Tradeable("clothes", 3)
s, c = symbols("s c")
xiaoyu = Consumer("xiaoyu", 10, [software, clothes], 4*ln(s + EPSILON) + 6*ln(c + EPSILON),
                  {software: s, clothes: c})
for x in range(10):
    xiaoyu.change_decision([software, clothes])
print(xiaoyu.get_total_utility())
print(xiaoyu.decision)

necklace = Tradeable("necklace", 4)
bracelet = Tradeable("bracelet", 2)
n, b = symbols("n b")
mary = Consumer("mary", 32, [necklace, bracelet], 3*Min(n, (1/3)*b),
                {necklace: n, bracelet: b})
for x in range(40):
    mary.change_decision([necklace, bracelet])
print(mary.get_total_utility())
print(mary.decision)

necklace = Tradeable("necklace", 4)
bracelet = Tradeable("bracelet", 2)
n, b = symbols("n b")
lily = Consumer("lily", 32, [necklace, bracelet], (n + EPSILON)*(b + EPSILON)**2,
                {necklace: n, bracelet: b})
for x in range(40):
    lily.change_decision([necklace, bracelet])
print(lily.get_total_utility())
print(lily.decision)
"""

x, y = symbols("x y")
xylo = Tradeable("xylo", 1)
yacht = Tradeable("yacht", 2)
u = Consumer("u", 120, [xylo, yacht], (x**2)*(y**3),
             {xylo: x, yacht: y})
for x in range(100):
    u.change_decision([xylo, yacht])
print(u.get_total_utility())

"""
s, m, c, g = symbols("s m c g")
snickers = Tradeable("snickers", 1)
mars = Tradeable("mars", 4)
cadbury = Tradeable("cadbury", 5)
gum = Tradeable("gum", 2)
kid = Consumer("kid", 20, [snickers, mars, cadbury, gum], 3*s+3*g + 3*m + 4*c,
               {snickers: s, mars: m, cadbury: c, gum: g})
for x in range(100):
    kid.change_decision([snickers, mars, cadbury, gum])


big_mac = Tradeable("big macs", 1.2)
bm, c, l = symbols("bm c l")

capital = Tradeable("capital", 100)
labor = Tradeable("labor", 1)
mcdonalds = Producer("McDonald's", [capital, labor], big_mac, -l*(l - 16), {capital: c, labor: l})
mcdonalds.decision[capital] += 1
for x in range(20):
    print("production", mcdonalds.get_total_production())
    print("marginal production", mcdonalds.find_mp())
    mcdonalds.change_decision([labor],100)

"""
"""
xylo = Tradeable("xylo", 1.2)
capital = Tradeable("capital", 15)
labor = Tradeable("labor", 1)
c, l = symbols("c l")
xylo_producer = Producer("xylo producer", [capital, labor], xylo, -(4*c + l)*((4*c + l) - 16), {capital: c, labor: l})

for x in range(20):
#   print("production", pencil_pushers.get_total_production())
    xylo_producer.change_decision([capital, labor])

"""
"""
#super_good = Tradeable("super good", 9)
#capital = Tradeable("capital", 20)
#labor = Tradeable("labor", 5)

c = 5
p = 10
a = 0.2
b = 0.4
wk = 20
wl = 8

classical_k = (c*p*(b/wk)**(1-a)*(a/wl)**a)**(1/(1-a-b))
classical_l = (c*p*(a/wl)**(1-b)*(b/wk)**b)**(1/(1-a-b))
    
super_good = Tradeable("super good", p)
capital = Tradeable("capital", wk)
labor = Tradeable("labor", wl)
k, l = symbols("k l")
graph_producer = Producer("graph producer", [capital, labor], super_good, c*(l**a)*(k**b), {capital: k, labor: l})
graph_producer.decision[capital] += 1
graph_producer.decision[labor] += 1

for x in range(20):
#   print("production", pencil_pushers.get_total_production())
    graph_producer.change_decision([capital, labor])
"""
