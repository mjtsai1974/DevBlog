---
layout: post
title: Introduction To The F Distribution
---

## Prologue To The F Distribution
<p class="message">
In probability theory and statistics, base on the most fundamental gamma distribution, F distribution is one of the many models of distributions further developed, furthermore, its definition is based on the chi-square distribution.  
With the basic realization of gamma, chi-square distributions, we could also treat the F distribution a special case of the gamma distribution.  
It would be greatly helpful in the evaluation of the regression model build on your hypothesis, the power of test for the precision in the machine learning results.   
</p>

### From The Chi-Square Distribution To The <font color="Red">F</font> Distribution
>The model of F distribution is defined by the combination of two chi-square in ratio expression.  
>&#10112;the definition is given by:  
>$F$=$\frac {\frac {\chi_{\nu_1}^2}{\nu_1}}{\frac {\chi_{\nu_2}^2}{\nu_2}}$, where $\chi_{\nu_i}^2$ is the chi-square PDF of DOF(degree of freedom) $\nu_i$, for $i=1,2$.  
>
>&#10113;the F distribution PDF is expressed in below equality:  
>$h(f)$=$\frac {\Gamma(\frac {\nu_1+\nu_2}{2})\cdot (\frac {\nu_1}{\nu_2})^{\frac {\nu_1}{2}}}{\Gamma(\frac {\nu_1}{2})\cdot\Gamma(\frac {\nu_2}{2})}\cdot\frac {f^{\frac {\nu_1}{2}-1}}{(1+\frac {\nu_1}{\nu_2}\cdot f)^{\frac {\nu_1+\nu_2}{2}}}$   
>
>In the next paragraph, this article would prove &#10113 by means of the joint probability density function in conjunction with the integration by part.  

### The <font color="Red">F</font> Distribution And The Joint PDF
>This section would like to detail the joint PDF for the <font color="Red">F</font> distribution model.  
>
>&#10112;suppose $X$, $Y$ are two <font color="OrangeRed">independent</font> random variables with PDF $f_X(x)$, $f_Y(y)$.  
>
>&#10113;let $Z$=$\frac {Y}{X}$, we denote $f_{XY}(x,y)$ to be the PDF of $Z$, where it is also a random variable.  Then for all $x\in X$, $y\in Y$, $z\in Z$, we have it that:  
>$P(\frac {y}{x}\le z)$=$P(y\le z\cdot x)$  
>
>Therefore, $F_{XY}(z)$=$\int_0^{\infty}\int_{-\infty}^{z\cdot x}f_{XY}(x,y)\operatorname dy\operatorname dx$  
>, well, we can treat $Y\in \chi_{\nu_1}^2$, $X\in \chi_{\nu_2}^2$ by intuition, and $F_{XY}(z)$ is the CDF(cumulative distribution function).  
>
>&#10114;let $y$=$x\cdot v$, then, $\operatorname dy$=$x\cdot\operatorname dv$, this is a little utilization of integration by part.  
>$F_{XY}(z)$=$\int_0^{\infty}\int_{-\infty}^{z}x\cdot f_{XY}(x,y)\operatorname dv\operatorname dx$  
>$\;\;\;\;\;\;\;\;$=$\int_{-\infty}^{z}\int_0^{\infty}x\cdot f_{XY}(x,y)\operatorname dx\operatorname dv$  
>
>&#10115;derivate $F_{XY}(z)$ with respect to $v$, would we eliminate the term $\operatorname dv$, and express $f_{XY}(z)$, the PDF of F only in one term of $x$.  
>$f_{XY}(z)$=$\frac {\operatorname dF_{XY}(z)}{\operatorname dv}$  
>$\;\;\;\;\;\;\;\;$=$\int_0^{\infty}x\cdot f_{XY}(x,y)\operatorname dx$  
>$\;\;\;\;\;\;\;\;$=$\int_0^{\infty}x\cdot f_{XY}(x,x\cdot z)\operatorname dx$...take $v=z$  
>$\;\;\;\;\;\;\;\;$=$\int_0^{\infty}x\cdot f_{X}\cdot f_{Y}(x\cdot z)\operatorname dx$  
>
>&#10116;let $X$, $Y$ now be the random variables in chi-square PDF with DOF=$n$, $m$ respectively, and recall that $Z$=$\frac {Y}{X}$, then:  
>$f_Z(z)$=$\int_0^{\infty}x\cdot\frac {x^{\frac {n}{2}-1}\cdot e^{-\frac {x}{2}}}{2^{\frac {n}{2}}\cdot\Gamma(\frac {n}{2})}\cdot\frac {(x\cdot z)^{\frac {m}{2}-1}\cdot e^{-\frac {x\cdot z}{2}}}{2^{\frac {m}{2}}\cdot\Gamma(\frac {m}{2})}\operatorname dx$  
>$\;\;\;\;\;\;\;\;$=$\frac {z^{\frac {m}{2}-1}}{\Gamma(\frac {m}{2})\cdot\Gamma(\frac {n}{2})\cdot 2^{\frac {m+n}{2}}}\cdot\int_0^{\infty}x^{\frac{m+n}{2}-1}\cdot e^{-\frac {x\cdot\(z+1)}{2}}\operatorname dx$  
>
>&#10117;let $t$=$\frac {x\cdot(z+1)}{2}$, then $\operatorname dt$=$\frac {z+1}{2}\cdot \operatorname dx$, and $x$=$\frac {2\cdot t}{z+1}$  
>$f_Z(z)$=$\frac {z^{\frac {m}{2}-1}}{\Gamma(\frac {m}{2})\cdot\Gamma(\frac {n}{2})\cdot 2^{\frac {m+n}{2}}}\cdot\int_0^{\infty}(\frac {2\cdot t}{z+1})^{\frac{m+n}{2}-1}\cdot e^{-t}\cdot\frac {2}{z+1}\operatorname dt$  
>$\;\;\;\;\;\;\;\;$=$\frac {z^{\frac {m}{2}-1}\cdot(\frac {2}{z+1})^{\frac {m+n}{2}}}{\Gamma(\frac {m}{2})\cdot\Gamma(\frac {n}{2})\cdot 2^{\frac {m+n}{2}}}\cdot\int_0^{\infty}t^{\frac{m+n}{2}-1}\cdot e^{-t}\operatorname dt$  
>$\;\;\;\;\;\;\;\;$=$\frac {z^{\frac {m}{2}-1}\cdot\Gamma(\frac {m+n}{2})}{\Gamma(\frac {m}{2})\cdot\Gamma(\frac {n}{2})\cdot (z+1)^{\frac {m+n}{2}}}$  

