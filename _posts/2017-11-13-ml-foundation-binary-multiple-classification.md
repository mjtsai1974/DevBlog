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

>We can then have $h_\theta(x)=P(Y=1\vert x;\theta),\;the\;probablity\;of\;Y=1\;given\;x\;and\;\theta$  
>&#10112;$P(Y=1\vert x;\theta)+P(Y=0\vert x;\theta)=1$  
>&#10113;$P(Y=1\vert x;\theta)=1-P(Y=0\vert x;\theta)$  

### The Logistic Regression Cost Function
>Can we re-using the cost function in linear regression model, $J(\theta)=\frac1{2m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2$ to be the logistic version of cost function?  The answer is <font color="red">no!!!</font>  Because the gradient descendent wouldn't be a smooth convex curve.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-13-ml-found-binary-multiple-classification-LRM-CF-not-fit.png "the sigmoid gradient descendent curve not a convext curve")

>The major purpose of the cost function is to reduce the error of the model and gradient descendent could then be applied on to get the $\theta$ that can really have <font color="red">the smallest error.</font>  
>Two key points must be clarified:  
>&#10112;when $P(Y=1)\approx1$, the error from 1 for $P(Y=1)\approx0$
>&#10113;when $P(Y=0)\approx0$, the error from 0 for $P(Y=0)\approx0$
>We thus define the cost function as:  
$$\left\{\begin{array}{l}-\log(h_\theta(x)),\;for\;Y=1\\-\log(1-h_\theta(x)),\;for\;Y=0\end{array}\right.$$
><font color="red">Why do we use log?</font>  Please recall $\log1=0$, whenever $h_\theta(x)\approx1$ or $h_\theta(x)\approx0$.  
><font color="red">Why to have a minus sign?</font>  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-13-ml-found-binary-multiple-classification-logistic-regression-cost-function.png "logistic regression cost function")
