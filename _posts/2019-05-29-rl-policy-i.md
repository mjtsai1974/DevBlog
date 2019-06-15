---
layout: post
title: Policy Iteration
---

## Prologue To <font color="Red">Policy Iteration</font>
<p class="message">
Prior post reveals that <font color="Red">value iteration</font> eventually leads us to the <font color="DeepPink">optimal policy</font> providing the action for the current state to take to get its maximum value when transiting to next state.  
Departuring from <font color="OrangeRed">multiple states</font> in <font color="OrangeRed">one MDP model</font>, this article would guide you through <font color="Red">value iteration</font> to find the <font color="#00ADAD">greedy policy</font> in each state's transition, and finally get the <font color="DeepPink">optimal policy</font> for each state.  The whole process is called <font color="Red">policy iteration</font>.  
</p>

### <font color="Red">Policy Iteration</font> Versus <font color="Red">Value Iteration</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The beginning in MDP</font>  
>Suppoose we are departuring from a beginning state in <font color="OrangeRed">one MDP model</font>, each time we do make a decision to choose the best action that can transit us to next state with the maximum value(or reward), and we are doing this over and over again, until we believe that we have build the <font color="DeepPink">optimal policy</font> for each state, and it brings the whole MDP problem to a convergence.  
>
>This means that <font color="RosyBrown">we are not facing the problem to choose the action of uncertainty in one single state</font>, and the same state would then be re-visited, since we are repeating this over and over again.  
>
><font color="OrangeRed">There is no doubts that different or similar policies in one same state often interleave one over the others</font>, that's the <font color="Red">policy iteration</font> process.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The concept of policy iteration</font>  
>We have actually involved below 3 phases on the way to solve a MDP issue:  
>&#10112;initially, $\forall S, Q_{0}(S)=0$...[A]  
>&#10113;proceeds with <font color="OrangeRed">policy improvement</font>  
>$\forall S, \pi_{t}(S)$=$maxarg_{A}Q_{t}(S,A), t\geq 0$...[B]  
>&#10114;do the <font color="OrangeRed">policy evaluation</font> task  
>$\forall S, Q_{t+1}(S)$=$Q^{\pi_{t}}(S)$...[C]  
>
>We are starting by picking any <font color="OrangeRed">arbitrary</font> $Q$ function, denote it the initialization step, that's [A].  
>
>After that, we just iterate by taking the $t$-th, $Q_{t}$ function, computing its <font color="#00ADAD">greedy policy</font>, $\pi_{t}(S)$, that's [B], then use that <font color="#00ADAD">greedy policy</font> to get a new $Q$ function, say $Q_{t+1}$, that's [C].  
>
>And we are repeating and iterating this over and over again.  So each time we go around in this loop, we rae taking our <font color="OrangeRed">previous $Q$ function</font>, finding its <font color="#00ADAD">policy</font>, taking that <font color="#00ADAD">policy</font> to find its <font color="OrangeRed">next value function</font>, such repeating would actually get convergence in finite time.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Policy iteration is a better way</font>  
>The sequence of $Q$ functions we get convergence to $Q^{\ast}$ after we are experienced <font color="OrangeRed">a series of value iteration</font> in <font color="OrangeRed">finite time</font>, in particular, it illustrates how <font color="Red">policy iteration</font> works implicitely in my prior post.  
>
>The <font color="OrangeRed">convergence of policy iteration is at least as fast as value iteration</font> in that <font color="OrangeRed">if at any point we sync up the $Q$ functions, we start value iteration and policy iteration from the same $Q$ function</font>.  Then, <font color="DeepPink">each step this policy iteration takes is moving us towards the optimal $Q$ function, no more slowly than value iteration</font>.  
>
>So, <font color="OrangeRed">policy iteration is a better way</font>.
>
><font color="DeepSkyBlue">[4]</font>
><font color="Brown">Concerns pertaining to policy iteration::mjtsai1974</font>  
>One thing needs to be taken into consideration when we are doing the <font color="OrangeRed">policy improvement</font> task, that is <font color="OrangeRed">faster convergence would be at the cost of greater computational expense</font>.  
>
>In particular, when transiting from $S_{i}$ to $S_{i+1}$ in stage $t$, we'd like to make <font color="OrangeRed">policy evaluation</font>, $\forall S, Q_{t+1}(S)$=$Q^{\pi_{t}}(S)$, by taking the policy and working out $Q_{t+1}$ function to be used by $S_{i}$ as its value obtained, after transiting to $S_{i+1}$.  
>
>When in stage $t+1$, it does the <font color="OrangeRed">policy improvement</font> again, with the <font color="DeepSkyBlue">new updated(or even the same) policy</font> come out, then $Q_{t+2}$ function would laterly be generated out, this cycle repeats, untile it converges.  
>
>Yes, it is solving a system of linaer equations.  
>
>The scenario might be constructed <font color="OrangeRed">by putting value iteration inside the inner loop wrapper by the outside loop of policy iteration</font>, since <font color="OrangeRed">the value iteration operates in accordance to the policy</font>, exactly, <font color="OrangeRed">the action mapped from current state by current greedy policy at this moment</font>.  So, <font color="#C20000">the value iteration should be in the inner loop of policy iteration</font>.  
>
>Trivially, the <font color="Red">policy iteration</font> is doing much works than value iteration, if the greedy policy seldomly changes on its way to convergence, it <font color="OrangeRed">should be at least as fast as value iteration</font>.  

