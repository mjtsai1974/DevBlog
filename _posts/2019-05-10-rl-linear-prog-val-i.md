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
>Here we ponder if the solution $7$ to this set of <font color="OrangeRed">inequality constraints</font> is exactly the max?  The answer is <font color="RosyBrown">no</font>, and why?  Because $9$, $10$, these numbers are also greater than or equal to all of these things(<font color="OrangeRed">the set of constraints</font>).  
>
>What we want is <font color="DeepSkyBlue">to pick up the smallest one</font> within those number greater than and equal to above set of inequalities, in this example, you can't get any number that is smaller than $7$, thta is $min X$=$7$.  
>
>Is <font color="DeepPink">$min X$</font> a linear operator?  No, it is just a <font color="DeepPink">linear objective function</font>!!!  Next, we are going to use this idea to generalize a <font color="DeepPink">linear objective function</font> of the <font color="Red">Bellman equation</font> in a very similar way.  

### The <font color="Red">Linear Programming</font>: <font color="Red">Primal</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Refine the Bellman equation</font>  
>Succeeding to above idea that we'd like to pick up the smallest one from within all possible value functions of maximum, we should refine our <font color="Red">Bellman equation</font> in [A] as below:  
>$\forall S,A\;V(S)\geq R(S,A)+\gamma\sum_{S'}P(S'\vert S,A)\cdot V(S')$...[B]  
>&#10112;for all states and actions, the value of a state is greater than or equal to the right part of the original expression, and we say the new expression of inequality [B].  
>&#10113;the whole right part of [B] is just the <font color="Red">Q</font>-value.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">What and how do we minimize here?</font>  
>Caution must be made that <font color="DeepSkyBlue">we are given a set of sampling data of a MDP model</font>:  
>&#10112;since inequality [B] is refined for all states and actions, <font color="RosyBrown">what we want to minimize is not a single state</font>.  
>&#10113;inequality [B] aims at all states, what we should minimize is a <font color="OrangeRed">vector</font>.  
>&#10114;<font color="OrangeRed">a single $V(S)$ is unbounded</font>, we should <font color="OrangeRed">as a whole</font> evaluate <font color="OrangeRed">all states</font> in one minimize operation.  
>
>Due to above concerns in &#10112;,&#10113;,&#10114;, it turns out <font color="DeepPink">to minimize the sum of all states</font> to make it work:  
>$min\;\sum_{S}V(S)$...[C]  
>
>So, <font color="OrangeRed">$min\;\sum_{S}V(S)$</font> is going to operate on all the individual $V(S)$ and make each of them to be <font color="OrangeRed">as small as they can be</font>, so that <font color="OrangeRed">it actually equals the $max\;V(S)$ for all $S$</font>.  
>
>Besides, <font color="RosyBrown">$min\;\sum_{S}V(S)$ isn't an upper bound on the max</font>, if any distinct $V(S)$ is an upper bound, then you <font color="RosyBrown">won't</font> have the minimum sum.  You can always move it down a little bit.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="Red">The primal</font>  
>This is atually a linear program by putting [B] and [C] together, some textbook name it the <font color="Red">primal</font>:  
>$\;\;\forall S,A\;V(S)\geq R(S,A)+\gamma\sum_{S'}P(S'\vert S,A)\cdot V(S')$  
>$\;\;\;\;min\;\sum_{S}V(S)$  
>
>You can regard <font color="OrangeRed">[C]</font> as the <font color="OrangeRed">linear objective function</font>.  To be believed that <font color="DeepSkyBlue">it is the solution equivalent to the solution to the MDP</font>.  We can just write down this linear program and give it to a linear program <font color="Red">solver</font> that runs in <font color="Red">polynomial time</font> and finally gets $V(S)$ for all state $S$.  
>
>How do we get our policy from that?  We just <font color="#00ADAD">choose the action that always returns the best(maximum) value</font>, choose this <font color="#00ADAD">greedy policy</font> with respect to that optimal value function, and we are doing it <font color="OrangeRed">in the unit of each distinct state</font>.  

### <font color="Red">Linear Programming Duality</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">A mechanical process</font>  
>One more thing about <font color="Red">linear programming</font> is by switching from the <font color="Red">primal</font> to what's called the <font color="Red">dual</font>.  It has such nice property that by:  
>&#10112;<font color="OrangeRed">changing constraints into variables</font>  
>&#10113;<font color="OrangeRed">changing variables into constraints</font>  
>
>You can get a <font color="OrangeRed">new</font> linear programming that is equivalent to the original old one, this is called the <font color="Red">linear programming duality</font>.  Sometimes, it would be useful to solve a MDP by putting bounds and constraints on the solutions.  
>
>We treat <font color="DeepPink">the process of producing the dual of linear programming</font> to be just <font color="DeepPink">a mechanical process</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="Red">The dual</font>  
>$max_{q_{S,A}}\sum_{S}\sum_{A}q_{S,A}\cdot R(S,A)$...[D]  
>$\;\;$such that $1$+$\gamma\cdot\sum_{S}\sum_{A}q_{S,A}\cdot P(S'\vert S,A)$=$\sum_{A'}q_{S',A'}$...[E]  
>$\;\;\;\forall S,A\;q_{S,A}\geq 0$...[F]  
>
>&#10112;[D] is the <font color="Red">linear objective function</font>.  
>&#10113;[E] and [F] are the <font color="OrangeRed">constraints</font>.  
>
>We perform a series of steps to turn <font color="OrangeRed">each constraint from the primal becomes variable in the dual</font>, <font color="OrangeRed">each variable in the primal becomes constraint in the dual</font>, and <font color="OrangeRed">maximum becomes minimum</font>, <font color="OrangeRed">bound becomes objective function</font>.  
>
>In more detail, <font color="OrangeRed">the $V(S)$ and $R(S,A)$ term in [B], the constraint of primal, has been turned into the variables in the linear objective function expressed by [D] in dual</font>, with <font color="OrangeRed">$V(S)$ be replaced with $q_{S,A}$</font>, which is the next new introduced concept, the <font color="OrangeRed">aganet flow</font>.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">New introduced policy flow</font>  
>In this <font color="Red">dual</font>, the <font color="OrangeRed">optimization is to maximize the sum over all state-action pairs of the reward</font> for that <font color="OrangeRed">state-action pair</font> times <font color="OrangeRed">the value of $q_{S,A}$</font>, which is the new introduced <font color="OrangeRed">policy flow</font>; it's <font color="RosyBrown">not</font> the same <font color="Red">Q</font>-value.  
>
>The <font color="OrangeRed">policy flow, $q_{S,A}$</font> could be regarded as <font color="OrangeRed">how much agentness is flowing through each state-action pair</font>.  If it follows the <font color="#00ADAD">policy</font>, it is going to spend some time running in that environment of MDP, passing through <font color="Red">each</font> state-action pair.  When it is transiting from <font color="#D600D6">current</font> state-action pair to its <font color="#D600D6">next</font> state-action pair, it is <font color="#D600D6">discounted by $\gamma$</font>.  
>
>Here is the <font color="OrangeRed">concept</font> that each time the <font color="OrangeRed">policy flow</font> passes through a state-action pair, we're going to get the reward associated with that state-action pair.  What we'd like to do is <font color="OrangeRed">to maximize the reward according to this concept by means of $max_{q_{S,A}}\sum_{S}\sum_{A}q_{S,A}\cdot R(S,A)$</font>.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Min in primal vs max in dual</font>  
>It's more intuitive for <font color="OrangeRed">we do the maximizing job in the dual</font>, comparing with <font color="DeepSkyBlue">the minimum we do in the primal</font>.  What we <font color="RosyBrown">don't</font> want is <font color="RosyBrown">to have an upper bound in the primal</font>, that's why we choose to minimize the sum of all states' value.  
>
>We choose $max_{q_{S,A}}\sum_{S}\sum_{A}q_{S,A}\cdot R(S,A)$, [C] <font color="OrangeRed">in the dual to maximize our reward each time the agent flow passing through each state-action pair</font>, <font color="Red">how to guarantee that we won't have an upper bound of each or some state-action pair?</font>  This is a good question.  
>
>It's going to be subject to the following idea, or just the constraint.  
>
><font color="DeepSkyBlue">[5]</font>
><font color="OrangeRed">$1$+$\gamma\cdot\sum_{S}\sum_{A}q_{S,A}\cdot P(S'\vert S,A)$=$\sum_{A'}q_{S',A'}, \forall A'$</font>  
>The answer is that we are constrainting this maximum to [D], that's a constraint, and for each state, in this case, would be better if we think oif them as <font color="OrangeRed">next state</font>.  
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