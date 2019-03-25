---
layout: post
title: Bellman Operator And Convergence Properties
---

## Prologue To The <font color="Red">Bellman Operator</font> And <font color="Red">Convergence Properties</font>
<p class="message">
The <font color="Red">Bellman operator</font> of <font color="Red">contraction mapping</font> makes the <font color="OrangeRed">statement</font> of convergence concrete and come out the major properties.
</p>

### The Statement of Convergence
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The statement</font>  
>&#10112;let <font color="Red">B</font> be an operator of <font color="Red">contraction mapping</font>, and $Q^{\ast}$=$BQ^{\ast}$ be it's fixed point.  
>&#10113;let $Q_{0}$ be a $Q$ function, and define $Q_{t+1}$=$\lbrack B_{t}Q_{t}\rbrack Q_{t}$, then $Q_{t}\rightarrow Q^{\ast}$.  
>
>Suppose we have been given some sequence of $Q$ functions.  
>&#10112;it starts off with $Q_{0}$ and the way we're going <font color="DeepSkyBlue">to generate the next step from the previous step</font>, is that we are going to have a <font color="Green">new</font> kind of operator, $B_{t}$.  
>&#10113;$B_{t}$ is going to be applied to $Q_{t}$, producing an operator $\lbrack B_{t}Q_{t}\rbrack$ that we then apply to $Q_{t}$, and that's what we assign $Q_{t+1}$ to be.  
>
>So, in the context of $Q$ learning, this is essential the <font color="Red">$Q$ learning update</font>, there exists <font color="DeepSkyBlue">2 different $Q$ functions</font> that are used in the <font color="Red">$Q$ learning update</font>:  
>&#10112;one is the $Q_{t}$ function in $\lbrack B_{t}Q_{t}\rbrack$ that is used to <font color="DeepSkyBlue">average</font> together, to take care of the fact there is <font color="OrangeRed">noise</font> in the <font color="#8400E6">probabilistic transitions</font> of <font color="#EB00EB">stochasticity</font>.  
>&#10113;the other one is the $Q_{t}$ that we are using in the <font color="DeepSkyBlue">one step look ahead</font> as part of the <font color="Red">Bellman operation</font>.   
>
><font color="DeepSkyBlue">[2]</font>
><font color="Brown">Notes::mjtsai1974</font>  
>&#10112;we can treat the term $\lbrack B_{t}Q_{t}\rbrack$=$B_{t++}$, be noted that it is <font color="OrangeRed">$t$ plus plus</font>, <font color="RosyBrown">not $t+1$</font>.  
>&#10113;<font color="OrangeRed">$t$ plus plus</font> means that we starts from $t$, with some effort of plus plus to gain some reward maybe.  If we are from $t+1$, then we say $\lbrack B_{t+1}Q_{t+1}\rbrack$=$B_{(t+1)++}$.  
>&#10114;in the final fixed point of $Q^{\ast}$=$BQ^{\ast}$, the $B$ term is actually $B_{\ast}$.  

