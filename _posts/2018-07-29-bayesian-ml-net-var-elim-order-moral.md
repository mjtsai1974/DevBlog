---
layout: post
title: Variable Elimination Order And Moral Graph
---

## Prologue To <font color="Red">Variable Elimination Order</font> And <font color="Red">Moral Graph</font>
<p class="message">
The <font color="Red">Bayesian network</font> is a DAG(directed acyclic graph), while the <font color="Red">moral graph</font> is an <font color="DeepSkyBlue">undirected</font> version, also known as the <font color="Red">Markov network</font>.  
The <font color="Red">moral graph</font> could facilitate the explanation of the <font color="DeepSkyBlue">factorization</font> in <font color="Red">variable elimination</font> process and its <font color="Red">order</font>.  
</p>

### <font color="Red">Moral Graph</font> Of A <font color="Red">BN</font>(<font color="Red">Bayesian Network</font>)
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

### <font color="Red">I-Map</font>(<font color="Red">Independence Map</font>)
><font color="DeepSkyBlue">[Definition]</font>  
>Given below 2 prerequisites:  
>&#10112;let $I(G)$ be the set of all conditional independences implied by the DAG, said $G$.  
>&#10113;let $I(P)$ be the set of all conditional independences that holds for or belongs to the joint probability distributiuon, said $P$.  
>
>We define <font color="#C20000">the DAG $G$ is an I-Map of a distribution $P$, if $I(G)\subseteq I(P)$</font>.  
>
><font color="DeepSkyBlue">[Full connected DAG]</font>  
>A fully connected DAG $G$ is an I-Map for any probability distribution, since:  
>$I(G)$=$\varnothing\subseteq I(P)$ for all $P$  
>
><font color="DeepSkyBlue">[Minimal I-Map]</font>  
>$G$ is a minimal I-Map for P, if any removal of a single edge makes it not an I-Map.  
>&#10112;a joint probability distributrion might have multiple minimal I-Maps.  
>&#10113;each corresponds to a specific node-ordering.  
>
><font color="DeepSkyBlue">[Perfect map]</font>  
>For <font color="DeepSkyBlue">$I(G)$=$I(P)$</font>, we say $G$ is a <font color="Red">perfect map</font> for $P$.  
>
>This section could be found at [Probabilistic graphical models, David Sontag, New York University, Lecture 2, February 2, 2012, p.5](http://people.csail.mit.edu/dsontag/courses/pgm12/slides/lecture2.pdf)  

### Concept Of <font color="Red">Potentials</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">What is a potential?</font>  
>A <font color="Red">potential</font> $\phi_{\chi}$ over a set of random variables $\chi$ is a function that maps each combination of configurations to a <font color="DeepSkyBlue">non-negative real number</font>.  
>
>The <font color="DeepSkyBlue">conditional</font> probability distribution, <font color="DeepSkyBlue">joint</font> probability distribution are all the special cases of <font color="Red">potential</font>.  The domain of a <font color="Red">potential</font> $\chi$ is denoted as:  
>$dom(\phi_{\chi})$=$\chi$  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Moralizing and domain graph</font>  
>Let $\phi$=$\\{\phi_{1},\phi_{2},...,\phi_{n}\\}$ to be the <font color="Red">potentials</font> over a set of random variables, $\chi$=$\\{X_{1},...,X_{m}\\}$, and with its domain distributed as $dim(\phi_{i})$=$D_{i}$.  
>&#10112;the <font color="Red">domain graph</font> for $\phi$ is the <font color="DeepSkyBlue">undirected graph</font> with random variables $X_{1}$,...,$X_{m}$ as nodes and <font color="DeepPink">link exists between node pairs belonging to the same domain</font>.  
>&#10113;it is also known as <font color="Red">moral graph</font>.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Potential and its domain </font>  
>Given that $\phi$=$\\{\phi_{1},...,\phi_{5}\\}$ is a set of <font color="Red">potentials</font> over $\\{X_{1},...,X_{5}\\}$, below graph exhibits the <font color="Red">potential</font> with respect to its <font color="Red">domain</font>:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-29-bayesian-ml-net-var-elim-order-moral-potential.png "potential")
>, where $\phi_{1}$=$P(X_{1})$,$\phi_{2}$=$P(X_{2}\vert X_{1})$,$\phi_{3}$=$P(X_{3}\vert X_{1})$,$\phi_{4}$=$P(X_{4}\vert X_{2},X_{3})$,$\phi_{5}$=$P(X_{5}\vert X_{4})$.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">The fill-ins</font>  
>In <font color="Red">variable elimination</font> process, <font color="DeepPink">the removal of one variable would possibly generate a new potential over a domain that didn't exist in the original domain graph, such new potential is the fill-in</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-29-bayesian-ml-net-var-elim-order-moral-fill-in.png "fill-in")
>The <font color="DeepSkyBlue">goal</font> of the most optimal <font color="Red">variable elimination</font> sequence is <font color="#C20000">to introduce no extra fill-ins</font>.  

