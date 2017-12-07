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
>[1]In this way, by introducting $\xi\geq0$, non-negative, such that:  
>&#10112;$w^t\cdot x_i-b\geq1-\xi_i$, for $y_i=1$  
>&#10113;$w^t\cdot x_i-b\leq-1+\xi_i$, for $y_i=-1$  
>This is to <font color="OrangeRed">shrink down</font> the distance between $H_1$ and $H_2$, thus <font color="DeepSkyBlue">to allow some noise within original margin</font>.  
>
>[2]In addition to $\xi$, we also introduce the <font color="OrangeRed">penalty</font> $C$, where $C$ is <font color="DeepSkyBlue">finite</font> in the objective function:    
>$\underset{w,\xi_i}{min}\left[w^t\cdot w+C\cdot(\sum_{i=1}^n\xi_i)^m\right]$, by usual $m=1$, which then leads to formulate our problem as:  
>$\underset{w,\xi_i}{min}\left[w^t\cdot w+C\cdot\sum_{i=1}^n\xi_i\right]$,  
><font color="OrangeRed">subject to</font> $y_i\cdot(w^t\cdot x_i-b)+\xi_i-1\geq0$, $\forall\xi_i\geq0$  
>
>[3]Next to build the lagrangian by introducing $\alpha_1$, $\alpha_2$,..., $\alpha_n$ and $\mu_1$, $\mu_2$,..., $\mu_n$, then:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+C\cdot\sum_{i=1}^n\xi_i\\\;\;\;\;-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)+\xi_i-1)\\\;\;\;\;-\sum_{i=1}^n\mu_i\cdot\xi_i\end{array}$$  
>; where the regularization terms are explained below:  
>&#10112;the term $y_i\cdot(w^t\cdot x_i-b)+\xi_i-1$ is regularized by $\alpha_i$.  
>&#10113;$\mu_i$ is for the regularization of the term $\xi_i$.  
>
>The lagrangian expression turns out to be:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+\sum_{i=1}^n(C-\alpha_i-\mu_i)\xi_i\\\;\;\;\;-\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i^t)\cdot w\\\;\;\;\;+\sum_{i=1}^n\alpha_i\cdot y_i\cdot b\\\;\;\;\;+\sum_{i=1}^n\alpha_i\end{array}$$  
>
>[4]To get the maximum of $L$ at $\alpha$ and $\xi$, below constraints must be satisfied for all $i$:  
>&#10112;$\frac{\partial L}{\partial w}=0$, &#10113;$\frac{\partial L}{\partial b}=0$, &#10114;$\frac{\partial L}{\partial \xi}=0$, for all $i$:  
>&#10112;we have $w$ in below expression:  
$$\begin{array}{l}w^t-\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i^t)=0\\\Leftrightarrow w=\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i)\end{array}$$  
>&#10113;implies $\sum_{i=1}^n\alpha_i\cdot y_i=0$  
>&#10114;we have $\sum_{i=1}^nC-\alpha_i-\mu_i=0$, then for all $i$, $C-\alpha_i-\mu_i=0$ just holds.  
>
>[5]Notes that $\alpha_i\geq0$, $\mu_i\geq0$, therefore, we have <font color="OrangeRed">$0\leq\alpha_i\leq C$</font>,  
>$\alpha_i$ is now <font color="OrangeRed">upper bounded</font> by <font color="OrangeRed">$C$</font>.  
>
>[6]Substituting &#10112;, &#10113;, &#10114; to $L(w,b,\xi,\alpha,\mu)$, then, we have:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+\sum_{i=1}^n0\cdot\xi_i\\\;\;\;\;-w^t\cdot w+0\cdot b\\\;\;\;\;+\sum_{i=1}^n\alpha_i\\=\sum_{i=1}^n\alpha_i-\frac12\cdot w^t\cdot w\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$  
<!-- $$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+\sum_{i=1}^n0\cdot\xi_i\\\;\;\;\;-w^t\cdot w+0\cdot b\\\;\;\;\;+\sum_{i=1}^n\alpha_i\end{array}$$ -->
<!-- $$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\sum_{i=1}^n\alpha_i-\frac12\cdot w^t\cdot w\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$ -->
>
>[7]To maximize $L(w,b,\xi,\alpha,\mu)$ for the <font color="DeepSkyBlue">optimal $\alpha_i$ value</font>, then, we formulate the lagrangian as:  
$$\begin{array}{l}\underset\alpha{min}L(w,b,\xi,\alpha,\mu)\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$  
>, subject to:  
>&#10112;$\sum_{i=1}^n\alpha_i\cdot y_i=0$  
>&#10113;<font color="OrangeRed">$0\leq\alpha_i\leq C$</font> for all $i$  