### The <font color="Red">F</font> Distribution PDF Deduction
>Above section, &#10117; leaves a useful <font color="DeepPink">expression of joint PDF of two chi-square in the form $Z$=$\frac {Y}{X}$</font>, inheriting from it, we will continue to deduce it out for the Z distribution PDF.  
>
>&#10112;let $Z$=$\frac {\frac {Y}{m}}{\frac {X}{n}}$ to meet F distribution definition,  then for all $x\in X$, $y\in Y$, $z\in Z$, we have:  
>$z$=$\frac {y}{x}\cdot\frac {n}{m}$, $y$=$\frac {m}{n}\cdot x\cdot z$  
>
>&#10113;this time, let $y$=$\frac {m}{n}\cdot x\cdot v$, then, $\operatorname dy$=$\frac {m}{n}x\cdot\operatorname dv$:  
>$F_{XY}(z)$=$\int_{-\infty}^{z}\int_0^{\infty}\frac {m}{n}\cdot x\cdot f_{XY}(x,y)\operatorname dx\operatorname dv$  
>
>&#10114;Differentiate $F_{XY}(z)$ by $\operatorname dv$:  
>$f_{XY}(z)$=$\frac {\operatorname dF_{XY}(z)}{\operatorname dv}$  
>$\;\;\;\;\;\;\;\;$=$\frac {m}{n}\int_0^{\infty}x\cdot f_{XY}(x,\frac {m}{n}\cdot x\cdot z)\operatorname dx$...take $v=z$  
>$\;\;\;\;\;\;\;\;$=$\frac {m}{n}\int_0^{\infty}x\cdot f_{X}\cdot f_{Y}(\frac {m}{n}\cdot x\cdot z)\operatorname dx$  
>...replace $x\cdot z$ by $\frac {m}{n}\cdot x\cdot z$
>
>&#10115;because $f_Z(z)$=$f_{XY}(z)$, now we have it that:  
>$f_Z(z)$=$\frac {m}{n}\int_0^{\infty}x\cdot\frac {x^{\frac {n}{2}-1}\cdot e^{-\frac {x}{2}}}{2^{\frac {n}{2}}\cdot\Gamma(\frac {n}{2})}\cdot\frac {(\frac {m}{n}\cdot x\cdot z)^{\frac {m}{2}-1}\cdot e^{-\frac {\frac {m}{n}\cdot x\cdot z}{2}}}{2^{\frac {m}{2}}\cdot\Gamma(\frac {m}{2})}\operatorname dx$  
>$\;\;\;\;\;\;\;\;$=$\frac {\frac {m}{n}\cdot(\frac {m}{n}\cdot z)^{\frac {m}{2}-1}}{\Gamma(\frac {m}{2})\cdot\Gamma(\frac {n}{2})\cdot 2^{\frac {m+n}{2}}}\cdot\int_0^{\infty}x^{\frac{m+n}{2}-1}\cdot e^{-\frac {x}{2}\cdot(\frac {m}{m}\cdot z+1)}\operatorname dx$  
>
>&#10116;let $t$=$\frac {x}{2}\cdot(\frac {m}{m}\cdot z+1)$, then we have it that:  
>$x$=$\frac {2\cdot t}{\frac {m}{m}\cdot z+1}$, $\operatorname dx$=$\frac {2\cdot t}{\frac {m}{m}\cdot z+1}\cdot\operatorname dt$  
>$f_Z(z)$=$\frac {\frac {m}{n}\cdot(\frac {m}{n}\cdot z)^{\frac {m}{2}-1}}{\Gamma(\frac {m}{2})\cdot\Gamma(\frac {n}{2})\cdot 2^{\frac {m+n}{2}}}\cdot\int_0^{\infty}(\frac {2\cdot t}{\frac {m}{m}\cdot z+1})^{\frac{m+n}{2}-1}\cdot e^{-t}\frac {2\cdot t}{\frac {m}{m}\cdot z+1}\cdot\operatorname dt$  

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- \overline{X_n} -->

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