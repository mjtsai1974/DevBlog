---
layout: post
title: Propagation In The Bayesian Network
---

## Prologue To <font color="Red">Propagation</font> In The <font color="Red">Bayesian Network</font>
<p class="message">
The <font color="Red">respective</font> and <font color="Red">retrospective</font> inferences ascertained by means of <font color="Red">variable elimination</font> is also computation expensive, it works for one variable at a time, the same operation would be repeated upon new inference on other variables is requested.  
An alternative to overcome these limitations is by using <font color="Red">propagation</font> in the <font color="Red">Bayesian network</font>.  
</p>

### <font color="Red">Posterior Probability</font>(<font color="Red">Belief</font>) Update Upon New Evidence Arrives
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Posterior probability(belief)</font>  
>The <font color="Red">posterior probability</font>(<font color="Red">belief</font>) of a random variable $X$=$x$, given <font color="DeepSkyBlue">evidence</font> $E$=$e$, is expressed as $Bel(x)\overset\triangle=P(x\vert e)$.  The <font color="DeepSkyBlue">evidence</font> could be further classified as 2 distinct subsets:  
>&#10112;$e_{X}^{-}$ denotes the <font color="DeepSkyBlue">evidence</font> introduced through its children nodes.  
>&#10113;$e_{X}^{+}$ stands for the <font color="DeepSkyBlue">evidence</font> coming from its parent nodes, for $X$ to be a root node, $e_{X}^{+}$ is the background.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Deduction of $Bel(x)$</font>  
>Assume $e_{X}^{-}$ and $e_{X}^{+}$ are independent, then the <font color="Red">belief</font> of $X$=$x$:  
>$Bel(x)$  
>=$P(x\vert e_{X}^{-},e_{X}^{+})$  
>=$\frac {P(e_{X}^{-},x\vert e_{X}^{+})}{P(e_{X}^{-}\vert e_{X}^{+})}$  
>=$\frac {P(e_{X}^{-}\vert x,e_{X}^{+})\cdot P(x\vert e_{X}^{+})}{P(e_{X}^{-}\vert e_{X}^{+})}$  
>=$\frac {P(e_{X}^{-}\vert x)\cdot P(x\vert e_{X}^{+})}{P(e_{X}^{-})}$  
>
>Why we have such deduction?  
>&#10112;the <font color="DeepSkyBlue">evidence</font> $e_{X}^{-}$ is given by <font color="DeepSkyBlue">hypothesis</font> $X$=$x$, and the <font color="DeepSkyBlue">background context</font> $e_{X}^{+}$, that explains $P(e_{X}^{-}\vert x,e_{X}^{+})$.  
>&#10113;$P(x\vert e_{X}^{+})$ says that the <font color="DeepSkyBlue">hypothesis</font> $X$=$x$ is propagated from the <font color="DeepSkyBlue">background context</font> $e_{X}^{+}$.  
>&#10114;the <font color="OrangeRed">normalizing factor</font> $P(e_{X}^{-}\vert e_{X}^{+})$ <font color="DeepPink">encompasses everything ranging from the background context to the final observed evidence</font>, since $e_{X}^{-}$ and $e_{X}^{+}$ are independent, the denominator part becomes $P(e_{X}^{-})$.  
>$P(e_{X}^{-})$  
>=$P(e_{X}^{-}\vert e_{X}^{+})$  
>=$P(e_{X}^{-}\vert x,e_{X}^{+})\cdot P(x\vert e_{X}^{+})$  
>=$P(e_{X}^{-}\vert x)\cdot P(x\vert e_{X}^{+})$  
>=$\lambda(X)\cdot\pi(X)$  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Generalization of $Bel(x)$</font>  
>Most of the textbooks have below common definition:  
>&#10112;$\pi(x)$=$P(x\vert e_{X}^{+})$ is the respective(predictive) direction of propagation.  
>&#10113;$\lambda(x)$=$P(e_{X}^{-}\vert x)$ is retrospective(diagnostic) direction of propagation.  
>
>We thus express the belief of $x$ as $Bel(x)$=$\alpha\cdot\pi(x)\cdot\lambda(x)$,  
>where $\alpha$ is the normalizing constant, in this illustration,  
>$\alpha$  
>=$[P(e_{X}^{-})]^{-1}$  
>=$[\sum_{x}\pi(x)\cdot\lambda(x)]^{-1}$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-08-26-bayesian-ml-progagation-message-passing.png "propagation")
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Message passing is propagation</font>  
>New <font color="DeepSkyBlue">evidence</font> enters a network when a variable is instantiated, ie when it receives a new value from the outside world. When this happens, the <font color="Red">posterior probability</font> of each node in the whole network must be re-calculated.  
>
>This is achieved by <font color="DeepPink">message passing, known as progapation</font>.  

