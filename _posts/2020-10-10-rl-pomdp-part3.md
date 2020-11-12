---
layout: post
title: Partial Observable Markov Decision Process - Part 3
---

## Prologue To Partial Observable Markov Decision Process - Part 3
<p class="message">
This post will begin with the difficulties in solving <font color="Red">POMDP</font>(Partial Observable Markov Decision Process), guide you througth the illustration of value iteration, and lead you to one of the canonical approach of the <font color="Red">PWLC</font>(piecewise linear convex).  
</p>

### <font color="Red">POMDP</font> Value Function
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Bellman equation for POMDP</font>  
>&#10112;$V^{\ast}(b)$=$max_{a}\\{\rho(b,a)$+$\gamma\cdot\int_{b^{\'}}P(b^{\'}\vert a,b)\cdot V^{\ast}(b^{\'})db^{\'}\\}$  
>, this expression is in rather intuition, where $\rho(b,a)$=$\sum_{s}R(s,a)\cdot b(s)$, and <font color="RoyalBlue">why</font> integrate over $b^{\'}$?  
>Because <font color="DeepSkyBlue">the continuous belief update in POMDP.</font>  
>
>&#10113;$V^{\ast}(b)$=$max_{a}\\{\rho(b,a)$+$\gamma\cdot\sum_{b^{\'}}P(b^{\'}\vert a,b)\cdot V^{\ast}(b^{\'})\\}$  
>, this is a more realistic format, where $P(b^{\'}\vert a,b)$=$\sum_{o}\sum_{s^{\'}}P(o\vert s^{\'},a)\cdot\sum_{s}P(s^{\'}|a,b)\cdot b(s)$  
>, which is the belief transition probability derived from POMDP transition/observation models.  
>
>Notes must be made that in my article, the uppercase letter stands for the variable, whereas the littlecase letter represents the value in it.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Solving POMDP by value iteration</font>  
>We take the value iteration in <font color="Red">POMDP</font> as:  
>&#10112;$V_{0}(b)$=$0$ to be initial value of belief $b$  
>&#10113;$V_{t}(b)$=$max_{a}\\{R(b,a)$+$\gamma\cdot\sum_{o}P(o\vert a,b)\cdot V_{t-1}(b^{\'})\\}$  
>, where $b^{\'}$=state estimated from $(a,b,o)$ at timestamp $t-1$.  
>
>It is the immediate reward plus the expected discounted value of where we end up, say $b^{\'}$ and make observation $o$.  
>
>$V_{t}(b)$ means that we have $t$ steps to go from $b$, and $V_{t-1}(b^{\'})$ indicates we have $t-1$ steps to go from $b^{\'}$, where $b$ has been belief updated to $b^{\'}$ by action $a$ and observation $o$.  
>
>The scary thing is the value function $V$, defined over <font color="RosyBrown">an infinite set of belief states</font>, $b$, if we make a loop for all belief states to do this update, &#10113;, it is just <font color="RosyBrown">an infinite number of belief states</font>, $b^{\'}s$, that would <font color="RosyBrown">not</font> terminated!!!  

### Difficulties In Solving <font color="Red">POMDP</font>
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Findings in the belief update of tiger example</font>
>A <font color="Red">POMDP</font> is a generalization of MDPs to situations that <font color="RosyBrown">world states are not fully observable</font>.  
>
>Recall in my last article [POMDP - Part 2]({{ site.github.repo }}{{ site.baseurl }}/2020/08/13/rl-pomdp-part2/), the tiger example, the full illustration of <font color="Red">belief updating</font> by listening, before the agent opens the correct door, it continues to listen until the resulting belief of probability distribution over world states is to be believed converged in each path of sequence of observations.  
>
>We have 2 findings:  
>&#10112;the agent has to keep track the history of belief update with respect to observation and action taken in each unique path, <font color="#C20000">we need memory in POMDP</font>.  
>&#10113;after each action, there is a new belief from prior belief.  <font color="#C20000">The belief update process is continuous</font>.  
>
><font color="DeepSkyBlue">[Difficulty 1]</font>
><font color="OrangeRed">Memory(POMDP) v.s. memoryless(DMP)</font>
>POMDP lacks important state information and must be compensated by memory.  
>
>The agent needs to learn <font color="OrangeRed">extraneous information</font> in observation to avoid/try, where such information should be maintained by a <font color="OrangeRed">memory-based model</font> of the world in order to predict what will happen accurately!!  
>
>If the agent has the complete full states, then it can choose optimal actions without memory.  
>
>Take two hallways for example, optimal policy might take right for the first, might take left for the first, a memoryless policy could not distinguish between them.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-2-hallways.png "2 hallways")
>
>You might ponder why not just use the optimal policy in each state to decide the action that leads to the maximum reward!!  Because in POMDP, to make observation after taking an action, <font color="DeepPink">we need further to know what state we are ranging from, to estimate such probabilistic observation, we need memory for these belief state information</font>.  
>
>If we'd like to get reward $R_{1}$, we might take left given that we are in $S_{1}$, then we need to remember that we are in $S_{1}$ already.  
>
><font color="DeepSkyBlue">[Difficulty 2]</font>
><font color="OrangeRed">Infinite belief states</font>
>In the belief update illustration of tiger example in [POMDP - Part 2]({{ site.github.repo }}{{ site.baseurl }}/2020/08/13/rl-pomdp-part2/), you can realize that new belief is generated from prior belief upon action taken, observation made, such process is in a continuous manner.  
>
>If we continue to listen in this simple tiger example, over and over, the set of belief states would definitely grow up in its size.  To be believe in other application with high complexity, it will be infinite, uncountable.  
>
>Then, we should <font color="Red">jump from infinity to finite</font>.  <font color="RosyBrown">Value iteration updates couldn't be carried out, because uncountable number of belief state</font>.  

### Policy Tree
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Brief description</font>  
>In general, an agent-step policy can be represented as a policy tree:  
>&#10112;search over sequences of actions with limited <font color="OrangeRed">look-ahead</font>  
>&#10113;branching over actions and observations  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-p-tree.png "policy tree")
>Suppose we begin from root node of certain action $A$, with probabilitistic distribution over observations $\\{O_{1},O_{2},...,O_{K}\\}$, and totally $H$ steps to go.  
>
>With 2 steps to go, it takes an action, make an observation, and make the final action.  
>
>With 1 step remaining, the agent must then just take an action and get the immediate reward.  
>
>In above tree, there are totally $\vert A\vert^{\frac {\vert O\vert^{H} - 1}{\vert O\vert - 1}}$ nodes.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Relate value function with policy tree</font>  
>* Value function of a policy tree  
>&#10112;if $P_{t}$ is 1-step policy tree, the value of executing that action in state $s$:  
>$V_{P_{t}}(s)$=$R(s,a(P_{t}))$, $t=1$  
>&#10113;if $P_{t}$ is t-steps policy tree, then  
>$V_{P_{t}}(s)$  
>=$R(s,A(P_{t}))$+$\gamma\cdot\\{Expected\;future\;value\\}$  
>=$R(s,A(P_{t}))$+$\gamma\cdot(\sum_{s^{\'}}P(s^{\'}\vert b,a)\cdot b(s)$  
>$\;\;\cdot(\sum_{o}P(o\vert s^{\'},a)\cdot V_{O(A(P_{t}))}(s^{\'})))$  
>, where we have next $b^{\'}$ probabilistically distributed over $s^{\'}$  
>, and $A(P_{t})$=$a$, the action taken in the root node  
>, with $\sum_{o}P(o\vert b,a)\cdot V(b^{\'})$=$\sum_{s^{\'}}P(s^{\'}\vert b,a)\cdot b(s)$  
>$\;\;\;\;\cdot(\sum_{o}P(o\vert s^{\'},a)\cdot V_{O(A(P_{t}))}(s^{\'}))$  
>
>* Value function over belief state  
>&#10112;we could think $V_{P_{t}}(b)$ as a vector associated with the policy tree of $t$-steps, where $dim(V_{P_{t}}(b))$=$n$, for $b$=$\\{s_{1},s_{2},...,s_{n}\\}$  
>&#10113;use the notation $\alpha_{P_{t}}$=$\left\langle V_{P_{t}}(s_{1}),V_{P_{t}}(s_{2}),...,V_{P_{t}}(s_{n})\right\rangle$  
>&#10114;treat value function of belief state $b$ with regard to the $t$-steps policy tree as $V_{P_{t}}(b)$=$\sum_{s}V_{P_{t}}(s)\cdot b(s)$  
>&#10115;we have $V_{P_{t}}(b)$=$b\cdot\alpha_{P_{t}}$...dot product  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Optimal $t$-steps policy</font>  
>To construct an optimal $t$-steps policy, we must maximize over all $t$-steps policy tree $P_{t}$:  
>$V_{t}^{\ast}(b)$=$max_{\alpha_{p}\in\alpha_{\tau}}\alpha_{p}\cdot b$, where $\alpha_{\tau}$ is a collection of $\alpha_{P_{t}}$  
>
>As $V_{P_{t}}(b)$ is linear in $b$ for each vector in $\alpha_{\tau}$, then $V_{t}^{\ast}(b)$ would be the <font color="DeepPink">upper surface</font> of these functions.  
>
>That is to say $V_{t}^{\ast}(b)$ is <font color="Red">piecewise linear and convex</font>.  

### Illustration Of <font color="Red">PWLC</font>(Piecewise Linear Convex)
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The preliminary</font>
>* The given scenario  
>Suppose we are given the world of 2 states, 2 actions and each action taken might lead to 3 possible observations in this environment of uncertainty.  
>
>* $V_{P_{t}(a_{i})}$  
>Let $V_{P_{t}(a_{i})}$ to be the value function induced by policy tree $P_{t}$, with $a_{i}$ the $i$-th action in the root node, and this value function is of the form:  
>$\;\;V_{P_{t}(a_{i})}(b)$=$b\cdot\alpha_{P_{t}}(a_{i})$  
>>It is a <font color="DeepSkyBlue">multi-linear function</font> of $b$, for <font color="DeepSkyBlue">each value function</font> could be shown as a <font color="DeepSkyBlue">line</font>, <font color="DeepSkyBlue">plan</font>, or <font color="DeepSkyBlue">hyperplan</font>, depends on <font color="OrangeRed">the number of states</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">$1$-step POMDP value function</font>
>For $1$-step policy tree, we just take one single action and get the <font color="#9300FF">immediate reward</font> to be the value function, such <font color="#9300FF">immediate reward</font> due to action execution is over $s_{0}$ and $s_{1}$, <font color="DeepSkyBlue">weighted by the initial belief distribution</font>, with respect to $a_{1}$ and $a_{2}$ each:  
>&#10112;$R(a_{1},b)$=$\\{R(s_{0},a_{1}),R(s_{1},a_{1})\\}$  
>&#10113;$R(a_{2},b)$=$\\{R(s_{0},a_{2}),R(s_{1},a_{2})\\}$  
>
>* The induction of $1$-step POMDP value function  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-1-step-vf.png "1-step vf")
>$V_{P_{t}(a_{i})}(b)$=$\sum_{s}R(s,a_{i})\cdot b(s)$, for $s\in\\{s_{0},s_{1}\\}$, given that $b_{0}\lbrack 0.5\;0.5\rbrack$, and <font color="#9300FF">immediate reward</font>s are initialized as shown, then  
>&#10112;$V_{P_{1}(a_{1})}(b)$  
>=$R(s_{0},a_{1})\cdot b(s_{0})$+$R(s_{1},a_{1})\cdot b(s_{1})$  
>=$1\cdot 0.5$+$0\cdot 0.5$  
>=$0.5$  
>&#10113;$V_{P_{1}(a_{2})}(b)$  
>=$R(s_{0},a_{2})\cdot b(s_{0})$+$R(s_{1},a_{2})\cdot b(s_{1})$  
>=$0\cdot 0.5$+$1.5\cdot 0.5$  
>=$0.75$  
>
>* The <font color="DeepSkyBlue">linearity</font>  
>Since $V_{P_{t}(a_{i})}(b)$ is linear in $b$, therefore we have  
>$\begin{bmatrix}R(s_{0},a_{1})&R(s_{1},a_{1})\\\\R(s_{0},a_{2})&R(s_{1},a_{2})\end{bmatrix}\begin{bmatrix}b(s_{0})\\\\b(s_{1})\end{bmatrix}=\begin{bmatrix}V_{P_1(a_1)}(b)\\\\V_{P_1(a_2)}(b)\end{bmatrix}$  
>$\Rightarrow\begin{bmatrix}1&0\\\\0&1.5\end{bmatrix}\begin{bmatrix}b(s_{0})\\\\b(s_{1})\end{bmatrix}=\begin{bmatrix}0.5\\\\0.75\end{bmatrix}$, just holds  
>The additive of $2$ linear lines leads to <font color="Red">PWLC</font> at $t$=1.  
>
>* Find out the <font color="OrangeRed">intersection point</font>   
>This turns to solve $V_{P_{1}(a_{1})}(b)$=$V_{P_{1}(a_{2})}(b)$,  
>$\Rightarrow R(s_{0},a_{1})\cdot b(s_{0})$+$R(s_{1},a_{1})\cdot b(s_{1})$  
>=$R(s_{0},a_{2})\cdot b(s_{0})$+$R(s_{1},a_{2})\cdot b(s_{1})$  
>$\Rightarrow 1\cdot b(s_{0})$+$0\cdot b(s_{1})$=$0\cdot b(s_{0})$+$1.5\cdot b(s_{1})$  
>After the deductio by $b(s_{0})$=$1-b(s_{1})$, we have $b(s_{0})$=0.6 and $b(s_{1})$=$0.4$  
>
>* Find out the <font color="Blue">optimal action</font>  
>&#10112;by maximizing over $1$-step policy tree $P_{1}$, we have <font color="#C20000">optimal action probabilistically distributed in proportion to the region partitioned at this intersection point</font>.  
>&#10113;this optimal $1$-step policy is determined <font color="DeepSkyBlue">by projecting the optimal value function back down to the belief space</font>.  
>&#10114;such projection yields a partition into regions, within each distinct region, there is a policy tree, say $P_{t}(a_{i})$, $t$=$1$ for horizon $1$, by taking action of $a_{i}$ leads us to the maximum of value function in this region.  
>&#10115;in this $1$-step policy tree, we have $a_{1}$ to be the optimal action in $\lbrack 0\;0.4\rbrack$ interval of belief space, and within $\lbrack 0.4\;1\rbrack$ interval, we have $a_{2}$ the optimal action in above exhibition.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-1-step-vf-partition.png "optimal actions")
>
>* <font color="RoyalBlue">Why do we have $s_{0}$ axis consisting of $R(s_{1},a_{i})$?</font>  
>$\because b(s_{1})$=$1-b(s_{0})$  
>$\therefore R(s_{1},a_{i})$ for $i=\\{1,2\\}$ in this example whould we have $s_{0}$ as the departuring point, extend the width with the portion to $1-b(s_{0})$, where the $s_{0}$ ranging in the opposite direction, heading toward $s_{1}$ axis.  Similarity could be found in axis of $s_{1}$.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">$2$-steps POMDP value function</font>  
>* The general format  
>&#10112;with 2 steps to go, we can take an action, make observation, then take next one left action base on the observation.  
>&#10113;the $2$-steps POMDP value function is obtained by adding the immediate reward of 1-st action taken, plus the value of taking next one left action, such expression is of the form:  
>$V_{P_{2}(a_{i})}(b)$  
>=$V_{2}(b)$...for simplicity  
>=$R(a_{i},b)$+$\gamma\cdot\\{expected\;future\;value\\}$  
>=$R(a_{i},b)$+$\gamma\cdot\sum_{o_{j}}P(o_{j}\vert b,a_{i})\cdot V_{1}(b^{\'})$  
>, where we have belief update from $b$ to $b^{\'}$ due to action $a_{i}$, observation $o_{j}$, and we write $V_{P_{2}(a_{i})}(b)$ as $V_{2}(a_{i},b)$ or $V_{2}(b)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-p-tree-2.png "2-step policy tree")  
>
>* <font color="Red">Value function transformation</font>  
>&#10112;the horizon $2$ value function is a function of next belief $b^{\'}$, since by taking action $a$, with certain observation, would this initial/prior belief $b$ be updated to $b^{\'}$.  As a result, that we have the horizon $2$ value function:  
>$V_{2}(b)$  
>=$max_{a}\\{R(a,b)$+$\gamma\cdot\sum_{o_{j}}P(o_{j}\vert b,a)\cdot V_{1}(b^{\'})\\}$  
>, where <font color="DeepPink">$P(o_{j}\vert b,a)\cdot V_{1}(b^{'})$ is the horizon $1$ value function transformation</font> denoted as $S(a,o_{j})$, <font color="DeepPink">each $o_{j}$ has its own transformed alpha vectors</font>.  
>&#10113;the transformed/next belief $b^{\'}$ is a function of the initial/prior belief $b$:  
>$b^{\'}(S^{\'})$  
>=$P(S^{\'}|A,O,b)$, we believe we are in state $S^{\'}$, given observation $O$  
>=$\frac {P(O|S^{\'},A,b)\cdot P(S^{\'}|A,b)}{P(O|A,b)}$
>
>* The induction of $2$-steps POMDP value function  
>&#10112;there are 2 actions in this example, we begin by extending from $a_{1}$ at $t$=$2$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-p-tree-2-vf-transform.png "vf transform")  
>&#10113;combine these linear lines together we get:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-p-tree-2-vf-transform-together.png "vf together")
>&#10114;by pruning and partioning we can get the optimal actions in each region:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-p-tree-2-vf-transform-partition.png "optimal actions")
>&#10115;we next extend from $a_{2}$ at $t$=$2$, suppose we get optimal action of region partitioned in below:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-p-tree-2-vf-transform-partition-a2.png "optimal actions")
>&#10116;put it all together, we could get the optimal actions as a whole image:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-10-10-rl-pomdp-part3-p-tree-2-vf-all.png "H2 optimal actions")
>

### Addendum
>&#10112;[Partial Observable Markov Decision Process, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4677668675/concepts/46822685970923)  
>&#10113;[POMDP Value Iteration Example, Tony, Brown University's Computer Science Department](http://cs.brown.edu/research/ai/pomdp/tutorial/pomdp-vi-example.html)  
>&#10114;[POMDP Tutorial, Stefan Kopp, Bielefeld University](https://www.techfak.uni-bielefeld.de/~skopp/Lehre/STdKI_SS10/POMDP_tutorial.pdf)  
>&#10115;[POMDPOs, Rowan McAllister and Alexandre Navarro, MLG Reading Group, 02 June 2016, Cambridge University](http://cbl.eng.cam.ac.uk/pub/Intranet/MLG/ReadingGroup/pomdp.pdf)  

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
<!-- \left\langle1,2,3\right\rangle => <1,2,3> -->
<!-- \because -->
<!-- \therefore -->

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