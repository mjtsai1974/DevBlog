---
layout: post
title: Model-Based RL Algorithm RMAX - Part 3
---

## Prologue To Model-Based RL Algorithm <font color="Red">RMAX</font> - Part 3
<p class="message">
The major insight behind the <font color="Red">RMAX</font> algorithm is the property that <font color="#C20000">it is always either optimal or it leads to efficient learning</font>.   
</p>

### The <font color="Red">RMAX</font> Property: <font color="#C20000">Implicit Explore Or Exploit</font>
>At each point during the learning process, the agent can either choose <font color="OrangeRed">one</font> of below:  
>&#10112;to exoplore to other states, <font color="OrangeRed">or</font>  
>&#10113;to exploit over the same state.
>
>If the agent follows an optimal policy with respect to the model it maintains for $T$ steps, it will either attain near-optimal average reward or it will update the statistics for one of the <font color="OrangeRed">unknown</font> states with sufficient high probability.
>
><font color="DeepPink">The choice in betwqeen exploration and exploitation is implicit.</font>  

### Prerequisites For <font color="#C20000">Implicit Explore Or Exploit</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Basic definition</font>  
>Before we proof <font color="DeepPink">The choice in betwqeen exploration and exploitation is implicit</font>, there shall exist definition of prerequisites to make this theorem of property more concrete:  
>&#10112;define $M$ to be a <font color="OrangeRed">stochastic game</font>.  
>&#10113;define $L$ to be a set of unknown states in the form of $(G_{i},a,a^{\'})$, that is to say $G_{i}$ is an unknown state.  
>&#10114;define $M_{L}$ to be a <font color="OrangeRed">stochastic game</font> identical to $M$, except that $M_{L}$ contains an extra $G_{0}$ state with $P(G_{i},a,a^{\'},G_{0})$=$1$ for any $G_{i}\in L$, and the reward is $R_{max}$ for the agent, and $0$ for the adversary.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">More detail</font>  
>Take a more close look in above definition:  
>* <font color="OrangeRed">$M_{L}$ is the deduced model of $M$</font>  
>&#10112;in the beginning of <font color="Red">RMAX</font> algorithm, <font color="OrangeRed">we treat all states as unknown</font>.  
>
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-02-28-rl-rmax-part3-implicit-explicit-exp-1.png "RMAX init")
>
>* After explore or exploit over some horizon in the given sampling of data  
>&#10112;the reward of known states in $M_{L}$ is at least as large as in $M$, in the instance of $G_{K}$.  
>&#10113;the optimal policy deduced out in $M_{L}$ is also optimal with respect to $M$.  Because $M_{L}$ is almost the same as $M$, except that $M_{L}$ has an extra $G_{0}$ with transitive probability to $1$ from all other states to $G_{0}$.  
>
>Base on all above, we'd like to prove the nature of implicit or explicit explore will either attains optimal reward or leads to efficient learning.  

### Addendum
>&#10112;[R-max: A General Polynomial Time Algorithm for Near-Optimal Reinforcement Learning, Ronen I. Brafman, CS in Ben-Gurion University, Moshe Tennenholtz, CS in Stanford University](http://www.jmlr.org/papers/volume3/brafman02a/brafman02a.pdf)  

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