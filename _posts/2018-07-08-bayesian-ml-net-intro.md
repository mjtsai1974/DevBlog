---
layout: post
title: Introduction To The Bayesian Network
---

## Prologue To Introduction To The <font color="Red">Bayesian Network</font>
<p class="message">
A <font color="Red">Bayesian network</font> is a model of a system, consisting of a number of random varaibles.  It provides much more information than simple classifier(like <font color="RosyBrown">neural networks</font>, <font color="RosyBrown">support vector machines</font>),  
when used, the <font color="Red">Bayesian network</font> comes out with <font color="#C20000">the probability distribution of the values of the random variable</font> to be predicted.  
</p>

### What is a <font color="Red">Bayesian Network</font>?
>We begin by a simple graph illustration:  
>&#10112;we can treat the it as <font color="DeepSkyBlue">a structured, graphical representation of probabilistic relationships between several random variables</font>.  
>&#10113;it explicitly encodes the <font color="Red">conditional independences</font> by the <font color="OrangeRed">missing arcs</font>.  
>&#10114;it can efficiently represent the joint PDF(probability distribution function) of the whole network or the combinatorial random variables in the model.  
>&#10115;it is a generative model, which allows arbitrary queries to be answered.   
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-08-bayesian-ml-net-intro-dag.png "BN")

### The <font color="Red">Conditional Independence</font> Relationship
>In my previous article [Introduction To The Conditional Probability]({{ site.github.repo }}{{ site.baseurl }}/2018/05/25/intro-cond-prob/), I have guided you through the <font color="DeepSkyBlue">conditional dependence</font>.  This article would then step into the field of <font color="Red">conditional independence</font>.  
>
<!-- to be conti by 10.1.1.124.2195.pdf for conditional independence axioms -->
<!-- to be conti by Lecture12.pdf for conditional independence in Bayesian  networks, p.7 -->

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

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha, quiz, example</font> -->
<!-- <font color="Green">new alpha</font> -->

<!-- <font color="#C20000">conclusion, finding</font> -->
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

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->