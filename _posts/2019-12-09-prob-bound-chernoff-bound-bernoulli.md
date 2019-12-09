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
>We are testing with a hope that we can <font color="OrangeRed">make our target value over expectation level after some amount of trials</font>.  To express the target value we want in terms of expect value, we let $X$=$\sum_{i=1}^{n}X_{i}$, $E\lbrack X\rbrack$=$\mu$=$\sum_{i=1}^{n}p_{i}$.  
>
><font color="RoyalBlue">[Question]</font>  
>How confident we are in the final outcome by the random variable $X$?  It is asking you 2 kinds of questions:  
>&#10112;the range of the confidence interval  
>&#10113;the error probability for the target value $X$ above or below the expect value $\mu$  
>The follwing section would guide you through the process to build the upper and lower bound of such error probability in <font color="Red">Chernoff</font> exponential decreasing form.  
>
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Even if our proof of &#10113; holds, the range of confidence interval must be guaranteed by the native design in your experiment.</font>  
>I will emphasize this at the end of this post.  

### The Upper Bound On Error Probability
>It is asking the error probability when target value $X$ is greater than the expect value $\mu$, and we'd like to bound it on the upper side.  
>
>$P(X>(1+\delta)\cdot\mu)$, for $\delta>0$  
>=$P(e^{t\cdot X}>e^{t\cdot (1+\delta)\cdot\mu)}$, for all $t>0$  
>$\leq \frac{E\lbrack e^{t\cdot X}\rbrack}{e^{t\cdot (1+\delta)\cdot\mu)}}$...<font color="Red">Markov inequality</font>  
>
>Since each $X_{i}$ is independent, we have  
>$E\lbrack e^{t\cdot X}\rbrack$  
>=$E\lbrack e^{t\cdot \sum_{i=1}^{n}X_{i}}\rbrack$  
>=$E\lbrack e^{t\cdot (X_{1}+X_{2}+...+{X_{n}})}\rbrack$  
>=$E\lbrack \prod_{i=1}^{n} e^{t\cdot X_{i}}\rbrack$  
>=$\prod_{i=1}^{n} E\lbrack e^{t\cdot X_{i}}\rbrack$  

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