### Why Does <font color="Red">Policy Iteration</font> Works?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">What is the convergence time?</font>  
>&#10112;we know there exists some MDPs, <font color="DeepPink">the number of iterations the policy iteration takes is linear</font>, it is <font color="DeepPink">at lease as large as the number of states in the MDP</font>.  
>&#10113;the worse case is that <font color="RosyBrown">it can't be larger than the number of actions raised to the number of states</font>.  
>
>$\;\;l$inear $\vert S\vert\leq$ convergence time $\leq \vert A\vert^{\vert S \vert}$  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Domination</font>  
>&#10112;the <font color="OrangeRed">domination</font>:  
>$\pi_{1}\geq\pi_{2}$ iff $\forall s\in S, V^{\pi_{1}}(s)\geq V^{\pi_{2}}(s)$  
>&#10113;the <font color="OrangeRed">strict domination</font>:  
>$\pi_{1}>\pi_{2}$ iff $\forall s\in S, V^{\pi_{1}}(s)\geq V^{\pi_{2}}(s)$  
>there exists some $s\in S, V^{\pi_{1}}(s)> V^{\pi_{2}}(s)$  
>&#10114;$\pi$ is <font color="OrangeRed">$\varepsilon$ optimal</font> iff <font color="OrangeRed">$\vert V^{\pi}(s)-V^{\pi^{\ast}}(s)\vert\leq\varepsilon$</font>  
>
>Expand further that a policy is <font color="OrangeRed">$\varepsilon$ optimal</font> if the value function for that <font color="#00ADAD">(greedy) policy</font> is $\varepsilon$ close to the value function for the <font color="DeepPink">optimal policy</font> at <font color="Red">all</font> states.  It gives us a concept of <font color="DeepSkyBlue">bounding loss</font> or <font color="DeepSkyBlue">bounding regret</font>.  
>
>We can treat a policy to be <font color="OrangeRed">nearly optimal</font> if <font color="OrangeRed">per step loss in each state transition is very very small</font>.  
>
>From above we can tell that if policy 1 dominates policy 2, but, <font color="RosyBrown">not strictly</font> dominates it, then they <font color="RosyBrown">must have the same value everywhere</font>.  Since it would never be greater than or equal to, it's always equal to.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Bellman operator is monotonic</font>  
>We define 2 <font color="Red">Bellman operator</font> on 2 policies, they are $B_{1}$, $B_{2}$ on $\pi_{1}$, $\pi_{2}$:  
>&#10112;$\lbrack B_{1}V\rbrack$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,\pi_{1})\cdot V(S')$  
>&#10113;$\lbrack B_{2}V\rbrack$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,\pi_{2})\cdot V(S')$  
>
>So, if we use $B_{1}$ over value function, it just returns the immediate reward, plus the discounted expected value following $\pi_{1}$, the same idea for $B_{2}$, and it is using $\pi_{2}$.  
>
>We already know a bunch of things about such updates.  If we apply <font color="OrangeRed">the same Bellman operator</font> on <font color="OrangeRed">distinct value functions</font>, then they are <font color="RosyBrown">not</font> moving further apart, by a factor of at least gamma, unless these 2 value functions are the same.  
>
>If ther are already perfectly together, staying at the same fixed point, then they <font color="RosyBrown">won't</font> move any close together.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Policy iteration behaves itself</font>  
>$\;\;$ if $V_{1}\geq V_{2}$, then $B_{2}V_{1}\geq B_{2}V_{2}$.  
>
><font color="Brown">proof::mjtsai1974</font>  
>$\lbrack B_{2}V_{1}-B_{2}V_{2}\rbrack(S)$  
>=$\gamma\cdot\sum_{S'}P(S'\vert S, \pi_{2})\cdot (V_{1}(S')-V_{2}(S'))$  
>, where the term $(V_{1}(S')-V_{2}(S'))\geq 0$ by given.  
>
>Then, we take a convex combination of a bunch of non-negative values by summing them up, there is no way it would be negative.  
>
>We thus proved that $V_{1}$ dominates $V_{2}$ leads to $B_{2}V_{1}$ dominates $B_{2}V_{2}$.  
>
><font color="DeepSkyBlue">[5]</font>
><font color="Brown">Cautions::mjtsai1974</font>  
>The same Bellman operator with the same greedy policy, might <font color="RosyBrown">not</font> guarantee $S_{1}$ and $S_{2}$ could get closer after this transition.  
>
>Because <font color="RosyBrown">the same policy</font> working on <font color="RosyBrown">different states</font> might <font color="RosyBrown">not</font> come out with <font color="RosyBrown">the same action</font>, even <font color="RosyBrown">the same action might leads to different one step transition</font>.  
>
>In <font color="DeepSkyBlue">above proof, we are applying on the same state, but different value functions</font>.  

