---
layout: post
title: Introduction To The Law Of Large Number
---

## Prologue To <font color="Red">The Law Of Large Number</font>
<p class="message">
Based on the result of the Chebyshev's inequality, the law of large number guarantees the precision of the averaged term quantity of interest would be well approximated to the mean of the term in the sample data.  
</p>

### <font color="Red">The Chebyshev's Inequality</Font>
>For $X$ to be any arbitrary random variable, and for ang given $a>0$:  
>$\;\;\;\;P(|X-E\lbrack X\rbrack|\ge a)\le \frac {1}{a^{2}}\cdot Var\lbrack X\rbrack$  
>proof::&#10112;  
>Please go to the article [Hoeffding Inequality v.s. Chebyshev's Inequality]({{ site.github.repo }}{{ site.baseurl }}/2017/10/24/prereq-hoeffding-vs-law-large-number/)  
>proof::&#10113;  
>Or you can see it in [Chebyshev's Inequality]({{ site.github.repo }}{{ site.baseurl }}/2018/02/28/prob-bound-chebyshev-inequality/)

### Theorem: <font color="Red">The Law Of Large Number</font>
>Given random variables $X_1$,$X_2$,...,$X_n$, each is <font color="OrangeRed">identically independent distributed</font> with mean $\mu$ and variance $\sigma^{2}$.  
>$\;\;\;\;\lim_{n\rightarrow\infty}P(|\overline {X_n}-E\lbrack \overline {X_n}\rbrack|\ge \varepsilon)$=$0$  
>
>proof:  
>&#10112;trivially, we know that $E\lbrack \overline {X_n}\rbrack$=$\mu$, $Var\lbrack \overline {X_n}\rbrack$=$\frac {\sigma^{2}}{n}$.  
>&#10113;by using the <font color="Red">Chebyshev's inequality</font>, we have:  
>$P(|\overline {X_n}-E\lbrack \overline {X_n}\rbrack|\ge \varepsilon)$  
>=$P(|\overline {X_n}-\mu|\ge \varepsilon)$  
>$\le \frac {Var\lbrack \overline {X_n}\rbrack}{\varepsilon^{2}\cdot n}$  
>=$\frac {\sigma^{2}}{\varepsilon^{2}\cdot n}$, for any $\varepsilon>0$  
>&#10114;$\lim_{n\rightarrow\infty}P(|\overline {X_n}-E\lbrack \overline {X_n}\rbrack|\ge \varepsilon)\le\lim_{n\rightarrow\infty}\frac {\sigma^{2}}{\varepsilon^{2}\cdot n}$, <font color="DeepSkyBlue">as $n\rightarrow\infty$</font>, it holds that <font color="DeepPink">$\lim_{n\rightarrow\infty}P(|\overline {X_n}-E\lbrack \overline {X_n}\rbrack|\ge \varepsilon)$=$0$</font>  

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- \vert_{0.5}^{\infty} -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- $E\lbrack X\rbrack$ -->
<!-- \overline{X_n} -->
<!-- \underset{Succss}P -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->
<!-- \lim_{t\rightarrow\infty} -->
<!-- \int_{0}^{a}\lambda\cdot e^{-\lambda\cdot t}\operatorname dt -->

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

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->