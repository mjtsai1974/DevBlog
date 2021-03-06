#!/usr/bin/python

'''
mjtsai1974@20180606, v1.1, scipy.norm for Gaussian normal distribution illustration

http://www.astroml.org/book_figures/chapter3/fig_gaussian_distribution.html

dist = scipy.stats.norm(...)

Where ... should be filled in with the desired distribution parameters Once we have defined the distribution parameters in this way, these distribution objects have many useful methods; for example:

    dist.pmf(x) computes the Probability Mass Function at values x in the case of discrete distributions
    dist.pdf(x) computes the Probability Density Function at values x in the case of continuous distributions
    dist.rvs(N) computes N random variables distributed according to the given distribution
'''

import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=False)

# Define the distributions to be plotted
sigma_values = [0.5, 1.0, 2.0]
linestyles = ['-', '--', ':']
mu = 0
x = np.linspace(-10, 10, 1000)

# plot the distributions
fig, ax = plt.subplots(figsize=(5, 3.75))

for sigma, ls in zip(sigma_values, linestyles):
    # create a gaussian / normal distribution
    dist = norm(mu, sigma)

    plt.plot(x, dist.pdf(x), ls=ls, c='black',
             label=r'$\mu=%i,\ \sigma=%.1f$' % (mu, sigma))

plt.xlim(-5, 5)
plt.ylim(0, 0.85)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu,\sigma)$')
plt.title('Gaussian Distribution')

plt.legend()
plt.show()