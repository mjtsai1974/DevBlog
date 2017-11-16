---
layout: post
title: Jacobian and Integration
---

## Jacobian
<p class="message">
Just like lagrange multiplier as a great add-in of constraint in differential to reach the local optimal.  Jacobian is treated as a ratio in between two coordinate system of references transformed in calculus integration process by often.  
Before proceeding any further, take a good look in this article would be quiet helpful.
</p>

### What Is Jacobian?
>Begin by a simple example, given $\int_a^bf(x)dx$:  
>If we let $x=h(y)$, take derivation on $y$:  
$$\frac{\partial x}{\partial y}=h^'(y)$$
>
>For the ease of understand, we illustrate by intuition:  
>&#10112;$\frac{\partial J(\theta)}{\partial\theta_j}=\frac1m\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})\cdot x_j^{(i)},for\;j=1,$ <font color="red">the bias term, no need for regularization!!!</font>  
>&#10113;$\frac{\partial J(\theta)}{\partial\theta_j}=\frac1m\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})\cdot x_j^{(i)}+\frac\lambda m\theta_j,\;for\;j>1$  
>;where the term $h_\theta(x^{(i)})-y^{(i)}$ is just the intuitive concept, the proof should make the derivation on the regularized version of cost function, next, we take the action.  
>