
# http://stackoverflow.com/questions/11067368/annotate-time-series-plot-in-matplotlib

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

x = [dt.datetime(2009, 05, 01), dt.datetime(2010, 06, 01), 
       dt.datetime(2011, 04, 01), dt.datetime(2012, 06, 01)];
y = [1, 3, 2, 5]

fig, ax = plt.subplots()
ax.plot_date(x, y, linestyle='--')

ax.annotate('Test', (mdates.date2num(x[1]), y[1]), xytext=(15, 15), textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))

fig.autofmt_xdate()
plt.show()
