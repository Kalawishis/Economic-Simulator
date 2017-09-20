import math
import statistics

f = open("data.txt")

class_consumer_x = []
class_consumer_y = []
sim_consumer_x = []
sim_consumer_y = []

class_producer_k = []
class_producer_l = []
sim_producer_k = []
sim_producer_l = []

class_market_s = []
class_market_d = []
sim_market_s = []
sim_market_d = []


for line_enum in enumerate(f):
    line = line_enum[1]
    i = line_enum[0]
    data = eval(line[line.index('['):])
    if i == 0: 
        for x, y in data:
            class_consumer_x.append(x)
            class_consumer_y.append(y)
    if i == 1: 
        for x, y in data:
            sim_consumer_x.append(x)
            sim_consumer_y.append(y)
    if i == 2: 
        for k, l in data:
            class_producer_k.append(k)
            class_producer_l.append(l)
    if i == 3: 
        for k, l in data:
            sim_producer_k.append(k)
            sim_producer_l.append(l)
    if i == 4: 
        for s, d in data:
            class_market_s.append(s)
            class_market_d.append(d)
    if i == 5: 
        for s, d in data:
            sim_market_s.append(s)
            sim_market_d.append(d)

data_x = [class_x - sim_x for class_x, sim_x in zip(class_consumer_x, sim_consumer_x)]
data_y = [class_y - sim_y for class_y, sim_y in zip(class_consumer_y, sim_consumer_y)]
data_k = [class_k - sim_k for class_k, sim_k in zip(class_producer_k, sim_producer_k)]
data_l = [class_l - sim_l for class_l, sim_l in zip(class_producer_l, sim_producer_l)]
data_s = [class_s - sim_s for class_s, sim_s in zip(class_market_s, sim_market_s)]
data_d = [class_d - sim_d for class_d, sim_d in zip(class_market_d, sim_market_d)]

data_a = []
data_a.extend(data_x)
data_a.extend(data_y)
data_a.extend(data_k)
data_a.extend(data_l)
data_a.extend(data_s)
data_a.extend(data_d)

data_con = []
data_con.extend(data_x)
data_con.extend(data_y)
data_pro = []
data_pro.extend(data_k)
data_pro.extend(data_l)
data_mar = []
data_mar.extend(data_s)
data_mar.extend(data_d)

def sem(l):
    return statistics.stdev(l)/math.sqrt(len(l))

def t(l):
    return statistics.mean(l)/sem(l)

print(statistics.mean(data_x))
print(statistics.stdev(data_x))
print(t(data_x))
print()

print(statistics.mean(data_y))
iqr = sorted(data_y)[74] - sorted(data_y)[24]
print("OUTLIERS ABOVE", sorted(data_y)[74] + 1.5*iqr)
print(statistics.stdev(data_y))
print(t(data_y))
print()

print(statistics.mean(data_k))
print(statistics.stdev(data_k))
print(t(data_k))
print()

print(statistics.mean(data_l))
print(statistics.stdev(data_l))
print(t(data_l))
print()

print(statistics.mean(data_s))
print(statistics.stdev(data_s))
print(t(data_s))
print()

print(statistics.mean(data_d))
print(statistics.stdev(data_d))
print(t(data_d))
print()

print("DATA A")
print(statistics.mean(data_a))
print(statistics.stdev(data_a))
print(t(data_a))
print()

print(statistics.mean(data_con))
print(statistics.stdev(data_con))
print(t(data_con))
print()

print(statistics.mean(data_pro))
print(statistics.stdev(data_pro))
print(t(data_pro))
print()

print(statistics.mean(data_mar))
print(statistics.stdev(data_mar))
print(t(data_mar))
print()
        
f.close()
