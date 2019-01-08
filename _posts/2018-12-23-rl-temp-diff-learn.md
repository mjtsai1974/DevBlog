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

### Computing Estimates Incrementally
><font color="RoyalBlue">[Question]</font>
>From prior example, we have the value of $S_{1}$=$5$, say $V_{3}(S_{1})$ after 3 episodes, then we ran an eposide, and the return of the episode, the total <font color="#D600D6">discounted reward</font> of $S_{1}$ in this distinct 4-th sequence was $2$, say $R_{4}(S_{1})$.  
>
><font color="RoyalBlue">Could we figure out what the new estimate of value of $S_{1}$, say $V_{4}(S_{1})$, just from this information?</font>  
>
><font color="DeepSkyBlue">[Answer]</font>
>By <font color="DeepSkyBlue">weighting</font>, $\frac {3\cdot 5 + 1\cdot 2}{4}$=$4.25$, we could get the same estimate identical to the way of <font color="DeepSkyBlue">expectation</font>.  
>
><font color="DeepSkyBlue">[The generalization]</font>
>Can we generalize it?  Yes!  
>$V_{T}(S_{1})$  
>=$\frac {(T-1)\cdot V_{T-1}(S_{1})+1\cdot R_{T}(S_{1})}{T}$  
>=$\frac {(T-1)\cdot V_{T-1}(S_{1})}{T}$+$\frac {1\cdot R_{T}(S_{1})}{T}$  
>=$\frac {(T-1)\cdot V_{T-1}(S_{1})}{T}$+$\frac {V_{T-1}(S_{1})}{T}$+$\frac {1\cdot R_{T}(S_{1})}{T}$-$\frac {V_{T-1}(S_{1})}{T}$  
>=$V_{T-1}(S_{1})$+$\alpha_{T}\cdot (R_{T}(S_{1})-V_{T-1}(S_{1}))$  
>, where we have it that:  
>&#10112;$\alpha_{T}$=$\frac {1}{T}$, the <font color="DeepSkyBlue">learning rate(parameter)</font>  
>&#10113;the <font color="Red">temporal difference</font> is <font color="DeepPink">the difference between the reward we get at this step and the estimate we had at th eprevious step</font>.  
>&#10114;$R_{T}(S_{1})-V_{T-1}(S_{1})$ is <font color="DeepSkyBlue">the error term</font>.  If the difference is <font color="OrangeRed">zero</font>, then <font color="OrangeRed">no change</font>; if the difference is <font color="DeepPink">(big) positive</font>, then, it <font color="DeepPink">goes up</font>; if the difference is <font color="RosyBrown">big negative</font>, then, it <font color="RosyBrown">goes down</font>.  
>
>As we get more and more eposides, this <font color="DeepSkyBlue">learning parameter</font> $\alpha_{T}$ is getting small and small, and making smaller and smaller changes.  It's just like the update rule in perceptrons learning and neural network learning.  