### <font color="Red">Value Improvement</font> In <font color="Red">Policy Iteration</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The background</font>  
>Suppose in the beginning, we are given <font color="Red">Bellman operator</font> $B_{1}$ applied on <font color="DeepSkyBlue">some</font> policy $\pi_{1}$ with respect to value function $Q_{1}$, such that <font color="DeepSkyBlue">$Q_{1}$=$B_{1}Q_{1}$</font> holds.  
>
>Still more, there exists another <font color="Red">Bellman operator</font> $B_{2}$ applied on a <font color="OrangeRed">greedy</font> policy $\pi_{2}$ with respect to value function $Q_{1}$, such that <font color="OrangeRed">$Q_{1}\leq B_{1}Q_{1}$</font> holds.  
>
>Above construction holds by <font color="Red">contraction property</font>.  We have this inequality:  
>$Q_{1}(S,A)$  
>=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S, \pi_{1}(S'))\cdot Q_{1}(S',\pi_{1}(S'))$  
>$\;\;\leq R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S, \pi_{2}(S'))\cdot Q_{1}(S',\pi_{2}(S'))$  
>
>Image we are beginning from state $S$ by using $B_{1}$ on $\pi_{1}$ to reach $Q_{1}$, as it is the <font color="OrangeRed">fixed point</font> of $B_{1}$, that is to say you start off with the policy, and you get the value function of that policy.  
>
>Then, we might back to the same state $S$, since we are repeating the value iteration over and over again, thus back to the original departuring point, under the case we are in the MDP model already known; or we are just evaluating over the sampling data, trying to complete the contour of this MDP model, eventhough, we still have the chance to re-visit the state we have ever arrived, say the initial state $S$.  
>
>This time, intuitively, we take $B_{2}$ following up $\pi_{2}$, this <font color="RosyBrown">greedy policy</font> would turn our value function $Q_{1}$ <font color="RosyBrown">no worse, possibly better</font>, that is $Q_{1}\leq B_{2}Q_{1}$.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The policy iteration moves in the right direction</font>  
>We have put all the things together to prove policy iteration moves in the right direction:  
>&#10112;the <font color="OrangeRed">Bellman operator monotonicity</font>  
>&#10113;the <font color="Red">value improvement</font> property  
>&#10114;the definition of $\pi_{1}$,$\pi_{2}$,$B_{1}$,$B_{2}$,$Q_{1}$,$Q_{2}$  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">The policy iteration in a summary</font>  
>&#10112;$B_{2}Q_{1}\geq Q_{1}$...<font color="Red">value improvement</font>  
>&#10113;$k\geq 0, B_{2}^{k+1}Q_{1}\geq B_{2}^{k}Q_{1}$...<font color="OrangeRed">monotonicity</font>  
>&#10114;$lim_{k\rightarrow\infty}B_{2}^{k}Q_{1}\geq Q_{1}$...<font color="OrangeRed">transitinity</font>  
>&#10115;$Q_{2}\geq Q_{1}$...<font color="OrangeRed">fixed point</font>  

### <font color="Red">Policy Iteration Won't Get Stuck In Local Optimal</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The important thing</font>  
>If there is any way to impriove, it will actually improve, <font color="Red">it won't get stuck in local optimal</font>.  This is really the very important thing.  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Value non deprovement or value improvement</font>  
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