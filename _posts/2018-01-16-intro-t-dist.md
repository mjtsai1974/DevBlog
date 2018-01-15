---
layout: post
title: Introduction To The t Distribution
---

## Prologue To The <font color="SpringGreen">t</font> Distribution
<p class="message">
In probability theory and statistics, base on the most fundamental gamma distribution, <font color="SpringGreen">t</font> distribution is one of the many models of distributions further developed, furthermore, its definition is based on the central limit theorem.  
With the basic realization of gamma, chi-square distributions, we could also treat the <font color="SpringGreen">t</font> distribution a special jointed case of standard normal distribution and the chi-square distribution.  
It would be greatly helpful in the evaluation of the regression model build on your hypothesis, the power of test for the precision in the machine learning results.   
</p>

### Why Do We Need <font color="SpringGreen">t</font> Distribution?
>As we know that <font color="DeepPink">$\frac{{\overline X}_n-\mu}{\delta/\sqrt n}\sim ɸ(0,\;1)$</font>, by the <font color="OrangeRed">central limit theorem</font>, when $n\rightarrow\infty$, the term $\frac{{\overline X}_n-\mu}{S/\sqrt n}$ approximates $\frac{{\overline X}_n-\mu}{\sigma/\sqrt n}$, where  
>&#10112;$S$ is the sample deviation.  
>&#10113;$\sigma$ is the population deviation.  
>
>After experiments over so many years, statisticians have it that when sample size is less than 30, <font color="DeepSkyBlue">$\frac{{\overline X}_n-\mu}{\delta/\sqrt n}\not\sim ɸ(0,\;1)$</font> as a conclusion, for $<30$, it would be insufficient the quantity of sample size to be distributed in normal distribution.  
>
>That's why we need to have <font color="SpringGreen">t</font> distribution, by usual, we take $T=\frac{{\overline X}_n-\mu}{S/\sqrt n}$.  

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- \overline{X_n} -->
<!-- \frac{{\overline X}_n-\mu}{S/\sqrt n} -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="SpringGreen">t</font> distribution -->
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