---
layout: post
title: Propagation In The Bayesian Network
---

## Prologue To <font color="Red">Propagation</font> In The <font color="Red">Bayesian Network</font>
<p class="message">
The <font color="Red">respective</font> and <font color="Red">retrospective</font> inferences are ascertained by means of <font color="Red">variable elimination</font> is also computation expensive, it works for one variable at a time, the same operation would be repeated upon new inference on other variables is requested.  
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
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Message passing is propagation</font>  
>New <font color="DeepSkyBlue">evidence</font> enters a network when a variable is instantiated, ie when it receives a new value from the outside world. When this happens, the <font color="Red">posterior probability</font> of each node in the whole network must be re-calculated.  
>This is achieved by <font color="DeepPink">message passing, known as progapation</font>.  

### <font color="Red">Propagation</font> Illustration In Causal Tree
>Given a causal tree of this serial chain <font color="Red">Bayesian network</font>, where $\lambda(Y)$=$P(e_{Y}^{-}\vert Y)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-08-26-bayesian-ml-progagation-causal-t.png "causal t propagate")
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Forward propagation</font>  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Backward propagation</font>  
>

<!-- 
### Addendum
>&#10112;[](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.124.2195&rep=rep1&type=pdf)  
>&#10113;[](https://www.doc.ic.ac.uk/~dfg/ProbabilisticInference/IDAPILecture04.pdf)  
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