### <font color="Red">Propagation</font> Illustration In Causal Tree
>Given a causal tree of this serial chain <font color="Red">Bayesian network</font>, where $\lambda(Y)$=$P(e_{Y}^{-}\vert Y)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-08-26-bayesian-ml-progagation-causal-t.png "causal t propagate")
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Forward propagation</font>  
>&#10112;$W$ is now the root node, the <font color="DeepPink">background context is the only forward propagated evidence</font>.  
>$\pi(w)$=$P(w\vert e_{W}^{+})$=$P(w)$, for $w\in W$.  
>&#10113;for node $X$, it receives the forward propagated evidence pass through it, thus:  
>$\pi(x)$  
>=$P(x\vert e_{X}^{+})$  
>=$P(x\vert e_{WX}^{+})$  
>=$\sum_{w}P(x\vert w)\cdot P(w\vert e_{W}^{+})$, for $w\in W$.  
>$\Rightarrow\pi(X)$=$P(X\vert W)\cdot\pi(W)$  
><font color="DeepPink">Node $X$ receives $W$ forward propagated evidence $P(w\vert e_{W}^{+})$, with each $X=x$ weighted by $P(x\vert w)$ for all $w\in W$.</font>  
>&#10114;similarly, $\pi(Y)$=$P(Y\vert X)\cdot\pi(X)$  
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Backward propagation</font>  
>&#10112;$Y$ is the leaf node, the <font color="DeepPink">evidence of observation is the only backward propagated message</font>.  
>$\lambda(y)$=$P(e_{Y}^{-}\vert y)$  
>&#10113;as $X$ receives the backward propagated evidence from $Y$, then:  
>$\lambda(x)$  
>=$P(e_{X}^{-}\vert x)$  
>=$P(e_{XY}^{-}\vert x)$  
>=$\sum_{y}P(y\vert x)\cdot\lambda(y)$, for $y\in Y$.  
>$\Rightarrow\lambda(X)$=$P(Y\vert X)\cdot\lambda(Y)$  
><font color="DeepPink">For each $x\in X$, $\lambda(x)$ is weighted by $P(y\vert x)$ with $\lambda(y)$, for all $y\in Y$.</font>  
>&#10113;similarly, for node $W$,  
>$\lambda(w)$  
>=$P(e_{W}^{-}\vert w)$  
>=$P(e_{WX}^{-}\vert w)$  
>=$\sum_{x}P(x\vert w)\cdot\lambda(x)$  
>$\Rightarrow\lambda(W)$=$P(X\vert W)\cdot\lambda(X)$  

