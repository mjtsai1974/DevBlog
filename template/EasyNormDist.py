#!/usr/bin/python

'''
mjtsai1974@20180606, v1.0, draw a simple normal distribution

https://stackoverflow.com/questions/10138085/python-pylab-plot-normal-distribution
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma))  #deprecated since Matplotlib v2.2
plt.show()
