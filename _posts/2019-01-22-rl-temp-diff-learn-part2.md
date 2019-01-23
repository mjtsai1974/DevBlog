---
layout: post
title: Temporal Difference Learning - Part 2
---

## Prologue To The <font color="Red">Temporal Difference Learning</font> - Part 2
<p class="message">
This is the part 2, new introduce $TD(0)$, continue with advantages and cons of $TD(0)$, $TD(1)$, come out with conclusion in <font color="Red">TD($\lambda$)</font>.  
</p>

### <font color="Red">$TD(0)$</font> Algorithm: $\lambda$=$0$
>This is by taking $\lambda$=$0$ in <font color="Red">$TD(\lambda)$</font> algorithm.  
><font color="DeepSkyBlue">[The rule]</font>
>Eposide $T$:  
>$\;\;$For all $S$, $e(S)$=<font color="Red">$0$</font> at <font color="DeepSkyBlue">start</font> of eposide, $V_{T}(S)$=$V_{T-1}(S)$  
>$\;\;$After $S_{t-1}\xrightarrow{r_{t}}S_{t}$:(from step $t-1$ to $t$ with <font color="#9300FF">reward</font> $r_{t}$)  
>$\;\;\;e(S_{t-1})$=$e(S_{t-1})$+$1$:  
>$\;\;\;\;$Update <font color="DeepSkyBlue">eligibility</font> of $S_{t-1}$ after arriving to $S_{t}$  
>$\;\;$For all $S$,  
>$\;\;V_{T}(S)$=$V_{T-1}(S)$+$\alpha_{T}\cdot(r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1}))$...[A]  
>$\;\;\;e(S_{t-1})$=$0\cdot\gamma\cdot e(S_{t-1})$=<font color="Red">$0$</font>:  
>$\;\;\;\;$<font color="Red">before</font> transite from $S_{t-1}$ to $S_{t}$ in <font color="Red">next</font> iteration, we can easily tell that <font color="DeepSkyBlue">the eligibility of state $S$ is always zero</font>.  
>
><font color="DeepSkyBlue">[Notes]</font>
>&#10112;the 2nd part of (A) is sum of the <font color="#9300FF">reward</font> plus the the <font color="#D600D6">discounted</font> value of the state we just arrived, minus the state value we just left; where these state values are all evaluated in <font color="Red">last</font> iteration.  It could just be the <font color="Red">temporal difference</font>.  
>&#10113;we are going to apply the <font color="Red">temporal difference</font> onto <font color="Red">$S$ itself only</font>, with <font color="RosyBrown">no proportion to the eligibility of any other states</font>, and the <font color="Red">learning rate</font> would be specified for we don't want it to move too much.  
>&#10114;<font color="Red">after</font> the state has been iterated, <font color="DeepSkyBlue">decay or decrease its eligibility</font> with $\lambda\cdot\gamma$, in their given value, in <font color="Red">$TD(0)$</font>, $\lambda$=$0$, <font color="DeepSkyBlue">the eligibility of state $S$ is always zero</font>.  
>&#10115;and we are backing up to next stae.  
>
><font color="Red">[Caution]</font>
>&#10112;<font color="Red">all the $S$ are all being done in parallel</font>.  
>&#10113;the value at state $S$(the $S$ in [A]) is going to be updated on this quantity, $r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1})$, which is the same for everybody, <font color="RosyBrown">doesn't</font> depend on which $S$ we are updating, and <font color="DeepSkyBlue">$e(S)$=$1$ is specific to the state $S$ at the moment we are evaluating(looking at)</font>.  

### MLE(Maximum Likelihood Estimate) And <font color="Red">$TD(0)$</font> Algorithm
>Given the condition that we are in $S_{t-1}$, and we don't know what state we are going to <font color="OrangeRed">end up</font> in.  But, there exists some probability of $r_{t}$+$\gamma\cdot V_{T-1}(S_{t})$-$V_{T-1}(S_{t-1})$.  
>
>If we take expectation of [A], then:  
>$V_{T}(S_{t-1})$=$\underset S_{t}E[r_{t}+\gamma\cdot V_{T-1}(S_{t})]$, we could treat it as the MLE of $V_{T}(S_{t-1})$  


### Addendum
>&#10112;[Temporal Difference Learning, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4178018883/concepts/41512300800923)  

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