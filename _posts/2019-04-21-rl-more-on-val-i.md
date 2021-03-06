---
layout: post
title: More On Value Iteration
---

## Prologue To More On <font color="Red">Value Iteration</font>
<p class="message">
Prior post details the way <font color="Red">contraction mapping</font> makes <font color="Red">value iteration</font> converges.  This post would dive a little bit on the <font color="DeepSkyBlue">horizontal length</font> for convergence.
</p>

### $\frac {1}{1-\gamma}$ Bits Of Precision
>We'd like to dive a little bit to relate the <font color="DeepSkyBlue">horizontal length</font> to the <font color="OrangeRed">convergence</font>, by below given:  
>&#10112;denote the <font color="OrangeRed">dimensionality</font> of states and actions as $\vert S\vert$ and $\vert A \vert$.  
>&#10113;also with $R_{max}$=$max_{S,A}\vert R(S,A)\vert$.  
>&#10114;$\frac {1}{1-\gamma}$ as bits of precision.  
>&#10115;for some $t^{\ast}$ polynomial in $\vert S\vert$ and $vert A \vert$.  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">There is some time before infinity</font>  
>&#10112;$\pi(S)$=$argmax_{A}Q_{t^{\ast}}(S,A)$ is optimal.    
>&#10113;we treat the $Q^{\ast}$ to be the $Q$ function after we iterate over $t^{\ast}$ times, we know that it converges in the limit, $Q_{t}$ eventually goes to $Q^{\ast}$.  
>
>$\Rightarrow$Here is the <font color="OrangeRed">hint</font> that we found there is some $t^{\ast}$ of <font color="OrangeRed">finite horizon</font>, <font color="Red">less than infinity</font>, that's <font color="DeepSkyBlue">polynomial</font> in:  
>&#10112;the <font color="OrangeRed">number of states</font>  
>&#10113;the <font color="OrangeRed">number of actions</font>  
>&#10114;the <font color="OrangeRed">magnitude of the rewards</font> in the reward function  
>&#10115;the <font color="OrangeRed">number of bits of precision</font> that are used to specified the <font color="Red">transition probability</font>  
>&#10116;<font color="OrangeRed">number of bits</font> of $\gamma$ in $\frac {1}{1-\gamma}$  
>
>$\Rightarrow$So, that, if we run value iteration for that <font color="DeepSkyBlue">many steps</font>, the $Q$ function that we get out is $Q_{t^{\ast}}$ of $(S,A)$.  If we define a <font color="#00ADAD">policy $\pi(S,A)$</font>, which is just the <font color="#00ADAD">greedy policy</font> with respect to that $Q$ function, then that <font color="#00ADAD">policy</font> is <font color="Red">optimal</font>.  
>
>$\Rightarrow$We know that <font color="OrangeRed">in the limit</font>, if we run value iteration for an <font color="OrangeRed">infinite</font> number of steps, then the $Q$ function that we get at that point, the <font color="#00ADAD">greedy policy</font> with respect to the $Q$ function, is just <font color="Red">optimal</font>.  
>
>$\Rightarrow$This leads to a finding that <font color="DeepPink">there is sometime before infinity where we get a $Q$ function that's close enough, so that if you do the greedy policy with respect to it(the $Q$ function), it really is optimal</font>.  Like all the way $100\%$ optimal.  
>
>$\Rightarrow$What that really means is that <font color="#C20000">it's polynomial(all the way $100\%$ optimal)</font> and <font color="DeepPink">you can actually solve this in a reasonable amount of time</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">$\frac {1}{1-\gamma}$ is not so just polynomial</font>  
>The whole convergence <font color="RosyBrown">might not be so just polynomial</font>, why?  The $\gamma$ in $\frac {1}{1-\gamma}$ is the key factor, <font color="RosyBrown">as $\gamma\rightarrow 1$, this blows up and that's not polynomial bounded</font>, say the number of bits it takes to write down $\gamma$.  
>
>$\Rightarrow$So, it's <font color="DeepPink">exponential</font> in terms of <font color="DeepPink">the number of bits</font> it takes to write down the whole problem.  
>
>$\Rightarrow$But even so, if you take <font color="OrangeRed">$\gamma$</font> to be some <font color="OrangeRed">fixed constant</font>, the <font color="DeepSkyBlue">$\frac {1}{1-\gamma}$</font> might be really big, but, it's some <font color="DeepSkyBlue">fixed constant</font> and we are polynomial in all the rest of $\vert S\vert$,$\vert A\vert$, $R_{max}=max_{S,A}R(S,A)$.  
>
>$\Rightarrow$This leads to an idea that <font color="DeepPink">once you fix an MDP model and the number of bits of precision $\gamma$, there is going to be some optimal action and there might be other actions that are tied for optimal in any given state</font>.  
>
>$\Rightarrow$One thing to be noted about <font color="OrangeRed">the second best action is going to be some bounded amount away from optimal</font>.  <font color="RosyBrown">It can't get any arbitrary close to optimal.</font>  It's going to be some distance away.  This says when we run value iteration <font color="OrangeRed">enough</font>, eventually, the <font color="OrangeRed">final</font> distance between the best action and the second best action gets bigger than this <font color="OrangeRed">original</font> gap.  
>&#10112;once it's bigger than this gap, then the greedy policy is going to be functioning work as <font color="DeepPink">optimal policy</font>.  
>&#10113;<font color="OrangeRed">it's going to start to choose the best action by optimal policy in all states</font>, maybe at this moment.  
>
>$\Rightarrow$<font color="#C20000">The greedy policy with respect to value iteration converges in a reasonable amount of time.</font>  

