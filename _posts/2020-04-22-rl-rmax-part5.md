---
layout: post
title: Model-Based RL Algorithm RMAX - Part 5
---

## Prologue To Model-Based RL Algorithm <font color="Red">RMAX</font> - Part 5
<p class="message">
This article reviews <font color="Red">RMAX</font> in summary of illustration.
</p>

### Two Main Reinforcement Learning Approaches: Recap
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Model-free approachs</font>  
>They don't learn a model, <font color="DeepPink">model-free approachs learn value function or policy function directly</font>, that is to say they directly estimate state-action value function.  
>* Q learning  
>$Q_{T+1}(S,A)$=$R_{T}(S,A,S^{\'})$+$\gamma\cdot max_{A^{\'}}Q_{T}(S^{\'},A^{\'})$  
>$\Rightarrow Q_{T+1}^{\ast}(S,A)$=$(1-\alpha)\cdot Q_{T}(S,A)$+$\alpha\cdot Q_{T+1}(S,A)$  
>
>* Temporal difference in value function form(<font color="OrangeRed">without action</font>)  
><font color="DeepSkyBlue">[The rule]</font>
>Eposide $T$:  
>$\;\;$For all $S$, $e(S)$=$0$ at start of eposide, $V_{T}(S)$=$V_{T-1}(S)$  
>$\;\;$After $S_{t-1}\xrightarrow{r_{t}}S_{t}$:(from step $t-1$ to $t$ with <font color="#9300FF">reward</font> $r_{t}$)  
>$\;\;\;e(S_{t-1})$=$e(S_{t-1})$+$1$:  
>$\;\;\;\;$Update <font color="DeepSkyBlue">eligibility</font> of $S_{t-1}$ after arriving to $S_{t}$  
>$\;\;$For all $S$,  
>$\;\;V_{T}(S)$=$V_{T-1}(S)$+$\alpha_{T}\cdot(r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1}))$  
>$\;\;\;e(S_{t-1})$=$\lambda\cdot\gamma\cdot e(S_{t-1})$:  
>$\;\;\;\;$<font color="Red">before</font> transite from $S_{t-1}$ to $S_{t}$ in <font color="Red">next</font> iteration  
>
>* Temporal difference in Q form(<font color="DeepSkyBlue">with action</font>)  
>&#10112;the <font color="Red">Q</font> function takes state and action as input parameters.  
>$Q^{\pi}(S_{t},A_{t})$=$E\lbrack R_{t+1}+\gamma\cdot R_{t+2}+\gamma^{2}\cdot R_{t+3}+...\vert S_{t},A_{t}\rbrack$  
>&#10114;take action $A$ to transite from state $S$ to $S'$  
>$Q_{T}(S,A)$  
>=$Q_{T-1}(S,A)$+$\alpha_{T}\cdot(R(S,A)$+$\gamma\cdot max_{A'}Q_{T-1}(S',A')$-$Q_{T-1}(S,A))$  
>By repeating above <font color="Red">Bellman equation</font> in <font color="Red">Q</font> form, the <font color="Red">Q</font> value will finally get converged, usually denoted as <font color="#00ADAD">$Q^{*}(S,A)$</font>, and it's the <font color="#00ADAD">policy</font> for you to take action $A$ when you are in state $S$ to get the <font color="OrangeRed">maximum value</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Model-base approachs</font>  
>Given sample of data seen so far:  
>&#10112;build the explicit model of MDP and compute policy for it in the beginning.  
>&#10113;explore the environment in the given data, <font color="OrangeRed">learn the transitive probability</font> $P(S,A,S^{\'})$ and <font color="OrangeRed">reward function</font> $R(S,A)$ in accordance to state-action pair.  
>&#10114;repeat until the transitive probability $P(S,A,S^{\'})$ and reward function $R(S,A)$ is to be believed converged to an acceptable confidence interval, during the convergence period, recompute the policy for that state <font color="OrangeRed">once the transitive probability and reward function has been updated</font>.  
>
>One of such approaches is the <font color="Red">RMAX</font> algorithm.  

### <font color="Red">RMAX</font> Algorithm Summary
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Proceed with explore or exploit</font>  
>By the given sample of data, this algorithm proceeds with explore to some unknown states or exploit over the same state, and <font color="RosyBrown">you will never know you are exploring or exploting</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Implicit explore or exploit lemma</font>  
>After every $T$ steps, you either:  
>&#10112;achieves or attains the near optimal reward for these $T$ steps.  
>&#10113;explore to certain unknown state in high probability, learns a little about an unknown state.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">The RMAX algorithm</font>  
>* Initialization  
>&#10112;add the state $S_{0}$ to the MDP model  
>&#10113;set <font color="OrangeRed">$P(S_{0},A,S)$=$1$</font> for all state $S$  
>&#10114;set <font color="OrangeRed">$R(S,A)$=$R_{max}$</font> for all state $S$ and action $A$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-04-22-rl-rmax-part5-init-1.png "Rmax")
>&#10115;set all states to unknown states, excepts for $S_{0}$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-04-22-rl-rmax-part5-init-0.png "unknown")
>&#10116;set all <font color="DeepSkyBlue">visited counter</font> of state-action pairs to $0$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-04-22-rl-rmax-part5-init-2.png "visited count")
>
>* Repeat  
>&#10112;compute a $T$-step policy for current state $S$ and execute it  
>&#10113;for any visited state-action pair, keep track of its count and reward with respect to state transition from $S$ to $S^{\'}$  
>&#10114;if the same state-action pair has been visited over enough times to estimate $P(S,A,S^{\'})$ and $R(S,A)$, <font color="OrangeRed">update the transitive probability</font>, <font color="OrangeRed">turn the state-action pair from unknown to know</font>, and repeat from &#10112;  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-04-22-rl-rmax-part5-init-3.png "known")
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-04-22-rl-rmax-part5-init-4.png "trans prob")
>&#10115;loops through &#10112;,&#10113;,&#10115; until all states has become known  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">How many times are enough?</font>  
>* By [Chernoff Bounds For Bernoulli Random Variable]({{ site.baseurl }}/2019/12/09/prob-bound-chernoff-bound-bernoulli/)  
>We have $P(\sum_{i=1}^{n}Z_{i}>a)<e^{-\frac {a^{2}}{2\cdot n}}$, where $Z_{1}$,$Z_{2}$,...,$Z_{n}$ are the $n$ distinct independent trials on state $G_{i}$, and $a$ is the error term, such inequality bounds the error probability by $e^{-\frac {a^{2}}{2\cdot n}}$ that after $n$ independent trials on state $G_{i}$, the total estimate bias is greater than the error term $a$.  
>
><font color="DeepSkyBlue">[5]</font>
><font color="OrangeRed">Put it all together</font>  
>With probability at least $1-\delta$, the <font color="Red">RMAX</font> algorithm will reach $\varepsilon$ close to optimal policy, in time polinomial in the number of states, the number of actions, $\frac {1}{\delta}$, $\frac {1}{\varepsilon}$.  
>
>* Every $T$ steps  
>By implicit explore or exploit lemma:  
>&#10112;achieve <font color="DeepSkyBlue">near</font> optimal reward, or  
>&#10113;explore to certain unknown state with high probability. Since the number of states and actions are finite, it wouldn't take too long before all states turn into known!  

### Addendum
>&#10112;[R-max: A General Polynomial Time Algorithm for Near-Optimal Reinforcement Learning, Ronen I. Brafman, CS in Ben-Gurion University, Moshe Tennenholtz, CS in Stanford University](http://www.jmlr.org/papers/volume3/brafman02a/brafman02a.pdf)  
>&#10113;[Reinforcement Learning: Machine Learning - CSE446, Carlos Guestrin, University of Washington, June 5, 2013](https://courses.cs.washington.edu/courses/cse446/13sp/slides/mdps-rl.pdf)  

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