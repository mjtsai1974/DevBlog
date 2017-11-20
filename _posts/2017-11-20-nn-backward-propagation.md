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
$$\frac{\partial J(\theta)}{\partial\theta_{1,1}^{(1)}}=\frac{\partial J(\theta)}{\partial a_1^{(2)}}\cdot\frac{\partial a_1^{(2)}}{\partial z_1^{(2)}}\cdot\frac{\partial z_1^{(2)}}{\partial\theta_{1,1}^{(1)}}$$

>This is <font color="green">the chain rule in calculus</font>, which would mostly be applied in our later paragraph of proof.  
>But, why we have the term $\frac{\partial a_1^{(2)}}{\partial z_1^{(2)}}$?  
><font color="red">Please be recalled that $a_1^{(2)}=g(z_1^{(2)})$</font>, where we have below deduction:  
$$\begin{array}{l}\frac{\partial J(\theta)}{\partial a_1^{(2)}}=\frac{\partial(-y\cdot\log(a_1^{(2)})-(1-y)\cdot\log(1-a_1^{(2)}))}{\partial a_1^{(2)}}\\\;\;\;\;\;\;\;\;\;\;\;\;\;=\frac{-y}{a_1^{(2)}}+\frac{1-y}{1-a_1^{(2)}}\cdots(a)\\\frac{\partial a_1^{(2)}}{\partial z_1^{(2)}}=\frac{\partial g(z_1^{(2)})}{\partial z_1^{(2)}}=g(z_1^{(2)})\cdot(1-g(z_1^{(2)}))\cdots(b)\\\frac{\partial z_1^{(2)}}{\partial\theta_{1,1}^{(1)}}=a_1^{(1)}\cdots(c)\end{array}$$

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
&#10112;suppose you can recognize above proof given in $3\times1$ neural network model, and we have the finding:<font color="green">  
$$\frac{\partial J(\theta)}{\partial\theta_{i,j}^{(\mathcal l)}}=(a_i^{(\mathcal l+1)}-y^{(i\_data)})\cdot a_j^{(\mathcal l)}=\delta_i^{(\mathcal l+1)}\cdot a_j^{(\mathcal l)}$$
></font>

>&#10113;next, we step further into 2 output nodes in final layer, $3\times2$ neural network model:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-22-nn-backward-propagation-proof-by-3-2.png "backward propagation by 3x2")

>In this case, for $i=1,2$, we can have:  
$$a_i^{(2)}=g(z_i^{(2)})=g(\theta_{i,1}^{(1)}\cdot a_1^{(1)}+\theta_{i,2}^{(1)}\cdot a_2^{(1)}+\theta_{i,3}^{(1)}\cdot a_3^{(1)})$$

>Succeeding to the result in &#10112;, take error costs at layer 2(in this example) as:  
$$\delta_{2\times1}^{(2)}={\begin{bmatrix}\delta_1^{(2)}\\\delta_2^{(2)}\end{bmatrix}}_{2\times1}={\begin{bmatrix}a_1^{(2)}-y^{(i\_data)}\\a_2^{(2)}-y^{(i\_data)}\end{bmatrix}}_{2\times1}$$

>We can deduce out:  
$$\begin{array}{l}\frac{\partial J(\theta)}{\partial\theta_{1,1}^{(1)}}=\frac{\partial J(\theta)}{\partial a_1^{(2)}}\cdot\frac{\partial a_1^{(2)}}{\partial z_1^{(2)}}\cdot\frac{\partial z_1^{(2)}}{\partial\theta_{1,1}^{(1)}}\\=(a_1^{(2)}-y^{(i\_data)})\cdot a_1^{(1)}\end{array}$$
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{1,2}^{(1)}}=(a_1^{(2)}-y^{(i\_data)})\cdot a_2^{(1)}$$
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{1,3}^{(1)}}=(a_1^{(2)}-y^{(i\_data)})\cdot a_3^{(1)}$$
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{2,1}^{(1)}}=(a_2^{(2)}-y^{(i\_data)})\cdot a_1^{(1)}$$
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{2,2}^{(1)}}=(a_2^{(2)}-y^{(i\_data)})\cdot a_2^{(1)}$$
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{2,3}^{(1)}}=(a_2^{(2)}-y^{(i\_data)})\cdot a_3^{(1)}$$
><font color="green">
By mathematics induction, we have a finding the same as the one in &#10112;:  
$$\frac{\partial J(\theta)}{\partial\theta_{i,j}^{(\mathcal l)}}=(a_i^{(\mathcal l+1)}-y^{(i\_data)})\cdot a_j^{(\mathcal l)}=\delta_i^{(\mathcal l+1)}\cdot a_j^{(\mathcal l)}$$
></font>

