---
layout: post
title: Series Convergence
---

## Prologue To The Series <font color="DeepPink">Convergence</font>
<p class="message">
Series is a collection of the data ordered by indices, maybe in a time sequence manner, pervasively by monotonic increasing numbers.  This article will inspect the <font color="DeepPink">convergence</font> versus <font color="RosyBrown">divergence</font> of a given series.
<font color="DeepSkyBlue">The convergence of series</font> could be a key factor in some topics in reinforcement learning, usually in a <font color="DeepSkyBlue">discounted representation of value function</font> deduction.
</p>

### Begin By <font color="OrangeRed">Geometric Series</font>
>&#10112;this is a geometric series, $1$,$x$,$x^2$,$x^3$,..., when you sum them up, then $1$+$x$+$x^2$+$x^3$+...=$\frac {1-x^{n+1}}{1-x}$, and why?  
>Since $1+x$=$\frac {1-x^2}{1-x}$,$1+x+x^2$=$\frac {1-x^3}{1-x}$,...,then, $1+x+x^2+...+x^{n-1}$=$\frac {1-x^n}{1-x}$  
>
>&#10113;what $1$+$x$+$x^2$+$x^3$+...finally becomes?  
>This equates to the discussion of the case when n approaches infinity:  
>When <font color="DeepPink">$\left|x\right|<1$</font>, it <font color="DeepPink">converges</font> and $\lim_{n\rightarrow\infty}\frac {1-x^n}{1-x}$=$\lim_{n\rightarrow\infty}\frac {1}{1-x}$  
>When <font color="RosyBrown">$\left|x\right|>1$</font>, it <font color="RosyBrown">divergence</font> and $\lim_{n\rightarrow\infty}\frac {1-x^n}{1-x}$=$\lim_{n\rightarrow\infty}\frac {1-x^n}{1-x}$  
>
>&#10114;by directly dividing, we have:
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-26-series-cnvg-direct-divide.png "1/(1-x) for geometric series")
>This says $1+x+x^2+...+x^{n-1}$=$\frac {1}{1-x}$  




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