### The Largest Difference Between <font color="DeepPink">Optimal Policy</font> And <font color="00ADAD">Greedy Policy</font>: $max_{S}\vert V^{\pi_{V_{t}}}(S)-V^{\ast}(S)\vert$<$\frac {2\cdot\varepsilon\cdot\gamma}{1-\gamma}$
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The background</font>  
>if $\vert V_{t}(S)-V_{t+1}(S)\vert<\varepsilon$,  
>$\;\;\forall S$, then, $max_{S}\vert V^{\pi_{V_{t}}}(S)-V^{\ast}(S)\vert$<$\frac {2\cdot\varepsilon\cdot\gamma}{1-\gamma}$  
>
>Here is the assumption that    
>&#10112;we run value iteration and get a series of value functions, say $V_{t}$.  
>&#10113;the amount of changes of $V_{t}$, from $t$ to $t+1$, is less than $\varepsilon$ for all states $S$ in this MDP model.  
>
>Then, the <font color="OrangeRed">largest difference</font> between the <font color="DeepPink">optimal value function</font> $V^{\ast}(S)$ and the value function we get by taking the <font color="00ADAD">greedy policy</font> with respect to the value function at time $t$ is small, say $\frac {2\cdot\varepsilon\cdot\gamma}{1-\gamma}$.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Why end up being $\frac {2\cdot\varepsilon\cdot\gamma}{1-\gamma}$?</font>  
>&#10112;<font color="DeepSkyBlue">because this($\frac {1}{1-\gamma}$) little bit of $\varepsilon$</font> that we could be <font color="OrangeRed">off</font>, could be <font color="OrangeRed">magnified</font>, even every single step as we think about this into future.  That's why we get a $1-\gamma$ in the denominator.  
>&#10113;<font color="DeepSkyBlue">there exists $2$ sides of $\varepsilon$, positive and negative for each</font>, that's why we have $2$ times $\varepsilon$.  
>&#10114;suppose we are at $t$, <font color="RosyBrown">such change doesn't take place right now at $t$</font>, <font color="DeepSkyBlue">it takes one step further into $t+1$</font>, then we need to times $\gamma$.  
>
>If you have a good enough approximation of the value function, then you can at least put a <font color="OrangeRed">bound</font> on &#10112;how far off you are in terms of following the resulting <font color="00ADAD">greedy policy</font> value function $V^{\pi_{V_{t}}}(S)$ <font color="OrangeRed">from</font> &#10113;how far that is following the <font color="DeepPink">optimal policy</font> value function $V^{\ast}(S)$.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Should we need to know how closed we are to $V^{\ast}$?</font>  
>We <font color="RosyBrown">don't</font> even need to know how closed we are to $V^{\ast}$, <font color="OrangeRed">all we need is $\vert V_{t}(S)-V_{t+1}(S)\vert$<$\varepsilon$</font> for all $S$, that is <font color="OrangeRed">any two consecutive iteration</font> of value iteration:  
>&#10112;that just gives us a <font color="OrangeRed">bound</font> on what if we stops now and follow that policy $\pi_{V_{t}}$.  
>&#10113;<font color="RosyBrown">knowning that value iteration eventually converges in the limit of $\varepsilon$</font> is <font color="RosyBrown">not</font> so helpful, because <font color="RosyBrown">you don't know when the converges takes place</font>.  
>&#10114;<font color="#C20000">$max_{S}\vert V^{\pi_{V_{t}}}(S)-V^{\ast}(S)\vert$<$\frac {2\cdot\varepsilon\cdot\gamma}{1-\gamma}$ is telling us when is the decent time(right moment) to stop.</font>  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Pick up smaller $\gamma$</font>  
>If <font color="DeepPink">$\gamma$</font> is <font color="DeepPink">tiny</font>, then, <font color="DeepPink">$\frac {1}{1-\gamma}$</font> stays <font color="DeepPink">small</font>, <font color="DeepPink">$\frac {2\cdot\varepsilon\cdot\gamma}{1-\gamma}$</font> also stays <font color="DeepPink">small</font>.  It's all good.  
>&#10112;<font color="OrangeRed">the more closer $\gamma$ gets to $1$</font>, the <font color="OrangeRed">more problematic</font> your learning convergence would be.  
>&#10113;$\gamma$ tells you what your horizon is.  
>&#10114;<font color="#C20000">the smaller $\gamma$ puts small weight on the relation of next state to the current state, then the state convergence would not over too long a horizon.</font>  
>&#10115;<font color="OrangeRed">as $\gamma$ gets closer to $1$, $\frac {1}{1-\gamma}$ would just explodes</font>, it takes you to look ahead a lot further, it's a <font color="OrangeRed">harder</font> problem, since <font color="OrangeRed">it is over a longer horizon</font>.  
>
><font color="DeepPink">The smaller and larger $\gamma$ leads to a trade off between the horizon and the feasibility of solving a problem in a rreasonable amount of time.</font>  

