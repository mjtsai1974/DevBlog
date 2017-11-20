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
>Take the cost function by intuition:  
$$J(\theta)=-y^{(i\_data)}\cdot\log(h_\theta(x^{(i\_data)}))-(1-y^{(i\_data)})\cdot\log(1-h_\theta(x^{(i\_data)}))$$
>, where the $i$_$data$ is the index of the input data record.

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-22-nn-backward-propagation-proof-by-3-1.png "backward propagation by 3x1")

>Suppose we are given $3\times1$ neural network model, we know:  
>&#10112;$z_1^{(2)}=\theta_{1,1}^{(1)}\cdot a_1^{(1)}+\theta_{1,2}^{(1)}\cdot a_2^{(1)}+\theta_{1,3}^{(1)}\cdot a_3^{(1)}$  
>&#10113;$a_1^{(2)}=g(z_1^{(2)})=\frac1{1+e^{-z_1^{(2)}}}$  
>&#10114;take partial derivative of $J(\theta)$ on $\theta_{1,1}^{(1)}$, we would obtain:  
$$\frac{\partial J(\theta)}{\partial\theta_{1,1}^{(1)}}=\frac{\displaystyle\partial J(\theta)}{\displaystyle\partial a_1^{(2)}}\cdot\frac{\displaystyle\partial a_1^{(2)}}{\displaystyle\partial z_1^{(2)}}\cdot\frac{\displaystyle\partial z_1^{(2)}}{\displaystyle\partial\theta_{1,1}^{(1)}}$$

>This is <font color="green">the chain rule in calculus</font>, which would mostly be applied in our later paragraph of proof.  
>But, why we have the term $\frac{\displaystyle\partial a_1^{(2)}}{\displaystyle\partial z_1^{(2)}}$?  
><font color="red">Please be recalled that $a_1^{(2)}=g(z_1^{(2)})$</font>, where we have below deduction:  
$$\begin{array}{l}\frac{\displaystyle\partial J(\theta)}{\displaystyle\partial a_1^{(2)}}=\frac{\partial(-y\cdot\log(a_1^{(2)})-(1-y)\cdot\log(1-a_1^{(2)}))}{\partial a_1^{(2)}}\\\;\;\;\;\;\;\;\;\;\;\;\;\;=\frac{-y}{a_1^{(2)}}+\frac{1-y}{1-a_1^{(2)}}\cdots(a)\\\frac{\displaystyle\partial a_1^{(2)}}{\displaystyle\partial z_1^{(2)}}=\frac{\partial g(z_1^{(2)})}{\partial z_1^{(2)}}=g(z_1^{(2)})\cdot(1-g(z_1^{(2)}))\cdots(b)\\\frac{\displaystyle\partial z_1^{(2)}}{\displaystyle\partial\theta_{1,1}^{(1)}}=a_1^{(1)}\cdots(c)\end{array}$$

>Then, combine above (a), (b), (c) terms, we can have:  
$$\begin{array}{l}\frac{\partial J(\theta)}{\partial\theta_{1,1}^{(1)}}\\=(a)\cdot(b)\cdot(c)\\=\frac{-y\cdot(1-a_1^{(2)})+(1-y)\cdot a_1^{(2)}}{a_1^{(2)}\cdot(1-a_1^{(2)})}\cdot a_1^{(2)}\cdot(1-a_1^{(2)})\cdot a_1^{(1)}\\=(a_1^{(2)}-y)\cdot a_1^{(1)}\end{array}$$

>Continue to apply, we can have results:  
$$\left\{\begin{array}{l}\frac{\partial J(\theta)}{\partial\theta_{1,2}^{(1)}}=(a_1^{(2)}-y)\cdot a_2^{(1)}\\\frac{\partial J(\theta)}{\partial\theta_{1,3}^{(1)}}=(a_1^{(2)}-y)\cdot a_3^{(1)}\end{array}\right.$$

>Next, we introduce <font color="deeppink">$\delta_j^{(\mathcal l)}$</font>, it is the <font color="deeppink">error cost</font> in $j$-th activation function of layer $\mathcal l$.  
>With above deduction result, for each distinct input data at index $i$_$data$, we can take error at output layer $2$(in this example):  
$$\delta^{(2)}={\begin{bmatrix}\delta_1^{(2)}\end{bmatrix}}_{1\times1}=a_1^{(2)}-y^{(i\_data)}$$

>Things would be a little complicated, before this article formularize the gradient computation for each $\frac{\partial J(\theta)}{\partial\theta_{i,j}^{(\mathcal l)}}$, just think that you can compute the errors from the final output layer, in the reversed order, back to the beginning second layer, and the output error from each layer $\mathcal l$ would then be propagated back into the gradient $\frac{\partial J(\theta)}{\partial\theta_{i,j}^{(\mathcal l-1)}}$.  

### Formularize The Gradient Computation - Mathematics Induction
>From now on, we are going to do the real proof to formularize the gradient in neural network model:  
>&#10112;suppose you can recognize above proof given in $3\times1$ neural network model, and we conclude:  
$$\delta^{(2)}={\begin{bmatrix}\delta_1^{(2)}\end{bmatrix}}_{1\times1}=a_1^{(2)}-y^{(i\_data)}$$

>&#10113;next, we step further into 2 output nodes in final layer, $3\times2$ neural network model:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-22-nn-backward-propagation-proof-by-3-2.png "backward propagation by 3x2")

>In this case, for $i=1,2$, we can have:  
$$a_i^{(2)}=g(z_i^{(2)})=g(\theta_{i,1}^{(1)}\cdot a_1^{(1)}+\theta_{i,2}^{(1)}\cdot a_2^{(1)}+\theta_{i,3}^{(1)}\cdot a_3^{(1)})$$

>Succeeding to the result in &#10112;, take error costs at layer 2(in this example) as:  
$$\delta_{2\times1}^{(2)}={\begin{bmatrix}\delta_1^{(2)}\\\delta_2^{(2)}\end{bmatrix}}_{2\times1}={\begin{bmatrix}a_1^{(2)}-y^{(i\_data)}\\a_2^{(2)}-y^{(i\_data)}\end{bmatrix}}_{2\times1}$$

>We can deduce out:  
$$\begin{array}{l}\frac{\partial J(\theta)}{\partial\theta_{1,1}^{(1)}}=\frac{\displaystyle\partial J(\theta)}{\displaystyle\partial a_1^{(2)}}\cdot\frac{\displaystyle\partial a_1^{(2)}}{\displaystyle\partial z_1^{(2)}}\cdot\frac{\displaystyle\partial z_1^{(2)}}{\displaystyle\partial\theta_{1,1}^{(1)}}\\=(a_1^{(2)}-y^{(i\_data)})\cdot a_1^{(1)}\end{array}$$

>Apply the same method, could we obtain the similar results:  
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{1,2}^{(1)}}=(a_1^{(2)}-y^{(i\_data)})\cdot a_2^{(1)}$$
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{1,3}^{(1)}}=(a_1^{(2)}-y^{(i\_data)})\cdot a_3^{(1)}$$
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{2,1}^{(1)}}=(a_2^{(2)}-y^{(i\_data)})\cdot a_1^{(1)}$$
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{2,2}^{(1)}}=(a_2^{(2)}-y^{(i\_data)})\cdot a_2^{(1)}$$
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{2,3}^{(1)}}=(a_2^{(2)}-y^{(i\_data)})\cdot a_3^{(1)}$$

### The Backward Propagation Algorithm
>
>