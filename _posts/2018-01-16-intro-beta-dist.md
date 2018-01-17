---
layout: post
title: Introduction To The Beta Distribution
---

## Prologue To The <font color="Red">Beta</font> Distribution
<p class="message">
In probability theory and statistics, base on the most fundamental gamma distribution, <font color="Red">beta</font> distribution is one of the many models of distributions further developed.  
With the basic realization of gamma distributions, we could also treat the <font color="Red">beta</font> function a <font color="DeepSkyBlue">special combination of gamma</font> functions.  
It would be greatly helpful in the evaluation of the regression model build on your hypothesis, the power of test for the precision in the machine learning results.  
</p>

### Begin From The <font color="Red">Beta</font> Function
>We formulate the <font color="Red">beta</font> function in below two expressions:  
>$\beta(x,y)$=$\int_{0}^{\infty}t^{x-1}\cdot(1+t)^{-x-y}\operatorname dt$...(1);  
>$\beta(x,y)$=$\int_{0}^{1}t^{x-1}\cdot(1-t)^{y-1}\operatorname dt$...(2);  
>Where (1)=(2), next to prove it.  
>
>proof:  
>&#10112;to change from $\int_{0}^{\infty}$ to $\int_{0}^{1}$, we focus on $t$:  
>$\int_{0}^{\infty}t^{x-1}\cdot(1+t)^{-x-y}\operatorname dt$  
>$=\int_{0}^{\infty}t^{x-1}\cdot\(frac {1}{1+t})^{x+y}\operatorname dt$  
>$=\int_{0}^{\infty}(\frac {t}{1+t})^{x-1}\cdot(\frac {1}{1+t})^{y+1}$
>
>&#10113;take $w$=$\frac {t}{1+t}$, then $1-w$=$\frac {1}{1+t}$  
>$w$=$1-\frac {1}{1+t}$=$1-(1+t)^{-1}$  
>$\Rightarrow\frac {\operatorname dw}{\operatorname dt}$=$(\frac {1}{1+t})^{2}$  
>$\Rightarrow \operatorname dw$=$(\frac {1}{1+t})^{2}\cdot\operatorname dt$=$(1+t)^{-2}\cdot\operatorname dt$  
>$\Rightarrow \operatorname dt$=$(1+t)^{2}\cdot\operatorname dw$  
>
>&#10114;<font color="DeepPink">$\lim_{t\rightarrow\infty}\frac t{1+t}=1$</font>, therefore <font color="DeepSkyBlue">$\int_{0}^{\infty}\operatorname dt$ transforms to $\int_{0}^{1}\operatorname dw$ is reasonable</font>, it says that integration from $0$ to $\infty$ could be changed to integration from $0$ to $1$.  
>
>$\int_{0}^{\infty}(\frac {t}{1+t})^{x-1}\cdot(\frac {1}{1+t})^{y+1}$  
>$=\int_{0}^{1}w^{x-1}\cdot(1-w)^{y+1}\cdot(1+t)^{2}\operatorname dw$  
>
>, where $1-w$=$(1+t)^{-1}$, and we have it that:  
>$(1+t)^{2}$=$((1+t)^{-1})^{-2}$=$(1-w)^{-2}$  
>therefore,  
>$=\int_{0}^{1}w^{x-1}\cdot(1-w)^{y+1}\cdot(1-w)^{-2}\operatorname dw$  
>$=\int_{0}^{1}w^{x-1}\cdot(1-w)^{y-1}\operatorname dw$  
>
>In some textbooks or web articles, they intend to use the form:  
>$\beta(x,y)$=$\int_{0}^{1}t^{x}\cdot(1-t)^{y}\operatorname dt$  
>The tiny difference mainly in the input parameters, $x\ge 1$, $y\ge 1$.  

### The Definition Of The <font color="Red">Beta</font> Function
>Next come to visit the definition of the <font color="Red">beta</font> function.  
>$\beta(x,y)$=$\frac {\Gamma(x)\cdot\Gamma(y)}{\Gamma(x+y)}$...by definition  
>
>proof:  
>&#10112;  
>$\Gamma(x)\cdot\Gamma(y)$  
>$=\int_{0}^{\infty}u^{x-1}\cdot e^{-u}\operatorname du\cdot\int_{0}^{\infty}v^{y-1}\cdot e^{-v}\operatorname dv$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}u^{x-1}\cdot v^{y-1}\cdot e^{-u-v}\operatorname du\operatorname dv$  
>
>&#10113;take $u$=$v\cdot t$, then $\operatorname du$=$v\cdot\operatorname dt$  
>why? <font color="OrangeRed">Because gamma function focus on the parameter of power, not integral itself</font>. Expand from &#10112;:  
>
>$\int_{0}^{\infty}\int_{0}^{\infty}u^{x-1}\cdot v^{y-1}\cdot e^{-(u+v)}\operatorname du\operatorname dv$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}v\cdot (v\cdot t)^{x-1}\cdot v^{y-1}\cdot e^{-(v\cdot t+v)}\operatorname dt\operatorname dv$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}t^{x-1}\cdot v^{x+y-1}\cdot e^{-(v\cdot t+v)}\operatorname dt\operatorname dv$  
>
>&#10114;take $w$=$v\cdot t+v$, then we have:  
>$v$=$\frac {w}{1+t}$, $\operatorname dv$=$\frac {1}{1+t}\cdot\operatorname dw$  
>
>$\int_{0}^{\infty}\int_{0}^{\infty}t^{x-1}\cdot v^{x+y-1}\cdot e^{-(v\cdot t+v)}\operatorname dt\operatorname dv$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}t^{x-1}\cdot (\frac {w}{1+t})^{x+y-1}\cdot e^{-w}\operatorname dt\frac {1}{1+t}\cdot\operatorname dw$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}t^{x-1}\cdot (\frac {1}{1+t})^{x+y}\cdot w^{(x+y-1)}\cdot e^{-w}\operatorname dt\operatorname dw$  
>$=\int_{0}^{\infty}w^{(x+y-1)}\cdot e^{-w}\operatorname dw\cdot\int_{0}^{\infty}t^{x-1}\cdot(\frac {1}{1+t})^{x+y}\operatorname dt$  
>$=\Gamma(x+y)\cdot\int_{0}^{\infty}t^{x-1}\cdot (1+t)^{-x-y}\operatorname dt$  
>
>$\beta(x,y)$  
>$=\Gamma(x+y)\cdot\int_{0}^{\infty}t^{x-1}\cdot (1+t)^{-x-y}\operatorname dt$  
>$=\frac {\Gamma(x)\cdot\Gamma(y)}{\Gamma(x+y)}$  

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- \overline{X_n} -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha</font> -->
<!-- <font color="Green">new alpha</font> -->

<!-- <font color="DeepPink">positive conclusion, finding</font> -->
<!-- <font color="RosyBrown">negative conclusion, finding</font> -->

<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->