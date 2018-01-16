---
layout: post
title: Introduction To The t Distribution
---

## Prologue To The <font color="Red">t</font> Distribution
<p class="message">
In probability theory and statistics, base on the most fundamental gamma distribution, <font color="Red">t</font> distribution is one of the many models of distributions further developed, furthermore, its definition is based on the central limit theorem.  
With the basic realization of gamma, chi-square distributions, we could also treat the <font color="Red">t</font> distribution a special <font color="DeepSkyBlue">joint case of standard normal distribution and the chi-square</font> distribution.  
It would be greatly helpful in the evaluation of the regression model build on your hypothesis, the power of test for the precision in the machine learning results.   
</p>

### Why Do We Need The <font color="Red">t</font> Distribution?
>As we know that <font color="DeepPink">$\frac {\overline {X_n}-\mu}{\sigma/\sqrt n}\sim ɸ(0,1)$</font>, by the <font color="OrangeRed">central limit theorem</font>, when <font color="DeepPink">$n\rightarrow\infty$</font>, the term <font color="DeepPink">$\frac {\overline {X_n}-\mu}{S/\sqrt n}$ approximates $\frac {\overline {X_n}-\mu}{\sigma/\sqrt n}$</font>, where  
>&#10112;$S$ is the sample deviation.  
>&#10113;$\sigma$ is the population deviation.  
>
>After experiments over so many years, statisticians have it that when sample size is less than 30, <font color="RosyBrown">$\frac {\overline {X_n}-\mu}{S/\sqrt n}\not\sim ɸ(0,1)$</font> as a conclusion, for $n<30$, it would be insufficient the quantity of sample size to be distributed in normal distribution.  
>
>That's why we need to have <font color="Red">t</font> distribution, by usual, we take $T$=$\frac {\overline {X_n}_n-\mu}{S/\sqrt n}$.  

### Expand The Definition Of The <font color="Red">t</font> Distribution
>Let T to be a random variable, expand from where it is defined:  
>$T$=$\frac {\overline {X_n}-\mu}{S/\sqrt n}$  
>$\;\;$=$\frac {\overline {X_n}-\mu}{\sigma/\sqrt n}$/$\frac {S/\sqrt n}{\sigma/\sqrt n}$  
>$\;\;$=$\frac {Z}{S/\sigma}$, where $Z\sim ɸ(0,1)$  
>$\;\;$=$\frac {Z}{\sqrt {S^2/\sigma^2}}$  
>$\;\;$=$\frac {Z}{\sqrt {\frac {\chi_{n-1}^2}{n-1}}}$  
>, where we have:  
>&#10112;[$\chi_{n-1}^2$=$(n-1)\cdot S^2$/$\sigma^2$]({{ site.github.repo }}{{ site.baseurl }}/2018/01/03/intro-chi-square-dist/)  
>&#10113;$n-1$ is the degree of freedom.  

