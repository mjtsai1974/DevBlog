---
layout: post
title: Overfitting versus Regularization
---

## Regularization
<p class="message">
Regularization aims at overfitting elimination; whereas underfitting should be improived by adding extra features in your hypothesis model.
</p>

### Overfitting

>Overfitting usually occurs with the symptom that the hypothesis model fits very well to the training data, but, when the model is processing the real thing, it wouldn't predict as well as it had estimated in training stage. 

### Regularization by means of Lagrangian

>When we suspect our hypothesis model is overfitting, it should have been regularized by means of lagrange multiplier.  For the ease of explain and better understand, in this article, we'd like to illustrate with linear regression model.  
>Take the cost function $J(\theta)=\frac1{2m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2$, where the purpose of S.L.R is to minimize $J(\theta)$.  Suppose that you already realize what cost function is for.  
>Given $h_\theta(x)=\theta^t\cdot x$, where $$\theta=\begin{bmatrix}\theta_1\\\theta_2\end{bmatrix}$$ is the coefficients.  
>Take $$X=\begin{bmatrix}x_1\\x_2\end{bmatrix}$$ as the input data, and $x_1=1$, it is the intercept, or the bias term.  The superscribe(i) of $X$, $Y$ are the index of the input data record, means it is the i-th input data $X$, $Y$.  
>Now, put an extra item after the cost function could we regularize our existsing cost function:  
>$\underset\theta{min}J(\theta)=\frac1{2m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2+\frac\lambda{2m}\sum_{j=1}^n\theta_j^2$  
>$$
\begin{array}{l}\underset\theta{min}J(\theta)=\frac1{2m}(\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2+\lambda\sum_{j=1}^n\theta_j^2);\;where\;h_\theta(x)=\theta^t\cdot x\\\theta_j=\theta_j-\;\frac\alpha m\frac{\partial J(\theta)}{\partial\theta_j}\\\;\;\;\;=\theta_j-\frac\alpha m\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})\cdot x_j^{(i)}-\frac\lambda m\theta_j;\;for\;j=1\;to\;n\end{array}
$$

### Why Lagrangian Achieves Regularization?

to be conti...
