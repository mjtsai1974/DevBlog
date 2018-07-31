---
layout: post
title: Variable Elimination Order And Moral Graph
---

## Prologue To <font color="Red">Variable Elimination Order</font> And <font color="Red">Moral Graph</font>
<p class="message">
The <font color="Red">Bayesian network</font> is a DAG(directed acyclic graph), while the <font color="Red">moral graph</font> is an <font color="DeepSkyBlue">undirected</font> version, also known as the <font color="Red">Markov network</font>.  
The <font color="Red">moral graph</font> could facilitate the explanation of the <font color="DeepSkyBlue">factorization</font> in <font color="Red">variable elimination</font> process and its <font color="Red">order</font>.  
</p>

### <font color="Red">Moral Graph</font> Of A <font color="Red">Bayesian Network</font>
><font color="OrangeRed">[The moralization algorithm]</font>  
>&#10112;<font color="DeepSkyBlue">drop the connectivity</font> in the original <font color="Red">Bayesian network</font>, that is to remove the arrow from the arc.  
>&#10113;<font color="DeepSkyBlue">connect the parents that shares a common child</font>, that is to <font color="DeepSkyBlue">marry</font> them.  
>
>The resulting <font color="DeepSkyBlue">undirected</font> graph is the <font color="Red">moral graph</font> of a <font color="Red">Bayesian network</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-29-bayesian-ml-net-var-elim-order-moral-mn.png "moralize")
><font color="#C20000">This undirected graph is also named Markov network.</font>  
>
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-29-bayesian-ml-net-var-elim-order-moral-factors.png "factor")
>The Markov network encodes the CPD in the Bayesian network as a factor of all related variables, like $P(E\vert B,C)$ is expressed in a factor form, $f(B,C,E)$, related variables in each distinct CDP are now be connected by an edge.  
>
><font color="RoyalBlue">[Question]</font>  
>Why we turn the CDP in the <font color="Red">Bayesian network</font> into the factorized form in the <font color="Red">Markov network</font>?  
><font color="DeepSkyBlue">[Answer]</font>  
>Because the moral graph is <font color="DeepSkyBlue">undirected</font>, it is <font color="RosyBrown">not</font> in <font color="RosyBrown">conditionally distributed</font>, rather than, in <font color="DeepPink">joint distributed</font>!!  

<!--
### <font color="Red">I-Map</font>(Independence Map)
p.5@http://people.csail.mit.edu/dsontag/courses/pgm12/slides/lecture2.pdf -->

<!--
### Factorization In Markov Network

potential
p.14@https://www.it.uu.se/edu/course/homepage/ai/ht11/Lecture%20Notes%20BN.pdf

the probability of a variable conditioned on its Markov
blanket depends only on potentials involving that node
p.31@http://people.csail.mit.edu/dsontag/courses/pgm12/slides/lecture2.pdf 

any BN conditioned on evidence can be regarded as a Markov network
p.6@https://cedar.buffalo.edu/~srihari/CSE574/Chap8/8.7-FromBNtoMN.pdf -->

### Addendum
>&#10112;[Variable elimination, CS228, Stefano Ermon ](http://kuleshov.github.io/cs228-notes/inference/ve/)  


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

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->