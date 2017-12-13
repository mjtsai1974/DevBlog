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
>[1]Suppose we'd like to have a hyperplane with a safeguard that can classify the given data sample.  
>&#10112;we formulate our problem as:  
>$\underset w{min}\frac12w^t\cdot w$, subject to $y_i\cdot(w^t\cdot x_i-b)\geq1,\forall i$.  
>The first part is the <font color="green">target</font>, the second part is the <font color="red">constraint</font>.  
>&#10113;then, introduce $\alpha_1,\alpha_2,\dots\alpha_n$ to be the lagrange multiplier and express in below lagrangian to be our <font color="deepink">objective function</font>:  
$$L(w,b,\alpha)=\frac12w^t\cdot w-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)-1)$$  
>&#10114;next to regularize the objective function, to get the optimal $\alpha$, we should take partial derivatives of $L$ on $w$, $b$ respectively and equate them to zero.  Finally, we get:  
$$\begin{array}{l}L(w,b,\alpha)\\=-\frac12\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot(x_i^t\cdot x_j)\\+\sum_{i=1}^n\alpha_i\end{array}$$  
>where $w=\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i$.  
>By such design guarantees that we could have <font color="green">$\forall\alpha_i>0$</font>, one basic condition must be satisfied in SMO.  
>
>[2]
>

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