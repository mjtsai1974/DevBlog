---
layout: post
title: Introduction To The Conditional Probability
---

## Prologue To Introduction To The <font color="Red">Conditional Probability</font>
<p class="message">
<font color="DeepSkyBlue">Based on the probability of some already occurred event, we can infer or reassess the probability of another event</font>, which is the major effect of the <font color="Red">conditional probability</font>.
</p>

### Definition: <font color="Red">Conditional Probability</font>
>Given the probability $P(C)$ of the <font color="OrangeRed">already occurred event</font> $C$, we can compute another event $A$'s probability $P(A\vert C)$.  The <font color="Red">conditional probability</font> is defined:  
>$\;\;\;\;P(A\vert C)$=$\frac {P(A\cap C)}{P(C)}$, provided that $P(C)>0$.  
>
>This implies that <font color="DeepSkyBlue">the conditonal probability could help to find out the fraction of the probability of event $C$ <font color="OrangeRed">is also</font> in event $A$</font>, which is <font color="OrangeRed">$P(A\cap C)$</font>.  

### <font color="Red">Conditional Probability</font> <font color="DeepSkyBlue">Properties</font>
>Given that $P(C)>0$, we can deduce out below <font color="DeepSkyBlue">properties</font>:  
>&#10112;$P(A\vert C)$+$P(A^{c}\vert C)$=$1$, holds for all conditions.  
>&#10113;if $A\cap C$=$0$, then $P(A\vert C)$=$0$.  
>&#10114;if $C\subset A$, then $A\cap C$=$C$, $P(A\vert C)$=$1$.  
>&#10115;if $A\subset C$, then $A\cap C$=$A$, $P(A\vert C)$=$\frac {P(A)}{P(C)}\ge P(A)$, since $P(C)\le 1$.  

<!-- Γ -->
<!-- \Omega -->
<!-- \subset -->
<!-- \cap intersection -->
<!-- \cup union -->
<!-- P(A\vert C) -->
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
<!-- http://www.wiris.com/editor/demo/en/ -->