>I have just proved for the simple model of only 2 layers, but, <font color="red">will the current finding hold for models of more than 3 layers?</font>  

>&#10114;further step into $3\times2\times1$ neural network model:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-22-nn-backward-propagation-proof-by-3-2-1.png "backward propagation by 3x2x1")

>Trivially, we can deduce out that:  
$$\delta^{(3)}={\begin{bmatrix}\delta_1^{(3)}\end{bmatrix}}_{1\times1}={\begin{bmatrix}a_1^{(3)}-y^{(i\_data)}\end{bmatrix}}_{1\times1}$$

>Then, we have a problem here, <font color="red">what is $\delta^{(2)}$?</font> How to evaluate it?  Since it is not at the final layer.  What is <font color="red">the gradient descendent evaluation in $\theta^{(1)}$?</font>  
>The same by taking partial derivative of $J(\theta)$:  
$$\begin{array}{l}\frac{\partial J(\theta)}{\partial\theta_{1,1}^{(1)}}=\frac{\partial J(\theta)}{\partial a_1^{(3)}}\cdot\frac{\partial a_1^{(3)}}{\partial\theta_{1,1}^{(1)}}\\\end{array}$$  
$$\begin{array}{l}=\frac{\partial J(\theta)}{\partial a_1^{(3)}}\cdot(\frac{\partial a_1^{(3)}}{\partial a_1^{(2)}}\cdot\frac{\partial a_1^{(2)}}{\partial z_1^{(2)}}\cdot\frac{\partial z_1^{(2)}}{\partial\theta_{1,1}^{(1)}}\\\end{array}$$  
$$\begin{array}{l}+\frac{\partial a_1^{(3)}}{\partial a_2^{(2)}}\cdot\frac{\partial a_2^{(2)}}{\partial z_2^{(2)}}\cdot\frac{\partial z_2^{(2)}}{\partial\theta_{1,1}^{(1)}})\;\cdots\;\frac{\partial z_2^{(2)}}{\partial\theta_{1,1}^{(1)}}=0\\\end{array}$$  
$$\begin{array}{l}=\frac{\partial J(\theta)}{\partial a_1^{(3)}}\cdot\frac{\partial g(z_1^{(3)})}{\partial z_1^{(3)}}\cdot\frac{\partial z_1^{(3)}}{\partial a_1^{(2)}}\cdot\frac{\partial a_1^{(2)}}{\partial z_1^{(2)}}\cdot\frac{\partial z_1^{(2)}}{\partial\theta_{1,1}^{(1)}}\\\end{array}$$  
$$\begin{array}{l}\cdots\frac{\partial a_1^{(3)}}{\partial a_1^{(2)}}=\frac{\partial g(z_1^{(3)})}{\partial z_1^{(3)}}\cdot\frac{\partial z_1^{(3)}}{\partial a_1^{(2)}}\\\end{array}$$  
$$\begin{array}{l}=(a_1^{(3)}-y^{(i\_data)})\cdot\theta_{1,1}^{(2)}\cdot g(z_1^{(2)})\cdot(1-g(z_1^{(2)}))\cdot a_1^{(1)}\\\end{array}$$  
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{1,2}^{(1)}}=(a_1^{(3)}-y^{(i\_data)})\cdot\theta_{1,1}^{(2)}\cdot g(z_1^{(2)})\cdot(1-g(z_1^{(2)}))\cdot a_2^{(1)}$$  
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{1,3}^{(1)}}=(a_1^{(3)}-y^{(i\_data)})\cdot\theta_{1,1}^{(2)}\cdot g(z_1^{(2)})\cdot(1-g(z_1^{(2)}))\cdot a_3^{(1)}$$  
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{2,1}^{(1)}}=(a_1^{(3)}-y^{(i\_data)})\cdot\theta_{1,2}^{(2)}\cdot g(z_2^{(2)})\cdot(1-g(z_2^{(2)}))\cdot a_1^{(1)}$$  
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{2,2}^{(1)}}=(a_1^{(3)}-y^{(i\_data)})\cdot\theta_{1,2}^{(2)}\cdot g(z_2^{(2)})\cdot(1-g(z_2^{(2)}))\cdot a_2^{(1)}$$  
$$\therefore\frac{\partial J(\theta)}{\partial\theta_{2,3}^{(1)}}=(a_1^{(3)}-y^{(i\_data)})\cdot\theta_{1,2}^{(2)}\cdot g(z_2^{(2)})\cdot(1-g(z_2^{(2)}))\cdot a_3^{(1)}$$  

