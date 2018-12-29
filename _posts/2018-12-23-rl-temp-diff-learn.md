---
layout: post
title: Temporal Difference Learning
---

## Prologue To The <font color="Red">Temporal Difference Learning</font>
<p class="message">
<font color="Red">Temporal difference learning</font>, called <font color="Red">TD Lambda</font>, <font color="Red">TD($\lambda$)</font>, it is about <font color="DeepPink">to learn to make prediction that takes place over time</font>.  
</p>

### Begin By Intuition
>Given below state transition, where $R_{i}$ is the <font color="#9300FF">immediate reward</font> associated with $S_{i}$, and we try to predict the expected sum of discounted rewards by TD($\lambda$).  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-12-23-rl-temp-diff-learn-example-over-time.png "TD Lambda")

### ReCap The <font color="DeepSkyBlue">Backup</font> In <font color="Red">Markov Chain</font>
><font color="RoyalBlue">[Question]</font>  
>Given this <font color="Red">Markov chain</font>, where all states are initialized with value $0$, and $S_{3}$ is stochastic with $0.9$ to $S_{4}$, $0.1$ to $S_{5}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-12-23-rl-temp-diff-learn-example-mc.png "M.C")
>For $S_{F}$ is the state we end up in, this final state is set to $0$ in its value.  As to other states, it's the expected value of the reward plus the discounted value of the state we end up in.  
>$V(S)$=  
>&#10112;$0$ for $S_{F}$.  
>&#10113;$E\lbrack R_{i}+\gamma\cdot V(S')\rbrack$, $S'$ is the state we arrive in.  
>The <font color="#9300FF">immediate reward</font> associated are $+1$ with $S_{1}$, $+2$ with $S_{2}$, $0$ with $S_{3}$, $+1$ with $S_{4}$ and $+10$ with $S_{5}$.  Let <font color="#D600D6">discounted factor</font> $\gamma$=$1$, <font color="RoyalBlue">what is V($S_{3}$)?</font>  
>
><font color="DeepSkyBlue">[Answer]</font>
>We'd like to use the <font color="DeepSkyBlue">backup propagation</font> to figure out the value function of these states:  
>&#10112;V($S_{4}$)=$1$+$\gamma\cdot 1\cdot 0$=$1$  
>&#10113;V($S_{5}$)=$10$+$\gamma\cdot 1\cdot 0$=$10$  
>&#10114;V($S_{3}$)=$0$+$\gamma\cdot(0.9\cdot 1+0.1\cdot 10)$  
>=$1.9$, where $\gamma$=$1$  
>&#10115;V($S_{1}$)=$1$+$\gamma\cdot 1\cdot 1.9$=$2.9$  
>&#10116;V($S_{2}$)=$2$+$\gamma\cdot 1\cdot 1.9$=$3.9$  

### Estimate From Data In Example
><font color="RoyalBlue">[Question]</font>  
>Given the same <font color="Red">Markov chain</font> with $\gamma$=$1$, this is the simulation before we know the whole image of the model.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-12-23-rl-temp-diff-learn-example-mc-2.png "M.C")
><font color="RoyalBlue">We'd like to estimate the value of $S_{1}$ after 3 and 4 episodes</font>, since nothing related to $S_{2}$, just ignore it.   
>
><font color="DeepSkyBlue">[Hints]::by mjtsai1974</font>
>The red marked numbers are the value of $S_{1}$ in each episode.  <font color="DeepPink">By using backup or expect discounted reward could we obtain the same value function of states, even for $\gamma$=$0.9$.</font>  Let me do the illustrtation of the 1st episode.  
>[1]by using <font color="DeepSkyBlue">backup</font>:  
>&#10112;$V(S_{4})$=$1+\gamma\cdot 1\cdot 1$  
>$V(S_{4})$=1 for $\gamma$=$1$ and $0.9$  
>&#10113;$V(S_{3})$=$0+\gamma\cdot V(S_{4})$  
>$V(S_{3})$=$1$ for $\gamma$=$1$ and $0.9$ for $\gamma$=$0.9$  
>&#10114;$V(S_{1})$=$1+\gamma\cdot V(S_{3})$  
>$V(S_{1})$=$2$ for $\gamma$=$1$ and $1.81$ for $\gamma$=$0.9$  
>[2]by using <font color="DeepSkyBlue">expect discounted reward</font>:  
>&#10112;$V(S_{1})$ expression  
>=$1$+$\gamma\cdot 1\cdot(0+\gamma\cdot 1\cdot(1+\gamma\cdot 1\cdot 0))$  
>, where $V(S_{1})$=$2$ for $\gamma$=$1$ and $1.81$ for $\gamma$=$0.9$  
>
><font color="DeepSkyBlue">[Answer]</font>
>The appropriate estimate for $V(S_{1})$ after 3 and 4 episodes would be $\frac {2+11+2}{3}$=$5$ and $\frac {2+11+2+2}{4}$=$4.25$ respectively.  
>
>To estimate from data is asking to do an <font color="DeepSkyBlue">expectation</font>, it is just <font color="DeepSkyBlue">averaging</font> things.  We can <font color="DeepPink">incrementally compute an estimate for the value of a state, given the previous estimate.</font>  
>
>But, it is a big jump for $V(S_{1})$ from $5$ to $4.25$, when it is estimated from eposide 3 to 4.  With an inifinite amount of data in an already known <font color="Red">Markov chain</font> model, we should get $V(S_{1})$=$2.9$, which is the converged value, could be found in above section ReCap The <font color="DeepSkyBlue">Backup</font> In <font color="Red">Markov Chain</font>.  
>
>Because, <font color="RosyBrown">not enough data</font>, just 3 episodes, an over-representation of the higher reward, that's why we have higher skewed estimate of $5$ than $4.25$ in 4 episodes.  

<!--
### Addendum
>&#10112;[Temporal Difference Learning, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4178018883/concepts/41512300800923)  
-->

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