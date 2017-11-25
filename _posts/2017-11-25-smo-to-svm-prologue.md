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

### Separating Hyperplane with Minimum Safe Guard
>Furthermore, we want this hyperplane to have <font color="green">the minimum separating margin</font> with respect to <font color="red">the two classes</font>.

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-25-svm-prologue-binary-classification.png "SVM for binary classification")

>




