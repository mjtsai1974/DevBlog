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
>The complete regularized cost function consists of two parts, part one is the cost function itself, part two is the regularized term:  
$$\begin{array}{l}\underset{REG}{J(\theta)}=\frac1m\sum_{i=1}^m\sum_{k=1}^K\left[-y_k^{(i)}\cdot\log(h_\theta^{(k)}(x^{(i)}))-(1-y_k^{(i)})\cdot\log(1-h_\theta^{(k)}(x^{(i)}))\right]\\+\frac\lambda{2m}\sum_{\mathcal l=1}^{L-1}\sum_{j=1}^{j_\mathcal l}\sum_{k=1}^{k_\mathcal l}(\theta_{j,k}^{(\mathcal l)})^2\\,where\;h_\theta(x)\in R^K\\\end{array}$$

>Suppose we are given totally m input data, the model where the cost function belongs to comes out with K outputs, and you all know that gradient descendent would be proceeded with derivation of $J(\theta)$ taken on the ($i,j$)th term in the weighting matrix $\theta^{(\mathcal l)}$ in between layer $\mathcal l$ and $\mathcal l+1$.  

>To make it more clear for the proof in next section, whenever you read <font color="green">$\theta_{i,j}^{(\mathcal l)}$</font>, in this article, they are:  
>&#10112;the weighting matrix $\theta^{(\mathcal l)}$ in between layer $\mathcal l$ and $\mathcal l+1$.  
>&#10113;$i$ is the $i$-th row of the weighting matrix $\theta^{(\mathcal l)}$, it is also the $i$-th activation function in next layer $\mathcal l+1$.  
>&#10114;{j} is the $j$-th output from the activation function at layer $\mathcal l$.  
>&#10115;<font color="green">$\theta_{i,j}^{(\mathcal l)}$</font> translates the <font color="green">$j$</font>-th output from the activation function at layer <font color="green">$\mathcal l$</font> into <font color="red">one of the input</font> of the <font color="green">$i$</font>-th activation function in next layer <font color="green">$\mathcal l+1$</font>!!!!  

>All we need to compute are $J(\theta)$ and $\frac{\partial J(\theta)}{\partial\theta_{i,j}^{(\mathcal l)}}$ in a gradient descendent manner, the point is how to achieve the goal and why!  

### The Gradient Computation By Intuition
>Things would be a little complicated, before this article formularize the gradient computation for each $\frac{\partial J(\theta)}{\partial\theta_{i,j}^{(\mathcal l)}}$, just treat the errors from the final output layer, in the reversed order, back to the beginning second layer, and the output error from each layer $\mathcal l$ would then be propagated back into the gradient $\frac{\partial J(\theta)}{\partial\theta_{i,j}^{(\mathcal l-1)}}$.  
>

### The Backward Propagation Algorithm
>
>