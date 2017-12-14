---
layout: post
title: SMO Framework And Algorithm
---

## SMO Framework And Algorithm
<p class="message"> 
SMO algorithm is the realization of updating mandatory coefficients in the objective function based on the long and tedious deduction with a hope to regularize 
by optimization in accordance to the KKT rules that can sequentially costruct the boundarys of the safeguard. 
</p>

### SMO Framework
>Let me make a brief summary of the major points from the initial idea to the end of the deduction of the objective function.  
>
>[1]Suppose we'd like to have a hyperplane with a safeguard that can classify the given data sample.  
>&#10112;we formulate our problem as:  
>$\underset w{min}\frac12w^t\cdot w$, subject to $y_i\cdot(w^t\cdot x_i-b)\geq1,\forall i$.  
>The first part is the <font color="green">target</font>, the second part is the <font color="red">constraint</font>.  
>&#10113;then, introduce $\alpha_1,\alpha_2,\dots\alpha_n$ to be the lagrange multiplier and express in below lagrangian to be our <font color="deepink">objective function</font>:  
$$L(w,b,\alpha)=\frac12w^t\cdot w-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)-1)$$  
>&#10114;next to regularize the objective function, to get the optimal $\alpha$, we should take partial derivatives of $L$ on $w$, $b$ respectively and equate them to zero.  Finally, we get:  
$$\begin{array}{l}L(w,b,\alpha)\\=-\frac12\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot(x_i^t\cdot x_j)\\+\sum_{i=1}^n\alpha_i\end{array}$$  
>where $w=\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i$.  
>
>By such design guarantees that we could have <font color="green">$\forall\alpha_i>0$</font>, one basic condition must be satisfied in SMO.  

>[2]Next to the imperfect separation with <font color="OrangeRed">noise</font>.  There exists some condition that we don't strictly enforce that <font color="OrangeRed">no</font> data points in between $H_1$ and $H_2$.  We can extend SVM to allow some <font color="OrangeRed">noise</font>(data points) in between the safeguard zone.  Thus, we want to <font color="OrangeRed">penalize</font> the data points that cross the boundaries($H_1$,$H_2$).  
>&#10112;we formulate our problem as:  
>$\underset{w,\xi_i}{min}\left[w^t\cdot w+C\cdot\sum_{i=1}^n\xi_i\right]$,  
><font color="OrangeRed">subject to</font> $y_i\cdot(w^t\cdot x_i-b)+\xi_i-1\geq0$, $\forall\xi_i\geq0$  
>Such design is to <font color="OrangeRed">shrink down</font> the distance between $H_1$ and $H_2$, thus <font color="DeepSkyBlue">to allow some noise within original margin</font>.  
>&#10113;next to build the lagrangian by introducing $\alpha_1$, $\alpha_2$,..., $\alpha_n$ and $\mu_1$, $\mu_2$,..., $\mu_n$, then:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+C\cdot\sum_{i=1}^n\xi_i\\\;\;\;\;-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)+\xi_i-1)\\\;\;\;\;-\sum_{i=1}^n\mu_i\cdot\xi_i\end{array}$$  
>The lagrangian expression turns out to be:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+\sum_{i=1}^n(C-\alpha_i-\mu_i)\xi_i\\\;\;\;\;-\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i^t)\cdot w\\\;\;\;\;+\sum_{i=1}^n\alpha_i\cdot y_i\cdot b\\\;\;\;\;+\sum_{i=1}^n\alpha_i\end{array}$$  
>&#10114;to get the maximum of $L$ at $\alpha$ and $\xi$, below constraints must be satisfied for all $i$:  
>$\frac{\partial L}{\partial w}=0$, $\frac{\partial L}{\partial b}=0$, $\frac{\partial L}{\partial \xi}=0$.  
>We have $w=\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i)$, $\sum_{i=1}^n\alpha_i\cdot y_i=0$,  
>and $\sum_{i=1}^nC-\alpha_i-\mu_i=0$, for all $i$, $C-\alpha_i-\mu_i=0$ just holds.  
>&#10115;to maximize $L(w,b,\xi,\alpha,\mu)$ for the <font color="DeepSkyBlue">optimal $\alpha_i$ value</font>, then, we formulate the lagrangian as:  
$$\begin{array}{l}\underset\alpha{min}L(w,b,\xi,\alpha,\mu)\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$  
>, subject to $\sum_{i=1}^n\alpha_i\cdot y_i=0$ and <font color="OrangeRed">$0\leq\alpha_i\leq C$</font> for all $i$  
>&#10116;Notes that $\alpha_i\geq0$, $\mu_i\geq0$, therefore, we have <font color="OrangeRed">$0\leq\alpha_i\leq C$</font>,  
>$\alpha_i$ is now <font color="OrangeRed">upper bounded</font> by <font color="OrangeRed">$C$</font>.  

>[3]Then, we make introduction to the <font color="Red">KKT</font> conditions:  
>&#10112;$\alpha_i=0$, $R_i\geq0$  
>&#10113;$0<\alpha_i<C$, $R_i\approx0$  
>&#10114;$\alpha_i=C$, $R_i\leq0$  
>Above <font color="Red">KKT</font> cases are evaluated by below constraints under <font color="OrangeRed">$0\leq\alpha_i\leq C$</font>:  
>&#10112;$\frac{\partial L}{\partial \xi}=C-\alpha_i-\mu_i=0$  
>&#10113;$\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)+\xi_i-1)=0$  
>
>Also, we give the <font color="OrangeRed">KKT violating cases</font>:  
>&#10112;$\alpha_i<C$ and $R_i<0$  
>&#10113;$\alpha_i>0$ and $R_i>0$  
>&#10114;$\alpha_i=0$ and $R_i>0$...by mjtsai  

>[4]



### SMO Algorithm
>

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha</font> -->
<!-- <font color="Green">new alpha</font> -->

<!-- <font color="DeepPink">positive conclusion, finding</font> -->
<!-- <font color="DimGray">negative conclusion, finding</font> -->

<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->

<!-- http://web.cs.iastate.edu/~honavar/smo-svm.pdf -->
<!-- http://cs229.stanford.edu/notes/cs229-notes3.pdf -->
<!-- https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-14.pdf -->

<!-- https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/ -->
<!-- https://machinelearningmastery.com/support-vector-machines-for-machine-learning/ -->