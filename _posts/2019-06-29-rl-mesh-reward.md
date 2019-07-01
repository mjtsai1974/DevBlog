---
layout: post
title: Meshing The Rewards
---

## Prologue To <font color="Red">Meshing The Rewards</font>
<p class="message">
In order to avoid the <font color="Red">local suboptimal</font> endless looping, the suggestive approach is <font color="DeepPink">to mesh the reward funtion without impact on the original optimal policy</font>.  The reward function should contain <font color="RosyBrown">not only the fixed return of constant</font>, as we are losing benifit of value obtained in current state, when transiting from current state to next state.  
</p>

### Why To Change The Reward Function In MDP?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">A brief summary</font>  
>As we have a lot study in MDP, we know that state value chnages(or has been accumulated), which is enclosed with every occurrence of state transition:  
>&#10112;it begins with initial configuration.  
>&#10113;makes value iteration by Bellman equation(or operation), coming out some policy, maybe non-optimal, suboptimal, or even the final optimal.  
>&#10114;then value improvement after policy iteration and leads to the very next policy improvement.  
>&#10115;oever and over again, finally to the convergence.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Because of the state transition</font>  
>We have learned the fact that the state value changes as transiting from current to next state.  <font color="DeepSkyBlue">Should the reward function returns only the fixed constant values?</font>  We think it mandatory to <font color="OrangeRed">reshape</font> the reward function.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="RosyBrown">The common issue in AI</font>  
>It would be easy to just <font color="RosyBrown">turn the reward function into all zeros</font>, then, <font color="RosyBrown">all policies maximize that reward function</font>, in which case, <font color="RosyBrown">learning is done</font>.  But, this is <font color="RosyBrown">not the problem we are trying to solve</font>.  
>
>This is a <font color="RosyBrown">common issue in AI</font>.
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">The target</font>  
>The reward function is a way to specify the behavior that is going to get compiled by the learning algorithminto actual behavior.  
>
>The semantics we'd like the agent to do by changing the reward function is for the efficiency:  
>&#10112;<font color="OrangeRed">speed of computation and experience</font> that the agent needs to learn.  
>&#10113;<font color="OrangeRed">space of memory</font> the learning algorithm requires.  
>&#10114;<font color="OrangeRed">solvability</font>, infinity versus <font color="RosyBrown">not</font>-infinity.  
>
>We want <font color="DeepPink">to change the reward function without changing what it's originally optimizing</font>.  

### Change The Reward Function
><font color="RoyalBlue">[Question]</font>  
>How to <font color="DeepPink">change the reward function without changing the optimal policy</font>?  
>
><font color="DeepSkyBlue">[Answer]</font>  
>We have defined MDP with states, actions, rewards, probability transition and gamma, denoted as $<S,A,R,P,\gamma>$.  
>
>By messing with $R$ only, and leaving all the rest uncganged:  
>&#10112;<font color="OrangeRed">multiply</font> the reward function by any <font color="DeepPink">positive</font> constant  
>&#10113;<font color="OrangeRed">shift</font> the reward function by constant  
>&#10114;<font color="Red">non-linear potential-bsed rewards</font>  

### <font color="OrangeRed">Multiply</font> $R$ By <font color="DeepPink">Positive</font> Constant: Illustration
><font color="RoyalBlue">[Question]</font>  
>$Q(S,A)$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q(S',A')$  
>This is the <font color="Red">Bellman equation</font> we already familar with, and multiply $R(S,A)$ by constant $c$ to get the new reward function, that is $R'(S,A)$=$c\cdot R(S,A)$, where $c>0$, then what is $Q'(S,A)$=?  
>
><font color="DeepSkyBlue">[Answer]</font>  
>We are asking $Q'(S,A)$ in terms of $Q(S,A)$, let's do the illustration:  
>$Q'(S,A)$  
>=$R'(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q'(S',A')$  
>=$c\cdot R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}($  
>$\;\;c\cdot R(S',A')$+$\gamma\cdot\sum_{S^{\"}}P(S^{\"}\vert S',A')\cdot max_{A^{\"}}Q'(S^{\"},A^{\"}))$  
>
>where we have  
>$Q'(S',A')$  
>=$c\cdot R(S',A')$+$\gamma\cdot\sum_{S^{\"}}P(S^{\"}\vert S',A')\cdot max_{A^{\"}}Q'(S^{\"},A^{\"}))$  
>
>in turn, we have  
>$Q'(S^{\"},A^{\"})$  
>=$c\cdot R(S^{\"},A^{\"})$+$\gamma\cdot\sum_{S^{\'\'\'}}P(S^{\'\'\'}\vert S^{\"},A^{\"})\cdot max_{A^{\'\'\'}}Q'(S^{\'\'\'},A^{\'\'\'}))$  
>
>still more, we have  
>$Q'(S^{\'\'\'},A^{\'\'\'})$  
>=$c\cdot R(S^{\'\'\'},A^{\'\'\'})$+$\gamma\cdot\sum_{S^{\'\'\'\'}}P(S^{\'\'\'\'}\vert S^{\'\'\'},A^{\'\'\'})\cdot max_{A^{\'\'\'\'}}Q'(S^{\'\'\'\'},A^{\'\'\'\'}))$  
>
>therefore,  
>$Q'(S',A')$  
>=$c\cdot R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}($  
>$\;\;c\cdot R(S',A')$+$\gamma\cdot\sum_{S^{\"}}P(S^{\"}\vert S',A')\cdot max_{A^{\"}}Q'(S^{\"},A^{\"}))$  
>=$c\cdot (R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}($  
>$\;\;R(S',A')+\gamma\cdot\sum_{S^{\"}}P(S^{\"}\vert S',A')\cdot max_{A^{\"}}(R(S^{\"},A^{\"})+...)))$  
>=$c\cdot Q(S,A)$  
>
><font color="DeepSkyBlue">[Notes::1]</font>  
><font color="OrangeRed">Multiply $R$ by zero leaves everything the same</font>  
>If you multiply the reward function by <font color="OrangeRed">zero</font>, each state transition will bring zero as the return, all states' value will all be zero, you will <font color="OrangeRed">lose all the information</font>.  
>
><font color="DeepSkyBlue">[Notes::2]</font>  
><font color="OrangeRed">$R$ negative multiply maximize the pain</font>  
>If you multiply the reward function by <font color="OrangeRed">negative value</font>, then the convergence would end up in <font color="OrangeRed">maximizing the pain</font>, or <font color="OrangeRed">by special design in policy iteration to converge in least pain</font>.  

### Addendum
>&#10112;[Meshing with rewards, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4388428967/concepts/43556087730923)  

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