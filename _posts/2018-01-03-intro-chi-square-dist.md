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

### From The Gamma Distribution To The Chi-Square Distribution
>Be recalled that we have gamma function and the PDF of the gamma distribution:  
>&#10112;$\Gamma(\alpha)$=$\int_0^\infty x^{\alpha-1}\cdot e^{-x}\operatorname dx$, where $\alpha>0$.  
>&#10113;$f(x)=\frac {1}{\beta^{\alpha}\cdot\Gamma(\alpha)}\cdot x^{\alpha-1}\cdot e^{-\frac{x}{\beta}}$, where $\alpha>0$, $\beta>0$  
>
>Next, we take $\alpha=\frac\nu2$, $\beta=2$, we turn the PDF function into below expression:  
>$f(x)=\frac {1}{2^{\frac \nu2}\cdot \Gamma(\frac \nu2)}\cdot x^{\frac \nu2 -1}\cdot e^{-\frac {x}{2}}$, for $x>0$  
>, where $\nu$ is a positive integer, and this is the chi-square PDF.  
>It is just a special case of the gamma distribution with $\alpha=\frac\nu2$, $\beta=2$, and $\nu$ is the degree of freedom.  

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