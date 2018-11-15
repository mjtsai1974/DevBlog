---
layout: post
title: The Calibrated Clique Tree
---

## Prologue To The <font color="Red">Calibrated Clique Tree</font>
<p class="message">
The quantitative evaluation of messages from one clique to its adjacent clique and from this adjacent clique to itself would be a <font color="DeepPink">equilibrium</font> in a <font color="Red">calibrated clique tree</font>.
</p>

### Before We Go Any Farther
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Recap: variable-elimination constructed clique tree</font>  
>Remember that my prior post [The Clique Tree Construction]({{ site.github.repo }}{{ site.baseurl }}/2018/10/14/bayesian-ml-clique-tree-construction/) has proved that <font color="DeepPink">slight different and very different elimination order constructed clique tree makes the same propagation</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Recap: message passing in the clique tree</font>  
>Still in another prior post of mine, [The Bayesian Network Propagation And Clique Tree]({{ site.github.repo }}{{ site.baseurl }}/2018/09/25/bayesian-ml-progagation-cliuque-tree/):  
>&#10112;the message propagation in the <font color="Red">clique tree</font> is proceeded in two stage operations with the former the <font color="DeepSkyBlue">collection</font>(from leaf nodes to the pivot node) and the next is the <font color="DeepSkyBlue">distribution</font>(from pivot node to the leaf nodes).  
>&#10113;<font color="Red">computation sharing</font> in all queries that <font color="#C20000">the function of the message from the pivot to the leafs are all expressed in terms of the variables the same as it is in the clique from which passes message to the pivot</font>.  
>&#10114;given clique $C$ and $C'$ in adjacent, there exists $C_{i}$ for $i$=$1$ to $k$ to be $C$'s neighbors, $g_{i}$ is the message from $C_{i}$ to $C$, and $f_{j}$ is the $j$-th function attached to clique $C$, the message from $C$ to $C'$ is denoted as $H$, expressed as:  
>$H((C\cap C')-E)$=$\sum_{C\backslash C'\cup E}\prod_{i}g_{i}\prod_{j}f_{j}$, with $E$ to be the evidence.  
>
><font color="DeepPink">The summation over elements purely from $C$</font>, <font color="RosyBrown">not</font> belonging to $C'$ and $E$(evidence), then:  
>$H((C\cap C')-E)$=$\sum_{C\backslash C\cap C'}\prod_{i}g_{i}\prod_{j}f_{j}$ also holds!!
>The term $(C\cap C')-E$ illustrates that the message purely propagates from $C$ to $C'$, exclusive of the intermediate noise.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Notes</font>  
>The <font color="Red">clique tree</font> is also called a <font color="Red">junction tree</font> or a <font color="Red">join tree</font>.  

### Addendum
>&#10112;[Graphical Models - Lecture 11: Clique Trees, Andrew McCallum, mccallum@cs.umass.edu](https://people.cs.umass.edu/~mccallum/courses/gm2011/11-clique-trees.pdf)  

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