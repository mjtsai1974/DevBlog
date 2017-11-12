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
>$$\begin{array}{l}\underset\theta{min}\;J(\theta)=\frac1{2m}(\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2+\lambda\sum_{j=1}^n\theta_j^2);\;where\;h_\theta(x)=\theta^t\cdot x\\\theta_j=\theta_j-\;\frac\alpha m\frac{\partial J(\theta)}{\partial\theta_j}\\\;\;\;\;=\theta_j-\frac\alpha m\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})\cdot x_j^{(i)}-\frac\lambda m\theta_j;\;for\;j=1\;to\;n\end{array}$$

### Why Lagrangian Achieves Regularization?

>Suppose you all realize and have the basic intuition about lagrange multiplier.  In this section, we will take the squared error part as the level curve, and is it subject to the constraint function of circle.  
>Suppose again, the level curve hits the circle on the point $x$, very very close to the local extreme point of the circle, say it $a$.  If we can bring the delta($\delta$) as much as closed to zero, that is $\nabla f\approx\nabla g$.  
>Since the $\nabla g$ if the normal vector and is perpendicular to the local extreme point $a$, then, we can then believe that we have reduced the projection error of delta($\delta$), $\nabla f$ would be as plausible solution as $$\nabla g$.

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-11-ml-foundation-overfitting-vs-regularization-lagrangian.png "lagrangian achieves regularization of cost function")

>In the next topic, we will further illustrate regularization in logistic regression for binary classification.