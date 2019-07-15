---
layout: post
title: Meshing The Rewards - Part 2
---

## Prologue To <font color="Red">Meshing The Rewards</font> - Part 2
<p class="message">
<font color="DeepPink">Meshing the reward funtion without impact on the original optimal policy</font> by taking <font color="Red">potential</font>(or <font color="Red">states of the world</font>) into consideration is the suggestive approach <font color="RosyBrown">not</font> to struggle over the <font color="Red">local suboptimal</font> endless looping.  
</p>

### The Concept Of <font color="Red">Potential</font>
>Instead of giving static( or fixed) bonus at the moment the state transition has been done, we change to put a little bonus with regards to the <font color="Red">states of the world</font>.  When you <font color="DeepPink">achieve a certain state of the world</font>, you <font color="DeepPink">get the bonus</font>, when you <font color="RosyBrown">unachieve that state of the world</font>, you <font color="RosyBrown">lose that bonus</font>.  Everything balances out nicely.  
>
><font color="Brown">[mjtsai think]</font>  
>Step further, such intuition should be aligned with <font color="Brown">Calculus fashion</font>, when it is <font color="Brown">in some fixed point</font> and <font color="Brown">approaching to the target</font>, the value(bonus) should be returned in <font color="Brown">certain proportion in that fixed point</font>, and <font color="Brown">this return value varies with respect to per changing from one distincet fixed point to its next</font>, might be in the time unit, or quantity in some scale.  Such returned value could be the accumulation in either increasing or descreasing fashion.  
>
><font color="DeepSkyBlue">[Notes::1]</font>  
><font color="OrangeRed">We want to give hints</font>  
>Suppose we are design a system of learning agent to make the socker robot to kick the ball into the door.  
>
>If we follow up the prior post, the existing official reward function would give us $+100$ for scoring the goal.  Now, we might want to <font color="OrangeRed">give hints</font> to the system about:  
>&#10112;how close the robot is to the ball  
>&#10113;the robot is hitting the ball  
>&#10114;the ball enters the goal
>  
>It depends how detail you'd like your design to simulate a physical socker game, maybe  
>&#10115;how close the ball is to the goal  
>
>We need to express &#10112;,&#10113;,&#10114;,&#10115; in terms of the <font color="Red">states of the world</font>.  
>
><font color="DeepSkyBlue">[Notes::2]</font>  
><font color="Red">The potential</font>  
>As to the MDP states we already know, you can regard it as the <font color="OrangeRed">fixed</font> state, the value function returns the value(bonus) that is binding in the state, <font color="RosyBrown">not</font> the state of the world mentioned above.  
>
>So, how close the robot is to the ball is the item we'd like to keep track of, we denote it as the <font color="Red">potential</font>.  
>
>The already know bonus(the reward) obtained after per state transition is left as it is, we'd like to illustrate the way to mesh the reward function by incorporating the factor of <font color="Red">potential</font>.  

