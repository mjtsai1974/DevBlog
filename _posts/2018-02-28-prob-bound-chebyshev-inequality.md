---
layout: post
title: Chebyshev's Inequality
---

## Prologue To The <font color="Red">Chebyshev's Inequality</font>
<p class="message">
The <font color="Red">Chebyshev's inequality</font> is the variation based on the <font color="Red">Markov inequality</font>, it uses the second moments, the variance instead of the mean of a random variable.  
</p>

### <font color="Red">Chebyshev's Inequality</font>
>Let $Z$ be any random variable with $Var\lbrack Z\rbrack>\infty$, then  
>$\;\;\;\;P(Z\ge E\lbrack Z\rbrack+t\;or\;Z\le E\lbrack Z\rbrack-t)\le\frac {Var\lbrack Z\rbrack}{t^2}$  
>$\;\;\;\;\;\;$, for any $t\ge 0$  
>
>Proof:  
>&#10112;$Z\ge E\lbrack Z\rbrack+t$ or $Z\le E\lbrack Z\rbrack-t$ is exactly the same as $\left|Z-E\lbrack Z\rbrack\right|\ge t$.  
>&#10113;therefore, we have it that:  
>$P(Z\ge E\lbrack Z\rbrack+t\;or\;Z\le E\lbrack Z\rbrack-t)$  
>=$P(\left|Z-E\lbrack Z\rbrack\right|\ge t)$  
>=$P((Z-E\lbrack Z\rbrack)^2\ge t^2)$  
>&#10114;by means of the <font color="Red">Markov inequality</font>, below inequality just holds.  
>$P((Z-E\lbrack Z\rbrack)^2\ge t^2)\le\frac {(Z-E\lbrack Z\rbrack)^2}{t^2}$  
>$\Rightarrow P(Z\ge E\lbrack Z\rbrack+t\;or\;Z\le E\lbrack Z\rbrack-t)\le\frac {Var\lbrack Z\rbrack}{t^2}$  
>
>Remember that we have a glance over the <font color="Red">Chebyshev's inequality</font> in [Hoeffding Inequality v.s. Chebyshev's Inequality]({{ site.github.repo }}{{ site.baseurl }}/2017/10/24/prereq-hoeffding-vs-law-large-number/), it has been proved by means of integral, now, distinct topic in the series of probability bounds would like to be chained together, said by using the <font color="Red">Markov inequality</font> in this proof.  

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- \overline{X_n} -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->
<!-- \lim_{t\rightarrow\infty} -->
<!-- \begin{array}{l}f'(x)\\f''(x)\\f'''(x)\\f''''(x)\end{array} -->
<!-- \\{Z\vert Z\ge t\\} -->
<!-- E\lbrack Z\rbrack -->
<!-- Var\lbrack Z\rbrack -->
<!-- \left|X\right| absolute value of X-->

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