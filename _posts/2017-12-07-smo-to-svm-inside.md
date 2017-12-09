---
layout: post
title: Inside Support Minimal Optimization
---

## Inside Sequential Minimal Optimization
<p class="message">
SMO(Sequential Minimal Optimization) is the regularization process by optimization in accordance to the rule that can minimize the cost error of the objective function sequentially. 
</p>

### Departure With Noise
>We'd like to begin from the imperfect separation, since no sampling is fully qualified and could be well separated.  Given the support vector formulated problem expressed in terms of $\alpha_i$, $y_i$, $x_i$; then the objective function:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$  
>for all i, $0<\alpha_i<C$  

### Works On 2 $\alpha$'s At A Time
>The algorithm of SMO works by <font color="OrangeRed">manipulating 2 $\alpha$'s at a time(with others fixed)</font>, a little <font color="OrangeRed">hill climbing</font> alike approach.  By <font color="OrangeRed">heuristics</font> to choose 2 $\alpha$'s at a time.  
>
>Begin by given $\alpha_i=0$ for $i=1$ to $n$.  Suppose we randomly choose $\alpha_1$, $\alpha_2$ and denote it as <font color="RoyalBlue">$\alpha_1^{old}$</font>, <font color="RoyalBlue">$\alpha_2^{old}$</font>.  
>Due to $\sum_{i=1}^n\alpha_i\cdot y_i=0$, therefore we have:  
>$y_1\cdot \alpha_1+y_2\cdot \alpha_2=y_1\cdot \alpha_1^{old}+y_2\cdot \alpha_2^{old}$  
>This confines the optimization of $\alpha_1$, $\alpha_2$ is on a line.  
>
>Next to examine the relation in between of these 2 $\alpha_1$, $\alpha_2$ of <font color="RoyalBlue">old</font> or <font color="Green">new</font>.  
>&#10112;for $y_1\neq y_2$, then, $\alpha_1-\alpha_2=r$, where $r$ is a constant.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-07-smo-to-svm-inside-alphas-on-line-1.png "2 alphas on a line")

>&#10113;for $y_1=y_2$, then, $\alpha_1+\alpha_2=r$.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-07-smo-to-svm-inside-alphas-on-line-2.png "2 alphas on a line")

>Take $S=y_1\cdot y_2$, multiply $y_1\cdot \alpha_1+y_2\cdot \alpha_2=const$ by $y_1$, then,  
>$\alpha_1+S\cdot \alpha_2=const$, we have:  
>$\alpha_1=const-S\cdot \alpha_2$,  
>where $\alpha_1+S\cdot \alpha_2=\alpha_1^{old}+S\cdot \alpha_2^{old}$.  
>
>Next to optimize $\alpha_1$, $\alpha_2$ with <font color="OrangeRed">other $\alpha$'s fixed</font>, the objective function could be rewritten as:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\alpha_1+\alpha_2+const\\-\frac12\cdot(part\;1+par\;2)\end{array}$$  
>  
>&#10112;we further express $part\;1$:  
$$\begin{array}{l}part\;1\\=\sum_{i,j=1,2}\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\\=\alpha_1^2\cdot y_1^2\cdot x_1^t\cdot x_1\\\;\;+\alpha_2^2\cdot y_2^2\cdot x_2^t\cdot x_2\\\;\;+2\cdot\alpha_1\cdot\alpha_2\cdot y_1\cdot y_2\cdot x_1^t\cdot x_2\end{array}$$  
>
>&#10113;we express $part\;2$ as:  
$$\begin{array}{l}part\;2\\=\sum_{i=3;j=1,2}^{j=n}\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\\\;\;+\sum_{i=1,2;j=3}^{j=n}\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\\=2\cdot(\sum_{i=3}^n\alpha_i\cdot y_i\cdot x_i^t)\cdot(\alpha_1\cdot y_1\cdot x_1+\alpha_2\cdot y_2\cdot x_2)\end{array}$$  

### Express $\alpha_1$ In Terms Of $\alpha_2$
>Next to express $\alpha_1$ in terms of $\alpha_2$, this is a quiet painful and confused process, it took me some while, now I'd like to share you with my viewpoint in each step in the deduction.  
>
>From current objective function, some symptoms could be found that $x_i$ is associasted with $x_j$.  
>Thus, we take $K_{11}=x_1^t\cdot x_1$, $K_{22}=x_2^t\cdot x_2$, $K_{12}=x_1^t\cdot x_2$.  
>
>Recall that it is deduced out by removing the <font color="RoyalBlue">old</font> $\alpha_1$, $\alpha_2$ associated terms from the term $w$, here comes the question, can we relate the <font color="RoyalBlue">old</font> $w$ to the <font color="Green">new evolved</font> $\alpha_1$, $\alpha_2$?  
$$\begin{array}{l}V_j=\sum_{i=3}^n\alpha_i\cdot y_i\cdot x_i^t\cdot x_j\\=(w^{old})^t\cdot x_j-\alpha_1^{old}\cdot y_1\cdot x_1^t\cdot x_j\\\;\;\;\;-\alpha_2^{old}\cdot y_2\cdot x_2^t\cdot x_j\\=(w^{old})^t\cdot x_j-b^{old}+b^{old}\\\;\;\;\;-\alpha_1^{old}\cdot y_1\cdot x_1^t\cdot x_j\\\;\;\;\;-\alpha_2^{old}\cdot y_2\cdot x_2^t\cdot x_j\\=U_j+b^{old}\\\;\;\;\;-\alpha_1^{old}\cdot y_1\cdot x_1^t\cdot x_j\\\;\;\;\;-\alpha_2^{old}\cdot y_2\cdot x_2^t\cdot x_j\end{array}$$  
>
>where $U_j=(w^{old})^t\cdot x_j-b^old$ is the output of $x_j$ under the old parameters, $w^{old}$, $b^{old}$.  Expression in this way with a hope to refine original objective function.  
>
>In order to make it the point, the subscript os the term indicates the index, usually in this proof, they are $i$,$j$ or $1$,$2$..., the superscript is ued for the identity of <font color="RoyalBlue">old</font> or <font color="Green">new clipped</font> term.  
>For the simplicity of the deduction and understanding, if no any word like <font color="RoyalBlue">old</font>, <font color="Green">new</font> in the superscript, then, the term is treated as <font color="RoyalBlue">old</font> term.  
>
>Deduce by replacing above terms in the objective function:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)=\alpha_1+\alpha_2-\frac12\cdot(\\\;\;\;\;K_{11}\cdot\alpha_1^2+K_{22}\cdot\alpha_2^2+2\cdot S\cdot K_{12}\cdot\alpha_1\cdot\alpha_2+\\\;\;\;\;2\cdot\alpha_1\cdot y_1\cdot V_1+2\cdot\alpha_2\cdot y_2\cdot V_2)\end{array}$$  
>

### Introduction Of $\eta$
>

### Feasible Rangle Of New $\alpha$ Value
>

### Clip New $\alpha$
>

### SMO Updating
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