### $\vert\vert B^{k}Q_{1}-B^{k}Q_{2}\vert\vert_{\infty}\leq\gamma^{k}\vert\vert Q_{1}-Q_{2}\vert\vert_{\infty}$
>if you start from with $Q_{1}$ and we run $k$ steps of value iteration, in other words, we apply the <font color="Red">Bellman operator</font> $k$ times, that is to say the $k$ step <font color="Red">Bellman operator</font> is a <font color="Red">contraction mapping</font>.  
>
>The <font color="OrangeRed">index of contraction</font> is just like <font color="OrangeRed">$\gamma$ raised to the $k$</font>, which is a <font color="OrangeRed">much much smaller</font> number.  
>  
>So running $k$ steps of value iterations actually makes your value functions much closer together than one single step value iteration.  
>
>Cautions must be made that <font color="OrangeRed">$\gamma$ raised to the $k$</font> is <font color="RosyBrown">not linear</font>, it's like gamma squared, gamma cubed, gamma to the $k$, that's the index of contraction.  So, if we run $10$ steps of value iteration, that's like running $1$ step in $10$ steps of value iteration, because the difference $<\frac {2\cdot\varepsilon\cdot\gamma}{1-\gamma}$ always holds.  
>
><font color="DeepPink">$\vert\vert B^{k}Q_{1}-B^{k}Q_{2}\vert\vert_{\infty}\leq\gamma^{k}\vert\vert Q_{1}-Q_{2}\vert\vert_{\infty}$</font> gives us a way of quantifying <font color="OrangeRed">how long we run value iteration</font> and connecting it with <font color="OrangeRed">how close you are to optimal</font> after you run <font color="OrangeRed">$k$ steps of value iteration</font>.  

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