### <font color="Red">Change-In-State-Based Bonus</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Basic idea</font>  
>Suppose we are designing the learning agent of socker robot, instead of just giving little bonus as a return every time the robot does a certain thing, we are going to <font color="Red">keep track of what the state of the world is</font>.  
>
>As we are more close to the state of the world we desire, we are going to obtain reward for it, in contrary to the case we are far away from the state of the world, we are going to lose the reward gained when we are close to this state of the world.  Therefore, we should substract the reward off when we move away from those states of the world.  
>
>The point is that the <font color="Red">change-in-state-based bonus</font> thus obtained would be an <font color="Red">increment</font> or <font color="Red">decrement</font> in accordance to <font color="Red">how close or how far you are subscribed by the state of the world</font>, <font color="RosyBrown">not the fixed constant</font>.  
>
>If the robot is 5 pixels away from the ball to 10 pixels away from the ball, then we might obtain $-5$ of decrement, it depends on how you design, we can also define the bonus as the inverse of distance by $\frac {1}{distance}$, that is to say, if we change from 10 pixels away from the ball to 5 pixels away from the ball, we get $\frac {1}{5}-\frac {1}{10}$=$0.1$; in reverse direction, we lose bonus of $-0.1$.  
>
>Such kind of design <font color="OrangeRed">keeps the account balance in a good shape</font>, it gives <font color="DeepPink">positive return</font> as you are <font color="DeepPink">approaching the state of world</font>, as you <font color="RosyBrown">leaves the same state of world</font>, you just <font color="RosyBrown">lose prior bonus by negating it</font>,  you are <font color="RosyBrown">not</font> just coninue to <font color="RosyBrown">loop over and over again</font> to get that positive return.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="Brown">Change-in-state-based v.s. state-based::mjtsai1974</font>  
>Here we are about this question how to tell the difference in between <font color="Red">change-in-state-based</font> and <font color="Red">state-based</font> bonus.  If it is a <font color="Red">state-based</font>, it returns bonus of fixed value.  To reach this <font color="Red">state-based</font> point, a sequence of actions might be taken, then we involve <font color="Red">change-in-state-based</font> concern, it could also be a state in MDP.  
>
>Given that we are developing a robot socker learning agent, the major purpose of the robot is <font color="OrangeRed">to hit the ball into the target</font>, there must exist a sequence of actions that could be break down:  
>&#10112;the ball <font color="OrangeRed">enter into the target</font>, which is the goal of this system  
>&#10113;the robot should be able to <font color="OrangeRed">hit the ball</font>  
>&#10114;the robot should go <font color="OrangeRed">near the ball</font>  
>&#10115;the learning agent should evaluate <font color="OrangeRed">if the ball near the target</font>  
>
>I think you can have even more break down items, for the simplicity in this illustration, I come out above 4 items, they are all the already known MDP states.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2019-07-07-rl-mesh-reward-part2-chg-in-state.png "chg-in-state")
>
>The point is that we can <font color="Red">mesh the reward function</font> by incorporating the <font color="Red">potential</font>(the <font color="Red">states of world</font>), when the robot is <font color="DeepPink">approaching</font> or <font color="RosyBrown">far away from</font> the ball, the return bonus gets <font color="DeepPink">increment</font> or <font color="RosyBrown">decrement(by negating previous increment)</font>.  When <font color="DeepPink">the ball is near the target</font>, the robot is encouraged by some <font color="DeepPink">positive incentive</font>, at the moment <font color="RosyBrown">the ball is away from the target</font>, the <font color="RosyBrown">previous returned bonus would be negated and lost</font>.  
>
>Above exhibition shows nothing different from already known MDP model.  It depends on how you design the learning system.  mjtsai think that <font color="Brown">we should also keep bonus in previous visited states, if we just lose everything learned in current state, at the moment transiting from current to next state, we could not reason for this transition</font>, therefore we should have an <font color="DeepSkyBlue">appropriate value</font> return as the reward <font color="DeepSkyBlue">when transiting from current to next state</font>, or such appropriate value might be figured out in accordance to <font color="DeepSkyBlue">the distance you are away from the ball and that momenmt which you start to speed up to hit the ball</font>.  

### <font color="Red">Potential</font>-Based Shapping: Illustration
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Something we already know</font>  
>We start from the $Q$ value function already know  
>$Q(S,A)$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q(S',A')$  
>
><font color="DeepSkyBlue">[2]</font>
><font color="Red">add the factor of potential in $R(S,A)$</font>  
>We take  
>$R'(S,A,S')$=$R(S,A)$-$\psi(S)$+$\gamma\cdot\psi(S')$  
>, and would like to integrate into the existing Q value function  
>, next would be the illustration of what the resulting $Q'(S,A)$ in terms of $Q(S,A)$ supposed to be.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="Red">The illustration</font>  
>&#10112;$Q(S,A)$  
>=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q(S',A')$  
>=$\sum_{S'}P(S'\vert S,A)\cdot R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q(S',A')$  
>=$\sum_{S'}P(S'\vert S,A)\cdot (R(S,A)$+$\gamma\cdot max_{A'}Q(S',A'))$  
>, where we departure from $S$ to $S'$, would definitely obtain $R(S,A)$, and <font color="DeepPink">the summation over all weighting averaged by the transition probability would finally leads to $1$</font>.  
>
>&#10113;$Q'(S,A)$  
>=$\sum_{S'}P(S'\vert S,A)\cdot (R(S,A,S')$+$\gamma\cdot max_{A'}Q(S',A'))$  
>=$\sum_{S'}P(S'\vert S,A)\cdot (R(S,A)$-$\psi(S)$+$\gamma\cdot\psi(S')$  
>$\;\;$+$\gamma\cdot max_{A'}Q'(S',A'))$  
>=$\sum_{S'}P(S'\vert S,A)\cdot (R(S,A)$-$\psi(S)$+$\gamma\cdot\psi(S')$  
>$\;\;$+$\gamma\cdot (R(S',A')$-$\psi(S')$+$\gamma\cdot\psi(S^{\'\'})$+$max_{A^{\'\'}}Q'(S^{\'\'},A^{\'\'})))$  

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