### <font color="Red">Factorization</font> In <font color="Red">MN</font>(<font color="Red">Markov Network</font>)
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The full/joint PDF in MN</font>  
>Given below <font color="Red">MN</font>, base on our concept that potential is a CPD or a factor of joint distribution, then:  
>&#10112;$P(A,B,C,D)$...joint PDF  
=$\frac {1}{Z}\cdot\phi_{1}(A,B)\cdot\phi_{2}(B,C)\cdot\phi_{3}(C,D)\cdot\phi_{4}(D,A)$  
>&#10113;Z..<font color="OrangeRed">normalization</font> factor  
>=$\sum_{A,B,C,D}\phi_{1}(A,B)\cdot\phi_{2}(B,C)\cdot\phi_{3}(C,D)\cdot\phi_{4}(D,A)$  
>also called the <font color="OrangeRed">partition function</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-29-bayesian-ml-net-var-elim-order-moral-mn-factor.png "MN-factor")
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Tight relation between factorization and independence</font>  
>$X\perp Y\vert Z$ iff $P(X,Y,Z)$=$\phi_{1}(X,Z)\cdot\phi_{2}(Y,Z)$,  
>then, $(A\perp C\vert D,B)$ and $(B\perp D\vert A,C)$.  
>
><font color="Brown">proof::mjtsai1974</font>  
>To show $(A\perp C\vert D,B)$'s independence:  
>&#10112;$P(A,C,D,B)$=$\psi_{1}(A,D,B)\cdot\psi_{2}(C,D,B)$  
>, where $\psi_{i}$ is the potential.  
>&#10113;for $\psi_{1}(A,D,B)$'s independence:  
>$B\perp D\vert A$  
>$\Leftrightarrow P(B,D,A)$=$\phi_{1}(B,A)\cdot\phi_{4}(D,A)$  
>&#10114;for $\psi_{2}(C,D,B)$'s independence:  
>$B\perp D\vert C$  
>$\Leftrightarrow P(B,D,C)$=$\phi_{2}(B,C)\cdot\phi_{3}(D,C)$  
>&#10115;$P(A,C,D,B)$  
>=$\phi_{1}(B,A)\cdot\phi_{2}(B,C)\cdot\phi_{3}(D,C)\cdot\phi_{4}(D,A)$  
>
>$(B\perp D\vert A,C)$'s independence could be proved in similar way.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Factors in MN</font>  
>A factor can below representations:  
>&#10112;a joint distribution over $D$ by defining $\phi(D)$.  
>&#10113;a CPD $P(X\vert D)$, by defining $\phi(X\cup D)$  
>
><font color="DeepPink">Factors in MN is a more symmetric parameterization that captures the affinities in between related random variables.</font>  

