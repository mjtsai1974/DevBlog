#!/usr/bin/python

'''
mjtsai1974@20180606, v1.0, MLE for https://mjtsai1974.github.io/DevBlog/2018/06/06/bayesian-ml-beyes-to-practice/

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

'''
#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=False)
'''

# Define the given measured weights
weights = [13.9, 14.1, 17.5]
n = len(weights)

# Define the distributions to be plotted
mu = np.mean(weights)
sample_variance = np.var(weights, ddof=1)
sample_std_deviation = np.sqrt(sample_variance)

population_variance = np.var(weights, ddof=0)
population_std_deviation = np.sqrt(population_variance)

sigma_values = [sample_std_deviation, population_std_deviation]
linestyles = ['-', '--']
colours = ['red', 'blue']
x_axis = np.linspace(mu - 2 * np.max(sigma_values), mu + 2 * np.max(sigma_values), 100) #use the 

# plot the distributions
fig, ax = plt.subplots(figsize=(5, 3.75))

for sigma, ls, color in zip(sigma_values, linestyles, colours):
    # create a gaussian / normal distribution
    dist = norm(mu, sigma)

    plt.plot(x_axis, dist.pdf(x_axis), ls=ls, c=color,
             label=r'$\mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))

plt.xlim(mu - 2 * np.max(sigma_values), mu + 2 * np.max(sigma_values))
plt.ylim(0, 0.45)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu,\sigma)$')
plt.title('Gaussian Distribution')

plt.legend()
plt.show()

# MLE to ask for possible real weight with max(sample std deviation, population std deviation)
MLE_max = 0
mu_max = mu

for i in range(len(x_axis)):
    dist = norm(x_axis[i], np.max(sigma_values))

    MLE_now = 1.0

    for j in range(len(weights)):
        MLE_now = dist.pdf(weights[j]) * MLE_now

    if MLE_now > MLE_max:
        MLE_max = MLE_now
        mu_max = x_axis[i]
		
print('using np.max(sigma_values), the MLE for weight {0: 5.3f}'.format(mu_max))

# MLE to ask for possible real weight with min(sample std deviation, population std deviation)
MLE_max = 0
mu_max = mu

for i in range(len(x_axis)):
    dist = norm(x_axis[i], np.min(sigma_values))

    MLE_now = 1.0

    for j in range(len(weights)):
        MLE_now = dist.pdf(weights[j]) * MLE_now

    if MLE_now > MLE_max:
        MLE_max = MLE_now
        mu_max = x_axis[i]
		
print('using np.min(sigma_values), the MLE for weight {0: 5.3f}'.format(mu_max))