### The Property Of <font color="DeepSkyBlue">Learning Rate</font>
>By given $V_{T}(S)$=$V_{T-1}(S)$+$\alpha_{T}\cdot(R_{T}(S)-V_{T-1}(S))$, then, $\lim_{T\rightarrow\infty}V_{T}(S)$=$V(S)$, with below 2 properties guarantee the convergence:  
>&#10112;$\sum_{T=0}^{\infty}\alpha_{T}\rightarrow\infty$  
>&#10113;$\sum_{T=0}^{\infty}(\alpha_{T})^{2}<\infty$  
><font color="Brown">proof::mjtsai1974</font>  
>I'd like to prove the learning rate property by using geometric series copnvergence/divergence by Gilbert Strange in Calculus.  
>&#10112;begin from $T$=$0$, initially $V_{0}(S)$=$C$, some constant, might be zero.  And $V_{T}(S)$=$V_{T-1}(S)$=$V_{0}(S)$ at this moment.  
>&#10113;suppose the equality holds, then expand from $T+1$:  
>$V_{T+1}(S)$  
>=$V_{T}(S)$+$\alpha_{T}\cdot(R_{T+1}(S)-V_{T}(S))$  
>=$V_{T}(S)$+$\alpha_{T}\cdot(R_{T+1}(S)-(V_{T-1}(S)$+$\alpha_{T}\cdot(R_{T}(S)-V_{T-1}(S))))$  
>=$V_{T}(S)$+$\alpha_{T}\cdot(R_{T+1}(S)-(V_{T-1}(S)$+$\alpha_{T}\cdot(R_{T}(S)-(V_{T-2}(S)$+$\alpha_{T}\cdot(R_{T-1}(S)-V_{T-2}(S))))))$  
>&#10114;the expand could be continued, but we stop over here for our proof...  
>=$V_{T}(S)$+$\alpha_{T}\cdot(R_{T+1}(S)-V_{T-1}(S))$  
>$\;\;$+$\alpha_{T}^{2}\cdot(R_{T}(S)-V_{T-2}(S))$  
>$\;\;$+$\alpha_{T}^{3}\cdot(R_{T-1}(S)-V_{T-2}(S))$  
>&#10115;to make it perfect, expand the term $V_{T-2}(S)$, we can get it down the way to $T=0$:  
>=$V_{T}(S)$+$\alpha_{T}\cdot(R_{T+1}(S)-V_{T-1}(S))$  
>$\;\;$+$\alpha_{T}^{2}\cdot(R_{T}(S)-V_{T-2}(S))$  
>$\;\;$+$\alpha_{T}^{3}\cdot(R_{T-1}(S)-V_{T-3}(S))$  
>$\;\;$+$\alpha_{T}^{4}\cdot(R_{T-2}(S)-V_{T-4}(S))$  
>$\;\;$+$\alpha_{T}^{5}\cdot(R_{T-3}(S)-V_{T-5}(S))$+...  
>&#10116;we take $E_{1}$=$R_{T+1}(S)-V_{T-1}(S)$  
>$\;\;\;\;E_{2}$=$R_{T}(S)-V_{T-2}(S)$  
>$\;\;\;\;E_{3}$=$R_{T-1}(S)-V_{T-3}(S)$  
>...
>, where each $E_{i}$ is a constant, assume they are rather stable, non-variant, then we take these error terms as $E$.  
>&#10117;then, the whole terms after the first + operator could be expressed as:  
>$\alpha_{T}\cdot E$+$\alpha_{T}^{2}\cdot E$+$\alpha_{T}^{3}\cdot E$+$\alpha_{T}^{4}\cdot E$+...  
>=$(\alpha_{T}+\alpha_{T}^{2}+\alpha_{T}^{3}+\alpha_{T}^{4}+...)\cdot E$  
>=$(\lim_{k\rightarrow\infty}\sum_{i=1}^{k}\alpha_{T}^{i})\cdot E$, then,  
>$\lim_{k\rightarrow\infty}\sum_{i=1}^{k}\alpha_{T}^{i}$=$\frac {\alpha_{T}}{1-\alpha_{T}}$, for $\left|\alpha_{T}\right|$<$1$, and it holds to have these 2 properties, it is the convergent series, you can see in my prior post [Series Convergence]({{ site.github.repo }}{{ site.baseurl }}/2018/01/26/series-cnvg/).  

### The <font color="Red">$TD(\lambda)$</font> Algorithm
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
><font color="DeepSkyBlue">[Notes]</font>
>Where the $T$ stands for the specific eposide, $t$ is the index for <font color="Red">state transition</font>, and $e(S_{t})$ is for the <font color="DeepSkyBlue">eligibility</font>.  

