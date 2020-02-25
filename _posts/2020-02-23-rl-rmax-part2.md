---
layout: post
title: Model-Based RL Algorithm RMAX - Part 2
---

## Prologue To Model-Based RL Algorithm <font color="Red">RMAX</font> - Part 2
<p class="message">
The <font color="Red">RMAX</font> theorem guarantees that the execution of algorithm will attain $-2\cdot\varepsilon$ close to optimal expected return <font color="DeepPink">in polynomial time</font>, whereas the algorithm <font color="Red">is developed by constructing a simulated model plugging with an extra fictitious $G_{0}$ state to approximate the target model</font>.  To validate the algorithm, this article would like to prove that <font color="DeepPink">the difference of the expected returns in between the simulated and the target model is infinitesimal</font>.  
</p>

### $\alpha$ Approximation
>Given that $M$ and $M^{\'}$ are 2 distinct <font color="OrangeRed">stochastic games</font> over the same set of states and actions, then $M^{\'}$ is <font color="Red">$\alpha$ approximation</font> of $M$ if below holds for every state $s$:  
>&#10112;$P_{M}(s,a,a^{\'},s^{\'})-\alpha\leq P_{M^{\'}}(s,a,a^{\'},s^{\'})\leq P_{M}(s,a,a^{\'},s^{\'})+\alpha$  
>, where $P_{M}(s,a,a^{\'},s^{\'})$ is the probabilistic transition for the agent from state $s$ to $s^{\'}$ by choosing action $a$, and the adversary chooses action $a^{\'}$ in model $M$, the same for $P_{M^{\'}}(s,s^{\'},a,a^{\'})$ is the same.  
>&#10113;for every state $s$, <font color="OrangeRed">the same</font> stage game is associated with $s$ in $M$ and $M^{\'}$, <font color="DeepPink">the rewards would be identical</font>.  

### Approximation Makes Small Difference
>Let $M$ and $M^{\'}$ be <font color="OrangeRed">stochastic games</font> over $N$ states, where $M^{\'}$ is an $\frac {\varepsilon}{N\cdot T\cdot R_{max}}$ approximation of $M$, then for every state $s$, agent policy $\pi$, adversary policy $\rho$, we have that  
>* $\left|U_{M^{\'}}(s,\pi,\rho,T)-U_{M}(s,\pi,\rho,T)\right|\leq\varepsilon$  
>, where $U_{M}(s,\pi,\rho,T)$ is the optimal expected reward with regards to agent policy $\pi$, adversary policy $\rho$, given that they are from state $s$, make state transitions over $T$ steps.  
>
><font color="Brown">Notes::mjtsai1974</font>  
>&#10112;begin from  
>$\left|U_{M^{\'}}(s,\pi,\rho,T)-U_{M}(s,\pi,\rho,T)\right|$  
>=$\sum_{p}\left|P_{M^{\'}}(p)\cdot U_{M^{\'}}(p) - P_{M}(p)\cdot U_{M}(p)\right|$  
>
>, where $p$ is the path starting from each state $s$, totally $N$ states, after ranging from $s$, make state transition of $T$ steps.  
>
>&#10113;each such optimal expexted reward of path $p$ in $M^{\'}$ could be expressed as:  
>$\sum_{s}\sum_{s'}P_{M^{\'}}(s,a,a^{\'},s^{\'})\cdot U_{M^{\'}}(s^{\'})$  
>
>, where $U_{M^{\'}}(s^{\'})$=$\sum_{i=1}^{T}\gamma^{i-1}\cdot V_{M^{\'}}(S_{i}^{\'})$  
>
>&#10114;origin formula in &#10112; becomes:  
>$\sum_{s}\sum_{s'}(P_{M^{\'}}(s,a,a^{\'},s^{\'})\cdot U_{M^{\'}}(s^{\'})$-$P_{M}(s,a,a^{\'},s^{\'})\cdot U_{M}(s^{\'}))$  
>
>, where $s$=$\\{s_{1},s_{2},...,s_{N}\\}$  
>
>&#10115;we are given $M^{\'}$ is an $\alpha$ approximation of $M$, and  
>$U_{M^{\'}}(s^{\'})$=$\sum_{i=1}^{T}\gamma^{i-1}\cdot V_{M^{\'}}(s_{i}^{\'})\leq\sum_{i=1}^{T}V_{M^{\'}}(s^{\'})$ must hold  
>
>&#10116;$\left|U_{M^{\'}}(s,\pi,\rho,T)-U_{M}(s,\pi,\rho,T)\right|$  
>=$\sum_{s}\sum_{s'}(P_{M^{\'}}(s,a,a^{\'},s^{\'})\cdot U_{M^{\'}}(s^{\'})$-$P_{M}(s,a,a^{\'},s^{\'})\cdot U_{M}(s^{\'}))$  
>=$\sum_{s}\sum_{s'}(P_{M^{\'}}(s,a,a^{\'},s^{\'})\cdot\sum_{i=1}^{T}V_{M^{\'}}(s^{\'})$-$P_{M}(s,a,a^{\'},s^{\'})\cdot\sum_{i=1}^{T}V_{M}(s^{\'}))$  
>=$\sum_{s}\sum_{s'}(P_{M^{\'}}(s,a,a^{\'},s^{\'})$-$P_{M}(s,a,a^{\'},s^{\'})\cdot T\cdot(V_{M^{\'}}(s^{\'})-V_{M}(s^{\'})))$  
>$\leq\sum_{s}\sum_{s'}(\frac {\varepsilon}{N\cdot T\cdot R_{max}}\cdot T\cdot(V_{M^{\'}}(s^{\'})-V_{M}(s^{\'})))$  
>$\;\;$...by given $M^{\'}$ is an $\frac {\varepsilon}{N\cdot T\cdot R_{max}}$ approximation of $M$  
>$\leq\sum_{s}\sum_{s'}(\frac {\varepsilon}{N\cdot T\cdot R_{max}}\cdot T\cdot R_{max})$  
>$\;\;$...<font color="DeepPink">all optimal expected rewards are bounded by $R_{max}$ in this algorithm, hence their difference</font>  
>$\leq N\cdot\frac {\varepsilon}{N\cdot T\cdot R_{max}}\cdot T\cdot R_{max}$=$\varepsilon$  
>$\;\;$...totally $N$ such states, each distinct $s$ has lots of $s^{\'}$ as its next state, which could then be sum up as $1$, thus $\sum_{s}\sum_{s^{\'}}$=$N$  

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