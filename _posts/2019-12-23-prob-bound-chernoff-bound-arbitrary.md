---
layout: post
title: Chernoff Bounds For Arbitrary Random Variable
---

## Prologue To The <font color="Red">Chernoff Bounds</font> For <font color="OrangeRed">Arbitrary</font> Random Variable
<p class="message">
There are many <font color="Red">Chernoff bounds</font> as a result.  This article develops the tail bound on the <font color="OrangeRed">independent arbitrary</font> random variable with outcome ranging from 0 to 1, that is $\lbrack 0,1\rbrack$.  
</p>

### The <font color="Red">Error Probability</font> After Test
<font color="OrangeRed">[The given condition]</font>
>Suppose we are given  
>&#10112;$X_{1}$,$X_{2}$,...,$X_{n}$ to be independent random variables with values in $\lbrack 0,1\rbrack$.  
>&#10113;$X$=$X_{1}$+$X_{2}$+...+$X_{n}$  
>&#10114;$E\lbrack X rbrack$=$\mu$  
>
>These $X_{1}$,...,$X_{n}$ needs <font color="RosyBrown">not</font> to be Bernoulli ranodm variables, but they must be <font color="OrangeRed">independent</font>.  
>
><font color="RoyalBlue">[Question]</font>
>Then, for every $\varepsilon$>$0$, what is the upper and lower bound for  
>&#10112;$P(X\geq (1+\delta)\cdot\mu)$=$P(X\geq \mu+\varepsilon)$  
>&#10113;$P(X\leq (1-\delta)\cdot\mu)$=$P(X\leq \mu-\varepsilon)$  
>, where $\varepsilon$=$\delta\cdot\mu$  

### The Upper Bound On Error Probability
>Still, it is asking the upper bound on error probability, when target value $X$ is greater than the expect value $\mu$, and we'd like to bound it on the upper side.  
>
>The major difference is that these random variables fall within $\lbrack 0,1\rbrack$, <font color="RosyBrown">not</font> the Bernoulli values $0$ or $1$.  here is the idea:  
>&#10112;take $Y_{i}$=$X_{i}$-$E\lbrack X_{i} rbrack$  
>&#10113;take $Y$=$\sum_{1}^{n}Y_{i}$  
>&#10114;$P(X\geq\mu+\varepsilon)$  
>=$P(X-\mu\geq\varepsilon)$  
>=$P(\sum_{1}^{n}(X_{i}-E\lbrack X_{i} rbrack)\geq\varepsilon)$  
>=$P(Y\geq\varepsilon)$  

<!-- Γ -->
<!-- \Omega -->
<!-- \cap intersection -->
<!-- \cup union -->
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
<!-- \Leftrightarrow -->
<!-- \prod_{v\in V} -->
<!-- \subset -->
<!-- \subseteq -->
<!-- \varnothing -->
<!-- \perp -->
<!-- \overset\triangle= -->
<!-- \left|X\right| -->
<!-- \xrightarrow{r_t} -->
<!-- \left\|?\right\| => ||?||-->
<!-- \left|?\right| => |?|-->
<!-- \lbrack BQ\rbrack => [BQ] -->
<!-- \subset -->
<!-- \subseteq -->
<!-- \widehat -->
<!-- \int_{}^{}{}\operatorname d{} -->

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