---
layout: post
title: Linear Programming In Value Iteration
---

## Prologue To Linear Programming In <font color="Red">Value Iteration</font>
<p class="message">
Prior post reveals that <font color="Red">value iteration</font> <font color="RosyBrown">doesn't</font> give us a <font color="OrangeRed">polynomial time</font> algorithm for solving MDPs.  The <font color="Red">linear programming</font> is the current only way to solve MDPs in <font color="OrangeRed">polynomial time</font>.
</p>

### $\frac {1}{1-\gamma}$ <font color="RosyBrown">Isn't Polynomial</font> $\approx$ <font color="RosyBrown">Isn't Proportional</font>
>The <font color="Red">value iteration</font> identifies an <font color="#00ADAD">optimal policy</font> and <font color="OrangeRed">polinomial time</font> in $\frac {1}{1-\gamma}$, where $\lim_{\gamma\rightarrow 1}\frac {1}{1-\gamma}$=$\infty$, just explodes.  That's why we need the <font color="Red">linear programming</font> to solve MDPs in a reasonable amount of time.  

### What's <font color="Red">Linear Programming</font>?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Encode MDP solution as a linear program</font>  
>In my prior post [Lagrange Multiplier]({{ site.github.repo }}{{ site.baseurl }}/2017/10/27/prereq-lagrange-multiplier/), you can find some similarity.  In this post, we'd like to dive into deep level to solve MDPs by means of <font color="Red">linear programming</font>:  
>&#10112;it's an <font color="DeepSkyBlue">optimization framework</font>, in which <font color="DeepSkyBlue">you can give linear constraint in a linear objective function</font>.  
>&#10113;as long as <font color="OrangeRed">the number of variables and costraints</font> are <font color="OrangeRed">polynomial</font>, we can <font color="OrangeRed">get a solution</font> in <font color="OrangeRed">polynomial time</font>.  
>&#10114;we need to <font color="OrangeRed">encode MDP solution as a linear program, we thus can have linear constraint(s) and a linear objective function</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">How to solve a MDP?</font>  
>For the time being, in this series of <font color="Red">RL</font> posts, we just need to solve the <font color="Red">Bellman equation</font>:  
>$\forall S, V(S)$=$max_{A}(R(S,A)+\gamma\sum_{S'}P(S'\vert S,A)\cdot V(S'))$...[A]  
>&#10112;for each state $S$, we have a variable $V(S)$ and relate each distinct $V(S)$ to its next $V(S')$.  
>&#10113;we thus have &#10112; to be a set of <font color="OrangeRed">constraints</font>.  If we could solve this set of constraints, it is suggested to be a good departure point.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Do we have a way to solve [A]?</font>  
>Unless<font color="DeepPink">the $max_{A}$ has become linear</font>, the answer is <font color="RosyBrown">no</font>.  
>
>The <font color="OrangeRed">max over action</font> is <font color="RosyBrown">not</font> linear, it <font color="RosyBrown">isn't</font> translatable directly to a set of linear equations and a linear objective function.  In the very beginning, we are given a set of non-linear equations.  
>
>We should express the <font color="OrangeRed">max over action</font> in terms of <font color="OrangeRed">a set of linear constraints</font> and <font color="OrangeRed">a linear objective function</font>.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Example of $max(-3,7,2,5)=X$</font>  
>Given this example of max, below is <font color="OrangeRed">a set of inequality constraints</font>:  
>&#10112;$X\geq -3$  
>&#10113;$X\geq 7$  
>&#10114;$X\geq 2$  
>&#10115;$X\geq 5$  
>
>Here is the question that the solution $7$ to this set of <font color="OrangeRed">inequality constraints</font>?  The answer is <font color="RosyBrown">no</font>, and why?  Because $9$, $10$, these numbers are also greater than or equal to all of these things(<font color="OrangeRed">the set of constraints</font>).  
>

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