### The <font color="Red">Gibbs</font> Distribution For <font color="Red">BN</font> Versus <font color="Red">MN</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The Gibbs distribution</font>  
>A distribution $P_{\phi}$ is a <font color="Red">Gibbs</font> distribution if it parameterizes a set of factors $\phi(D_{1})$,...,$\phi(D_{m})$ in the expression:  
>$\;\;P_{\phi}(X_{1},...,X_{n})$=$\frac {1}{Z}\cdot\phi(D_{1})\cdot\cdots\cdot\phi(D_{m})$, where:  
>&#10112;$X_{1},...,X_{n}$ are the random variables, $\phi(D_{1}),...,\phi(D_{m})$ are the factors over <font color="Red">domains</font> grouped by the related variables and $D_{i}$'s are the <font color="Red">domains</font>.  
>&#10113;$Z$...<font color="OrangeRed">partition function</font>  
>=$\sum_{X_{1},...,X_{n}}\phi(D_{1})\cdot\cdots\cdot\phi(D_{m})$  
>&#10114;a factor is one contribution on the <font color="DeepSkyBlue">joint</font> operation in <font color="Red">variable elimination</font> process.  
>&#10115;a <font color="DeepPink">distribution $P_{\phi}$ with $\phi(D_{1})$,...,$\phi(D_{m})$ factorizes a Markov network if each $\phi_{i}$ is a complete subgraph</font> of it.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The independence in MN</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-29-bayesian-ml-net-var-elim-order-moral-bn-mn-serial.png "BN-MN-series")
>Given this network, we'd like to prove $A\perp C\vert B$ given $P(A,B,C)$=$\frac {1}{Z}\cdot\phi_{A,B}(A,B)\cdot\phi_{B,C}(B,C)$:  
><font color="Brown">proof::mjtsai1974</font>  
>&#10112;$P(a\vert c)$  
>=$\frac {P(a\cap c)}{P(c)}$  
>=$\frac {\sum_{b}P(a,b,c)}{\sum_{a,b}P(a,b,c)}$  
>=$\frac {\sum_{b}\phi_{A,B}(a,b)\cdot\phi_{B,C}(b,c)}{\sum_{a,b}\phi_{A,B}(a,b)\cdot\phi_{B,C}(b,c)}$  
>=$\frac {\phi_{A,C}(a,c)}{\phi_{C}(c)}$  
>It is evident $A$ is independent from $C$ and could be figured out by factors of $A$ and $C$.  
>&#10113;$P(a\vert b)$  
>=$\frac {\sum_{c}P(a,b,c)}{\sum_{a,c}P(a,b,c)}$  
>=$\frac {\sum_{c}\phi_{A,B}(a,b)\cdot\phi_{B,C}(b,c)}{\sum_{a,c}\phi_{A,B}(a,b)\cdot\phi_{B,C}(b,c)}$  
>=$\frac {\phi_{A,B}(a,b)\cdot\sum_{c}\phi_{B,C}(b,c)}{\sum_{a}\phi_{A,B}(a,b)\cdot\sum_{c}\phi_{B,C}(b,c)}$  
>=$\frac {\phi_{A,B}(a,b)}{\sum_{a}\phi_{A,B}(a,b)}$  
>It is evident that the relationship of $A$ and $B$ is estimated by only factor of $A$ and $B$.  
>&#10114;$P(a,c\vert b)$  
>=$\frac {P(a,b,c)}{P(b)}$  
>=$\frac {\phi_{A,B}(a,b)\cdot\phi_{B,C}(b,c)}{\sum_{a,c}\phi_{A,B}(a,b)\cdot\phi_{B,C}(b,c)}$  
>=$\frac {\phi_{A,B}(a,b)\cdot\phi_{B,C}(b,c)}{\sum_{a}\phi_{A,B}(a,b)\cdot\sum_{c}\phi_{B,C}(b,c)}$  
>=$\frac {\phi_{A,B}(a,b)}{\sum_{a}\phi_{A,B}(a,b)}\cdot\frac {\phi_{B,C}(b,c)}{\sum_{c}\phi_{B,C}(b,c)}$  
>=$P(a\vert b)\cdot P(c\vert b)$  
>This evidence is more confident in our deduction result!!  By &#10112;, &#10113;, we can conclude that <font color="DeepPink">the probability of a variable conditioned on its Markov blanket depends only on potentials involving that node</font>.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">BN with evidence is Gibbs in MN</font>  
>&#10112;suppose you are given a <font color="Red">Bayesian network</font> over $\chi$=$\\{A,B,C,D,E\\}$ illustrated in this graph, where we have the full joint PDF as:  
>$P_{\chi}(A,B,C,D,E)$  
>=$P(E\vert C)\cdot P(D\vert B,C)$  
>$\;\;\cdot P(B\vert A)\cdot P(C\vert A)\cdot P(A)$  
>&#10113;given the observation of $e$ on node $E$, then:  
>$P(a,b,c,d\vert E=e)$  
>=$\frac {P(a\cap b\cap c\cap d\cap e)}{P(e)}$  
>=$\frac {P(e\vert c)\cdot P(d\vert b,c)\cdot P(b\vert a)\cdot P(c\vert a)\cdot P(a)}{\sum_{A,B,C,D}P(A,B,C,D,e)}$  
>Evidently, this is a <font color="Red">Gibbs</font> distribution!!  
>&#10114;we <font color="DeepSkyBlue">moralize</font> the BN by connecting nodes $B$ and $C$ for they are parents of node $D$, and we have potentials thus expressed:  
>$\phi_{\chi}(A,B,C,D,E)$  
>=$\frac {\phi_{A,B,C}(A,B,C)\cdot\phi_{B,C,D}(B,C,D)\cdot\phi_{C,E}(C,E)}{\sum_{A,B,C,D,E}\phi_{A,B,C}(A,B,C)\cdot\phi_{B,C,D}(B,C,D)\cdot\phi_{C,E}(C,E)}$  
>, where $\phi_{A,B,C}(A,B,C)$=$\phi_{A,B}(A,B)\cdot\phi_{A,C}(A,C)\cdot\phi_{A}(A)$  
>&#10115;given the observation of $e$ on node $E$, then:  
>$\phi(a,b,c,d\vert e)$  
>=$\frac {\phi_{\chi}(a,b,c,d,e)}{\phi(e)}$  
>=$\frac {\phi_{A,B,C}(a,b,c)\cdot\phi_{B,C,D}(b,c,d)\cdot\phi_{C,E}(c,e)}{\sum_{A,B,C,D}\phi_{A,B,C}(A,B,C)\cdot\phi_{B,C,D}(B,C,D)\cdot\phi_{C,E}(C,e)}$  
>Surprisingly, a <font color="Red">Gibbs</font> distribution again!!  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-29-bayesian-ml-net-var-elim-order-moral-gibbs-dist.png "Gibbs for BN-MN")
>We can conclude that <font color="DeepPink">any BN conditioned on evidence can be regarded as a Markov network</font>.  

