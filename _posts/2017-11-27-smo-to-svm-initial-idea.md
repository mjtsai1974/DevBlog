---
layout: post
title: Support Vector Machine Initial Idea
---

## Initial Idea
<p class="message">
Now, we know the distance from $H$ to $H_1$ is $\frac{\left|w^t\cdot x-b\right|}{\left\|w\right\|}=\frac1{\left\|w\right\|}$; where $H_1:w^t\cdot x-b=1$.  As to distance between $H_1$ and $H_2$, 
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
>The first part is the <font color="green">target</font>, the second part is the <font color="red">constraint</font>.  

>We introduce $\alpha_1,\alpha_2,\dots\alpha_n$ to be the lagrange multiplier and express in below lagrangian to be our <font color="deepink">objective function</font>:  
$$L(w,b,\alpha)=\frac12w^t\cdot w-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)-1)$$  
>;where $L$ is actually the <font color="deepink">maximum likelihood function</font> for $w$, $\alpha$, $b$ to be estimated out the best optimal value at the corresponding largest possibility.

### 
>Next to inspect inside $L(w,b,\alpha)$ to get the best optimal value of $w$, $\alpha$, $b$:  
$$\begin{array}{l}L(w,b,\alpha)\\=\frac12w^t\cdot w-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)-1)\\=\frac12w^t\cdot w-\sum_{i=1}^n\alpha_i\cdot y_i\cdot(w^t\cdot x_i-b)+\sum_{i=1}^n\alpha_i\end{array}$$  
>To get the optimal $\alpha$, we should take partial derivatives of $L$ on $w$, $b$ respectively and equate them to zero:  
>&#10112;$\frac{\partial L}{\partial w}=w-\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i=0$, then, we have $w=\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i$  
>&#10113;$\frac{\partial L}{\partial b}=\sum_{i=1}^n\alpha_i\cdot y_i$  

>&#10114;use the deduction result of &#10112; and &#10113; in $L(w,b,\alpha)$, we obtain:  
$$\begin{array}{l}L(w,b,\alpha)\\=\frac12(\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i)^t\cdot(\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i)\\-\sum_{i=1}^n\alpha_i\cdot y_i\cdot((\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i)^t\cdot x_i-b)\\+\sum_{i=1}^n\alpha_i\end{array}$$  
>&#10115;reduce from the second term, we have below deduction:  
$$\begin{array}{l}\sum_{i=1}^n\alpha_i\cdot y_i\cdot((\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i)^t\cdot x_i-b)\\=\sum_{i=1}^n\alpha_i\cdot y_i\cdot(\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i)^t\cdot x_i\\-\sum_{i=1}^n\alpha_i\cdot y_i\cdot b\\=(\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i)^t\cdot(\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i)\\\dots\sum_{i=1}^n\alpha_i\cdot y_i\cdot b=0\end{array}$$  
>&#10116;take it back to $L(w,b,\alpha)$, we get:  
$$\begin{array}{l}L(w,b,\alpha)\\=-\frac12(\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i)^t\cdot(\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i)\\+\sum_{i=1}^n\alpha_i\\=-\frac12\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot(x_i^t\cdot x_j)\\+\sum_{i=1}^n\alpha_i\end{array}$$  

>But, why do we design $L(w,b,\alpha)$ in the expression of the target <font color="red">plus</font> the constraint?  Recall that in the lagrange multiplier article, I have shown you by taking $L(x,\lambda)=f(x)+\lambda\cdot g(x)$, finally leads to <font color="red">$\lambda<0$</font>.  