### The <font color="Red">Convergence Property 1</font>
>The cool thing is that this sequence of $Q$ functions, starting from any $Q_{0}$, by keeping applying $Q_{t+1}$=$\lbrack B_{t}Q_{t}\rbrack Q_{t}$, we're going to approach $Q^{\ast}$, as long as we have certain properties holding on how we define this $B_{t}$.  
>
>For all $U_{1}$,$U_{2}$, $S$, $A$:  
>$\;\;\vert(\lbrack B_{t}U_{1}\rbrack Q^{\ast})(S,A)-(\lbrack B_{t}U_{2}\rbrack Q^{\ast})(S,A)\vert$  
>$\;\;\leq(1-\alpha_{t}(S,A))\cdot\vert U_{1}(S,A)-U_{2}(S,A)\vert$  
>, where the littlecase <font color="OrangeRed">$t$</font> says that <font color="Red">$B$</font> is applied onto the <font color="OrangeRed">$t$-th</font> state's <font color="OrangeRed">current transition</font> to <font color="OrangeRed">next $t+1$ state</font>.  
>
><font color="Brown">proof::mjtsai1974</font>  
>$\Rightarrow$Recall that in [Bellman Operator Makes Convergence]({{ site.github.repo }}{{ site.baseurl }}/2019/03/05/rl-bellman-conv/):  
>$\;\;\lbrack BQ\rbrack(S,A)$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q(S',A')$  
>&#10112;if we take $Q^{\ast}$=$BQ^{\ast}$, this indicates that  
>$Q^{\ast}(S,A)$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q_{any}(S',A')$  
>, we can transite from any $Q$, the $Q_{any}$ to $Q^{\ast}$  
>, where $Q_{any}$=$\\{Q_{t},Q_{t+1},Q_{t+2},...Q^{\ast}\\}$  
>&#10113;therefore, we have it holds:  
>$Q_{t+1}(S,A)$=$R(S,A)$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q_{t}(S',A')$  
>
>$\Rightarrow\lbrack BQ\rbrack$ is a kind of operator, could be used to apply on $Q$.  By $TD(0)$, we can establish it:  
>$(\lbrack BQ_{T-1}\rbrack Q_{T-1})(S,A)$  
>=$Q_{T}(S,A)$  
>=$Q_{T-1}(S,A)$+$\alpha_{T}\cdot(R(S,A)$  
>$\;\;$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q_{T-1}(S',A')-Q_{T-1}(S,A))$  
>, where uppercase <font color="OrangeRed">$T$</font> stands for the <font color="OrangeRed">$T$-th eposide from state $S$ to state $S'$</font>.  
>
>$\Rightarrow$Take $(\lbrack BQ_{T-1}\rbrack Q_{T-1})(S,A)$'s first $Q_{T-1}$ term as $U_{1}$ and $U_{2}$, and have the second $Q_{T-1}$ term replaced by $Q^{\ast}$, then:  
>$\vert(\lbrack BU_{1}\rbrack Q^{\ast})(S,A)-(\lbrack BU_{2}\rbrack Q^{\ast})(S,A)\vert$  
>=$\vert\alpha_{U_{1}}\cdot(R(S,A)$  
>$\;\;$+$\gamma\cdot\sum_{S'}P_{U_{1}}(S'\vert S,A)\cdot max_{A'}Q^{\ast}(S',A')-Q^{\ast}(S,A))$  
>-$\alpha_{U_{2}}\cdot(R(S,A)$  
>$\;\;$+$\gamma\cdot\sum_{S'}P_{U_{2}}(S'\vert S,A)\cdot max_{A'}Q^{\ast}(S',A')-Q^{\ast}(S,A))\vert$  
>=$\vert\alpha_{U_{1}}\cdot D_{U_{1}}-\alpha_{U_{2}}\cdot D_{U_{2}}\vert$  
>, where the update term $D_{U_{i}}$, could be expressed as:  
>$R(S,A)$+$\gamma\cdot\sum_{S'}P_{U_{i}}(S'\vert S,A)\cdot max_{A'}Q^{\ast}(S',A')$-$Q^{\ast}(S,A))$  
>, and $i$=$1,2$ in this proof.  
>
>$\Rightarrow$Continue above deduction:  
>$\vert\alpha_{U_{1}}\cdot D_{U_{1}}-\alpha_{U_{2}}\cdot D_{U_{2}}\vert$  
>$\approx\vert(D_{U_{1}}-\frac {\alpha_{U_{2}}}{\alpha_{U_{1}}}\cdot D_{U_{2}})\vert\cdot\alpha_{U_{1}}$  
>$\leq\vert(1-\frac {\alpha_{U_{2}}}{\alpha_{U_{1}}})\cdot (D_{U_{1}}-D_{U_{2}})\vert\cdot\alpha_{U_{1}}$...[A]
>
>$\Rightarrow$Why it holds?  
>Because $(D_{U_{1}}-\frac {\alpha_{U_{2}}}{\alpha_{U_{1}}}\cdot D_{U_{2}})\leq(1-\frac {\alpha_{U_{2}}}{\alpha_{U_{1}}})\cdot (D_{U_{1}}-D_{U_{2}})$...[B]  
>$\Leftrightarrow$  
>$maxarg(D_{U_{1}})$=$1$  
>$maxarg(D_{U_{2}})$=$\frac {\alpha_{U_{2}}}{\alpha_{U_{1}}}$  
>$maxarg(D_{U_{1}}-D_{U_{2}})$=$1-\frac {\alpha_{U_{2}}}{\alpha_{U_{1}}}$  
>, it is the <font color="OrangeRed">maximum non-expansion</font>.  
>
>$\Rightarrow$Multiplying both side of [B] with $\alpha_{U_{1}}$ would we get [A], then:  
>&#10112;take $1-\alpha_{T}$=$(1-\frac {\alpha_{U_{2}}}{\alpha_{U_{1}}})\cdot\alpha_{U_{1}}$, we just get the inequality proved.    
>&#10113;take $T$=$t$, for we are evaluating the $t$-th transition by $T$-th eposide, then we get  
>$(1-\alpha_{t})\cdot (D_{U_{1}}-D_{U_{2}})$...[C]  
>&#10114;next, add the term $Q_{T-1}(S,A)$  
>$(1-\alpha_{t})\cdot (Q_{T-1}(S,A)+D_{U_{1}}-(Q_{T-1}(S,A)+D_{U_{2}}))$...[D]  
>, which is identical to [C].  
>
>$\Rightarrow$Finally, we establish this property:   
>$\;\;\vert(\lbrack B_{t}U_{1}\rbrack Q^{\ast})(S,A)-(\lbrack B_{t}U_{2}\rbrack Q^{\ast})(S,A)\vert$  
>$\;\;\leq(1-\alpha_{t}(S,A))\cdot\vert U_{1}(S,A)-U_{2}(S,A)\vert$  
>, in this proof we're expressing the distinct $U_{1}$ and $U_{2}$ in terms of <font color="OrangeRed">temporal difference</font> form:  
>$Q_{T}(S,A)$  
>=$Q_{T-1}(S,A)$+$\alpha_{T}\cdot(R(S,A)$  
>$\;\;$+$\gamma\cdot\sum_{S'}P(S'\vert S,A)\cdot max_{A'}Q_{T-1}(S',A')-Q_{T-1}(S,A))$  
>&#10112;<font color="OrangeRed">$T$ means the $U_{1}$, $U_{2}$ is evaluating in the $T$-th eposide for their state transition</font>.  
>&#10113;take $T$=$\\{T_{U_{1}}, T_{U_{2}}\\}$, <font color="DeepPink">if $T_{U_{1}}$=$T_{U_{2}}$, the proof just makes it right</font>; however, <font color="#C20000">the difference won't become larger even if $T_{U_{1}}\neq T_{U_{2}}$, and we keep on applying this Bellman operator oevr and oevr again!!!</font>  

### The <font color="Red">Convergence Property 2</font>
>For all $Q$,$U$,$S$,$A$:  
>$\;\;\vert(\lbrack B_{t}U\rbrack Q^{\ast})(S,A)-(\lbrack B_{t}U\rbrack Q)(S,A)\vert$  
>$\;\;\leq(\gamma\cdot\alpha_{t}(S,A))\cdot\vert Q^{\ast}(S,A)-Q(S,A)\vert$  
>, if we hold $U$ fixed, then we get the contraction of $Q$ toward $Q^{\ast}$, by applying $\lbrack B_{t}U\rbrack$ onto $Q^{\ast}$ and $Q$.  
>
><font color="Brown">proof::mjtsai1974</font>  
>

<!--
><font color="OrangeRed">[Property 2]</font>  
>
><font color="OrangeRed">[Property 3]</font>  
>
-->

### Addendum
>&#10112;[Convergence-1, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4436560172/concepts/44332503000923)  
>&#10113;[Convergence-2, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4436560172/concepts/44332503010923)  
>&#10114;[Convergence theorem explained-1, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4436560172/concepts/44332503020923)  
>&#10115;[Convergence theorem explained-2, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4436560172/concepts/44332503030923)  

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