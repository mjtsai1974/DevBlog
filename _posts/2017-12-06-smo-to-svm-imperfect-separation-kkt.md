---
layout: post
title: Support Vector Machine Imperfect Separation And KKT Condition
---

## Imperfect Separation And KKT Condition

<p class="message">
How, if there exists some data points in the safeguard zone?  When we are studying the field of SVM, it is the condition never be abandoned.  This article will lead you break through the <font color="OrangeRed">noise</font> case and come out to the <font color="Red">KKT condition</font>.  
</p>

### Imperfect Separation With <font color="OrangeRed">Noise</font>
>There exists some condition that we don't strictly enforce that <font color="OrangeRed">no</font> data points in between $H_1$ and $H_2$.  We can extend SVM to allow some <font color="OrangeRed">noise</font>(data points) in between the safeguard zone.  Thus, we want to <font color="OrangeRed">penalize</font> the data points that cross the boundaries($H_1$,$H_2$).  
>In this way, by introducting $\xi\geq0$, non-negative, such that:  
>&#10112;$w^t\cdot x_i-b\geq1-\xi_i$, for $y_i=1$  
>&#10113;$w^t\cdot x_i-b\leq-1+\xi_i$, for $y_i=-1$  
>This is to <font color="OrangeRed">shrink down</font> the distance between $H_1$ and $H_2$, thus <font color="DeepSkyBlue">to allow some noise within original margin</font>.  
>
>In addition to $\xi$, we also introduce the <font color="OrangeRed">penalty</font> $C$, where $C$ is <font color="DeepSkyBlue">finite</font> in the objective function:    
>$\underset{w,\xi_i}{min}\left[w^t\cdot w+C\cdot(\sum_{i=1}^n\xi_i)^m\right]$, by usual $m=1$, which then leads to formulate our problem as:  
>$\underset{w,\xi_i}{min}\left[w^t\cdot w+C\cdot\sum_{i=1}^n\xi_i\right]$,  
><font color="OrangeRed">subject to</font> $y_i\cdot(w^t\cdot x_i-b)+\xi_i-1\geq0$, $\forall\xi_i\geq0$  
>
>Next to build the lagrangian by introducing $\alpha_1$, $\alpha_2$,..., $\alpha_n$ and $\mu_1$, $\mu_2$,..., $\mu_n$, then:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+C\cdot\sum_{i=1}^n\xi_i\\\;\;\;\;-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)+\xi_i-1)\\\;\;\;\;-\sum_{i=1}^n\mu_i\cdot\xi_i\end{array}$$  
>; where $\alpha_i$ is for the regularization of the term $y_i\cdot(w^t\cdot x_i-b)+\xi_i-1$, $\mu_i$ is for the regularization of the term $\xi_i$.  
>$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+\sum_{i=1}^n(C-\alpha_i-\mu_i)\xi_i\\\;\;\;\;-\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i^t)\cdot w\\\;\;\;\;+\sum_{i=1}^n\alpha_i\cdot y_i\cdot b\\\;\;\;\;+\sum_{i=1}^n\alpha_i\end{array}$  
>
>To get the maximum of $L$ at $\alpha$ and $\xi$, below constraints must be satisfied for all $i$:  
>&#10112;$\frac{\partial L}{\partial w}=0$, &#10113;$\frac{\partial L}{\partial b}=0$, &#10114;$\frac{\partial L}{\partial \xi}=0$, for all $i$:  
>&#10112;we have $w$ in below expression:  
$$\begin{array}{l}w^t-\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i^t)=0\\\Leftrightarrow w=\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i)\end{array}$$  
>&#10113;implies $\sum_{i=1}^n\alpha_i\cdot y_i=0$  
>&#10114;we have $\sum_{i=1}^nC-\alpha_i-\mu_i=0$, then for all $i$, $C-\alpha_i-\mu_i=0$ just holds.  
>
>Notes that $\alpha_i\geq0$, $\mu_i\geq0$, therefore, we have <font color="OrangeRed">$0\leq\alpha_i\leq C$</font>,  
>$\alpha_i$ is now <font color="OrangeRed">upper bounded</font> by <font color="OrangeRed">$C$</font>.  
>
>Substituting &#10112;, &#10113;, &#10114; to $L(w,b,\xi,\alpha,\mu)$, then, we have:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+\sum_{i=1}^n0\cdot\xi_i\\\;\;\;\;-w^t\cdot w+0\cdot b\\\;\;\;\;+\sum_{i=1}^n\alpha_i\\=\sum_{i=1}^n\alpha_i-\frac12\cdot w^t\cdot w\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$  
<!-- $$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+\sum_{i=1}^n0\cdot\xi_i\\\;\;\;\;-w^t\cdot w+0\cdot b\\\;\;\;\;+\sum_{i=1}^n\alpha_i\end{array}$$ -->
<!-- $$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\sum_{i=1}^n\alpha_i-\frac12\cdot w^t\cdot w\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$ -->
>

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->

<!-- <font color="#C20000">positive conclusion, finding</font> -->
<!-- <font color="green">negative conclusion, finding</font> -->

<!-- <font color="Green">value iteration</font> -->
<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->
