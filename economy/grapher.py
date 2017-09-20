import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

from market import *


#xylo yacht consumer test
#let x be the number of xylos bought by the consumer
#let y be the number of yachts bought by the consumer
#let z be the number of iterations
"""
x_val_list = []
y_val_list = []
z_val_list = list(range(100))

x, y = symbols("x y")
xylo = Tradeable("xylo", 1)
yacht = Tradeable("yacht", 2)
u = Consumer("u", 120, [xylo, yacht], (x**2)*(y**3),
             {xylo: x, yacht: y})
for x in range(100):
    x_val_list.append(u.decision[xylo])
    y_val_list.append(u.decision[yacht])
    u.change_decision([xylo, yacht])

simulator_trace = go.Scatter3d( #the trace of the simulator on each iteration
    x = x_val_list,
    y = y_val_list,
    z = z_val_list,
    mode = "markers"
)

classical_trace = go.Scatter3d(  #the line representing classical economic predictions
    x = [48, 48],
    y = [36, 36],
    z = [0, 99],
    mode = "lines"
)

data = [simulator_trace, classical_trace]
py.iplot(data, filename = 'xylo_yact_consumer_graph')
"""
"""
trace1 = go.Scatter3d(
    x = [9, 8, 5],
    y = [1, 2, 3],
    z = [11, 8, 15],
    mode = "markers"
)
#py.iplot(data, filename = 'simple_3d_test')

trace2 = go.Scatter3d(
    x = [6, 6],
    y = [6, 6],
    z = [0, 12],
    mode = "lines"
)
data = [trace1, trace2]
py.iplot(data, filename = 'simple_3d_test')
"""
"""
c_val_list = []
l_val_list = []
z_val_list = list(range(100))

super_good = Tradeable("super good", 9)
capital = Tradeable("capital", 20)
labor = Tradeable("labor", 5)
c, l = symbols("c l")
graph_producer = Producer("graph producer", [capital, labor], super_good, 5*sqrt(c)*sqrt(l), {capital: c, labor: l})
graph_producer.decision[capital] += 1
graph_producer.decision[labor] += 1

for x in range(100):
    c_val_list.append(graph_producer.decision[capital])
    l_val_list.append(graph_producer.decision[labor])
    graph_producer.change_decision([capital, labor], 177)

simulator_trace = go.Scatter3d( #the trace of the simulator on each iteration
    x = c_val_list,
    y = l_val_list,
    z = z_val_list,
    mode = "markers"
)

classical_trace = go.Scatter3d(  #the line representing classical economic predictions
    x = [25, 25],
    y = [50, 50],
    z = [0, 99],
    mode = "lines"
)

data = [simulator_trace, classical_trace]
py.iplot(data, filename = 'graph_producer_graph')
"""


