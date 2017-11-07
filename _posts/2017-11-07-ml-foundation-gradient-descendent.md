---
layout: post
title: Gradient Descendent
---

## Gradient Descendent
<p class="message">
Most widely used in machine learning with respect to linear regression, logistic regression for supervised learning.  But, the gradient descendent itself actually knows nothing when to stop!!    
</p>

### Begin from Cost Function in Simple Linear Regressoin(S.L.R)
>take the cost function J(&Theta;) = (1 ∕ (2m))&sum;<sub>i</sub>(h<sub>&Theta;</sub>(x<sup>(i)</sup>) − y<sup>(i)</sup>)<sup>2</sup>, where the purpose of S.L.R is to minimize J(&Theta;).  
>given h<sub>&Theta;</sub>(x) = &Theta;<sup>t</sup> &sdot; x, where &Theta; = [&Theta;<sub>1</sub> &Theta;<sub>2</sub>]<sup>t</sup> is the coefficients, x = [x<sub>1</sub> x<sub>2</sub>]<sup>t</sup> is the input data and x<sub>1</sub> = 1, it is the intercept, or the bias term.  
>as to the divide by 2m is an artificial design:  
>&#10112;1 ∕ 2 is to eliminate the power of 2 in the square, after differentiation is taken.  
>&#10113;1 ∕ m is to average all squared errors of m input rows of data.

### Step into Gradient &nabla; of J(&Theta;)
>take derivation of J(&Theta;) on &Theta;<sub>j</sub>, then we obtain:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-07-ml-found-gradient-descendent-size-m.png "m records of input data")

>in gradient descendent, 1 ∕ m is required to average it.
>if m = 1, then, we just have the j-th term as:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-07-ml-found-gradient-descendent-size-1.png "single input data")

>since we are running batch gradient descendent

### Learning Rate &alpha;
