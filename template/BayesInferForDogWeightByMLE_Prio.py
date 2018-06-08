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

# Define the given measured weights and the prior(the most current value)
prior = 14.2
weights = [13.9, 14.1, 17.5]
n = len(weights)

# Define the distributions to be plotted
mu = prior
sample_variance = np.var(weights, ddof=1)
sample_std_deviation = np.sqrt(sample_variance)

population_variance = np.var(weights, ddof=0)
population_std_deviation = np.sqrt(population_variance)

sigma_values = [sample_std_deviation, population_std_deviation]
linestyles = ['-', '--', ':']
colours = ['red', 'blue']
colours_sample = ['black', 'purple', 'green']
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

# plot the new distribution v.s. mother N(prior, sample_std_deviation)
fig, ax = plt.subplots(figsize=(5, 3.75))

mother_dist = norm(mu, sample_std_deviation)
weight_sample_sigmas = []

for w in weights:
    weight_sigma = 1/(mother_dist.pdf(w) * np.sqrt(2 * np.pi))
    weight_sample_sigmas.append(weight_sigma)

    print('P({0:5.3f}) of N({1:5.3f},{2:5.3f}) = {3:5.3f} for N({0:5.3f}), the std error {4:5.3f}'.format(w, prior, sample_std_deviation, mother_dist.pdf(w), weight_sigma))

# plot the mother N(prior, sample_std_deviation)
plt.plot(x_axis, mother_dist.pdf(x_axis), ls='-', c='red',
             label=r'$\mu=%.3f,\ \sigma=%.3f$' % (mu, sample_std_deviation))

# plot the new N(w_sample, weight_sigma)
for w, sigma, ls, color in zip(weights, weight_sample_sigmas, linestyles, colours_sample):
    dist = norm(w, sigma)  # create a gaussian / normal distribution

    plt.plot(x_axis, dist.pdf(x_axis), ls=ls, c=color,
             label=r'$\mu=%.3f,\ \sigma=%.3f$' % (w, sigma))

plt.xlim(mu - 2 * np.max(sigma_values), mu + 2 * np.max(sigma_values))
plt.ylim(0, 0.45)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu,\sigma)$')
plt.title('Gaussian Distribution')

plt.legend()
plt.show()

# plot the new distribution v.s. mother N(prior, population_std_deviation)
fig, ax = plt.subplots(figsize=(5, 3.75))

mother_dist = norm(mu, population_std_deviation)
weight_population_sigmas = []

for w in weights:
    weight_sigma = 1/(mother_dist.pdf(w) * np.sqrt(2 * np.pi))
    weight_population_sigmas.append(weight_sigma)

    print('P({0:5.3f}) of N({1:5.3f},{2:5.3f}) = {3:5.3f} for N({0:5.3f}), the std error {4:5.3f}'.format(w, prior, population_std_deviation, mother_dist.pdf(w), weight_sigma))

# plot the mother N(prior, sample_std_deviation)
plt.plot(x_axis, mother_dist.pdf(x_axis), ls='-', c='blue',
             label=r'$\mu=%.3f,\ \sigma=%.3f$' % (mu, population_std_deviation))

# plot the new N(w_sample, weight_sigma)
for w, sigma, ls, color in zip(weights, weight_population_sigmas, linestyles, colours_sample):
    dist = norm(w, sigma)  # create a gaussian / normal distribution

    plt.plot(x_axis, dist.pdf(x_axis), ls=ls, c=color,
             label=r'$\mu=%.3f,\ \sigma=%.3f$' % (w, sigma))

plt.xlim(mu - 2 * np.max(sigma_values), mu + 2 * np.max(sigma_values))
plt.ylim(0, 0.45)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu,\sigma)$')
plt.title('Gaussian Distribution')

plt.legend()
plt.show()

# MLE to ask for possible real weight with N(prior, sample std deviation)
MLE_max = 0
mu_max = 0

mother_dist = norm(mu, sample_std_deviation)

for w, sigma in zip(weights, weight_sample_sigmas):
    dist = norm(w, sigma)

    MLE_now = 1.0

    for j in range(len(weights)):
        MLE_now = dist.pdf(weights[j]) * mother_dist.pdf(w) * MLE_now

    if MLE_now > MLE_max:
        MLE_max = MLE_now
        mu_max = w
		
print('using N(prior, sample std deviation), the MLE for weight {0: 5.3f}'.format(mu_max))

# MLE to ask for possible real weight with N(prior, population std deviation)
MLE_max = 0
mu_max = 0

mother_dist = norm(mu, population_std_deviation)

for w, sigma in zip(weights, weight_sample_sigmas):
    dist = norm(w, sigma)

    MLE_now = 1.0

    for j in range(len(weights)):
        MLE_now = dist.pdf(weights[j]) * mother_dist.pdf(w) * MLE_now

    if MLE_now > MLE_max:
        MLE_max = MLE_now
        mu_max = w
		
print('using N(prior, population std deviation), the MLE for weight {0: 5.3f}'.format(mu_max))