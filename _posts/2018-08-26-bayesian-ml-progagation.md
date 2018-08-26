---
layout: post
title: Propagation In The Bayesian Network
---

## Prologue To <font color="Red">Propagation</font> In The <font color="Red">Bayesian Network</font>
<p class="message">
The <font color="Red">respective</font> and <font color="Red">retrospective</font> inferences are ascertained by means of <font color="Red">variable elimination</font> is also computation expensive, it works for one variable at a time, the same operation would be repeated upon new inference on other variables is requested.  
An alternative to overcome these limitations is by using <font color="Red">propagation</font> in the <font color="Red">Bayesian network</font>.  
</p>

<!--
### Posterior Probability(Belief) Update Upon New Evidence
>

p.13, "bayesian network tutorial"
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.124.2195&rep=rep1&type=pdf

New evidence enters a network when a variable is instantiated, ie when it receives a new value from the outside
world. When this happens the posterior probabilities of each node in the whole network must be re-calculated.
This is achieved by message passing.

p.5
https://www.doc.ic.ac.uk/~dfg/ProbabilisticInference/IDAPILecture04.pdf
-->


<!-- 
### Addendum
>&#10112;[Variable elimination, CS228, Stefano Ermon ](http://kuleshov.github.io/cs228-notes/inference/ve/)  
>&#10113;[Probabilistic graphical models, David Sontag, New York University, Lecture 2, February 2, 2012](http://people.csail.mit.edu/dsontag/courses/pgm12/slides/lecture2.pdf)  
>&#10114;[Bayesian networks and decision graphs, F.V.Jensen, Springer-Verlag New York, 2001](https://pdfs.semanticscholar.org/presentation/22b4/97a5431e961792e5c46d6348e92b362d378b.pdf)  
>&#10115;[Probabilistic graphical models, Raquel Urtasun and Tamir Hazan, TTI Chicago, April 4, 2011](https://www.cs.toronto.edu/~urtasun/courses/GraphicalModels/lecture4.pdf)  
>&#10116;[From Bayesian networks to Markov networks, Sargur Srihari](https://cedar.buffalo.edu/~srihari/CSE574/Chap8/8.7-FromBNtoMN.pdf)  
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