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
>Recap the neural network model, note that the final identity from logistic regression model would be:
$$\begin{array}{l}a^{(j+1)}=g(z^{(j+1)})=h_{\mathrm\theta^{(\mathrm j)}}(a^{(\mathrm j)})=\left\{\begin{array}{l}\geq0.5,\;\mathrm{classify}\;\mathrm{as}1\\<0.5,\;\mathrm{classify}\;\mathrm{as}\;0\end{array}\right.\\,where\;z=(\theta^{(j)})^t\cdot a^{(j)},\;g(z)=\frac1{1+e^{-z}}\\,j+1\;is\;the\;final\;layer\;index\end{array}$$
<!-- $$h_\theta(z)=\left\{\begin{array}{l}\geq0.5,\;classify\;as1\\<0.5,\;classify\;as\;0\end{array}\right.$$ -->

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-19-nn-forward-propagation.png "forward propagation")

>