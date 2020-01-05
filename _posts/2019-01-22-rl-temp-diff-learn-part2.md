---
layout: post
title: Temporal Difference Learning - Part 2
---

## Prologue To The <font color="Red">Temporal Difference Learning</font> - Part 2
<p class="message">
This is the part 2, new introduce $TD(0)$, continue with advantages and cons of $TD(0)$, $TD(1)$, come out with conclusion in <font color="Red">TD($\lambda$)</font>.  
</p>

### <font color="Red">$TD(0)$</font> Algorithm: $\lambda$=$0$
>This is by taking $\lambda$=$0$ in <font color="Red">$TD(\lambda)$</font> algorithm.  
><font color="DeepSkyBlue">[The rule]</font>
>Eposide $T$:  
>$\;\;$For all $S$, $e(S)$=<font color="Red">$0$</font> at <font color="DeepSkyBlue">start</font> of eposide, $V_{T}(S)$=$V_{T-1}(S)$  
>$\;\;$After $S_{t-1}\xrightarrow{r_{t}}S_{t}$:(from step $t-1$ to $t$ with <font color="#9300FF">reward</font> $r_{t}$)  
>$\;\;\;e(S_{t-1})$=$e(S_{t-1})$+$1$:  
>$\;\;\;\;$Update <font color="DeepSkyBlue">eligibility</font> of $S_{t-1}$ after arriving to $S_{t}$  
>$\;\;$For all $S$,  
>$\;\;V_{T}(S)$=$V_{T-1}(S)$+$\alpha_{T}\cdot(r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1}))$...[A]  
>$\;\;\;e(S_{t-1})$=$0\cdot\gamma\cdot e(S_{t-1})$=<font color="Red">$0$</font>:  
>$\;\;\;\;$<font color="Red">before</font> transite from $S_{t-1}$ to $S_{t}$ in <font color="Red">next</font> iteration, we can easily tell that <font color="DeepSkyBlue">the eligibility of state $S$ is always zero</font>.  
>
><font color="DeepSkyBlue">[Notes]</font>
>&#10112;the 2nd part of (A) is sum of the <font color="#9300FF">reward</font> plus the the <font color="#D600D6">discounted</font> value of the state we just arrived, minus the state value we just left; where these state values are all evaluated in <font color="Red">last</font> iteration.  It could just be the <font color="Red">temporal difference</font>.  
>&#10113;we are going to apply the <font color="Red">temporal difference</font> onto <font color="Red">$S$ itself only</font>, with <font color="RosyBrown">no proportion to the eligibility of any other states</font>, and the <font color="Red">learning rate</font> would be specified for we don't want it to move too much.  
>&#10114;<font color="Red">after</font> the state has been iterated, <font color="DeepSkyBlue">decay or decrease its eligibility</font> with $\lambda\cdot\gamma$, in their given value, in <font color="Red">$TD(0)$</font>, $\lambda$=$0$, <font color="DeepSkyBlue">the eligibility of state $S$ is always zero</font>.  
>&#10115;and we are backing up to next stae.  
>
><font color="Red">[Caution]</font>
>&#10112;<font color="Red">all the $S$ are all being done in parallel</font>.  
>&#10113;the value at state $S$(the $S$ in [A]) is going to be updated on this quantity, $r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1})$, which is the same for everybody, <font color="RosyBrown">doesn't</font> depend on which $S$ we are updating, and <font color="DeepSkyBlue">$e(S)$=$1$ is specific to the state $S$ at the moment we are evaluating(looking at)</font>.  

