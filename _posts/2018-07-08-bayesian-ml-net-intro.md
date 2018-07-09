---
layout: post
title: Introduction To The Bayesian Network
---

## Prologue To Introduction To The <font color="Red">Bayesian Network</font>
<p class="message">
A <font color="Red">Bayesian network</font> is a model of a system, consisting of a number of random varaibles.  It provides much more information than simple classifier(like <font color="RosyBrown">neural networks</font>, <font color="RosyBrown">support vector machines</font>),  
when used, the <font color="Red">Bayesian network</font> comes out with <font color="#C20000">the probability distribution of the values of the random variable</font> to be predicted.  
</p>

### What is a <font color="Red">Bayesian Network</font>?
>We begin by a simple graph illustration:  
>&#10112;we can treat the it as <font color="DeepSkyBlue">a structured, graphical representation of probabilistic relationships between several random variables</font>.  
>&#10113;it explicitly encodes the <font color="Red">conditional independences</font> by the <font color="OrangeRed">missing arcs</font>.  
>&#10114;it can efficiently represent the joint PDF(probability distribution function) of the whole network or the combinatorial random variables in the model.  
>&#10115;it is a generative model, which allows arbitrary queries to be answered.   
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-08-bayesian-ml-net-intro-dag.png "bn")

### The <font color="Red">Conditional Independence</font> Relationship
>In my previous article [Introduction To The Conditional Probability]({{ site.github.repo }}{{ site.baseurl }}/2018/05/25/intro-cond-prob/), I have guided you through the <font color="DeepSkyBlue">conditional dependence</font>.  This article would then step into the field of <font color="Red">conditional independence</font>.  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Conditional independence axioms</font>  
>[Bayesian network tutorial, Mark L Krieg, p.3](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.124.2195&rep=rep1&type=pdf) brief describes the axiomatic basics for the conditional independence, which is in turn from the paper by Pearl, 1988.  
>
>Let $X$,$Y$,$Z$ denote any 3 distinct subsets of variables in the universe, called $U$.  We define $I(X,Y,Z)_p$ to represent the <font color="Red">conditional independence of $X$ from $Y$, given $Z$</font> in the probabilistic model $p$.  
>$\;\;I(X,Y,Z)_p$, iff $P(x\vert z,y)$=$P(x\vert z)$ and $P(y)>0$.  
>
>The following relationships holds:  
>&#10112;$I(X,Z,Y)_p$  
>$\Leftrightarrow P(x,y\vert z)$=$P(x\vert z)\cdot P(y\vert z)$  
>&#10113;$I(X,Z,Y)_p$  
>$\Leftrightarrow P(x,y,z)$=$P(x\vert z)\cdot P(y,z)$  
>&#10114;$I(X,Z,Y)_p$  
>$\Leftrightarrow\;\exists f,g: P(x,y,z)$=$f(x,z)\cdot g(y,z)$, where $f,g$ are arbitrary functions of conditional probability or joint probability.  
>
>Above 3 equilibrium are based on the model that $X$ is the descendent of $Z$, where $Y$ is some unrelated node to both $X$,$Z$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-08-bayesian-ml-net-intro-ci-axiom.png "ci axiom")
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">3 dependencies</font>  
>They could be treated as 3 types of connections in the <font color="Red">Bayesian network</font>, they are:  
>&#10112;<font color="Red">serial</font> connection, <font color="DeepPink">knowing $B$ makes $A$ and $C$ independent</font>, this is the <font color="#C20000">intermediate</font> cause.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-08-bayesian-ml-net-intro-serial-conn.png "serial connection")
>&#10113;<font color="Red">diverging</font> connection, <font color="DeepPink">knowing $B$ makes $A$ and $C$ independent</font>, this is the <font color="#C20000">common</font> cause.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-08-bayesian-ml-net-intro-diverg-conn.png "diverging connection")
>&#10114;<font color="Red">converging</font> connection, this is the <font color="#C20000">common effect</font>, <font color="DeepPink">not knowing $Y$ makes $X_{1}$,$X_{2}$,...,$X_{n}$ independent</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-08-bayesian-ml-net-intro-converg-conn.png "converging connection")

<!-- to be conti by 10.1.1.124.2195.pdf for conditional independence axioms -->
<!-- to be conti by Lecture12.pdf for conditional independence in Bayesian  networks, p.7 -->

### Addendum
>&#10112;[Bayesian network tutorial, Mark L Krieg](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.124.2195&rep=rep1&type=pdf)  

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


<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
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