### The <font color="Red">t</font> Distribution PDF and Proof
>The PDF of <font color="Red">t</font> distribution is given by:  
>$f(t)$=$\frac {\Gamma(\frac {\nu+1}{2})}{\sqrt {\pi\cdot\nu}\cdot\Gamma(\frac {\nu}{2})}\cdot(1+\frac {t^2}{\nu})^{-\frac {\nu+1}{2}}$,  
>where $\nu$ is the degree of freedom, $-\infty<t<\infty$.  
>
>proof:  
>&#10112;please recall that $T$=$\frac {Z}{\sqrt {\frac {\chi_{n-1}^2}{n-1}}}$, and we learn the deduction of [the F distribution joint PDF]({{ site.github.repo }}{{ site.baseurl }}/2018/01/05/intro-f-dist/).  
>Take $f_Z(z)$=$\frac {1}{\sqrt {2\cdot\pi}}\cdot e^{-\frac {z^2}{2}}$, where $-\infty<z<\infty$, $Z\sim ɸ(0,1)$.  
>Take $f_{\chi_{\nu}^2}(x)$=$\frac {x^{\frac {\nu}{2}-1}}{2^{\frac {\nu}{2}}\cdot\Gamma(\frac {\nu}{2})}\cdot e^{-\frac {x}{2}}$, where $0<x<\infty$, $X \sim\chi_{\nu}^2$.  
>
>&#10113;express the joint PDF in below form:  
>$f_{Z,\chi_{\nu}^2}(z,x)$=$f_Z(z)\cdot f_{\chi_{\nu}^2}(x)$, where $z\in Z$, $x\in X$  
>$\Rightarrow F_{Z,\chi_{\nu}^2}(z,x)$=$\int_{-\infty}^{\infty}\int_{0}^{\infty}f_Z(z)\cdot f_{X}(x)\operatorname dx\operatorname dz$  
>For the simplicity of notation, we use $f_{X}(x)$ for $f_{\chi_{\nu}^2}(x)$, since $X \sim\chi_{\nu}^2$, and the $F_{Z,\chi_{\nu}^2}(z,x)$ is the CDF(cumulative distributed function).  
>
>&#10114;by the definition of $T$=$\frac {Z}{\sqrt {\frac {\chi_{n-1}^2}{n-1}}}$  
>Let <font color="DeepSkyBlue">$t$=$z$/$\sqrt\frac {x}{\nu}$</font>, and, <font color="OrangeRed">why we use $x$, not $x^2$?</font>  
>Be noted that <font color="DeepPink">$x$ is one sample distributed in $\chi_{\nu}^2$</font>.  Don't get confused!!  
>
>&#10115;let $z$=$\frac {t\cdot\sqrt x}{\sqrt \nu}$, $\operatorname dz$=$\frac {\sqrt x}{\sqrt \nu}\cdot\operatorname dt$  
>We can express $z$ in terms of $t$, which then in turns expressed in terms of $x$.  
>
>$F_{Z,\chi_{\nu}^2}(z,x)$  
>$=F_{T,\chi_{\nu}^2}(t,x)$, where $t \in T$  
>$=\int_{-\infty}^{\infty}\int_{0}^{\infty}f_Z(\frac {t\cdot\sqrt x}{\sqrt \nu})\cdot f_{X}(x)\operatorname dx\frac {\sqrt x}{\sqrt \nu}\cdot\operatorname dt$  
>$=\int_{-\infty}^{\infty}\int_{0}^{\infty}\frac {1}{\sqrt {2\cdot\pi}}\cdot e^{-\frac {t^2}{2}\cdot\frac {x}{\nu}}\cdot\frac {x^{\frac {\nu}{2}-1}\cdot e^{-\frac {x}{2}}}{2^{\frac {\nu}{2}}\cdot\Gamma(\frac {\nu}{2})}\operatorname dx\frac {\sqrt x}{\sqrt \nu}\cdot\operatorname dt$  
>$=\frac {1}{\sqrt {2\cdot\pi}\cdot\sqrt\nu}\cdot\frac {1}{2^{\frac {\nu}{2}}\cdot\Gamma(\frac {\nu}{2})}\int_{-\infty}^{\infty}\int_{0}^{\infty}x^{\frac {\nu+1}{2}-1}\cdot e^{-(\frac {t^2}{2}\cdot\frac {x}{\nu}+\frac {x}{2})}\operatorname dx\operatorname dt$  
>
>&#10116;let $w$=$\frac {t^2}{2}\cdot\frac {x}{\nu}+\frac {x}{2}$=$\frac {(t^2+\nu)\cdot x}{2\cdot\nu}$  
>, then $x$=$\frac {2\cdot\nu}{t^2+\nu}\cdot w$, $\operatorname dw$=$\frac {t^2+\nu}{2\cdot\nu}\cdot\operatorname dx$  
>, and $\operatorname dx$=$\frac {2\cdot\nu}{t^2+\nu}\cdot\operatorname dw$  
>
>$F_{T,\chi_{\nu}^2}(t,x)$  
>$=\frac {1}{\sqrt {2\cdot\pi}\cdot\sqrt\nu}\cdot\frac {1}{2^{\frac {\nu}{2}}\cdot\Gamma(\frac {\nu}{2})}\int_{-\infty}^{\infty}\int_{0}^{\infty}(\frac {2\cdot\nu}{t^2+\nu}\cdot w)^{\frac {\nu+1}{2}-1}\cdot e^{-w}\cdot\frac {2\cdot\nu}{t^2+\nu}\cdot\operatorname dw\operatorname dt$  
>

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