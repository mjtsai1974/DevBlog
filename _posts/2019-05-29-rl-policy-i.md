---
layout: post
title: Policy Iteration
---

## Prologue To <font color="Red">Policy Iteration</font>
<p class="message">
Prior post reveals that <font color="Red">value iteration</font> eventually leads us to the <font color="DeepPink">optimal policy</font> providing the action for the current state to take to get its maximum value when transiting to next state.  
Departuring from <font color="OrangeRed">multiple states</font> in <font color="OrangeRed">one MDP model</font>, this article would guide you through <font color="Red">value iteration</font> to find the <font color="#00ADAD">greedy policy</font> in each state's transition, and finally get the <font color="DeepPink">optimal policy</font> for each state.  The whole process is called <font color="Red">policy iteration</font>.  
</p>

### <font color="Red">Policy Iteration</font> Versus <font color="Red">Value Iteration</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The beginning in MDP</font>  
>Suppoose we are departuring from a beginning state in <font color="OrangeRed">one MDP model</font>, each time we do make a decision to choose the best action that can transit us to next state with the maximum value(or reward), and we are doing this over and over again, until we believe that we have build the <font color="DeepPink">optimal policy</font> for each state, and it brings the whole MDP problem to a convergence.  
>
>This means that <font color="RosyBrown">we are not facing the problem to choose the action of uncertainty in one single state</font>, and the same state would then be re-visited, since we are repeating this over and over again.  
>
><font color="OrangeRed">There is no doubts that different or similar policies in one same state often interleave one over the others</font>, that's the <font color="Red">policy iteration</font> process.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The concept of policy iteration</font>  
>We have actually involved below 3 phases on the way to solve a MDP issue:  
>&#10112;initially, $\forall S, Q_{0}(S)=0$...[A]  
>&#10113;proceeds with <font color="OrangeRed">policy improvement</font>  
>$\forall S, \pi_{t}(S)$=$maxarg_{A}Q_{t}(S,A), t\geq 0$...[B]  
>&#10114;do the <font color="OrangeRed">policy evaluation</font> task  
>$\forall S, Q_{t+1}(S)$=$Q^{\pi_{t}}(S)$...[C]  
>
>We are starting by picking any <font color="OrangeRed">arbitrary</font> $Q$ function, denote it the initialization step, that's [A].  
>
>After that, we just iterate by taking the $t$-th, $Q_{t}$ function, computing its <font color="#00ADAD">greedy policy</font>, $\pi_{t}(S)$, that's [B], then use that <font color="#00ADAD">greedy policy</font> to get a new $Q$ function, say $Q_{t+1}$, that's [C].  
>
>And we are repeating and iterating this over and over again.  So each time we go around in this loop, we rae taking our <font color="OrangeRed">previous $Q$ function</font>, finding its <font color="#00ADAD">policy</font>, taking that <font color="#00ADAD">policy</font> to find its <font color="OrangeRed">next value function</font>, such repeating would actually get convergence in finite time.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Policy iteration is a better way</font>  
>The sequence of $Q$ functions we get convergence to $Q^{\ast}$ after we are experienced <font color="OrangeRed">a series of value iteration</font> in <font color="OrangeRed">finite time</font>, in particular, it illustrates how <font color="Red">policy iteration</font> works implicitely in my prior post.  
>
>The <font color="OrangeRed">convergence of policy iteration is at least as fast as value iteration</font> in that <font color="OrangeRed">if at any point we sync up the $Q$ functions, we start value iteration and policy iteration from the same $Q$ function</font>.  Then, <font color="DeepPink">each step this policy iteration takes is moving us towards the optimal $Q$ function, no more slowly than value iteration</font>.  
>
>So, <font color="OrangeRed">policy iteration is a better way</font>.

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