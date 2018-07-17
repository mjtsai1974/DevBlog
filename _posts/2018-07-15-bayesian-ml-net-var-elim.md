---
layout: post
title: Variable Elimination In Bayesian Network
---

## Prologue To Variable Elimination In <font color="Red">Bayesian Network</font>
<p class="message">
<font color="Red">Inference</font> via <font color="Red">Bayesian Network</font> could be achieved by probabilistic marginalization, i.e. summing out over <font color="DeepSkyBlue">irrelevant</font> or <font color="DeepSkyBlue">hidden</font> variables.  
</p>

### <font color="Red">Inference</font> Via <font color="Red">Bayesian Network</font>
>Given a well-constructed BN of nodes, 2 types of inference are supported:  
>&#10112;<font color="Red">predictive</font> support(<font color="Red">top-down reasoning</font>) with the evidence nodes connected to node $X$, through its parent nodes, the same direction as predictive propagation.  
>&#10113;<font color="Red">diagnostic</font> support(<font color="Red">bottom-up reasoning</font>), with vidence nodes connected to node $X$, through its children nodes, the same direction as <font color="Red">retrospective</font> propagation.  
>
>In my Bayesian articles, I have guided you through both types of support by means of <font color="DeepSkyBlue">variable enumeration</font> over the factorized terms of full joint PDF(probability distribution function).  Most of the examples are all in small network, trivially, <font color="DeepSkyBlue">variable enumeration</font> is old, she will hold for complex model consisting of a lot random variables, resulting in high expenditure of computation efficiency.  

<!--
### Addendum
>&#10112;[](http://kuleshov.github.io/cs228-notes/inference/ve/)  
>&#10113;[](https://www.youtube.com/watch?v=FDNB0A61PGE)  
>&#10114;[](https://www.youtube.com/watch?v=qyXspkUOhGc&list=PLBF898A2F63224F39&t=0s&index=14)  
>&#10115;[Bayesian Networks, Ben-Gal Irad, in Ruggeri F., Faltin F. & Kenett R., Encyclopedia of Statistics in Quality & Reliability, Wiley & Sons (2007).](http://www.eng.tau.ac.il/~bengal/BN.pdf)  
-->

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

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus, mathematic expression</font> -->
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