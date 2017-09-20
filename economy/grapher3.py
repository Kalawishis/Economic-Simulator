import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

f = open("data.txt")

allowed_chars = " 0123456789.[],"

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
            
"""
data_x = np.array([class_x - sim_x for class_x, sim_x in zip(class_consumer_x, sim_consumer_x)])
data_y = np.array([class_y - sim_y for class_y, sim_y in zip(class_consumer_y, sim_consumer_y)])
data_k = np.array([class_k - sim_k for class_k, sim_k in zip(class_producer_k, sim_producer_k)])
data_l = np.array([class_l - sim_l for class_l, sim_l in zip(class_producer_l, sim_producer_l)])
data_s = np.array([class_s - sim_s for class_s, sim_s in zip(class_market_s, sim_market_s)])
data_d = np.array([class_d - sim_d for class_d, sim_d in zip(class_market_d, sim_market_d)])

h_data_x = [
    go.Histogram(
        x=data_x
    )
]

h_data_y = [
    go.Histogram(
        x=data_y
    )
]

h_data_k = [
    go.Histogram(
        x=data_k
    )
]

h_data_l = [
    go.Histogram(
        x=data_l
    )
]

h_data_s = [
    go.Histogram(
        x=data_s
    )
]

h_data_d = [
    go.Histogram(
        x=data_d
    )
]

py.iplot(h_data_x, filename = "histogram consumer good x")
py.iplot(h_data_y, filename = "histogram consumer good y")
py.iplot(h_data_k, filename = "histogram producer capital")
py.iplot(h_data_l, filename = "histogram producer labor")
py.iplot(h_data_s, filename = "histogram market supply")
py.iplot(h_data_d, filename = "histogram market demand")
"""
data = []
data.extend([class_x - sim_x for class_x, sim_x in zip(class_consumer_x, sim_consumer_x)])
data.extend([class_y - sim_y for class_y, sim_y in zip(class_consumer_y, sim_consumer_y)])
data.extend([class_k - sim_k for class_k, sim_k in zip(class_producer_k, sim_producer_k)])
data.extend([class_l - sim_l for class_l, sim_l in zip(class_producer_l, sim_producer_l)])
data.extend([class_s - sim_s for class_s, sim_s in zip(class_market_s, sim_market_s)])
data.extend([class_d - sim_d for class_d, sim_d in zip(class_market_d, sim_market_d)])

h_data = [
    go.Histogram(
        x=data
    )
]

py.iplot(h_data, filename = "histogram total data")

f.close()
