---
layout: post
title: Introduction To The Poisson Process Inter-arrival Times
---

## Prologue To The <font color="Red">Poisson</font> Process <font color="Red">Inter-arrival Times</font>
<p class="message">
On the way to the <font color="Red">Poisson</font> distribution, the <font color="Red">inter-arrival times</font> could be easily found, and both exponential and <font color="Red">Poisson</font> distribution could be an appropriate modeling of it.  Formally, <font color="Red">inter-arrival times</font> could be distributed in gamma probability as a result of the nature of exponential distribution.  
</p>

### The <font color="Red">Inter-arrival Times</font>
>Given that $X_{1}$,$X_{2}$,...,$X_{n}$ are random variables with event outcome occurrences arrived at specific time.  To make it more formally, we take the difference $T_{i}$=$X_{i}$-$X_{i-1}$ as the <font color="Red">inter-arrival times</font>.  

### The Very First <font color="Red">Inter-arrival Times</font> Follows <font color="DeepSkyBlue">Exponential Distribution</font>
>We start to derive the probability distribution of <font color="Red">inter-arrival times</font>, let's focus on the <font color="OrangeRed">very first one</font> as the prelude.  
>&#10112;take $T_{1}$=$X_{1}$ as the very first arrival time.  
>&#10113;the probability of first arrival at time greater than t is equivalent to the probability of zero arrival within time $[0,t]$.  
>$P(T_{1}>t)$=1-$P(T_{1}\le t)$=1-$P(N_{[0,t]}=0)$=1-$e^{-\lambdat\cdot t}$  
>, where $\lambda$ is the intensity, the rate of event occurrence.  
>
><font color="DeepPink">The very first inter-arrival times is itself an exponential distribution.</font>  



<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- $E\lbrack X\rbrack$ -->
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
<!-- <font color="RoyalBlue">old alpha, quiz, example</font> -->
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