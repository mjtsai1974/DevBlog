---
layout: post
title: Partial Observable Markov Decision Process - Part 2
---

## Prologue To Partial Observable Markov Decision Process - Part 2
<p class="message">
This post will make a full illustration of belief update in <font color="Red">POMDP</font>(Partial Observable Markov Decision Process).  
</p>

### <font color="OrangeRed">The Real World Is Almost Partially Observable</font>
>* Regular MDP  
>When we are in the regular MDP, the agent observes the state of the environment, it can make full observation.  The chess grid and the 2 states examples exhibit the environment of the regular MDP.  
>&#10112;[Markov Decision Process In Stochastic Environment]({{ site.github.repo }}{{ site.baseurl }}/2017/12/03/mdp-markov-decision-process-stochastic-env/)  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-grid.png "Grid MDP")
>&#10113;[Markov Decision Process To Seek The Optimal Policy]({{ site.github.repo }}{{ site.baseurl }}/2017/12/04/mdp-markov-decision-process-optimal-policy/)  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-2-states.png "2 states MDP")
>
>* Partially Observable MDP  
>If we are <font color="RosyBrown">in the partially observable environment, the agent can't observe the full world state, but the observation gives hint about true state</font>.  
>&#10112;the agent has no idea about the world state, what's behind the door, where am I.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-intuition.png "world state")
>&#10113;the agent don't know what state he is in if he didn't get reward after taking action.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-2-way-hallway.png "what state")

### Addendum
>&#10112;[Partial Observable Markov Decision Process, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4677668675/concepts/46822685970923)  
>&#10113;[Decsision Making in Intellingent Systems: POMDP, 14 April 2008, Frans Oliehoek](http://www.fransoliehoek.net/docs/pomdp-lect-b.pdf)  

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