### <font color="Red">MLE</font>(<font color="Red">Maximum Likelihood Estimate</font>) And <font color="Red">$TD(0)$</font> Algorithm
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">MLE</font>  
>Given data of a lot trajectories and we are under the condition that we are in $S_{t-1}$, and we don't know what state we are going to <font color="OrangeRed">end up</font> in.  But, there exists some <font color="OrangeRed">probability</font> of $r_{t}$+$\gamma\cdot V_{T-1}(S_{t})$-$V_{T-1}(S_{t-1})$.  
>
>If we take <font color="Red">expectation</font> of [A], then:  
>$V_{T}(S_{t-1})$=$E_{S_{t}}[r_{t}+\gamma\cdot V_{T-1}(S_{t})]$...[B]  
>We could treat it as <font color="Red">the MLE of $V_{T}(S_{t-1})$ over all possible $V_{T-1}(S_{t})$</font>.  What we are doing is just sampling different possible $S_{t}$ values, that is $V_{T-1}(S_{t})$, and is crossing over different trajectories for we have dataset of trajectories.  
>
>We are just taking an expectation over what we get as the next state of the <font color="#9300FF">reward</font> plus the <font color="#D600D6">discounted</font> estimated value(evaluated in last eposide) of that next state.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Why [B] is supposed to be the MLE?</font>  
>$\;\;$<font color="DeepPink">[B] is the MLE</font>  
>
><font color="Brown">proof::mjtsai1974</font>  
>&#10112;$V_{T}(S_{t-1})$  
>=$V_{T-1}(S_{t-1})$+$\alpha_{T}\cdot(r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1}))$  
>=$V_{T-1}(S_{t-1})\cdot(1-\alpha_{T})$+$\alpha_{T}\cdot(r_{t}+\gamma\cdot V_{T-1}(S_{t}))$...[B.1]  
>This is the value of $S_{t-1}$ in eposide $T$, when transiting from $S_{t-1}$ to $S_{t}$, and remind that we are given data of a lot trajectories with each containing state transition in it.  
>&#10113;suppose we are in $S_{t-1}$ in one trajectory, and the next $S_{t}$ does exist, there exists $k$ such $S_{t}$ and $n-k$ different states of $S_{t}$, and totally $n$ trajectories in the given data.  Therefore, <font color="Red">there exists some probability $P(S_{t}\vert S_{t-1})$=$\frac {k}{n}$</font>.  
>&#10114;$V_{T}(S_{t-1})$  
>=$\sum_{S{t}}P(S_{t}\vert S_{t-1})\cdot([B.1])$  
>=$E_{S_{t}}[r_{t}+\gamma\cdot V_{T-1}(S_{t})]$ just holds.  
>, where $V_{T-1}(S_{t-1})\cdot(1-\alpha_{T})$ and $\alpha_{T}\cdot(r_{t}+\gamma\cdot V_{T-1}(S_{t}))$ are some values varying in each trajectory, the former is the departuring state, the later is the ending state, $\alpha_{T}$ is the learning rate, depends on how you would like the learning process to be.  I just use the term $r_{t}+\gamma\cdot V_{T-1}(S_{t})$ to be the <font color="OrangeRed">random variable</font> to be taken expectation.  

