---
layout: post
title: Introduction To The Chi-Square Distribution
---

## Prologue To The Chi-Square Distribution
<p class="message">
In probability theory and statistics, base on the most fundamental gamma distribution, one of the many models of distributions further developed is the chi-square distribution.  
With the basic realization of gamma distribution, we can treat the chi-square distribution a special case of the gamma distribution.  
It would be greatly helpful in the evaluation of the regression model build on your hypothesis, the power of test for the precision in the machine learning results.   
</p>

### From The Gamma Distribution To The <font color="Red">Chi-Square</font> Distribution
>Be recalled that we have gamma function and the PDF of the gamma distribution:  
>&#10112;$\Gamma(\alpha)$=$\int_0^\infty x^{\alpha-1}\cdot e^{-x}\operatorname dx$, where $\alpha>0$.  
>&#10113;$f(x)=\frac {1}{\beta^{\alpha}\cdot\Gamma(\alpha)}\cdot x^{\alpha-1}\cdot e^{-\frac{x}{\beta}}$, where $\alpha>0$, $\beta>0$  
>
>Next, we take $\alpha=\frac\nu2$, $\beta=2$, we turn the PDF function into below expression:  
>$f(x)=\frac {1}{2^{\frac \nu2}\cdot \Gamma(\frac \nu2)}\cdot x^{\frac \nu2 -1}\cdot e^{-\frac {x}{2}}$, for $x>0$  
>, where $\nu$ is a positive integer, and this is the <font color="DeepSkyBlue">chi-square PDF.</font>  
>
>It is just a special case of the gamma distribution with $\alpha=\frac\nu2$, $\beta=2$, and <font color="DeepSkyBlue">$\nu$ is the degree of freedom.</font>  

### The <font color="Red">Chi-Square</font> Distribution Is <font color="Red">Right-Skew</font>
><font color="DeepPink">As degree of freedom increases, chi-square distribution would approximate the normal distribution</font>.  
>You can easily see that <font color="DeepPink">as $\nu$ increases, the distribution of chi-square changes.</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-03-intro-chi-square-dist-nu-increase.png "nu changes the distribution")
>Gradually, it will <font color="DeepPink">approximate the normal distribution.</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-03-intro-chi-square-dist-approx-normal-dist.png "approximate normal distribution")

### The <font color="Red">Chi-Square</font> And The <font color="Red">MGF</font>, Why?
>Because by means of the moment, we can easily figure out the $E\lbrack X\rbrack$, $E\lbrack X^2\rbrack$, $E\lbrack X^3\rbrack$ with 1st, 2nd, 3rd order of differentiation.  
>&#10112;we can formulate the MGF of chi-square in below expression:  
>$M_x(t)=\int_0^\infty e^{t\cdot x}\cdot \frac {1}{2^{\frac \nu2}\cdot \Gamma(\frac \nu2)}\cdot x^{\frac \nu2 -1}\cdot e^{-\frac {x}{2}}\operatorname dx$  
>$\;\;\;\;\;\;=\int_0^\infty \frac {1}{2^{\frac \nu2}\cdot \Gamma(\frac \nu2)}\cdot x^{\frac \nu2 -1}\cdot e^{-\frac {1}{2}\cdot (1-2\cdot t)\cdot x}\operatorname dx$  
>
>&#10113;let $y=\frac {1}{2}\cdot (1-2\cdot t)\cdot x$  
>$\Rightarrow x=\frac {2\cdot y}{1-2\cdot t}$  
>$\Rightarrow \frac {\operatorname dx}{\operatorname dx}=\frac {2}{1-2\cdot t}\cdot\frac {\operatorname dy}{\operatorname dx}$  
>$\Rightarrow 1\cdot \operatorname dx=\frac {2}{1-2\cdot t}\cdot \operatorname dy$  
>$\Rightarrow \operatorname dx=\frac {2}{1-2\cdot t}\cdot \operatorname dy$  
>
>&#10114;replace $\operatorname dx$ with $\frac {2}{1-2\cdot t}\cdot \operatorname dy$  
>$M_x(t)=\int_0^\infty \frac {1}{2^{\frac \nu2}\cdot \Gamma(\frac \nu2)}\cdot (\frac {2\cdot y}{1-2\cdot t})^{\frac \nu2 -1}\cdot e^{-y}\cdot\frac {2}{1-2\cdot t}\cdot \operatorname dy$  
>$\;\;\;\;\;\;=\frac {1}{2^{\frac \nu2}\cdot\Gamma(\frac \nu2)}\cdot (\frac {2}{1-2\cdot t})^{\frac \nu2}\cdot\int_0^\infty y^{\frac \nu2 -1}\cdot e^{-y} \operatorname dy$  
>$\;\;\;\;\;\;=\frac {1}{2^{\frac \nu2}\cdot\Gamma(\frac \nu2)}\cdot (\frac {2}{1-2\cdot t})^{\frac \nu2}\cdot\Gamma(\frac \nu2)$  
>$\;\;\;\;\;\;=(\frac {1}{1-2\cdot t})^{\frac \nu2}$  
>$\;\;\;\;\;\;=(1-2\cdot t)^{-\frac \nu2}$  
>, where we have $\Gamma(\frac \nu2)$=$\int_0^\infty y^{\frac \nu2 -1}\cdot e^{-y} \operatorname dy$  

### Expect Value And Variance Of <font color="Red">Chi-Square</font> Distribution
>Succeeding to above, we have deduce out the MGF of chi-square, we could just easily figure out the $\mu_1$, $\mu_2$:  
>$\mu_1$=$M_x^{′}(t)\vert_{t=0}$  
>$\;\;\;\;$=$\frac{\operatorname dM_X(t)}{\operatorname dt}\vert_{t=0}$  
>$\;\;\;\;$=$-\frac {\nu}{2}\cdot (1-2\cdot t)^{-\frac \nu2 -1}\cdot (-2)\vert_{t=0}$  
>$\;\;\;\;$=$\nu\cdot (1-2\cdot t)^{-\frac \nu2 -1}\vert_{t=0}$  
>$\;\;\;\;$=$\nu$=$E\lbrack X\rbrack$  
>
>$\mu_2$=$M_x^{″}(t)\vert_{t=0}$  
>$\;\;\;\;$=$\frac{\operatorname d^{2}M_X(t)}{\operatorname dt^{2}}\vert_{t=0}$  
>$\;\;\;\;$=$\nu\cdot (-\frac {\nu}{2}-1)\cdot (1-2\cdot t)^{-\frac \nu2 -2}\cdot (-2)\vert_{t=0}$  
>$\;\;\;\;$=$2\cdot\nu\cdot (\frac {\nu}{2}+1)\cdot (1-2\cdot t)^{-\frac \nu2 -2}\vert_{t=0}$  
>$\;\;\;\;$=$\nu^2+2\cdot\nu$=$E\lbrack X^2\rbrack$  

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->

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

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->