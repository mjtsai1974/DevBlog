---
layout: post
title: Introduction To The Central Limit Theorem
---

## Prologue To <font color="Red">The Central Limit Theorem</font>
<p class="message">
<font color="Red">The central limit theorem</font> is a <font color="DeepSkyBlue">refinement of the law of large number</font>.  For a large number of random variables $X_1$,$X_2$,...,$X_n$, with <font color="DeepSkyBlue">converged</font> expect value and <font color="DeepSkyBlue">finite</font> variance, the <font color="DeepPink">standardization process would settle down $\overline {X_n}$ in a normal distribution</font>, irrelevant to the original distribution these $X_i$ is belonging to.
</p>

### <font color="Red">Standardizing</font> The Average
>Given a large number of random variables $X_i$ belonging to the same sample, with the same expect value $\mu$ and variance $\sigma^{2}$, <font color="OrangeRed">the law of large number guarantees the average would approximate to $\mu$</font>.  
>
>Here comes the question as <font color="OrangeRed">what is the distribution of $\overline {X_n}$?</font>  Since each random variables $X_i$ has the same $\mu$ and $\sigma^{2}$, it would be a good idea <font color="DeepSkyBlue">to stablize the expect value and variance of $\overline {X_n}$</font>.  
>
>We already know $E\lbrack \overline{X_n}\rbrack$=$\mu$ and $Var\lbrack \overline{X_n}\rbrack$=$\frac {\sigma^{2}}{n}$.  <font color="OrangeRed">What would be the acceptable expect value with regards to the stablized variance?</font>  
>&#10112;by $E\lbrack \overline{X_n}-\mu\rbrack$=$0$, we can <font color="DeepSkyBlue">zerolize</font> the expect value, to be believed the smallest value.  
>&#10113;next to make the variance stable, suppose there exists any $c>0$ such that $Var\lbrack c\cdot\overline{X_n}\rbrack$ could be well stablized.  If we can <font color="DeepSkyBlue">factor out whatever the variance residing in the distribution of $\overline {X_n}$</font> itself, then there will be a hope.  For unknown distribution, this is quiet difficult.  
>&#10114;but, we would make it easy by taking $c=\frac {\sqrt n}{\sigma}$, the mathematic thing guarantees the purity and balance of the variance, since $Var\lbrack \frac {\sqrt n}{\sigma}\cdot\overline{X_n}\rbrack$=$\frac {n}{\sigma^{2}}\cdot Var\lbrack \overline{X_n}\rbrack$=$1$  
>&#10115;$Var\lbrack \frac {\sqrt n}{\sigma}\cdot(\overline{X_n}-\mu)\rbrack$  
>=$Var\lbrack \frac {\sqrt n}{\sigma}\cdot\overline{X_n}\rbrack$, we can further stablize the variance in a <font color="DeepSkyBlue">centered average</font> format.  
>
>Above procedure is the <font color="Red">standardization</font> or the <font color="Red">standardize process</font>.

### <font color="Red">The Central Limit Theorem</font>
>Given $X_1$,$X_2$,...,$X_n$ are <font color="DeepSkyBlue">identically independent distributed</font> random variables, each has the same expect value $\mu$ and variance $\sigma^{2}$, which are all <font color="OrangeRed">finite</font>.  
>For any $n\ge 1$, let $Z_n$ be any random variable, defined by  
><font color="DeepSkyBlue">$\;\;\;\;Z_n$=$\frac {\overline {X_n}-\mu}{\sigma/\sqrt {n}}$;</font>  
>then, $E\lbrack Z_n\rbrack$=$0$ and $Var\lbrack Z_n\rbrack$=$1$.  
><font color="DeepPink">$Z_n$ itself is the standard normal distribution, $N(0,1)$</font>, for any $a$, we have $F_{Z_n}(a)$=$ɸ(a)$.  
>
><font color="DeepSkyBlue">We treat $Z_n$ as the standardized $\overline {X_n}$.</font>  

### <font color="RoyalBlue">Example</font>: Illustration Of <font color="Red">The Central Limit Theorem</font>
>Suppose you are given a random sample of size $500$ containing random variables $X_1$,$X_2$,...,$X_500$, all of them coming from the same <font color="OrangeRed">unknown</font> distribution with each having expect value $2$ and variance also $2$.  
><font color="OrangeRed">After completing all the $500$ runs of test, we get the experiement average of $\overline {X_n}$=$2.06$, do you think it a plausible result?</font>  
>To answer this question, we have to compute <font color="DeepSkyBlue">the probability of the case that $\overline {X_n}$ is greater than or equal to $2.06$</font>.  
>$P(\overline {X_n}\ge 2.06)$  
>=$P(\overline {X_n}-\mu\ge 2.06-\mu)$  
>=$P(\frac {\overline {X_n}-\mu}{\sigma/\sqrt {n}}\ge \frac {2.06-\mu}{\sigma/\sqrt {n}})$  
>=$P(\frac {\overline {X_{500}}-\mu}{\sigma/\sqrt {500}}\ge \frac {2.06-2}{\sqrt {2}/\sqrt {500}})$...$\mu$=$2$,$\sigma$=$\sqrt {2}$  
>=$P(Z_{500}\ge 0.95)$  
>=1-$P(Z_{500}<0.95)$  
>=1-$ɸ(0.95)$  
>$\approx 0.1711$, <font color="DeepSkyBlue">it indicates that there exists probability of $0.1711$ that the average is $0.06$ larger than $2$</font>, the expect value of the real thing.  
>Since $0.1711$ is quiet a large probability, it is rather weak to say that $2.06$ is an abnormal experimental result of average.  <font color="DeepPink">$2.06$ would thus be plausible.</font>  

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