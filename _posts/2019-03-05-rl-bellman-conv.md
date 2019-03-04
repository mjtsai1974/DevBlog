---
layout: post
title: Bellman Operator Makes Convergence
---

## Prologue To The <font color="Red">Bellman Operator</font> Makes <font color="Red">Convergence</font>
<p class="message">
to be conti...
</p>

<!--
Bellman Operator
Contraction Mapping
-->

<!--
### Maximum Is Non-Expansion
>Next to do ..

### Convergence Theorem: The Bellman Operator
>Next to do..the 3 properties
-->

<!--
The Q form of Bellman equation is much more useful in the context of reinforcement learning.  
Because we are going to take expectation of $Q(S,A)$=$R(S,A)+\gamma\cdot \sum_{S'}P(S,A,S')\cdot max_{A'}Q(S',A')$ by just using experienced data.  You don't need to access the reward function of the probabilistic transition function to do that.  

$V(S)$=$max_{A}(R(S,A)+\gamma\cdot \sum_{S'}P(S,A,S')\codt V(S'))$
If we try to learn the $V(S)$ values, the only one way to connect current $S$ to next $S'$ must have been done by knowing $R(S,A)$ and $P(S,A,S')$.

So the Q form is very useful in reinforcement learning when we don't know the reward and the probabilistic transition in advance.  

$Q_{T-1}(S,A)$+$\alpha\cdot(R(S,A)+\gamma\cdot \sum_{S'}P(S,A,S')\cdot max_{A'}Q_{T-1}(S',A')-Q_{T-1}(S,A))$  
-->

### Addendum
>&#10112;[Temporal Difference Convergence, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4436560172/concepts/44332503090923)  
>&#10113;[An introduction to Q-Learning: reinforcement learning, ADL](https://medium.freecodecamp.org/an-introduction-to-q-learning-reinforcement-learning-14ac0b4493cc)  

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