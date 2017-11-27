---
layout: post
title: Support Vector Machine Initial Idea
---

## Initial Idea
<p class="message">
Now, we know the distance from $H$ to $H_1$ is \frac{\left|w^t\cdot x-b\right|}{\left\|w\right\|}=\frac1{\left\|w\right\|}; where $H_1:w^t\cdot x-b=1$.  As to distance between $H_1$ and $H_2$, 
we must minimize the term $\left\|w\right\|=(w^t\cdot w)^{\textstyle\frac12}$ to satisfy the condition that no points between $H_1$ and $H_2$.
</p>

### Formulate Our Problem By Lagrange Multiplier
>More precisely, by minimizing $w^t\cdot w$, we expect to have:  
>&#10112;for positive examples, $w^t\cdot x-b\geq1$, where $y=1$.  
>&#10113;for negative examples, $w^t\cdot x-b\leq-1$, where $y=-1$.  
>Then, combine &#10112; and &#10113; we can have:  
$$y_i\cdot(w^t\cdot x_i-b)\geq-1$$, $$\forall i\in\{1,2,...,n\}$$  
>We can formulate our problem as:  
$$\underset w{min}\frac12w^t\cdot w$$, subject to $$y_i\cdot(w^t\cdot x_i-b)\geq-1,\forall i$$  
>The first part is the target, the second part is the constraint.  

>We introduce $\alpha_1,\alpha_2,\dots\alpha_n$ to be the lagrange multiplier and express in below lagrangian to be our objective function:  
$$&#8466;(w,b,\alpha)=\frac12w^t\cdot w-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)-1)$$;  
>;where &#8466; is actually the maximum likelihood function for $w$, $\alpha$, $b$ to be estimated out the best optimal value at the corresponding largest possibility.

### 