### <font color="Red">Variable Elimination</font> From <font color="Red">BN</font> To <font color="Red">MN</font>
>Still using the same example in [Prof. Abbeel, steps through a few variable examples](https://www.youtube.com/watch?v=FDNB0A61PGE) for the illustration with a mapping of each step from <font color="Red">BN</font> to <font color="Red">MN</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-29-bayesian-ml-net-var-elim-order-moral-illustrate.png "VE BN-MN")
>To speed up the explanation, I use the optimal order of elimination: $W$,$Y$,$X$,$V$  
>&#10112;eliminate node $W$.  


### Addendum
>&#10112;[Variable elimination, CS228, Stefano Ermon ](http://kuleshov.github.io/cs228-notes/inference/ve/)  
>&#10113;[Probabilistic graphical models, David Sontag, New York University, Lecture 2, February 2, 2012](http://people.csail.mit.edu/dsontag/courses/pgm12/slides/lecture2.pdf)  
>&#10114;[Bayesian networks and decision graphs, F.V.Jensen, Springer-Verlag New York, 2001](https://pdfs.semanticscholar.org/presentation/22b4/97a5431e961792e5c46d6348e92b362d378b.pdf)  
>&#10115;[Probabilistic graphical models, Raquel Urtasun and Tamir Hazan, TTI Chicago, April 4, 2011](https://www.cs.toronto.edu/~urtasun/courses/GraphicalModels/lecture4.pdf)  
>&#10116;[From Bayesian networks to Markov networks, Sargur Srihari](https://cedar.buffalo.edu/~srihari/CSE574/Chap8/8.7-FromBNtoMN.pdf)  

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