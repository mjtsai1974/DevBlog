---
layout: post
title: More On Value Iteration
---

## Prologue To More On <font color="Red">Value Iteration</font>
<p class="message">
Prior post details the way <font color="Red">contraction mapping</font> makes <font color="Red">value iteration</font> converges.  This post would dive a little bit on the <font color="DeepSkyBlue">horizontal length</font> for convergence.
</p>

### $\frac {1}{1-\gamma}$ Bits Of Precision
>We'd like to dive a little bit to relate the <font color="DeepSkyBlue">horizontal length</font> to the <font color="OrangeRed">convergence</font>, by below given:  
>&#10112;denote the <font color="OrangeRed">dimensionality</font> of states and actions as $\vert S\vert$ and $\vert A \vert$.  
>&#10113;also with $R_{max}$=$max_{S,A}\vert R(S,A)\vert$.  
>&#10114;$\frac {1}{1-\gamma}$ as bits of precision.  
>&#10115;for some $t^{\ast}$ polynomial in $\vert S\vert$ and $vert A \vert$.  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">There is some time before infinity</font>  
>&#10112;$\pi(S)$=$argmax_{A}Q_{t^{\ast}}(S,A)$ is optimal.    
>&#10113;we treat the $Q^{\ast}$ to be the $Q$ function after we iterate over $t^{\ast}$ times, we know that it converges in the limit, $Q_{t}$ eventually goes to $Q^{\ast}$.  
>
>$\Rightarrow$Here is the <font color="OrangeRed">hint</font> that we found there is some $t^{\ast}$ of <font color="OrangeRed">finite horizon</font>, <font color="Red">less than infinity</font>, that's <font color="DeepSkyBlue">polynomial</font> in:  
>&#10112;the <font color="OrangeRed">number of states</font>  
>&#10113;the <font color="OrangeRed">number of actions</font>  
>&#10114;the <font color="OrangeRed">magnitude of the rewards</font> in the reward function  
>&#10115;the <font color="OrangeRed">number of bits of precision</font> that are used to specified the <font color="Red">transition probability</font>  
>&#10116;<font color="OrangeRed">number of bits</font> of $\gamma$ in $\frac {1}{1-\gamma}$  
>
>$\Rightarrow$So, that, if we run value iteration for that <font color="DeepSkyBlue">many steps</font>, the $Q$ function that we get out is $Q_{t^{\ast}}$ of $(S,A)$.  If we define a <font color="#00ADAD">policy $\pi(S,A)$</font>, which is just the <font color="#00ADAD">greedy policy</font> with respect to that $Q$ function, then that <font color="#00ADAD">policy</font> is <font color="Red">optimal</font>.  
>
>$\Rightarrow$We know that <font color="OrangeRed">in the limit</font>, if we run value iteration for an <font color="OrangeRed">infinite</font> number of steps, then the $Q$ function that we get at that point, the <font color="#00ADAD">greedy policy</font> with respect to the $Q$ function, is just <font color="Red">optimal</font>.  
>
>$\Rightarrow$This leads to a finding that <font color="DeepPink">there is sometime before infinity where we get a $Q$ function that's close enough, so that if you do the greedy policy with respect to it(the $Q$ function), it really is optimal</font>.  Like all the way $100\%$ optimal.  
>
>$\Rightarrow$What that really means is that <font color="#C20000">it's polynomial(all the way $100\%$ optimal)</font> and <font color="DeepPink">you can actually solve this in a reasonable amount of time</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">$\frac {1}{1-\gamma}$ is not so just polynomial</font>  
>The whole convergence <font color="RosyBrown">might not be so just polynomial</font>, why?  The $\gamma$ in $\frac {1}{1-\gamma}$ is the key factor, <font color="RosyBrown">as $\gamma\rightarrow 1$, this blows up and that's not polynomial bounded</font>, say the number of bits it takes to write down $\gamma$.  
>
>$\Rightarrow$So, it's <font color="DeepPink">exponential</font> in terms of <font color="DeepPink">the number of bits</font> it takes to write down the whole problem.  

### Addendum
>&#10112;[Advanced, algorithmic, analysis, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4602578895/concepts/45888989130923)  

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