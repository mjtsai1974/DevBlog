---
layout: post
title: Neural Network Backward Propagation
---

## Neural Network Backward Propagation
<p class="message">
<font color="red">Backward propagation</font> is for the deduction of the <font color="green">$\theta_{i,j}^{(\mathcal l)}$</font> that could bring the error in <font color="green">the cost function</font> to a minimum state.  In neural network, <font color="blue">gradient descendent</font> 
is a mandatory mean to reach the <font color="green">$\theta_{i,j}^{(\mathcal l)}$</font> to the local minimum, and together with <font color="blue">regularization</font> to have an optimal approximation.  <font color="red">Backward propagation</font> proceeds in the reversed order 
and propagate the error from the <font color="green">final last one</font> layer back to the the <font color="green">final last two</font> layer, until the second layer, the algorithm would facilitate the whole <font color="blue">gradient descendent</font> process to find its local minimum.
</p>

### The Regularized Neural Network Cost Function
>