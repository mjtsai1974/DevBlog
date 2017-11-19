---
layout: post
title: Neural Network Feedforward Propagation
---

## Neural Network Feedforward Propagation
<p class="message">
Neural network works as a whole to behave like a perceptron, the output from layer $j$ would be mapped by <font color="green">$\theta^{(j)}$</font> to the input of layer $j+1$.  The final output in last layer would then be classified to 
the identity of the target object. 
</p>

### Neural Network Works by Feedforward Propagation
>Recap the neural network model, note that <font color="green">the final identity from logistic regression model would be determined at final layer</font>:  
$$\begin{array}{l}a^{(j+1)}=g(z^{(j+1)})=h_{\mathrm\theta^{(\mathrm j)}}(a^{(\mathrm j)})\\,where\;z=(\theta^{(j)})^t\cdot a^{(j)},\;g(z)=\frac1{1+e^{-z}}\\,j+1\;is\;the\;index\;of\;last\;layer\end{array}$$

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-19-nn-forward-propagation.png "forward propagation")

>