### Introduction To The <font color="Red">KKT</font> Condition
>[1]The <font color="Red">KKT</font> optimality conditions of the formula in our problem are:  
>&#10112;the gradient of $L(w,b,\xi,\alpha,\mu)$ with respect to $w$, $b$, $\xi$ vanish, $\frac{\partial L}{\partial w}=0$, &#10113;$\frac{\partial L}{\partial b}=0$, &#10114;$\frac{\partial L}{\partial \xi}=0$  
>&#10113;$\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)+\xi_i-1)=0$  
>&#10114;$\mu_i\cdot\xi_i$  
>where <font color="#DeepPink">&#10113;+&#10114; guarantees that $\xi$ will have the smallest impact on $(w^t\cdot x_i-b)-1$</font>.  
>
>[2]By <font color="Red">KKT</font> conditions, there exists 3 cases to be evaluated by below constraints:  
>&#10112;$\frac{\partial L}{\partial \xi}=C-\alpha_i-\mu_i=0$  
>&#10113;$\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)+\xi_i-1)=0$  
>from which, this paragraph would guide you through the deduction process.    
>
>[3]Remember that we have <font color="OrangeRed">$0\leq\alpha_i\leq C$</font> for all $i$.  
>[case 1]$\alpha_i=0$, then, we are at the boundary:  
>$\mu_i=C-\alpha_i=C>0$, by $\mu_i\cdot\xi_i=0$, we have $\xi_i=0$, thus,  
><font color="#DeepPink">$y_i\cdot(w^t\cdot x_i-b)-1\geq0$</font> just holds.  
>
>[case 2]$0<\alpha_i<C$, the case of non-boundary.  
>then, $\mu_i=C-\alpha_i>0$, by $\mu_i\cdot\xi_i=0$, again, we have $\xi_i=0$, then,  
>$y_i\cdot(w^t\cdot x_i-b)+\xi_i-1=0$,  
>therefore, <font color="#DeepPink">$y_i\cdot(w^t\cdot x_i-b)-1=0$</font>.  
>
>[case 3]$\alpha_i=C$, also, the boundary case.
>then, $\mu_i=C-\alpha_i=0$, by $\mu_i\cdot\xi_i=0$, we have $\xi_i\geq0$, then,  
>$y_i\cdot(w^t\cdot x_i-b)+\xi_i-1=0$,  
>$y_i\cdot(w^t\cdot x_i-b)-1\leq0$ just holds, more precisely, it should be:  
><font color="#DeepPink">$y_i\cdot(w^t\cdot x_i-b)-1\leq\-xi_i$</font>...by mjtsai  
>
>[4]Continue the deduction on the condition term to be regularized by $\alpha_i$ in the most original objective function.  
>$y_i\cdot(w^t\cdot x_i-b)-1$  
>$=y_i\cdot(w^t\cdot x_i-b)-y_i^2$  
>$=y_i\cdot((w^t\cdot x_i-b)-y_i)$  
>$=y_i\cdot E_i$...$E_i=u_i-y_i$  
>$=R_i$...$u_i=w^t\cdot x_i-b$  
>
>Let's summarize the <font color="#DeepPink">KKT conditions</font>:
>&#10112;$\alpha_i=0$, $R_i\geq0$  
>&#10113;$0<\alpha_i<C$, $R_i\approx0$  
>&#10114;$\alpha_i=C$, $R_i\leq0$  
>
>[5]Below lists the <font color="OrangeRed">KKT violating cases</font>:  
>&#10112;$\alpha_i<C$ and $R_i<0$  
>&#10113;$\alpha_i>0$ and $R_i>0$
>&#10114;$\alpha_i=0$ and $R_i>0$...by mjtsai


<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->

<!-- <font color="#DeepPink">positive conclusion, finding</font> -->
<!-- <font color="DimGray">negative conclusion, finding</font> -->

<!-- <font color="Green">value iteration</font> -->
<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->
