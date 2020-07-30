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

### <font color="Red">Belief State</font> In POMDP
>Below exhibits the POMDP model, wherein the probability distribution is over the world states with <font color="Red">true state is only partially observable</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-07-21-rl-pomdp-part1-model.png "POMDP")
>
>&#10112;the agent keeps/maintains an internal <font color="Red">belief state</font>, say <font color="Red">$b$</font>, that summarizes its experience.  
>&#10113;the agent makes state estimation to update from <font color="Red">belief state</font> $b$ to next <font color="Red">belief state</font> $b^{\'}$, based on the last action it has taken, the current <font color="OrangeRed">observation</font> it has made, and the previous <font color="Red">belief state</font> $b$.  

### <font color="RoyalBlue">[Question]Why Belief State in POMDP?</font>
><font color="DeepSkyBlue">[Answer]</font>  
>&#10112;the state of the real world is only <font color="Red">partially observable</font>.  
>&#10113;the agent needs to learn how the observations might aid its performance.  
>&#10114;there might exists <font color="RosyBrown">no immediate observation</font> pertaining to the desired state.  
>$\Rightarrow$This rerveals that <font color="DeepPink">the states are probabilistically distributed over the given observations at any time, such probability distribution varies over time</font>, that's why we have belief state from initial $b$ to $b^{\'}$, or say from $b_{0}$ to $b_{1}$, $b_{2}$,...,$b_{i}$, $b_{i+1}$,...,$b_{\infty}$.  
>
>&#10115;the whole POMDP is illustrated/iterated in <font color="Red">the environment of uncertainty</font>.  
>&#10116;<font color="Red">uncertainty</font> about action outcome, about the world state due to <font color="OrangeRed">imperfect</font>(<font color="OrangeRed">partial</font>) information.  

### POMDP Parameters
>&#10112;initial belief:  
>$b(S)$=$P(S)$, this means the probability for we are in state $S$.  
>&#10113;belief state updating:  
>$b^{\'}(S^{\'})$=$P(S^{\'}|O,A,b)$, this represents the probability for we are in state $S^{\'}$, given that we take action $A$, make observation $O$, from previous <font color="Red">belief state distribution</font>, say $b$.  
>&#10114;observation function:  
>$O(S^{\'},A,O)$=$P(O|S^{\'},A)$, it represents the probability for we make observation $O$, given that we are transiting to state $S^{\'}$, by taking action $A$.  
>&#10115;transitive probability:  
>$T(S,A,S^{\'})$=$P(S^{\'}|S,A)$, it represents the probability for we transit from $S$ to $S^{\'}$, by taking action $A$.  
>&#10116;rewards:  
>$R(A,b)$=$\sum_{S}R(S,A)\cdot b(S)$, where $R(S,A)$ is the same as it is in MDP, and the reward is summing over the reward by taking action $A$ with proportion to the probabilistic distribution for each state $S$ in $b$.  

### Understand The Belief State <font color="Red">$b$</font>
>Suppose we are given $n$ underlying states, a <font color="OrangeRed">discrete state space of size $n$</font>, then <font color="DeepPink">the belief state $b$ is a vector of $n$ states</font>.  
>
>Partial observable turns discrete problem of $n$ states into continuous problem, a POMDP with $n$ states induces an $n$-dimensional <font color="Red">belief-MDP</font>.  
>
>* <font color="RoyalBlue">Why?</font>  
><font color="DeepSkyBlue">[Answer]</font>  
>The true state is only partial observable, where $b(S)$=probability of being in state $S$.  
>At each step, the agent:  
>&#10112;takes some action, say $A$  
>&#10113;transites to next state $S^{\'}$ form state $S$  
>&#10114;makes observation $O$, with probability $P(O|S^{\'},A)$  
>&#10115;suppose we are given initial belief state $b$, after &#10112;,&#10113;,&#10114;, the probabilistic distribution over the belief state would definitely be changed.  
>
>* The <font color="Red">posterior belief</font>  
>That's why we need to make belief update, say the <font color="Red">posterior belief</font>:  
>$b^{\'}(S)$=$\alpha\cdot P(O|S^{\'},A)\cdot\sum_{S}P(S^{\'}|S,A)\cdot b(S)$  
>, where $\alpha$ is certain coefficient, such <font color="DeepPink">belief update is continuous rather than discrete!!!</font>  
>
>* <font color="Red">Continuous belief update</font>  
>POMDP could be regarded as continuous belief update over underlying MDP states, as the agent's belief is encoded through a continuous belief state.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-07-21-rl-pomdp-part1-conti-upd.png "conti belief upd")
>Each MDP state is a probability distribution(<font color="Red">continuous belief state</font>) over the state of the original POMDP.  

<!-- State transitions are products of actions and observations. -->

### POMDP: <font color="Red">Belief Update</font>
>$b^{\'}(S^{\'})$  
>=$P(S^{\'}|A,O,b)$, we believe we are in state $S^{\'}$, given observation $O$  
>=$P(O|S^{\'},A,b)\cdot\frac {P(S^{\'}|A,b)}{P(O|A,b)}$  
>
><font color="Brown">mjtsai think we can treat $b'$ as $P(S'|O)$ in viewpoint of Bayer theorem.</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-07-21-rl-pomdp-part1-belief-upd.png "belief update")
>
>* $P(O|S^{\'},A,b)$  
>&#10112;it is the probability that we make observation $O$, given that we are in state $S^{\'}$, by taking action $A$, probabilistically distributed over belief state $b$(or say from previous belief state $b$).  
>&#10113;therefore, we can treat $P(O|S^{\'},A,b)$=$P(O|S^{\'})$  
>
>* $P(S^{\'}|A,b)$  
>This stands for the probability that we are in $S^{\'}$, given action $A$ has been taken, from belief state $b$  
>, where $P(S^{\'}|A,b)$=$\sum_{S}P(S^{\'}|A,S)\cdot b(S)$ and this $b$ is to be believed a vector of states, a vector of state space.  
>
>* $P(O|A,b)$  
>This indicates we make observation $O$, given that we has taken action $A$, from belief state $b$  
>, this is a normalization factor, where  
>$P(O|A,b)$  
>=$\sum_{S^{\'}P(O|S^{\'})}\cdot P(S^{\'}|A,b)$  
>=$\sum_{S^{\'}P(O|S^{\'})}\cdot\sum_{S}P(S^{\'}|A,S)\cdot b(S)$  
>
><font color="Brown">Notes::mjtsai1974</font>  
>This expression is asking for the probability of the fact that we are in state $S^{\'}$, given that we make observation $O$, by taking action $A$, from somewhat belief state $b$.  
>
>It could be further expanded as the qualitative probability that we make observation $O$, given that we are in state $S^{\'}$, by taking action $A$, from belief state $b$.  Such likeli in turn multiplied by the probabilty, which is a prior that we are in $S^{\'}$, by taking action $A$, from belief state $b$.  Finally, over the total/marginal probability probability that we make observation $O$, given that we take action $A$, from somewhat belief state $b$.  

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