### <font color="Red">Propagation</font> Illustration In Multiple Child Nodes
>Now take a look at the illustration for the case of multiple child nodes.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-08-26-bayesian-ml-progagation-2-childs.png "2 childs")
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Backward propagation</font>  
>This time, we begin by inspecting the behavior in $\lambda$.  We have evidence on the subtree at node $X$ partitioned into 2 disjoint sets $e_{XY_{1}}^{-}$,$e_{XY_{2}}^{-}$.  
>&#10112;as $X$ receives backward propagated evidence from $Y_{1}$, $Y_{2}$, the backward propagation is in joint distribution form:  
>$\lambda(x)$...$x\in X$  
>=$P(e_{X}^{-}\vert x)$  
>=$P(e_{XY_{1}}^{-}\vert x)\cdot P(e_{XY_{2}}^{-}\vert x)$  
>=$\prod_{Y_{i}\in Y}P(e_{XY_{i}}^{-}\vert x)$...multiple $Y_{i}$ children  
>$\Rightarrow\lambda(x)$=$\lambda_{Y_{1}}(x)\cdot\lambda_{Y_{2}}(x)$  
>&#10113;as $X$ backward propagates the evidence to $W$:  
>$\lambda(w)$...$w\in W$  
>=$\sum_{x}P(x\vert w)\cdot\lambda(x)$  
>$\Rightarrow\lambda_{X}(W)$=$P(X\vert W)\cdot\lambda(X)$  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Forwardward propagation</font>  
>&#10112;as to the forward propagated evidence in node $X$, that's $\pi(X)$, we evaluate it from its parent node $W$.  
>$\pi(x)$...$x\in X$  
>=$P(x\vert e_{X}^{+})$  
>=$P(x\vert e_{WX}^{+})$  
>=$\sum_{w}P(x\vert w)\cdot\pi(w)$  
>$\Rightarrow\pi(X)$=$P(X\vert W)\cdot\pi(W)$  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Forwardward propagation to multiple descendent</font>  
>The forward propagated evidence in node $X$ would be taken into 2 distinct parts.  Consider the evidence forward propagated from $X$ to $Y_{1}$, it consists of 2 major factors:  
>&#10112;the forward propagated evidence from $W$.  
>&#10113;the backward propagated evidence from $Y_{2}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-08-26-bayesian-ml-progagation-2-childs-fwd-xy1.png "fwd xy1")
>The point is that the total forward propoagated evidence from $X$ to $Y_{2}$ is the joint probability function in combinatory format of these 2 factors.  
>$\pi_{Y_{1}}(x)$  
>=$P(x\vert e_{X}^{+},e_{Y_{2}}^{-})$  
>=$\frac {P(e_{Y_{2}}^{-}\vert x,e_{X}^{+})\cdot P(x\vert e_{X}^{+})}{P(e_{Y_{2}}^{-}\vert e_{X}^{+})}$  
>=$\frac {P(e_{Y_{2}}^{-}\vert x)\cdot P(x\vert e_{X}^{+})}{P(e_{Y_{2}}^{-}\vert e_{X}^{+})}$  
>, where $x\in X$ and $e_{Y_{2}}^{-}\in e_{X}^{-}$, more precisely, we can take $e_{Y_{2}}^{-}$=$e_{XY_ {2}}^{-}$, next to expand it.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Forwardward propagation to multiple descendent: extension</font>  
><font color="Brown">proof::mjtsai1974</font>  
>Continue from $\pi_{Y_{1}}(x)$:  
>&#10112;multiply nominator and denominator by $P(e_{Y_{1}}^{-}\vert x)$:  
>$\pi_{Y_{1}}(x)$  
>=$\frac {P(e_{Y_{2}}^{-}\vert x)\cdot P(x\vert e_{X}^{+})\cdot P(e_{Y_{1}}^{-}\vert x)}{P(e_{Y_{2}}^{-}\vert e_{X}^{+})\cdot P(e_{Y_{1}}^{-}\vert x)}$  
>&#10113;$P(e_{Y_{2}}^{-}\vert e_{X}^{+})$  
>=$\sum_{x}P(e_{Y_{2}}^{-}\vert x,e_{X}^{+})\cdot P(x\vert e_{X}^{+})$  
>=$\sum_{x}P(e_{Y_{2}}^{-}\vert x)\cdot P(x\vert e_{X}^{+})$  
>=$\alpha_{XY_{2}}^{-1}$  
>=$P(e_{XY_{2}}^{-})$...$e_{Y_{2}}^{-}$ and $e_{X}^{+}$ are independent  
>&#10114;we also have further deduction below for $P(e_{X}^{-})$:  
>$P(e_{Y_{2}}^{-}\vert e_{X}^{+})\cdot P(e_{Y_{1}}^{-}\vert x)$  
>=$\sum_{x}P(e_{Y_{2}}^{-}\vert x)\cdot P(x\vert e_{X}^{+})\cdot P(e_{Y_{1}}^{-}\vert x)$  
>=$P(e_{X}^{-})$  
>=$\alpha_{X}^{-1}$  
>&#10115;therefore, rewrite &#10112;:  
>$\pi_{Y_{1}}(x)$  
>=$P(x\vert e_{X}^{+},e_{Y_{2}}^{-})$  
>=$\frac {P(e_{Y_{2}}^{-}\vert x)\cdot P(x\vert e_{X}^{+})\cdot P(e_{Y_{1}}^{-}\vert x)}{P(e_{XY_{2}}^{-})\cdot P(e_{Y_{1}}^{-}\vert x)}$  
>=$\frac {P(e_{Y_{2}}^{-}\vert x)\cdot P(x\vert e_{X}^{+})\cdot P(e_{Y_{1}}^{-}\vert x)}{\alpha_{XY_{2}}^{-1}\cdot P(e_{Y_{1}}^{-}\vert x)}$  
>=$\frac {\alpha_{XY_{2}}\cdot P(e_{Y_{2}}^{-}\vert x)\cdot P(x\vert e_{X}^{+})\cdot P(e_{Y_{1}}^{-}\vert x)}{P(e_{Y_{1}}^{-}\vert x)}$  
>=$\frac {Bel_{Y_{1}}(x)}{\lambda_{Y_{1}}(x)}$  
>Here, we take $Bel_{Y_{1}}(x)$  
>=$\alpha_{XY_{2}}\cdot P(e_{Y_{2}}^{-}\vert x)\cdot P(x\vert e_{X}^{+})\cdot P(e_{Y_{1}}^{-}\vert x)$  
>
><font color="DeepSkyBlue">[5]</font>
><font color="OrangeRed">Forwardward propagation to multiple descendent: generalization</font>  
>Given that node $X$ has $n$ multiple child nodes $\\{Y_{1},...,Y_{n}\\}$, then, the forward propagated evidence from $X$ to $Y_{k}$ could be generalized in below expression:  
>$\pi_{Y_{k}}(x)$  
>=$\frac {Bel_{Y_{k}}(x)}{\lambda_{Y_{k}}(x)}$  
>, where $Bel_{Y_{k}}(x)$=$\alpha_{XY_{k}}\cdot\prod_{i\neq k} P(e_{Y_{i}}^{-}\vert x)\cdot P(x\vert e_{X}^{+})$  

