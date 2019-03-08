---
layout: post
title: Bellman Operator Makes Convergence
---

## Prologue To The <font color="Red">Bellman Operator</font> Makes <font color="Red">Convergence</font>
<p class="message">
<font color="#C20000">By contiguous Bellman update, the value of each state eventually get converged, this happens a lot in reinforcement learning.</font>
</p>

### Begin By <font color="Red">Bellman Operator</font> - <font color="Red">B</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Beginning</font>  
>Let <font color="Red">B</font> be an operator, or mapping from value function to value function.  You give a <font color="Red">Q</font> function, the <font color="Red">Bellman operator</font> will give you back, possibly, a different <font color="Red">Q</font> function.  You can treat <font color="Red">B</font> a function from <font color="Red">Q</font> functions to <font color="Red">Q</font> functions.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Definition of Bellman operator</font>  
>$[BQ](S,A)$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q(S',A')$...definition  
>
>Give <font color="Red">B</font> a <font color="Red">Q</font> function, the new thing we get out when we apply <font color="Red">B</font> onto <font color="Red">Q</font>, has the property that at the state action pair $(S,A)$, it is equal to the <font color="#9300FF">immediate reward</font> plus the <font color="#D600D6">discounted expected value</font> of the <font color="OrangeRed">next state, $S'$</font>.  
>
>So, <font color="Red">Q</font> goes in, <font color="Red">BQ</font> goes out, treat <font color="Red">BQ</font> a <font color="DeepSkyBlue">new</font> function.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Another way of writing</font>  
>With <font color="Red">Bellman operator</font> - <font color="Red">B</font>, we can have below alternatives:  
>&#10112;$Q^{\ast}$=$BQ^{\ast}$ is another way of writing <font color="Red">Bellman equation</font>.  
>&#10113;$Q_{t}$=$BQ_{t-1}$ is another way of writing <font color="Red">value iteration</font>.  

### <font color="Red">Contraction Mapping</font>
>It happens a lot in reinforcement learning.  Take <font color="Red">B</font> to be an operator,  
>$\;\;$if for all $F$,$G$ and some $0\leq\gamma<1$, $\left\|\|BF-BG\right\|\|$,   
>$\;\;{\left\|BF-BG\right\|}_\infty\leg\gamma\cdot{\left\|F-G\right\|}_\infty$,  
>then <font color="Red">B</font> is <font color="Red">contraction mapping</font>, where  
>&#10112;$F$ and $G$ are value functions of <font color="Red">Q</font> form.  
>&#10113;${\left\|Q\right\|}_\infty$=$max_{S,A}\left|Q(S,A)\right|$, this notation sometimes called the infinity form, the max norm.  
>&#10114;${\left\|F-G\right\|}_\infty$ this means the biggest difference between $F$ and $G$.  

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
<!-- \left\|?\right\| => ||?||-->
<!-- \left|?\right| => |?|-->

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