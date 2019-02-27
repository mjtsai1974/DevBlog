---
layout: post
title: Temporal Difference In Q Form
---

## Prologue To The <font color="Red">Temporal Difference</font> In <font color="Red">Q</font> Form
<p class="message">
<font color="RosyBrown">Not</font> just learn the value, <font color="Red">TD</font>(<font color="Red">Temporal Difference</font>) rule with <font color="DeepSkyBlue">action control</font> in <font color="Red">Q</font> form would learn the <font color="DeepSkyBlue">values of different actions</font> we might take as a way to figure out the <font color="Red">most optimal</font>(<font color="Red">maximum valued</font>) behavior in each state.  
<font color="DeepPink">By given enough data, enough time, TD with action control would just do the right thing and eventually converge.</font>
</p>

### Glance At The <font color="Red">Q</font>-Learning
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Overview</font>  
>Here I am just to have a simplistic overview of <font color="Red">Q</font>-learning:  
>&#10112;<font color="Red">Q</font>-learning is a <font color="OrangeRed">value-based reinforcement learning algorithm</font>, which is used to find the most optimal(best) <font color="#00ADAD">policy</font> to choose <font color="OrangeRed">the action that can maximize the value of each state</font> by using a <font color="Red">Q</font> function.  
>&#10113;the <font color="Red">Q</font> function takes state and action as input parameters.  
>$Q^{\pi}(S_{t},A_{t})$=$E\lbrack R_{t+1}+\gamma\cdot R_{t+2}+\gamma^{2}\cdot R_{t+3}+...\vert S_{t},A_{t}\rbrack$  
>  
>The $\pi$ indicates the <font color="Red">$Q$</font> function asks for <font color="#00ADAD">policy</font> could be expressed in the form of <font color="#D600D6">expected discounted cumulative reward</font>, given $S_{t}$ and $A_{t}$.  
>&#10114;take action $A$ to transite from state $S$ to $S'$  
>$Q_{T}(S,A)$  
>=$Q_{T-1}(S,A)$+$\alpha_{T}\cdot(R(S,A)$+$\gamma\cdot max_{A'}Q_{T-1}(S',A')$-$Q_{T-1}(S,A))$...[A]  
>
>By repeating above <font color="Red">Bellman equation</font> in <font color="Red">Q</font> form, the <font color="Red">Q</font> value will finally get converged, usually denoted as <font color="#00ADAD">$Q^{*}(S,A)$</font>, and it's the <font color="#00ADAD">policy</font> for you to take action $A$ when you are in state $S$ to get the <font color="OrangeRed">maximum value</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Notes::mjtsai1974</font>  
>As to equation [A], it could be further expanded:  
>$Q_{T}(S,A)$  
>=$Q_{T-1}(S,A)$+$\alpha_{T}\cdot(R(S,A)$+$\gamma\cdot max_{A'}Q_{T-1}(S',A')$-$Q_{T-1}(S,A))$...[A]  
>=$Q_{T-1}(S,A)$+$\alpha_{T}\cdot(R(S,A)$+$\gamma\cdot (\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q_{T-1}(S',A'))$-$Q_{T-1}(S,A))$...[B]  
>
>Say it [B], where the term $(\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q_{T-1}(S',A'))$ in [B] could be treated as $max_{A'}Q_{T-1}(S',A')$ in [A].  
>
>&#10112;if we know the probability transition from $S$ to $S'$, its associated immediate reward, we can take advantage of [B].  
>&#10113;if we <font color="RosyBrown">neither</font> know probability distribution of state $S$, nor the immediate reward, we can just use [A], take <font color="OrangeRed">only</font> the <font color="Red">Q</font> value learned in last eposide.  
>
>See, the <font color="Red">Q</font> form is just expressed in terms of <font color="Red">temporal difference</font>.  
>
><font color="DeepPink">The Q form is quiet usefule in the reinforcement learning, when we are under the condition that we know nothing about the immediate reward and the probability distribution from current state to next state is uncertain, it is converinet to use this Q value as the experience.</font>  

### <font color="Red">Bellman Equation</font>: <font color="DeepSkyBlue">With</font> versus <font color="DeepSkyBlue">Without</font> Actions
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Without actions</font>  
>&#10112;<font color="RosyBrown">no action</font> in value function:  
>$V(S)$=$R(S)$+$\gamma\cdot\sum_{S'}P(S'\vert S, A)\cdot V(S')$  
>The value function $V(S)$ of state $S$ takes <font color="RosyBrown">no</font> action control into consideration, the term $P(S'\vert S, A)$ indicates the we are <font color="OrangeRed">in stochastic MDP model, the outcome of action execution is uncertain</font>.  
>&#10113;$TD(0)$ isomorphism:  
>$V_{T}(S_{t-1})$=$V_{T}(S_{t-1})$+$\alpha_{T}\cdot (r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1}))$  
>By using $TD(0)$ to update the value of $S_{t-1}$ when transiting from $S_{t-1}$ to $S_{t}$ in one eposide.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">With actions</font>  
>&#10112;the <font color="Red">Q</font> form value function:  
>$Q(S,A)$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S, A)\cdot max_{A'}Q(S',A')$  
>The value function now <font color="OrangeRed">takes</font> action into concern, after transiting from $S$ to $S'$, targeting at the action $A'$ chose by $S'$ to <font color="OrangeRed">maximize</font> value of $S'$, the term $Q(S',A')$.  
>&#10113;$TD(0)$ isomorphism:  
>$Q_{T}(S_{t-1},A_{t-1})$=$Q_{T-1}(S_{t-1},A_{t-1})$+$\alpha_{T}\cdot (r_{t}+\gamma\cdot max_{A_{t}}Q_{T-1}(S_{t},A_{t})-Q_{T-1}(S_{t-1},A_{t-1}))$  
>By using $TD(0)$ to update the value of $S_{t-1}$ in one eposide, be noted the term $max_{A_{t}}Q_{T-1}(S_{t},A_{t})$ aims at the action $A_{t}$ chose by $S_{t}$ that can <font color="OrangeRed">maximize</font> the value of $S_{t}$, the term $Q_{T-1}(S_{t},A_{t})$.  If such $A_t$ exists and can maximize $Q_{T}(S_{t},A_{t})$ across all eposide $T$, then it is just the <font color="#00ADAD">policy</font> to choose $A_{t}$.  

### Approximations
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">We know the whole MDP model</font>  
>If we know the whole MDP model, then, <font color="Red">synchronuous</font> update, simply by applying <font color="Red">Bellman equation</font>:  
>$Q_{T}(S,A)$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q_{T-1}(S',A')$  
>&#10112;as to the term $R(S,A)$, this is the <font color="#9300FF">immediate reward</font>, $A$ is just the best action taken by state $S$ to transite to $S'$.  <font color="OrangeRed">Because the whole MDP model is known, we know this $R(S,A)$.</font>  
>&#10113;the <font color="Red">synchronuous</font> update is by suming over all probabilistic transitions from $S$ to $S'$, given action $A$.  
>&#10114;we take the old $Q_{T-1}(S',A')$ value estimated in eposide $T-1$ and do the <font color="Red">Bellman update</font> in specific state, action pair or particular state connection pair.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">the whole MDP model is not clear, but $Q_{T-1}^{*}(S_{t-1},A_{t-1})$ is known</font>  
>If we know $Q_{T-1}^{*}(S_{t-1},A_{t-1})$,  
>we could use it to learn $Q_{T}^{*}(S_{t},A_{t})$ by sampling <font color="Red">asynchronuously</font> update.  
>
>$Q_{T}(S_{t-1},A_{t-1})$=$Q_{T-1}(S_{t-1},A_{t-1})$+$\alpha_{T}\cdot(r_{t}+\gamma\cdot max_{A_{t}}Q_{T-1}^{*}(S_{t},A_{t})-Q_{T-1}(S_{t-1},A_{t-1}))$  
>Where we can take $Q^{*}(S_{t-1},A_{t-1})$=$Q_{T}(S_{t-1},A_{t-1})$.  

<!--
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Without actions</font>  
-->

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