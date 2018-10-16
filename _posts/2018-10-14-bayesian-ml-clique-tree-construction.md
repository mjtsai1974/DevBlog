---
layout: post
title: The Clique Tree Construction
---

## Prologue To The <font color="Red">Clique Tree</font> Construction
<p class="message">
The construction of <font color="Red">clique tree</font> aims at <font color="Red">minimal cliques</font> with none of them being the subsets of their neighbors, by using <font color="Red">VE(variable elimination) in moral graph</font>.
</p>

### <font color="OrangeRed">VE</font> Versus <font color="Red">Clique Tree Propagation</font>
>In my early post [Variable Elimination Order And Moral Graph]({{ site.github.repo }}{{ site.baseurl }}/2018/07/29/bayesian-ml-net-var-elim-order-moral/), we have explored how to query <font color="DeepSkyBlue">non-directly connected</font> variables in the <font color="Red">BN</font> by means of VE and have a clear mapping in the <font color="Red">MN</font>.  In advance to construct the <font color="Red">clique tree</font>, recap the VE and make comparison with <font color="Red">clique tree propagation</font>.  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Variable elimination</font>  
>&#10112;<font color="DeepSkyBlue">answers one query at a time</font>, for query of other variables, the whole VE must be proceeded.  
>&#10113;<font color="RosyBrown">delete non-queried</font> variables during VE process.  
>&#10114;<font color="RosyBrown">no</font> computation sharing among different queries.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Clique tree propagation</font>  
>&#10112;make posterior belief update for <font color="DeepPink">all</font> variables, inclusive of these <font color="DeepPink">un-observed</font> variables.  
>&#10113;delete <font color="DeepPink">no</font> any variable in the propagation of message passing.  
>&#10114;allows <font color="Red">computation sharing</font> among different queries.  
>
>Since <font color="Red">clique tree propagation</font> could be distributed on un-observed variables, empirical results suggest to use it when we'd like to make posteriro belief update on un-observed variables.  

### <font color="Red">Clique Tree</font> Construction Algorithm
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Target</font>  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Algorithm</font>  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Illustration by example</font>  
>

### Addendum
>&#10112;[Introduction to Bayesian Networks, Lecture 5: Inference as Message Propagation, Nevin L. Zhang, lzhang@cse.ust.hk, Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Fall 2008](http://www.cse.ust.hk/bnbook/pdf/l05.h.pdf)  

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