>We can normalize above result in this given example:  
$$\frac{\partial J(\theta)}{\partial\theta_{i,j}^{(\mathcal l)}}=(a_1^{((\mathcal l+1)+1)}-y^{(i\_data)})\cdot\theta_{1,i}^{(\mathcal l+1)}\cdot g(z_i^{(\mathcal l+1)})\cdot(1-g(z_i^{(\mathcal l+1)}))\cdot a_j^{(\mathcal l)}$$  
$$\therefore\delta_i^{(\mathcal l+1)}=(a_1^{((\mathcal l+1)+1)}-y^{(i\_data)})\cdot\theta_{1,i}^{(\mathcal l+1)}\cdot g(z_i^{(\mathcal l+1)})\cdot(1-g(z_i^{(\mathcal l+1)}))$$  

>For $\mathcal l=1$, we have error costs at layer two:  
$$\delta_i^{(2)}=(a_1^{(3)}-y^{(i\_data)})\cdot\theta_{1,i}^{(2)}\cdot g(z_i^{(2)})\cdot(1-g(z_i^{(2)}))$$  
>where $i=1,2$, then:  
$$\delta_{2\times1}^{(2)}={\begin{bmatrix}\delta_1^{(2)}\\\delta_2^{(2)}\end{bmatrix}}_{2\times1}$$  
$$=(a_1^{(3)}-y^{(i\_data)})\cdot{\begin{bmatrix}\theta_{1,1}^{(2)}\\\theta_{1,2}^{(2)}\end{bmatrix}}_{2\times1}.\times$$  
$${\begin{bmatrix}g(z_1^{(2)})\cdot(1-g(z_1^{(2)}))\\g(z_2^{(2)})\cdot(1-g(z_2^{(2)}))\end{bmatrix}}_{2\times1}$$  
$$\cdots\;.\times\;element-wised\;operator$$  
$$=(a_1^{(3)}-y^{(i\_data)})\cdot{\begin{bmatrix}\theta_{1,1}^{(2)}\cdot g(z_1^{(2)})\cdot(1-g(z_1^{(2)}))\\\theta_{1,2}^{(2)}\cdot g(z_2^{(2)})\cdot(1-g(z_2^{(2)}))\end{bmatrix}}_{2\times1}$$  
><font color="green">
By mathematics induction, we have a finding the same as the one in &#10112;:  
$$\frac{\partial J(\theta)}{\partial\theta_{i,j}^{(\mathcal l)}}=(a_i^{(\mathcal l+1)}-y^{(i\_data)})\cdot a_j^{(\mathcal l)}=\delta_i^{(\mathcal l+1)}\cdot a_j^{(\mathcal l)}$$
></font>

>&#10115;further step into $3\times2\times2$ neural network model:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-22-nn-backward-propagation-proof-by-3-2-2.png "backward propagation by 3x2x2")