### <font color="Red">Propagation</font> Illustration In Multiple Parent Nodes
>Causal polytree is the structure to be used in this section, each node might have multiple parents.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-08-26-bayesian-ml-progagation-causal-poly-t.png "caual poly tree")
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Forward propagation</font>  
>&#10112;the predictive support at $X$ comes from its 2 parents $W_{1}$, $W_{2}$.  
>$\pi(x)$...$x\in X$  
>=$P(x\vert e_{X}^{+})$  
>=$P(x\vert e_{W_{1}X}^{+},e_{W_{2}X}^{+})\cdot P(x\vert W_{1},W_{2})$  
>=$P(x\vert e_{W_{1}X}^{+})\cdot P(x\vert e_{W_{2}X}^{+})\cdot P(x\vert W_{1},W_{2})$  
>=$\sum_{w_{1}}\sum_{w_{2}}P(x\vert e_{W_{1}X}^{+})\cdot P(x\vert e_{W_{2}X}^{+})\cdot P(x\vert w_{1},w_{2})$  
>=$\sum_{w_{1}}\sum_{w_{2}}\pi_{W_{1}}(x)\cdot\pi_{W_{2}}(x)\cdot P(x\vert w_{1},w_{2})$  
>&#10113;the generalization of forward propagation at $X$ for $n$ parents:  
>$\pi(x)$=$\sum_{w_{1},...,w_{n}}\pi_{W_{1}}(x)\cdots\pi_{W_{n}}(x)\cdot P(x\vert w_{1},...,w_{n})$  
>&#10114;as the forward propagation from $X$ to one of its child, say $Y_{k}$, it will have to combine the forward propagation thus obtain above with the backward propagated evidence from $\\{Y_{1},...,Y_{k-1},Y_{k+1},...,,Y_{m}\\}$, suppose $X$ has $m$ multiple child nodes.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Backward propagation</font>  
>&#10112;the diagnostic support at $X$ comes from its 2 children $Y_{1}$, $Y_{2}$, where $\lambda(x)$=$\lambda_{Y_{1}}(x)\cdot\lambda_{Y_{2}}(x)$, must be splitted into 2 parts to be transfered to $W_{1}$, $W_{2}$, which are $\lambda_{X}(w_{1})$,$\lambda_{X}(w_{2})$.  
>&#10113;to diagnose in $W_{1}$ the symptom/evidence backward propagated from $X$:  
>$\lambda_{X}(w_{1})$  
>=$P(e_{W_{1}X}^{-}\vert W_{1})$  
>=$P(e_{X}^{-},e_{W_{2}X}^{+}\vert W_{1})$  
>=$P(e_{X}^{-}\vert W_{1})\cdot P(e_{W_{2}X}^{+}\vert W_{1})$  
>=$P(e_{X}^{-}\vert x)\cdot P(x\vert W_{1})\cdot P(e_{W_{2}X}^{+})$  
>=$P(e_{X}^{-}\vert x)\cdot P(x\vert W_{1},W_{2})\cdot S_{1}\cdot P(e_{W_{2}X}^{+})$  
>=$P(e_{X}^{-}\vert x)\cdot P(x\vert W_{1},W_{2})\cdot S_{2}\cdot P(W_{2}\vert e_{W_{2}X}^{+})$  
>=$P(e_{X}^{-}\vert x)\cdot P(x\vert W_{1},W_{2})\cdot\beta\cdot P(e_{W_{2}X}^{+}\vert W_{2})$  
>=$\beta\sum_{x}\lambda(x)\cdot\sum_{w_{2}}P(x\vert w_{1},w_{2})\cdot\pi_{W_{2}}(x)$  
>, where the $S_{1}$,$S_{2}$,$\beta$ are arbitrary constants to hold the equality.  We turn from $P(W_{2}\vert e_{W_{2}X}^{+})$ to $P(e_{W_{2}X}^{+}\vert W_{2})$ to express the deduction in terms of $\pi_{W_{2}}(x)$ for its simplicity.  
>&#10114;the generalization of $n$ multiple parents:  
>$\lambda_{X}(w_{i})$  
=$\beta\sum_{x}\lambda(x)$  
$\;\;\cdot\sum_{w_{k}:k\neq i}P(x\vert w_{1},...,w_{n})$  
$\;\;\cdot\prod_{k=1:k\neq i}^{n}\pi_{W_{k}}(x)$  
>
><font color="Red">[Cautions]</font>
>The belief updated by propagation would result in expensive computation consumption when there exists multiple parents.  The introduction of propagation aims to eliminate the potential expensive computation of NP-hard order in variable elimination, now it seems that it is struggling over.  Next to see the <font color="Red">clique tree</font> series, to be believed workable in a lot references.  

### Addendum
>&#10112;[A T utorial on Bayesian Belief Networks, Mark L Krieg, Surveillance Systems Division Electronics and Surveillance Research Laboratory, DSTO-TN-0403](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.124.2195&rep=rep1&type=pdf)  
>&#10113;[Lecture 4: Probability Propagation in Singly Connected Bayesian Networks, Duncan Fyfe Gillies, Department of Computing Imperial College London](https://www.doc.ic.ac.uk/~dfg/ProbabilisticInference/IDAPILecture04.pdf)  

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