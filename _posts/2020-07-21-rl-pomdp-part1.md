---
layout: post
title: Partial Observable Markov Decision Process - Part 1
---

## Prologue To Partial Observable Markov Decision Process - Part 1
<p class="message">
This post is an entry of <font color="Red">POMDP</font>(Partial Observable Markov Decision Process), from the most foundamental to the belief update.  
</p>

### Summary Of All Markov Models
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Markov chain</font>  
>&#10112;finite number of <font color="OrangeRed">discrete</font> states with probabilistic transition between states.  
>&#10113;the <font color="DeepSkyBlue">Makrov property</font> is that <font color="DeepSkyBlue">next state is determined by current state only!!</font>  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Hidden Markov model</font>  
>&#10112;all the same in Markov chain, except that <font color="OrangeRed">we're unsure which state we are in.</font>  
>&#10113;the current state emits an observation.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Markov decision process</font>  
>&#10112;finite number of <font color="OrangeRed">discrete</font> states.  
>&#10113;probabilistic transition between states and executable actions in each state.  
>&#10114;<font color="DeepSkyBlue">next state is determined by current state and current action.</font>  
>&#10115;<font color="OrangeRed">the execution of an action might lead to unexpected result due to random stochasticity.</font>  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Partial observal Markov decision process</font>  
>&#10112;all the same as Markov decision process, except that <font color="OrangeRed">we're unsure which state we are in.</font>  
>&#10113;the current state emits an observation.  
>
>Below table exhibits the summary:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-07-21-rl-pomdp-part1-summary.png "Summary")

### <font color="Red">Belief States</font> In POMDP
>Below exhibits the POMDP model, wherein the probability distribution is over the world states with <font color="Red">true state is only partially observable</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-07-21-rl-pomdp-part1-model.png "POMDP")
>
>&#10112;the agent keeps/maintains an internal <font color="Red">belief state</font>, say <font color="Red">$b$</font>, that summarizes its experience.  
>&#10113;the agent makes state estimation to update from <font color="Red">belief state</fonmt> $b$ to next <font color="Red">belief state</font> $b^{\'}$, based on the last action it has taken, the current <font color="OrangeRed">observation</font> it has made, and the previous <font color="Red">belief state</font> $b$.  

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