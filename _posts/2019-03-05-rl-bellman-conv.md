---
layout: post
title: Bellman Operator Makes Convergence
---

## Prologue To The <font color="Red">Bellman Operator</font> Makes <font color="Red">Convergence</font>
<p class="message">
<font color="#C20000">By contiguous Bellman update, the value of each state eventually get converged, this happens a lot in reinforcement learning.</font>
</p>

### Begin By <font color="Red">Bellman Operator</font> - <font color="Red">B</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Beginning</font>  
>Let <font color="Red">B</font> be an operator, or mapping from value function to value function.  You give a <font color="Red">Q</font> function, the <font color="Red">Bellman operator</font> will give you back, possibly, a different <font color="Red">Q</font> function.  You can treat <font color="Red">B</font> a function from <font color="Red">Q</font> functions to <font color="Red">Q</font> functions.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Definition of Bellman operator</font>  
>$BQ$=$R(S,A)$+$\gamma\cdot{\textstyle\sum_{S'}}P(S'\vert S,A)\cdot max_{A'}Q(S',A')$
<!--
not working!!!!
>$[BQ](S,A)$  
>=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q(S',A')$...definition  
-->
>
>Give <font color="Red">B</font> a <font color="Red">Q</font> function, the new thing we get out when we apply <font color="Red">B</font> onto <font color="Red">Q</font>, has the property that at the state action pair $(S,A)$, it is equal to the <font color="#9300FF">immediate reward</font> plus the <font color="#D600D6">discounted expected value</font> of the <font color="OrangeRed">next state, $S'$</font>.  
>
>So, <font color="Red">Q</font> goes in, <font color="Red">BQ</font> goes out, treat <font color="Red">BQ</font> a <font color="DeepSkyBlue">new</font> function.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Another way of writing</font>  
>With <font color="Red">Bellman operator</font> - <font color="Red">B</font>, we can have below alternatives:  
>&#10112;$Q^{\ast}$=$BQ^{\ast}$ is another way of writing <font color="Red">Bellman equation</font>.  
>&#10113;$Q_{t}$=$BQ_{t-1}$ is another way of writing <font color="Red">value iteration</font>.  

### <font color="Red">Contraction Mapping</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Definition</font>  
>It happens a lot in reinforcement learning.  Take <font color="Red">B</font> to be an operator,  
>$\;\;$if for all $F$,$G$ and some $0\leq\gamma<1$,   
>$\;\;\vert\vert BF-BG\vert\vert_{\infty}\leq\gamma\cdot \vert\vert F-G\vert\vert_{\infty}$,  
>then <font color="Red">B</font> is <font color="Red">contraction mapping</font>, where  
>&#10112;$F$ and $G$ are value functions of <font color="Red">Q</font> form.  
>&#10113;$\vert\vert Q\vert\vert_{\infty}$=$max_{S,A}\vert Q(S,A)\vert$, this notation sometimes called the <font color="Orange">infinity form</font>, the <font color="Orange">max norm</font>.  
>&#10114;$\vert\vert F-G\vert\vert_{\infty}$ this means the biggest difference between $F$ and $G$.  
>
>The <font color="Red">contraction mapping</font> means whatever largest difference is, we are going to multiply it by something that makes it even <font color="OrangeRed">smaller</font>.  If you apply <font color="Red">B</font> onto $F$ and $G$, the distance between the resulting function is even <font color="OrangeRed">closer together</font> than they <font color="OrangeRed">started</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Hints</font>  
>It's the case that over time as we apply the <font color="Red">Bellman operator</font> - <font color="Red">B</font> over and over again, the state action pair where their maximum is, might change every time.  
>&#10112;$\vert\vert F-G\vert\vert_{\infty}$, this <font color="DeepSkyBlue">maximum norm</font> is computing for the specific value function of $F$ and $G$, where their <font color="OrangeRed">absolute difference</font> is given the <font color="OrangeRed">biggest</font>.   
>&#10113;$\vert\vert BF-BG\vert\vert_{\infty}$ is different from $\vert\vert F-G\vert\vert_{\infty}$ in that there is <font color="RosyBrown">no reason that $\vert\vert BF-BG\vert\vert_{\infty}$ needs to the the same over and over again</font>.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Properties</font>  
>If <font color="Red">B</font> is an operaton leads to <font color="Red">contraction mapping</font>:  
>&#10112;$F^{\ast}$=$BF^{\ast}$ has a <font color="DeepPink">unique</font> solution.  
>proof:  
>Suppose we have $F_{1}^{\ast}$=$BF^{\ast}$ and $F_{1}^{\ast}$=$BF^{\ast}$, then $F^{\ast}$=$F_{1}^{\ast}$=$F_{2}^{\ast}$ just holds to hvave the unique $F^{\ast}$.  
>
>&#10113;$F_{t}$=$BF_{t-1}$, this leads to $F_{t}\rightarrow F^{\ast}$, value iteration converges.  
><font color="Brown">proof::mjtsai1974</font> 
>Start from definition, we have:  
>$\vert\vert BF_{t-1}-BF^{\ast}\vert\vert_{\infty}\leq\gamma\cdot \vert\vert F_{t-1}-F^{\ast}\vert\vert_{\infty}$...[A]  
>$\Rightarrow \vert\vert F_{t}-F^{\ast}\vert\vert_{\infty}\leq\gamma\cdot \vert\vert F_{t-1}-F^{\ast}\vert\vert_{\infty}$  
>
>By <font color="DeepSkyBlue">mathematics induction</font>, below deduction holds:  
>$\vert\vert BF_{t}-BF^{\ast}\vert\vert_{\infty}\leq\gamma\cdot \vert\vert F_{t}-F^{\ast}\vert\vert_{\infty}\leq\gamma^{2}\cdot \vert\vert F_{t-1}-F^{\ast}\vert\vert_{\infty}$...[B]  
>
>Next, substract [B] from [A], we get:  
>$\vert\vert BF_{t-1}-BF_{t}\vert\vert_{\infty}\leq\gamma\cdot(1-\gamma)\cdot\vert\vert F_{t-1}-F^{\ast}\vert\vert_{\infty}$  
>$\Rightarrow\vert\vert BF_{t-1}-BF_{t+1}\vert\vert_{\infty}\leq\gamma\cdot(1-\gamma^{2})\cdot\vert\vert F_{t-1}-F^{\ast}\vert\vert_{\infty}$  
>$\Rightarrow\vert\vert BF_{t-1}-BF_{t+2}\vert\vert_{\infty}\leq\gamma\cdot(1-\gamma^{3})\cdot\vert\vert F_{t-1}-F^{\ast}\vert\vert_{\infty}$  
>...  
>$\Rightarrow\vert\vert BF_{t-1}-BF_{t+n}\vert\vert_{\infty}\leq\gamma\cdot(1-\gamma^{n+1})\cdot\vert\vert F_{t-1}-F^{\ast}\vert\vert_{\infty}$  
>
>We can tell that the <font color="OrangeRed">first</font> difference term will become <font color="OrangeRed">stable</font> with respect to each transition in $t$, $t+1$,..., the vaule of $F$ just converges to $F^{\ast}$.  As $n\rightarrow\infty$, we have $\gamma\cdot(1-\gamma^{n})\rightarrow \gamma$, for $\gamma<1$just holds.  
>
>If $F$ is evaluated from $t-1$, after $n\rightarrow\infty$, it will just converge to $F^{\ast}$ with the acceptable difference <font color="RosyBrown">no</font> more than $\gamma$ times the difference between the original departuring $F_{t-1}$ and the final expected $F^{\ast}$.  

### <font color="DeepPink">The Bellman Operator Contracts</font>: The Proof
>Given $Q_{1}$ and $Q_{2}$, then $\vert\vert BQ_1-BQ_2\vert\vert_\infty\leq\gamma\cdot\vert\vert Q_1-Q_2\vert\vert_\infty$, this says that after we apply <font color="Red">B</font> onto $Q_{1}$ and $Q_{2}$, the distance between them is less than or equal to $\gamma$ times the original difference betwen them before we apply it.  
>
>So, by applying the <font color="Red">Bellman operator</font>, we move these 2 $Q$ functions <font color="Red">closer</font> together.  
>
>In this section, we are going to prove the definition of <font color="Red">contraction mapping</font> by <font color="Red">B</font>.  
>
>proof:  
>&#10112;when we apply <font color="Red">B</font> onto $Q$:  
>$\lbrack BQ\rbrack(S,A)$=$R(SA)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q(S',A')$  
>&#10113;the next thing is to unpack the definition of the <font color="Orange">max norm</font>.  
>$\vert\vert BQ_{1}-BQ_{2}\vert\vert_{\infty}$  
>=$max_{S,A}\vert BQ_{1}(S,A)-BQ_{2}(S,A)\vert$  
>...we are going to maximize over all state action pair  
>=$max_{S,A}\vert R(S,A)+\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A_{Q_{1}}'}Q_{1}(S',A_{Q_{1}}')$  
>$\;\;$-$R(S,A)-\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A_{Q_{2}}'}Q_{2}(S',A_{Q_{2}}')\vert$  
>=$max_{S,A}\vert \gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A_{Q_{1}}'}Q_{1}(S',A_{Q_{1}}')$  
>$\;\;$-$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A_{Q_{2}}'}Q_{2}(S',A_{Q_{2}}')\vert$  
>=$max_{S,A}\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot\vert max_{A_{Q_{1}}'}Q_{1}(S',A_{Q_{1}}')$  
>$\;\;$-$max_{A_{Q_{2}}'}Q_{2}(S',A_{Q_{2}}')\vert$  
>$\leq \gamma\cdot max_{S'}\vert max_{A_{Q_{1}}'}Q_{1}(S',A_{Q_{1}}')$  
>$\;\;$-$max_{A_{Q_{2}}'}Q_{2}(S',A_{Q_{2}}')\vert$  
>=$\gamma\cdot max_{S',A_{Q_{1}}',A_{Q_{2}}'}\vert Q_{1}(S',A_{Q_{1}}')$-$Q_{2}(S',A_{Q_{2}}')\vert$  
>
>By tossing out the <font color="OrangeRed">weight combination</font>, the term <font color="OrangeRed">$\sum_{S'}P(S'\vert S,A)$</font> of $Q$ values, <font color="DeepSkyBlue">we just worry about the $S'$, where the difference is the largest</font>, <font color="DeepPink">the weighted average or the convex combination could not be larger than the biggest difference at any $S'$</font>, therefore, <font color="RosyBrown">no</font> need to keep $max_{S,A}$.  
>
>&#10114;$\vert\vert BQ_1-BQ_2\vert\vert_\infty\leq\gamma\cdot\vert\vert Q_1-Q_2\vert\vert_\infty$ is thus proved.  

<!--
>As we can tell that the first difference term $||BF_{t-1}-BF_{t}||\infty$ will become smaller with respect to each transition in $t$, $t+1$,..., the vaule of $F$ just converges to $F^{\ast}$.  
-->

<!--
>If $F_{1}^{\ast}\neq F_{2}^{\ast}$, we could <font color="RosyBrown">not</font> get $||BF-BG||\infty$ smaller or converge, <font color="RosyBrown">no</font> way to get $F_{1}^{\ast}$ and $F_{2}^{\ast}$ closer.  
-->

### <font color="DeepPink">Maximum Is Non-Expansion</font>
>For all $f$ and $g$, we have:  
>$\vert max_{a}f(a)-max_{a}g(a)\vert\leq max_{a}\vert f(a)-g(a)\vert$  
>
>proof:  
>$\Rightarrow$Suppose we have below maximum argument holds:  
>&#10112;$maxarg_{a}f(a)$=$a_{1}$  
>&#10113;$maxarg_{a}g(a)$=$a_{2}$    
>And, we assume $f(a_{1})\geq g(a_{2})$, this assumption owuld not lose generality in this proof, we can also prove with the assumption $f(a_{1})\leq g(a_{2})$.  
>
>$\Rightarrow$since $maxarg_{a}g(a)$=$a_{2}$, we have $g(a_{2})\geq g(a_{1})$  
>
>$\Rightarrow\vert max_{a}f(a)-max_{a}g(a)\vert$  
>=$f(a_{1})-g(a_{2})$  
>$\leq f(a_{1})-g(a_{1})$  
>=$max_{a}\vert f(a)-g(a)\vert$  

>!--
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
<!-- \left\|?\right\| => ||?||-->
<!-- \left|?\right| => |?|-->
<!-- \lbrack BQ\rbrack => [BQ] -->

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