### <font color="Red">$TD(1)$</font> Algorithm: $\lambda$=$1$
>This is by taking $\lambda$=$1$ in <font color="Red">$TD(\lambda)$</font> algorithm.  
><font color="DeepSkyBlue">[The rule]</font>
>Eposide $T$:  
>$\;\;$For all $S$, $e(S)$=$0$ at start of eposide, $V_{T}(S)$=$V_{T-1}(S)$  
>$\;\;$After $S_{t-1}\xrightarrow{r_{t}}S_{t}$:(from step $t-1$ to $t$ with <font color="#9300FF">reward</font> $r_{t}$)  
>$\;\;\;e(S_{t-1})$=$e(S_{t-1})$+$1$:  
>$\;\;\;\;$Update <font color="DeepSkyBlue">eligibility</font> of $S_{t-1}$ after arriving to $S_{t}$  
>$\;\;$For all $S$,  
>$\;\;V_{T}(S)$=$V_{T-1}(S)$+$\alpha_{T}\cdot(r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1}))$...(A)  
>$\;\;\;e(S_{t-1})$=$\gamma\cdot e(S_{t-1})$:  
>$\;\;\;\;$<font color="Red">before</font> transite from $S_{t-1}$ to $S_{t}$ in <font color="Red">next</font> iteration 
>
><font color="DeepSkyBlue">[Notes]</font>
>&#10112;the 2nd part of (A) is sum of the <font color="#9300FF">reward</font> plus the the <font color="#D600D6">discounted</font> value of the state we just arrived, minus the state value we just left; where these state values are all evaluated in <font color="Red">last</font> iteration.  It could just be the <font color="Red">temporal difference</font>.  
>&#10113;we are going to apply the <font color="Red">temporal difference</font> onto all states, <font color="Red">proportional to the eligibility of each distinct state</font>, and the <font color="Red">learning rate</font> would be specified for we don't want it to move too much.  
>&#10114;<font color="Red">after</font> the state has been iterated, <font color="DeepSkyBlue">decay or decrease its eligibility</font> with $\lambda\cdot\gamma$, in their given value, in <font color="Red">$TD(1)$</font>, $\lambda$=$1$.  
>&#10115;and we are backing up to next stae.  
>
><font color="Red">[Caution]</font>
>&#10112;<font color="Red">all the $S$ are all being done in parallel</font>.  
>&#10113;the value at state $S$(the $S$ in (A)) is going to be updated on this quantity, $r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1})$, which is the same for everybody, <font color="RosyBrown">doesn't</font> depend on which $S$ we are updating, and $e(S)$ is specific to the state $S$ we are evaluating(looking at).  

### Example: <font color="Red">$TD(1)$</font> Illustration
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Keeping track of changes ultimately</font>  
>Let's walk through the pseudo code in this given example, just to see how value update works.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-12-23-rl-temp-diff-learn-example-td1.png "TD(1)")
>&#10112;we are starting off at the beginning of an eposide.  Now, <font color="DeepSkyBlue">the eligibility for all states are all zero</font>.  
>&#10113;we'd like to keep track of changes ultimately, it's all going to get added to whatever the <font color="Red">previous</font> value.  
>&#10114;the 1st transition is from $S_{1}$ to $S_{2}$ with <font color="#9300FF">reward</font> $r_{1}$, and sets the <font color="DeepSkyBlue">eligibility $e(S_{1})$ to 1 for $S_{1}$</font>.  
>&#10115;we'd like to loop through all the states, all of them, and apply the same little update to all of the states.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The expression of the update</font>  
>The update has the form:  
>&#10112;whatever the current <font color="DeepSkyBlue">learning rate</font> is, times the <font color="#9300FF">reward</font> which we just experienced, say $r_{1}$, plus the <font color="#D600D6">discount factor gamma $\gamma$</font> times the previous value of the state we newly arrived, minus the the previous value of the state we just left.  
>&#10113;$\alpha_{T}\cdot(r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1}))$, it is going to get added to <font color="OrangeRed">all</font> states, such quantity <font color="DeepSkyBlue">is proportional to the eligibility of that state</font>.  

<!--
### Example: <font color="Red">$TD(1)$</font> Illustration
### <font color="Red">$TD(0)$</font> Illustration: $\lambda$=$0$
### <font color="Red">$TD(0)$</font> Illustration: $0\ge\lambda\le 1$
-->

### Addendum
>&#10112;[Temporal Difference Learning, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4178018883/concepts/41512300800923)  

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