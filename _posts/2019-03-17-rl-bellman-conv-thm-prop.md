---
layout: post
title: Bellman Operator And Convergence Properties
---

## Prologue To The <font color="Red">Bellman Operator</font> And <font color="Red">Convergence Properties</font>
<p class="message">
The <font color="Red">Bellman operator</font> of <font color="Red">contraction mapping</font> makes the <font color="OrangeRed">statement</font> of convergence concrete and come out the major properties.
</p>

### The Statement of Convergence
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The statement</font>  
>&#10112;let <font color="Red">B</font> be an operator of <font color="Red">contraction mapping</font>, and $Q^{\ast}$=$BQ^{\ast}$ be it's fixed point.  
>&#10113;let $Q_{0}$ be a $Q$ function, and define $Q_{t+1}$=$\lbrack B_{t}Q_{t}\rbrack Q_{t}$, then $Q_{t}\rightarrow Q^{\ast}$.  
>
>Suppose we have been given some sequence of $Q$ functions.  
>&#10112;it starts off with $Q_{0}$ and the way we're going <font color="DeepSkyBlue">to generate the next step from the previous step</font>, is that we are going to have a <font color="Green">new</font> kind of operator, $B_{t}$.  
>&#10113;$B_{t}$ is going to be applied to $Q_{t}$, producing an operator $\lbrack B_{t}Q_{t}\rbrack$ that we then apply to $Q_{t}$, and that's what we assign $Q_{t+1}$ to be.  
>
>So, in the context of $Q$ learning, this is essential the <font color="Red">$Q$ learning update</font>, there exists <font color="DeepSkyBlue">2 different $Q$ functions</font> that are used in the <font color="Red">$Q$ learning update</font>:  
>&#10112;one is the $Q_{t}$ function in $\lbrack B_{t}Q_{t}\rbrack$ that is used to <font color="DeepSkyBlue">average</font> together, to take care of the fact there is <font color="OrangeRed">noise</font> in the <font color="#8400E6">probabilistic transitions</font> of <font color="#EB00EB">stochasticity</font>.  
>&#10113;the other one is the $Q_{t}$ that we are using in the <font color="DeepSkyBlue">one step look ahead</font> as part of the <font color="Red">Bellman operation</font>.   
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Special notes</font>  
>to be conti...

### Addendum
>&#10112;[Convergence-1, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4436560172/concepts/44332503000923)  
>&#10113;[Convergence-2, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4436560172/concepts/44332503010923)  
>&#10114;[Convergence theorem explained-1, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4436560172/concepts/44332503020923)  
>&#10115;[Convergence theorem explained-2, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4436560172/concepts/44332503030923)  

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

<!--
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Why at this moment, the Poisson and exponential probability come out with different result?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->