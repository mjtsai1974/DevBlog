---
layout: post
title: Model-Based RL Algorithm RMAX - Part 4
---

## Prologue To Model-Based RL Algorithm <font color="Red">RMAX</font> - Part 4
<p class="message">
The <font color="Red">RMAX</font> theorem guarantees that the learning efficiency is polynomial and would be proved in this article.
</p>

### The <font color="Red">RMAX</font> Theorem
><font color="Brown">[Theorem of optimality and convergence]</font>  
>Given below condition:  
>&#10112;let $M$ be the <font color="OrangeRed">stochastic game</font> with $N$ states and $k$ actions.  
>&#10113;let $0 < \delta < 1$ and $\varepsilon > 0$ be constants, where <font color="OrangeRed">$\delta$</font> is the <font color="OrangeRed">error probability</font> and <font color="OrangeRed">$\varepsilon$</font> is the <font color="OrangeRed">error term</font>.  
>&#10114;denote the policy for $M$ whose <font color="OrangeRed">$\varepsilon$-return mixing time</font> is $T$ by $\prod_{M}(\varepsilon,T)$.  
>&#10115;denote the <font color="#00ADAD">optimal</font> expected return by such policy by $Opt(\prod_{M}(\varepsilon,T))$.  
>
>Then, <font color="DeepPink">with probability of no less than $1-\delta$ the <font color="Red">RMAX</font> algorithm will attain an expected return of $Opt(\prod_{M}(\varepsilon,T))-2\cdot\varepsilon$, within a number of steps polynomial in $N$,$k$,$T$,$\frac {1}{\varepsilon}$ and $\frac {1}{\delta}$</font>.  
>
><font color="Brown">Notes::mjtsai1974</font>
>Why the execution of the <font color="Red">RMAX</font> algorithm will attain an expected return of $Opt(\prod_{M}(\varepsilon,T))-2\cdot\varepsilon$?  
>
>As a result of the fact that the <font color="#00ADAD">optimal policy</font> is defined on <font color="OrangeRed">$\varepsilon$-return mixing time</font> of $T$, the <font color="#D600D6">real return</font> of the execution of the <font color="Red">RMAX</font> algorithm must be smaller than it, thus we choose it to be $-2\cdot\varepsilon$.  

### <font color="RoyalBlue">Why the RMAX algorithm is polynomial?</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Recap on implicit explore or exploit lemma</font>  
>The implicit explore or exploit lemma guarantees that the policy generated from the simulated model $M_{L}$ onto the target model $M$ could either leads to $\alpha$ close to optimal reward or explore efficiently with hight probability of at least $\frac {\alpha}{R_{max}}$, where $M_{L}\rightarrow_{\alpha}M$ and $\alpha$=$\frac {\varepsilon}{N\cdot T\cdot R_{max}}$.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Due to $\alpha$ approximation</font>  
>Since $\alpha$=$\frac {\varepsilon}{N\cdot T\cdot R_{max}}$, the $T$ step phases in which we are exploring in the execution of the <font color="Red">RMAX</font> algorithm is polynomial in $N$,$T$,$\varepsilon$.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Learn over $N$ states and $k^{2}$ actions</font>  
>There are totally $N$ states(or stage games) in model $M$ with $k$ actions for the agent and the adversary, therefore, we have a polynomial number of parameters to learn, say $N$ and $k$.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">The probability to update the unknown information</font>  
>The probability the <font color="Red">RMAX</font> alrorithm to turn a state from unknown to known or to update statistics information is polynomial in $\varepsilon$,$T$,$N$.  
>
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">A brief summary</font>  
>Base on all of above, <font color="OrangeRed">by sampling in a large number of times</font>, the implicit explore or exploit lemma guarantees <font color="DeepSkyBlue">the least probabilistic exploration</font>, and we can ensure that <font color="OrangeRed">the fail rate in attaining the optimal reward is quiet small</font>, say $\delta$.  
>
>The <font color="Red">RMAX</font> algorithm claims that we can get near optimal reward with probability $1-\delta$ <font color="OrangeRed">by sampling a sufficient large number of trials over the same state</font>, which is polynomial in $\frac {1}{\delta}$.  
>
>Watch out that <font color="OrangeRed">each trial contains either exploration or exploitation</font>, next to prove this theorem.  

### The <font color="Red">RMAX</font> Theorem Proof::The Accuracy In The Transitive Probability Estimate
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The accuracy in the estimate of transitive probability</font>  
>First, we'd like to prove that the estimate of transitive probability in the implicit explore or exploit is accurate.  
>
>The majority focus on <font color="Red">the number of trials in this same state</font>, that is <font color="RoyalBlue">how many times of state transition in this same state for explore or exploit could we believe that the estimated transitive probability is accurate?</font>  
>
><font color="DeepSkyBlue">[2]</font>
><font color="Red">By sampling in a large number of trials over the same state</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-03-26-rl-rmax-part4-trials-over-same-state.png "trials over same state")
>How many number of trials on $G_{i}$(<font color="Red">in this same state</font>) could we update the transitive statistics of $G_{i}$?  
>&#10112;suppose there exists such transitive probability $p$ on $G_{i}$, <font color="RosyBrown">it could not be guaranteed with probability $1$</font>, that is $0\leq p\leq 1$.  
>&#10113;totally, there are $N\cdot k^{2}$ such probabilities, for we have $N$ states, with agent and adversary each having $k$ actions.  
>&#10114;treat the random variable <font color="DeepSkyBlue">$X_{i}$</font> to be <font color="DeepSkyBlue">the distinct trial on state $G_{i}$</font>, with above denoted transitive probability $p$ to transite from state $G_{i}$ to $G_{i^{\'}}$, that is to say  
>* The value of $X_{1}$=$1$, iff it transits from $G_{i}$ to $G_{i^{\'}}$ with probability $p$; otherwise, 
>the value of $X_{1}$=$0$, iff it just revisits over the same state $G_{i}$ with probability $1-p$.  
>
>&#10115;let $Z_{i}$=$X_{i}-p$, then  
>$E\lbrack Z_{i}\rbrack$  
>=$E\lbrack X_{i}-p\rbrack$  
>=$E\lbrack X_{i}\rbrack$-$p$  
>=$1\cdot p$-$p$  
>=$0$, and $\vert Z_{i}\vert\leq 1$  
>* By [Chernoff Bounds For Bernoulli Random Variable]({{ site.baseurl }}/2019/12/09/prob-bound-chernoff-bound-bernoulli/), we have  
>$P(\sum_{i=1}^{n}Z_{i}>a)<e^{-\frac {a^{2}}{2\cdot n}}$,  
>where $Z_{1}$,$Z_{2}$,...,$Z_{n}$ are the $n$ distinct independent trials on state $G_{i}$, and $a$ is the error term, such inequality is to ask for the error probability that after $n$ independent trials on state $G_{i}$, the total estimate bias is greater than the error term $a$.  This error probability is upper bounded by $e^{-\frac {a^{2}}{2\cdot n}}$.  
>
>&#10116;  

### Addendum
>&#10112;[R-max: A General Polynomial Time Algorithm for Near-Optimal Reinforcement Learning, Ronen I. Brafman, CS in Ben-Gurion University, Moshe Tennenholtz, CS in Stanford University](http://www.jmlr.org/papers/volume3/brafman02a/brafman02a.pdf)  

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