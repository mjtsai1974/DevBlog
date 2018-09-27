---
layout: post
title: The Bayesian Network Propagation And Clique Tree
---

## Prologue To The <font color="Red">Bayesian Network Propagation</font> And <font color="Red">Clique Tree</font>
<p class="message">
The introduction of <font color="Red">clique tree</font> algorithm aims at <font color="Red">posterior belief update</font> distributed in all variables of a network by means of <font color="Red">message propagation</font>.
</p>

### The <font color="Red">Clique Tree</font>
>A <font color="Red">clique tree</font> is an <font color="Red">undirected</font> tree, where:  
>&#10112;each node in the tree is a set of variables, called a <font color="Red">clique</font>.  
>&#10113;<font color="DeepPink">if one variable appears in 2 cliques, it must exist in all the cliques in the path between the 2 cliques</font>.  It is <font color="DeepPink">variable-connected</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-invalid.png "invalid")
>This is an <font color="RosyBrown">invalid</font> clique tree, variable B should exist in all the cliques in the path in between cliques of $(B,S)$ and $(R,D,B)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-valid.png "valid")
>This is a <font color="DeepPink">valid</font> clique tree, since it meets the criteria that a variable could be found on all cliques in the path between 2 cliques containing it.  
>
>A <font color="DeepSkyBlue">clique tree covers a Bayesian network</font> if below conditions are meet:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-bn.png "BN sample")
>&#10112;the union of the cliques is the set of the variables in the <font color="Red">Bayesian network</font>.  
>&#10113;for any variable $X$, the clique tree has one clique containing this variable with all its parent variables, such clique is called the <font color="OrangeRed">family cover clique</font> of $X$.  
>Suppose we are given above <font color="Red">Bayesian network</font>, below <font color="Red">clique tree</font> is just one such example.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-family-cover.png "valid")

### The <font color="Red">Clique Tree</font> For <font color="Red">Variable Elimination</font>
>Supposed we are given this <font color="Red">Bayesian network</font> and would like to make the posterior belief update of <font color="Red">all</font> variables based on the observed evidence.  This paragraph will guide you through the whole process by using the <font color="Red">clique tree</font>.  
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Initialize the cliques with independence probability distribution of BN variables</font>  
>For each variable $X$ in <font color="Red">Bayesian network</font>:  
>&#10112;find the probability of $P(X\vert Pa(X))$ and attach it onto the clique containing $X$.  
>&#10113;if the clique has no probability of independence attached, set it to the <font color="Green">identity</font> function.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-ve-step-1.png "step 1")
>Trivially, the multiplication of all functions on the clique tree is equivalent to the full joint probability distribution in the <font color="Red">Bayesian network</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Instantiate the variable with the observed evidence</font>  
>Using the same <font color="Red">Bayesian network</font>, we denote the observed evidence as $E$, <font color="OrangeRed">in the real world, we can have observation of multiple variables at the same time</font>.  
>Suppose we have observed $A=y$ and $X=y$, to instantiate the clique tree, we associate the independence probability function containing $A$ and $X$ with the observed value $y$.  
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