### Illustration: The Idea Of TD(0) After TD(1)
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The given example</font>  
>Succeeding to the same example as part 1 article, this time we are given data of 5 trajectories, the red quantity is the value of the state after <font color="DeepSkyBlue">backup propagation</font> with $\gamma$=$1$.  Recall that each distinct state's initial value is $0$.  We'd like to ask for <font color="RoyalBlue">the value of $S_{2}$ in the 5-th eposide</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2019-01-22-rl-temp-diff-learn-part2-ex.png "M.C")
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">By using TD(1)</font>  
>&#10112;we can deduce it out the <font color="Red">temporal difference</font> term:  
>$\triangle V_{T}(S_{2})$  
>=$r_{2}$+$\gamma\cdot r_{3}$+$\gamma^{2}\cdot r_{5}$+$\gamma^{3}\cdot V_{T-1}(S_{F})-V_{T-1}(S_{2})$  
>=$12$  
>&#10113;$V_{T}(S_{2})$  
>=$V_{T-1}(S_{2})$+$\triangle V_{T}(S_{2})$  
>=$0$+$12$  
>=$12$  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">By using MLE</font>  
>$V_{T}(S_{2})$  
>=$r_{2}$+$\gamma\cdot P(S_{3}\vert S_{2})\cdot V_{T}(S_{3})$  
>=$r_{2}$+$\gamma\cdot P(S_{3}\vert S_{2})\cdot [r_{3}$  
>$\;\;$+$\gamma\cdot (P(S_{4}\vert S_{3})\cdot(V_{T}(S_{4}))$  
>$\;\;\;\;$+$P(S_{5}\vert S_{3})\cdot (V_{T}(S_{5}))]$  
>=$r_{2}$+$\gamma\cdot P(S_{3}\vert S_{2})\cdot [r_{3}$  
>$\;\;$+$\gamma\cdot (P(S_{4}\vert S_{3})\cdot(r_{4}+\gamma\cdot P(S_{F}\vert S_{4})\cdot V_{T}(S_{F}))$  
>$\;\;\;\;$+$P(S_{5}\vert S_{3})\cdot (r_{5}+\gamma\cdot P(S_{F}\vert S_{5})\cdot V_{T}(S_{F})))]$  
>
>, and from data, we have <font color="OrangeRed">probability of transition</font> that  
>&#10112;$\gamma$=$1$  
>&#10113;$P(S_{3}\vert S_{2})$=$1$  
>&#10114;$P(S_{4}\vert S_{3})$=$0.6$  
>&#10115;$P(S_{5}\vert S_{3})$=$0.4$  
>&#10116;$P(S_{F}\vert S_{4})$=$1$  
>&#10117;$P(S_{F}\vert S_{5})$=$1$  
>
>Therefore,  
>$V_{T}(S_{2})$  
>=$2$+$1\cdot 1\cdot [0$  
>$\;\;$+$1\cdot (0.6\cdot(1+1\cdot 1\cdot 0)$  
>$\;\;\;\;$+$0.4\cdot (10+1\cdot 1\cdot 0))]$  
>=$6.6$, by the same approach, $V_{T}(S_{1})$=$5.6$.  
>
>Cautions must be made that <font color="DeepPink">by using MLE for $V_{T}(S_{2})$, we choose to refer to the same eposide $T$</font>, <font color="RosyBrown">not $T-1$</font>, why?  
>This is all due to <font color="DeepPink">we are doing the estimiation by using data</font>.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">The breakdown</font>  
>Please recall in [Temporal Difference Learning - Part 1]({{ site.github.repo }}{{ site.baseurl }}/2018/12/23/rl-temp-diff-learn-part1/), I have figured out that $V_{T}(S_{1})$=$2.9$, $V_{T}(S_{2})$=$3.9$, $V_{T}(S_{3})$=$1.9$, by using both <font color="DeepSkyBlue">backup propagation</font> and <font color="DeepSkyBlue">expect discounted reward</font> in the section of ReCap The Backup In Markov Chain.  
>
>The <font color="RosyBrown">MLE of $V_{T}(S_{2})$</font>=$6.6$, which is more, whereas the <font color="RosyBrown">$TD(1)$</font> estimate is $12$, a lot more, <font color="RosyBrown">all wrong</font>, <font color="DeepPink">except for $V_{T}(S_{2})$=$3.9$ by using backup based on the whole model</font>.  <font color="RoyalBlue">Why MLE is less wrong?  Why $TD(1)$ estimate is so far off?</font>  
>&#10112;when we compute the <font color="RosyBrown">$TD(1)$</font> estimate, we <font color="RosyBrown">use only the 5-th trajectory, one of the five trajectories</font> to propagate the information back.  
>&#10113;when we use <font color="OrangeRed">MLE</font> for the estimation, we <font color="OrangeRed">use all data</font>, more information, more accurate.  The more might not be the better, but, we can resort the inaccuracy of <font color="RosyBrown">MLE of $V_{T}(S_{2})$</font>=$6.6$ to that <font color="RosyBrown">we don't have the complete data set</font> to build this whole MC model.  
>
>Specifically be noted that <font color="Red">$TD(1)$ is alos be treated as outcome-based estimate for it uses the immedaite reward and ignores the intermediate encountered states' value</font>.  
>
><font color="DeepSkyBlue">[5]</font>
><font color="OrangeRed">A tiny finding</font>  
>We have a tiny finding that <font color="DeepPink">$TD(0)$ relates current state's value to next most closed state's value, is more like MLE estimate</font>, even if we are using it in one trajectory, the 5-th in this illustration.  
>
>The <font color="DeepPink">temporal difference</font> is about to learn to make prediction of states value for these states transit over time <font color="DeepPink">in the unit of one distinct trajectory</font>, whereas the <font color="DeepPink">MLE</font> tends to estimate states' value <font color="DeepPink">accrossing all trajectories</font> in given sample.  
>
><font color="OrangeRed">The argument in between $TD(0)$, $TD(1)$ and MLE is in that we don't have the full image of the Markov chain model, with only a little sampling data.</font>  

### The <font color="Red">Outcome Based</font> v.s. The <font color="Red">Intermediate Estimate Based</font>::<font color="Brown">mjtsai1974</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Summary of these equations</font>  
>I'd like to step further to deeper inside in the concept with $TD(0)$ and $TD(1)$.  Given below 3 expression:  
>&#10112;$V_{T}(S_{t-1})$  
>=$V_{T-1}(S_{t-1})$+$\alpha_{T}\cdot(r_{t}+\gamma\cdot V_{T-1}(S_{t})-V_{T-1}(S_{t-1}))$...[A]  
>&#10113;$V_{T}(S_{t-1})$  
>=$E_{S_{t}}[r_{t}+\gamma\cdot V_{T-1}(S_{t})]$...[B]  
>&#10114;$V_{T}(S_{t-1})$  
>=$E[r_{t}+\gamma\cdot r_{t+1}+\gamma^{2}\cdot r_{t+2}+\gamma^{3}\cdot r_{t+3}+...]$...[C]  
>, where [A] is the regular expression in temporal difference, works for both $TD(0)$ and $TD(1)$, the difference is in <font color="DeepSkyBlue">$TD(0)$ rule the eligibility of the evaluated state would be reset to $0$</font>; the equation [B] is by taking expect of [A], more description is in $TD(0)$ related section; whereas <font color="OrangeRed">[C] is the idea by taking only the reward sequence that we saw, ignoring the estimate we might have gotten in some other states</font>, which is the spiritual $TD(1)$.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Why toss out $\gamma^{k}\cdot V_{T-1}(S_{t+k})-V_{T-1}(S_{t-1})$?</font>  
>Moreover, the full [C] expression should be refined as:  
>$V_{T}(S_{t-1})$  
>=$E[r_{t}+\gamma\cdot r_{t+1}+\gamma^{2}\cdot r_{t+2}$  
>$\;\;+...+\gamma^{k-1}\cdot r_{t+k-1}+\gamma^{k}\cdot V_{T-1}(S_{t+k})-V_{T-1}(S_{t-1})]$...[D]  
>
>The reason we <font color="OrangeRed">ignore</font> these 2 terms <font color="OrangeRed">$\gamma^{k}\cdot V_{T-1}(S_{t+k})-V_{T-1}(S_{t-1})$</font> is that <font color="OrangeRed">when $k$ is quiet large, the $\gamma^{k}$ would then approach $0$</font>, and <font color="OrangeRed">$V_{T-1}(S_{t-1})$'s initial value is $0$ in one eposide, if $S_{t-1}$ is the target state to be evaluated</font>, especially the <font color="OrangeRed">very first time</font> it is evaluated.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Evaluation on [B] and [C]</font>  
>By using [C], is just like the $S_{2}$ in the 5-th trajectory in above illustrated example, however, <font color="DeepPink">when the trajectory is an infinite series, the $TD(1)$ also does the right thing</font>, repeating that update over and over again <font color="RosyBrown">won't</font> change anything, because <font color="OrangeRed">the expectation is the expectation</font> expressed in terms of the <font color="#9300FF">saw rewards</font>.  
>
>By using [B], it takes the <font color="OrangeRed">intermediate estimates</font> that we have computed and refined on all the <font color="OrangeRed">intermediate nodes</font>, that is taking all the states we encountered along the way into concern to improve our estimate of the value of every other state.  
>
>Therefore, [B] is more self-consistent of connecting the value of states to the value of the other states you want(or encountered), and [C] is just using the experience that it saws and ignores the existence of the intermediate states.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="Red">Cautions</font>  
>All above are under the condition that we have been given <font color="RosyBrown">partial</font>, <font color="RosyBrown">incomplete</font> data <font color="RosyBrown">before</font> we know the full model of state transition, or <font color="OrangeRed">even if</font> we are given the complete data of a target model to be predicted, we still believe that we don't have it yet!!  
>
><font color="DeepSkyBlue">[5]</font>
><font color="Brown">The appropriate apply::mjtsai1974</font>  
>Trivially, [D] relates the final state value of $V_{T-1}(S_{t+k})$ to the target evaluated state $S_{t-1}$ in eposide $T$, whose value is expressed in terms of $V_{T-1}(S_{t-1})$.  
>$V_{T}(S_{t-1})$  
>=$E[r_{t}+\gamma\cdot r_{t+1}+\gamma^{2}\cdot r_{t+2}$  
>$\;\;+...+\gamma^{k-1}\cdot r_{t+k-1}+\gamma^{k}\cdot V_{T-1}(S_{t+k})-V_{T-1}(S_{t-1})]$  
>
>The point is:  
>&#10112;<font color="#C20000">how large $k$(<font color="OrangeRed">the length of trajectory</font>) should be for we to safely toss out these 2 terms?</font>  
>&#10113;<font color="DeepSkyBlue">before $k$ is large enough</font>, we should be able to <font color="DeepSkyBlue">calculate(or incorporate) new arrivaed state's value</font>, which is reasonable <font color="DeepSkyBlue">to relate current arrived state to the target evaluated state</font>, <font color="OrangeRed">repeat</font> this behavior <font color="OrangeRed">until $k$ is large enough</font>.  
>
><font color="DeepSkyBlue">[6]</font>
><font color="Brown">After $k$ is large enough::mjtsai1974</font>  
>Evenmore, <font color="Red">after $k$ is large enough</font> to ignore these 2 terms, the algorithm should have a design to go back to <font color="OrangeRed">re-calculate</font> the target state's value, <font color="OrangeRed">the transition must range from $S_{t-1}$ to $S_{t+k-1}$</font>, thus to move toward a bit more closed to have a much maturer condition <font color="OrangeRed">to make a toggle of decision according to the new evaluated target state's value</font>.  
>
>Finally, <font color="Red">when $k$ is large enough</font>, it means that we have <font color="OrangeRed">state transition over a rather long horizon</font>, we are <font color="9300FF">safe to just use the experience of saw rewards</font>, since the update term of intermediate nodes would just be cancel out by the temporal difference equation(like [A] with $\lambda\neq 0$), thought by mjtsai1974, and might be evaluated by program in the future(to be conti).  

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