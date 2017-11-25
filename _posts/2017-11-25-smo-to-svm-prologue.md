---
layout: post
title: From Sequential Minimum Optimization To Support Vector Machine
---

## Prologue To Support Vector Machine
<p class="message">
Given training data set of size $n$, where they are {($x_1$, $y_1$), ($x_2$, $y_2$),...,($x_n$, $y_n$)}, $\forall x_i\in R^d$, $\forall y_i\in\{+1,-1\}$.  
Supposed these data could be classified and we'd like to learn a <font color="green">hyperplane classifier</font>:  
$$f(x)=sign(w^t\cdot x-b)$$
</p>

### Separating Hyperplane With Minimum Safe Guard
>Furthermore, we want this hyperplane to have <font color="green">the minimum separating margin</font> with respect to <font color="red">the two classes</font>.

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-25-svm-prologue-binary-classification.png "SVM for binary classification")

>Specifically, if all goes well, there shall exist no data points in between $h_1$ and $h_2$.  
$$\begin{array}{l}H:w^t\cdot x-b=0\\H_1:w^t\cdot x-b=1\\H_2:w^t\cdot x-b=-1\\\\\end{array}$$

>For any separaing $H$ and the corresponding $H_1$ and $H_2$, we can solve by <font color="red">normalizing</font> the coefficient vector $w$, such that $H_1$ and $H_2$ exist.  
>proof:  
>&#10112;suppose $H_1:a^t\cdot x-b_1=0$ and $H_1:a^t\cdot x-b_2=0$ are two <font color="blue">parallel</font> hyperplanes.  Since they are parallel, they can have the same weight $a$.  
>&#10113;take $\overline b=\frac{b_1+b_2}2$ and $\delta=b_1-\overline b=\overline b-b_2$  
$$\begin{array}{l}\therefore H_1:a^t\cdot x-(\delta+\overline b)=0\\\;\;\;\;H_2:a^t\cdot x-(\overline b-\delta)=0\\\therefore H_1:a^t\cdot x-\overline b=\delta\\\;\;\;\;H_2:a^t\cdot x-\overline b=-\delta\\\end{array}$$
>&#10114;then, divide both equality by $\delta$, we obtain:  
$$\begin{array}{l}H_1:\frac{a^t}\delta\cdot x-\frac{\overline b}\delta=1\\H_2:\frac{a^t}\delta\cdot x-\frac{\overline b}\delta=-1\\\\\end{array}$$
>&#10115;take $w=\frac{a^t}\delta$ and $b=\frac{\overline b}\delta$, could we get our expected $H_1$ and $H_2$.