>It would be easy to show error costs at layer three and two:  
$$\delta_{2\times1}^{(3)}={\begin{bmatrix}\delta_1^{(3)}\\\delta_2^{(3)}\end{bmatrix}}_{2\times1}={\begin{bmatrix}a_1^{(3)}-y^{(i\_data)}\\a_2^{(3)}-y^{(i\_data)}\end{bmatrix}}_{2\times1}$$  
$$\delta_{2\times1}^{(2)}=\begin{bmatrix}\theta^{(2)}\end{bmatrix}_{2\times2}^t\cdot{\begin{bmatrix}\delta^{(3)}\end{bmatrix}}_{2\times1}.\times{\begin{bmatrix}g(z_1^{(2)})\cdot(1-g(z_1^{(2)}))\\g(z_2^{(2)})\cdot(1-g(z_2^{(2)}))\end{bmatrix}}_{2\times1}$$
$$\cdots\;.\times\;element-wised\;operator$$  

>First, evaluate $J(\theta)$ at layer 2, that is take derivation of $J(\theta)$ on $\theta_{i,j}^{(2)}$:  
$$\begin{array}{l}\frac{\partial J(\theta)}{\partial\theta_{1,1}^{(2)}}=\frac{\partial J(\theta)}{\partial a_1^{(3)}}\cdot\frac{\partial a_1^{(3)}}{\partial\theta_{1,1}^{(2)}}\\=\frac{\partial J(\theta)}{\partial a_1^{(3)}}\cdot\frac{\partial g(z_1^{(3)})}{\partial z_1^{(3)}}\cdot\frac{\partial z_1^{(3)}}{\partial\theta_{1,1}^{(2)}}\\=(a_1^{(3)}-y^{(i\_data)})\cdot a_1^{(2)}\\=\delta_1^{(3)}\cdot a_1^{(2)}\end{array}$$  
$$\begin{array}{l}\therefore\frac{\partial J(\theta)}{\partial\theta_{1,2}^{(2)}}=\delta_1^{(3)}\cdot a_2^{(2)}\\\therefore\frac{\partial J(\theta)}{\partial\theta_{2,1}^{(2)}}=\delta_2^{(3)}\cdot a_1^{(2)}\\\therefore\frac{\partial J(\theta)}{\partial\theta_{2,2}^{(2)}}=\delta_2^{(3)}\cdot a_2^{(2)}\end{array}$$  

>We can by mathematics induction to have error costs at layer two:  
$$\frac{\partial J(\theta)}{\partial\theta_{i,j}^2}=\delta_i^{(3)}\cdot a_j^{(2)}$$  

>Next, evaluate $J(\theta)$ at layer 1, that is take derivation of $J(\theta)$ on $\theta_{i,j}^{(1)}$:  
$$\begin{array}{l}\frac{\partial J(\theta)}{\partial\theta_{1,1}^{(1)}}=\frac{\partial J(\theta)}{\partial a_1^{(3)}}\cdot\frac{\partial a_1^{(3)}}{\partial\theta_{1,1}^{(1)}}+\frac{\partial J(\theta)}{\partial a_2^{(3)}}\cdot\frac{\partial a_2^{(3)}}{\partial\theta_{1,1}^{(1)}}\\=\frac{\partial J(\theta)}{\partial a_1^{(3)}}\cdot\frac{\partial g(z_1^{(3)})}{\partial z_1^{(3)}}\cdot\frac{\partial z_1^{(3)}}{\partial\theta_{1,1}^{(1)}}\\+\frac{\partial J(\theta)}{\partial a_2^{(3)}}\cdot\frac{\partial g(z_2^{(3)})}{\partial z_2^{(3)}}\cdot\frac{\partial z_2^{(3)}}{\partial\theta_{1,1}^{(1)}}\end{array}$$  
$$take\;part\;1=\frac{\partial g(z_1^{(3)})}{\partial z_1^{(3)}}\cdot\frac{\partial z_1^{(3)}}{\partial\theta_{1,1}^{(1)}}$$  
$$take\;part\;2=\frac{\partial g(z_2^{(3)})}{\partial z_2^{(3)}}\cdot\frac{\partial z_2^{(3)}}{\partial\theta_{1,1}^{(1)}}$$  

### The Backward Propagation Algorithm
>
>