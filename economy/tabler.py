import plotly.plotly as py
from plotly.tools import FigureFactory as FF 

data_matrix = [['Quantity Type', 'Test Statistic', 'P-value'],
               ['Consumer Good X', 4.4935, 1.9043E-5],
               ['Consumer Good Y', 3.7429, 3.0535E-4],
               ['Producer Captial', -0.0380, 0.9698],
               ['Producer Labor', 0.4477, 0.6553],
               ['Market Supply', -1.1042, 0.2722],
               ['Market Demand', 16.0873, 2.2412E-29],
               ['All Quantities', 9.9520, 2.2412E-22]]

table = FF.create_table(data_matrix)
py.iplot(table, filename='economic_simulator_table')
