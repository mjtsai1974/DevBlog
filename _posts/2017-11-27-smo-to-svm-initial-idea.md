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
$$y_i\cdot(w^t\cdot x_i-b)\geq1$$, $$\forall i\in\{1,2,...,n\}$$  
>We can formulate our problem as:  
>$\underset w{min}\frac12w^t\cdot w$, subject to $y_i\cdot(w^t\cdot x_i-b)\geq1,\forall i$.  
>The first part is the <font color="green">target</font>, the second part is the <font color="red">constraint</font>.  

>We introduce $\alpha_1,\alpha_2,\dots\alpha_n$ to be the lagrange multiplier and express in below lagrangian to be our <font color="deepink">objective function</font>:  
$$L(w,b,\alpha)=\frac12w^t\cdot w-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)-1)$$  
>;where $L$ is actually the <font color="deepink">maximum likelihood function</font> for $w$, $\alpha$, $b$ to be estimated out the best optimal value at the corresponding largest possibility.

### Regularize The Objective Function
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

### Why $L(w,b,\alpha)$ = the target <font color="red">plus</font> the constraint?
>But, why do we design $L(w,b,\alpha)$ in the expression of the target <font color="red">plus</font> the constraint?  Recall that in the [lagrange multiplier article]({{ site.github.repo }}{{ site.baseurl }}/2017/10/27/prereq-lagrange-multiplier/), I have shown you by taking $L(x,\lambda)=f(x)+\lambda\cdot g(x)$, finally leads to <font color="red">$\lambda<0$</font>.  

>&#10112;if we choose $L(x,\lambda)=f(x)-\lambda\cdot g(x)$, then $\lambda>0$.  This is by artificial design.  Whether plus or minus sign is used in the expression, could we have the similar achievement.  
>&#10113;now, back to the formulate of our problem:  
>$\underset{w,b}{min}\frac12w^t\cdot w$, subject to $y_i\cdot(w^t\cdot x_i-b)\geq1$  
>&#10114;suppose we take the constraint function function to be $g(x)=y_i\cdot(w^t\cdot x_i-b)\geq1$, if $\lambda$ would be negative by [prior lagrangian proof]({{ site.github.repo }}{{ site.baseurl }}/2017/10/27/prereq-lagrange-multiplier/), to get <font color="green">positive</font> $\lambda$, we should use the <font color="green">minus</font> operator in $L(x,\lambda)$.  
>&#10115;Therefore, almost all SVM articles design $L(w,b,\alpha)$; where $\alpha$ is the lagrange multiplier given in the expression by using the <font color="green">minus</font> operator:  
$$L(w,b,\alpha)=\frac12w^t\cdot w-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)-1)$$  
>&#10116;such design guarantees that we could have <font color="green">$\forall\alpha_i>0$</font>, which would be one major condition that must be satisfied in the following SVM article.

>After solving the $\alpha_i$, we can get $w=\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i$, then, we can classify a new object x by:  
$$\begin{array}{l}f(x)\\=sign(w^t\cdot x-b)\\=sign((\sum_{i=1}^n\alpha_i\cdot y_i\cdot xi)^t\cdot x-b)\\=sign(\sum_{i=1}^n\alpha_i\cdot y_i\cdot(xi)^t\cdot x-b)\end{array}$$  

### Non-Linear Training Set
>Here, we have a question, what, if the separating surface of the two classes is <font color="red">not linear</font>?  
>This might imply that the training set is distributed in a <font color="red">non-linear pattern</font>.  Suggestion would be made to transform the training set into another high-dimensional(maybe) space, such that they could be linearly separable.  
>&#10112;let $\Phi(\cdot)$ to be the transformation function to some high-dimensional space, then:  
$$\begin{array}{l}L(\alpha)\\=-\frac12\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot(\Phi(x_i).\times\Phi(x_j))\\+\sum_{i=1}^n\alpha_i\end{array}$$  
>, where $k(x_i,x_j)=\Phi(x_i).\times\Phi(x_j)$, $k(x_i,x_j)$ is the kernel function, the element-wise dot product $\Phi^t(x_i).\times\Phi(x_j)$ in the high-dimensional space is equivalent to the kernel function of the space of the output(or maybe input) parameters.  
>&#10113;we can take $k(x_i,x_j)=e^{-(\frac{\left\|x_i-x_j\right\|^2}{2\cdot\delta^2})}$,  
>where, $k(x_i,x_j)\in R^{n2},\Phi(x_i).\times\Phi(x_j)\in R^{n2}$  
>$x_i,x_j\in R^{n1}$ and $n1\leq n2$.  