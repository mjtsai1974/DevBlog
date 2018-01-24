---
layout: post
title: Introduction To The Exponential Distribution
---

## Prologue To The <font color="Red">Exponential</font> Distribution
<p class="message">
In probability theory and statistics, the <font color="Red">exponential</font> distribution is the model of distribution further developed, base on the most fundamental gamma distribution.  
With the basic realization of gamma distributions, we could also treat the <font color="Red">exponential</font> distribution a <font color="DeepSkyBlue">special case of gamma</font> distribution.  
It would be greatly helpful in the evaluation of the experimental model build on your hypothesis, the power of test for the precision in the machine learning results.   
</p>

### Cases of The <font color="Red">Exponential</font> Distribution
>This article would like to guide you through a design of a simple case to generalize the <font color="Red">exponential</font> distribution.  
>
>&#10112;the experiment is proceeded with the assumption that $x$ is the <font color="DeepSkyBlue">rate</font> of event occurrence during one time interval $t$, totally, $x\cdot t$ events.  
>&#10113;suppose $V$ is the volumetric space where these events occur within.  Trivially, the success probability of event occurrence, we take it as $P_{success}$=$\frac {x\cdot t}{V}$, then the failure probability could be regarded as $P_{fail}$=$1-\frac {x\cdot t}{V}$.  
>&#10114;suppose the <font color="DeepSkyBlue">rate</font> $x$ do exist and <font color="OrangeRed">remain constant</font> over each disjoint interval for some event occurrence.  
>&#10115;each disjoint interval are of the same time length, say it $t$, and we further divide it into n subsections.  Then each subsection would have $P_{success}$=$\frac {x\cdot t}{V\cdot n}$, then the failure probability could be regarded as $P_{fail}$=$1-\frac {x\cdot t}{V\cdot n}$.  
>&#10116;we assume that <font color="DeepSkyBlue">each occurrence of the event in distinct subsection is independent</font>, the success v.s. failure probability in each subsection just matches the the Bernoulli distribution.  
>&#10117;let the random variable $T$ to be the time it takes until the very first event to occur, and the whole behavior follows the geometric distribution, if it takes time larger than time $t$ for the very first event to occur, then we have such probability:  
>$P(T>t)$=$\lim_{t\rightarrow\infty}(P_{fail})^{n}$=$\lim_{t\rightarrow\infty}(1-\frac {x\cdot t}{V\cdot n})^{n}$  
>

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- \overline{X_n} -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->
<!-- \lim_{t\rightarrow\infty} -->

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
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->