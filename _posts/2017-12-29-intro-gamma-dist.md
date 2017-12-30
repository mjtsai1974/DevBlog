---
layout: post
title: Introduction To The Gamma Distribution
---

## Prologue To The Gamma Distribution
<p class="message">
In probability theory and statistics, the gamma distribution is the most foundamental, which is based on for further development of many distributions, they are beta, exponential, F, chi-square, t distributions and still others.
With the basic intuition of gamma distribution would it be greatly helpful in the evaluation of the regression model build on your hypothesis, even more, the power of test for the precision in the machine learning results.   
</p>

### The Gamma Function <font color="Red">$\Gamma$</font>
>It is very important in the gamma distribution, first of all, we take not only a glance over it, but go through some of the major properties of it.  The gamma function comes in definition:  
>$\Gamma(\alpha)$=$\int_0^\infty x^{\alpha-1}\cdot e^{-x}\operatorname dx$, where $\alpha>0$.  
>
>Taking advantage of <font color="DeepSkyBlue">integration by part</font>:  
>Let $u=x^{\alpha-1}$, $\operatorname dv$=$e^{-x}\operatorname dx$, then,  
>$\operatorname du$=$(\alpha-1)\cdot x^{\alpha-2}$, $v$=$-e^{-x}$.  
>
>$\Gamma(\alpha)$=$x^{\alpha-1}\cdot(-e^{-x})\vert_0^\infty$-$\int_0^\infty -e^{-x}\cdot (\alpha-1)\cdot x^{\alpha-2}\operatorname dx$  
>$\;\;\;\;\;\;\;$=$0$+$\int_0^\infty e^{-x}\cdot (\alpha-1)\cdot x^{\alpha-2}\operatorname dx$  
>$\;\;\;\;\;\;\;$=$(\alpha-1)\cdot\int_0^\infty e^{-x}\cdot x^{\alpha-2}\operatorname dx$  
>$\;\;\;\;\;\;\;$=$(\alpha-1)\cdot\Gamma(\alpha-1)$  
>
>$\Gamma(5)=4\cdot\Gamma(4)$, therefore, we can deduce it out that: 
>$\Gamma(\alpha)$=$(\alpha-1)\cdot\Gamma(\alpha-1)$  
>$\;\;\;\;\;\;\;$=$(\alpha-1)\cdot(\alpha-2)\cdot\Gamma(\alpha-2)$=$\cdots$  
>
>[1]the corollary has it that:  
>$\Gamma(n)$=$(n-1)\cdot(n-2)\cdot(n-3)\cdots\Gamma(1)$  
>,where $\Gamma(1)$=$\int_0^\infty x^0\cdot e^{-x}\operatorname dx$=$-e^{-x}\vert_0^\infty$=$1$  
>, thus, <font color="DeepPink">$\Gamma(n)=(n-1)!$</font> is obtained. 
>
>[2]$\Gamma(\frac{1}{2})$=$\sqrt{\mathrm\pi}$  
>There exists some alternatives, either way could be:  
>proof::&#10112;  
>As we don't like $-\frac{1}{2}$, by means of <font color="DeepSkyBlue">change unit</font>,  
>let $x$=$u^2$, then, $\operatorname dx$=$2\cdot u\operatorname du$:  
>$\Gamma(\frac{1}{2})$=$\int_0^\infty x^{-\frac{1}{2}}\cdot e^{-x}\operatorname dx$  
>$\;\;\;\;\;\;\;$=$\int_0^\infty u^{-1}\cdot e^{-u^{2}}\cdot 2\cdot u\operatorname du$  
>$\;\;\;\;\;\;\;$=$2\cdot\int_0^\infty e^{-u^{2}}\operatorname du$  
>
>Take $I$=$\int_0^\infty e^{-u^{2}}\operatorname du$, then,  
>$I^2$=$\int_0^\infty e^{-x^{2}}\operatorname dx$&nbsp;$\int_0^\infty e^{-y^{2}}\operatorname dy$  
>$\;\;\;\;$=$\int_0^\infty\int_0^\infty e^{-(x^{2}+y^{2})}\operatorname dx\operatorname dy$  
>
>Guess what?  We just transform our integral to the <font color="OrangeRed">quadrant one</font>.  
>Take $r^2$=$x_2$+$y_2$, we can have below two sets of deduction:  
>&#10112;$\frac{\operatorname dr^2}{\operatorname dx}$=$\frac{\operatorname d(x^2+y^2)}{\operatorname dx}$=$2\cdot x$  
>$\Rightarrow\operatorname dr^2$=$2\cdot x\operatorname dx$  
>
>&#10113;$\frac{\operatorname dr^2}{\operatorname dr}$=$\frac{\operatorname d(x^2+y^2)}{\operatorname dr}$  
>$\Rightarrow 2\cdor r$=$\frac{\operatorname d(x^2+y^2)}{\operatorname dr}$  
>$\Rightarrow 2\cdor r\operatorname dr$=$\operatorname d(x^2+y^2)$  
>$\Rightarrow 2\cdor r\frac{\operatorname dr}{\operatorname dx}$=$2\cdot x$  
>$\Rightarrow r\operatorname dr$=$x\operatorname dx$  
>
>Stems from 

>proof::&#10113;  
>

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
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