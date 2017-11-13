---
layout: post
title: Binary and Multiple Classification
---

## Classification
<p class="message">
Classificatiuon could be categorized into two major variety, they are binary and multiple classifications.  
The major purpose of binary classification is to identify an object as two mutual exclusive identity by means of logistic regression.  
The multiple regression comes out with a wider rage of identity, might be 0, 1, 2, 3,...n, nevertheless, it is using one versus all, 
which is the same algorithm of binary classification.
</p>

### Binary Classification
>Given input data of size n, binary classification is to classify it to be true or false, or identity of another alternative, 0 and 1, and still further.  
>Before we step into multiple classification, a full illustration of the logistic regression model is mandatory.

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-13-ml-found-binary-multiple-classification-BC.png "binary classification")

### Why We Need The Logistic Regression Model?
>Suppose we'd like to classify the given input data as 0 or 1, in example of tumor size identification of maligant or benight.  
>We are given m records of tumor history and come out the fitted linear regression line in grapg labeled &#10112;, where m-1 th record is identified as non-maligant($Y=0$).

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-13-ml-found-binary-multiple-classification-tumor-non-maligant.png "m-1 record is non-maligant")

>After record m+1, m+2 have been added to the given sample, we get the new fitted regression line in graph labeled &#10113;, watch out that <font color="red">m-1 th record is now identified as maligant($Y=1$)!!!</font>

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-13-ml-found-binary-multiple-classification-tumor-maligant.png "m-1 record is now maligant after new records added in the same")

><font color="blue">Caution must be made that by tradition, the fitted linear regression line could be biased with the input sample and $h_\theta(x)>1\;or\;<\;0$ could happen.</font>  What we want for binary classification in this example is to classify  
$$\left\{\begin{array}{l}Y=1,\;h_\theta(x)\geq0.5\\Y=0,\;h_\theta(x)<0.5\end{array}\right.$$
>The linear regression model is likely to have $h_\theta(x)>1\;or\;<\;0$; while <font color="green">the logistic regression model has $0\leq h_\theta(x)\leq1$!!!</font>

### The Logistic Regression Function
>It is also named as the sigmoid function, and defined as:
$$h_\theta(x)=\frac1{1+e^{-\theta^t\cdot x}},\;where\;\left\{\begin{array}{l}\theta\in R^n,\;M_{n\times1}\\x\in R^n,\;M_{n\times1}\end{array}\right.$$

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-13-ml-found-binary-multiple-classification-logistic-regression-function.png "the logistic regression function")

>&#10112;$h_\theta(x)=P(Y=1\vert x;\theta),\;the\;probablity\;of\;Y=1\;given\;x\;and\;\theta$  
>&#10113;$\P(Y=1\vert x;\theta)+P(Y=0\vert x;\theta)=1$  
>&#10114;$\P(Y=1\vert x;\theta)=1-P(Y=0\vert x;\theta)$  