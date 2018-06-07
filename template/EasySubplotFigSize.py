#!/usr/bin/python

'''
mjtsai1974@20180606, v1.0, simple subplot with figure size

https://stackoverflow.com/questions/41530975/set-size-of-subplot-in-matplotlib
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(20)
y = np.random.randn(20)

#fig = plt.figure(figsize=(20, 8))
fig = plt.figure(figsize=(8, 20))

for i in range(0,10):
    ax = fig.add_subplot(5, 2, i+1)
    plt.plot(x, y, 'o')
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    # x and y axis should be equal length
    x0,x1 = ax.get_xlim()
    y0,y1 = ax.get_ylim()
    ax.set_aspect(abs(x1-x0)/abs(y1-y0))

plt.show()
fig.savefig('plot.pdf', bbox_inches='tight')