#!/usr/bin/python

'''
mjtsai1974@20180606, v1.0, draw a simple normal distribution

https://stackoverflow.com/questions/10138085/python-pylab-plot-normal-distribution
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from scipy.stats import norm
import math

'''
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm
The probability density is defined in the “standardized” form. To shift and/or scale the distribution 
use the loc and scale parameters. Specifically, norm.pdf(x, loc, scale) is identically equivalent to 
norm.pdf(y) / scale with y = (x - loc) / scale.
'''

x_axis = np.arange(-3, 3, 0.001)
#x_axis = np.linspace(-3, 3, 100)
plt.plot(x_axis, norm.pdf(x_axis,0,1))