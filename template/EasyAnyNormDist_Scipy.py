#!/usr/bin/python

'''
mjtsai1974@20180606, v1.0, scipy.stats.norm for Gaussian normal distribution with regards to any mu, sigma
'''

import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt

mu = 14.2
sigma = 2.22

x_axis=np.arange(8, 20, 0.01)
dist = norm(mu, sigma)

plt.plot(x_axis, dist.pdf(x_axis))
plt.show()

'''
Other articles of reference
http://bookdata.readthedocs.io/en/latest/beginning/04_matplotlib.html
'''