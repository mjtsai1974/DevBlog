---
layout: post
title: Chernoff Bounds For Bernoulli Random Variable
---

## Prologue To The <font color="Red">Chernoff Bounds</font> For <font color="Red">Bernoulli</font> Random Variable
<p class="message">
The <font color="Red">Chernoff bounds</font> is a technique to build the <font color="Red">exponential decreasing bounds on tail probabilities</font>.  This article develops the tail bound on the <font color="Red">Bernoulli</font> random variable with outcome 0 or 1.  
</p>

### The <font color="Red">Error Probability</font> After Test
>Let $X_{i}$ to be a <font color="Red">Bernoulli</font> random variable for $i$=$\\{1,2,...,n\\}$  
>&#10112;$X_{i}$=$1$ with probability $p_{1}$  
>&#10113;$X_{i}$=$0$ with probability $1$-$p_{1}$  
>, where all $X_{i}$s are I.I.D and suppose at least one of the $p_{i}$ is non-zero.  
>
>We are testing with a hope that we can make our target of mean value over some quantity of expectation after some amount of trials.  Hence, we let $X$=$\sum_{i=1}^{n}X_{i}$, $E\lbrack X\rbrack$=$\mu$=$\sum_{i=1}^{n}p_{i}$.  
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
<!-- \begin{array}{l}f'(x)\\f''(x)\\f'''(x)\\f''''(x)\end{array} -->
<!-- \\{Z\vert Z\ge t\\} -->
<!-- E\lbrack Z\rbrack -->
<!-- Var\lbrack Z\rbrack -->
<!-- \left|X\right| absolute value of X-->
<!-- \Leftrightarrow -->

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

<!-- ### <font color="RoyalBlue">Example</font>: Illustration By Rainy And Sunny Days In One Week -->
<!-- <font color="RoyalBlue">[Question]</font> -->
<!-- <font color="DeepSkyBlue">[Answer]</font> -->

<!-- <font color="Brown">Notes::mjtsai1974</font> -->

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!--
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Why at this moment, the Poisson and exponential probability come out with different result?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->