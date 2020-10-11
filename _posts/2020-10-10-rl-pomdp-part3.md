---
layout: post
title: Partial Observable Markov Decision Process - Part 3
---

## Prologue To Partial Observable Markov Decision Process - Part 3
<p class="message">
This post will begin with the difficulties in solving <font color="Red">POMDP</font>(Partial Observable Markov Decision Process), guide you througth the illustration of value iteration, and lead you to one of the canonical approach of the <font color="Red">PWLC</font>(piecewise linear convex).  
</p>

### <font color="Red">POMDP</font> Value Function
>* <font color="OrangeRed">Bellman equation for POMDP</font>  
>$V^{\ast}(b)$=$max_{a}\{\rho(b,a)$+$\gamma\cdot\int_{b^{\'}}P(b^{\'}\vert a,b)\cdot V^{\ast}(b^{\'})db^{\'}\}$  
>, where $\rho(b,a)$=$\sum_{s}R(s,a)\cdot b(s)$, and <font color="RoyalBlue">why integrate over $b^{\'}$?</font>  
><font color="DeepSkyBlue">Because the continuous belief update in POMDP.</font>  
>>$\Rightarrow V^{\ast}(b)$=$max_{a}\{\rho(b,a)$+$\gamma\cdot\sum_{b^{\'}}P(b^{\'}\vert a,b)\cdot V^{\ast}(b^{\'})\}$  
>>, where $P(b^{\'}\vert a,b)$=$\sum_{o}\sum_{s^{\'}}P(o\vert s^{\'},a)\cdot\sum_{s}P(s^{\'}|a,b)\cdot b(s)$  
>>, which is the belief transition probability derived from POMDP transition/observation models.  
>

### Difficulties In Solving <font color="Red">POMDP</font>
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Findings in the belief update of tiger example</font>
>A <font color="Red">POMDP</font> is a generalization of MDPs to situations that <font color="RosyBrown">world states are not fully observable</font>.  
>
>Recall in my last article [POMDP - Part 2]({{ site.github.repo }}{{ site.baseurl }}/2020/08/13/rl-pomdp-part2/), the tiger example, the full illustration of <font color="Red">belief updating</font> by listening, before the agent opens the correct door, it continues to listen until the resulting belief of probability distribution over world states is to be believed converged in each path of sequence of observations.  
>
>We have 2 findings:  
>&#10112;the agent has to keep track the history of belief update with respect to observation and action taken in each unique path, <font color="#C20000">we need memory in POMDP</font>.  
>&#10113;after each action, there is a new belief from prior belief.  <font color="#C20000">The belief update process is continuous</font>.  
>
><font color="DeepSkyBlue">[Difficulties]</font>
><font color="OrangeRed">Memory(POMDP) v.s. memoryless(DMP)</font>
>POMDP lacks important state information and must be compensated by memory.  
>
><font color="OrangeRed">Extraneous information</font> in observation needs to learn to avoid/try, where such information should be maintained by a <font color="OrangeRed">memory-based model</font> of the world in order to predict what will happen accurately!!  
>
>If the agent has the complete full states, then it can choose optimal actions without memory.  
>
>Take two hallways for example, optimal policy might take right for the first, might take left for the first, a memoryless policy could not distinguish between them.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-2-hallways.png "2 hallways")
>
>You might ponder why not just use the optimal policy in each state to decide the action that leads to the maximum reward!!  Because in POMDP, to make observation after taking an action, <font color="DeepPink">we need further to know what state we are ranging from, to estimate such probabilistic observation, we need memory for these belief state information</font>.  
>
>If we'd like to get reward $R_{1}$, we might take left given that we are in $S_{1}$, then we need to remember that we are in $S_{1}$ already.  

### Addendum
>&#10112;[Partial Observable Markov Decision Process, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4677668675/concepts/46822685970923)  

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