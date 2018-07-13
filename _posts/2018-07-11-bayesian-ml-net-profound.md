---
layout: post
title: The Bayesian Network Profound Meaning
---

## Prologue To The <font color="Red">Bayesian Network</font> Profound Meaning
<p class="message">
<font color="Red">Bayesian networks</font>(BNs), also known as <font color="Red">belief networks</font>(or Bayes nets for short), belong to the family of probabilistic graphical models(GMs), which are used to represent knowledge about an <font color="DeepSkyBlue">uncertain</font> domain.  
BNs combine principles from graph theory, probability theory, computer science, and statistics.  
</p>

### <font color="Red">Explaining Away</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Recap: d-separation</font>  
>Accordingly, when one set of random variables, $\Theta_{1}$, is conditionally independent of another, $\Theta_{2}$, given a third, $\Theta_{3}$, then we say that the random variables in $\Theta_{1}$ are d-separated from $\Theta_{2}$ by $\Theta_{3}$.  For the simplicity, you can treat each set containing only one random variable.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Illustration of explaining away</font>  
>Given that you got a headache, there exists more than a dozen of possible causes, the causal relationship is depicted below.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-11-bayesian-ml-net-profound-exp-away.png "explain away")
>&#10112;suppose the <font color="DeepSkyBlue">inferred</font> correct root cause to your headache is the nasal congestion.  
>&#10113;the possibility of the rest nodes to be the root cause is greatly reduced, said they has been <font color="Red">explained away</font>.  
>&#10114;given the evidence of a headache, some knowledge of food poisoning, caffeine, alcohol, faulty posture would be inferred from the state of nasal congestion and the observation of a headache.  
>&#10115;they are no longer d-separated, but d-connected.  Or they are <font color="Red">conditionally dependent</font> given a headache.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Conclusion</font>  
>D-connection in converging type networks requires some knowledge of the connection variable(the headache node in this example), at least one of the descendants, the observed evidence must have the positive or the negative information.  

### The <font color="Red">Markov Blanket</font> And <font color="Red">Markov Equivalence</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Markov blanket</font>  
>The <font color="Red">Markov blanket</font> claims <font color="#C20000">a node is conditionally independent(d-separated) from all of the other nodes(entire graph), given its parents, childs, child's parents.</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-11-bayesian-ml-net-profound-markov-blanket.png "Markov blanket")
>&#10112;in above graph, given nodes $C$, $D$, $E$, $F$, $G$, node $X$ is d-separated from all othere nodes, $A$, $B$, $H$, $I$, $J$.  
>&#10113;<font color="DeepPink">the parents, the children, other parents of a node's children are called the Markov blanket of a node</font>.  
>&#10114;therefore <font color="#C20000">Markov blanket contains all the variables that shields the target node from the rest of the network</font>.  This means that <font color="#C20000">the Markov blanket of a target node is the only knowledge needed to predict the behavior of that target node</font>.  
>
>Suppose we know the value of each node in the Markov blanket, if we'd like to predict the probability distribution of $X$, then there is <font color="#C20000">no</font> more information regarding to the value taken by the node $X$.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Markov equivalence</font>  
>Two DAGs are to be said <font color="Red">Markov equivalent</font>, if they have the same d-separations.  

### Prove The <font color="Red">Markov Blanket</font>
>A node is conditionally independent of all other nodes given its Markov blanket, i.e. its parents, its children, and parents of common children(spouses).  
>
><font color="Brown">proof::mjtsai1974</font>  
>By using the same DAG of Markov blanket:  
>&#10112;given target node's parent, the target node is conditionally independent from the parent's ascendant.  $X$ is d-separated from $A$, given $C$ or $D$.  
>&#10113;knowing $A$ could <font color="DeepSkyBlue">predict</font> $C$, then from $C$ to <font color="DeepSkyBlue">predict</font> $X$; knowing $X$ could <font color="DeepSkyBlue">infer</font> $C$, then from $C$ to <font color="DeepSkyBlue">infer</font> $A$.  But, knowing $X$ helps nothing in inferring $A$, if we already know $C$; knowing $A$ makes no prediction about $X$, if we already know $C$.  
>&#10114;given target node's children, the target node is conditionally independent from the children's descendants.  $X$ is d-separated from $H$, given $F$, and is d-separated from $I$, $J$, given $G$.  Similar in &#10112;.  
>&#10115;given target node's children, the children's parent, the target node would be <font color="Red">explained away</font>, the same for that children's parent, depends on the information on that children.  
>&#10116;continue on, given $E$, $G$ is d-separated from $B$, then $X$ is also d-separated from $B$.  
>
>Therefore, the <font color="Red">Markov blanket</font> contains everything we need to predict and infer the target node.  

### <font color="Red">Bayes Theorem</font> With <font color="DeepSkyBlue">Background Context</font>
>Below is an intuitive <font color="Red">Bayesian network</font>:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-11-bayesian-ml-net-profound-markov-blanket.png "Markov blanket")
>We can deduce the posterior by incorporating the <font color="DeepSkyBlue">background context</font> in the <font color="Red">Bayes theorem</font> expression:  
>$\;\;P(H\vert E,C)$=$\frac {P(E\vert H,C)\cdot P(H\vert C)}{P(E\vert C)}$  
>
>&#10112;$C$, the <font color="DeepSkyBlue">background context</font>.  
>&#10113;$P(H\vert C)$, the hypothesis or prior term, based on the <font color="DeepSkyBlue">background context</font>.  
>&#10114;$P(E\vert H,C)$, the likelihood term, for the evidence, given the hypothesis and the <font color="DeepSkyBlue">background context</font>.  
>&#10115;$P(E\vert C)$, the total probability of evidence given the <font color="DeepSkyBlue">background context</font>, and is independent of the hypothesis.  It is the <font color="OrangeRed">normalizing</font> or <font color="OrangeRed">scaling</font> factor.  
>&#10116;$P(H\vert E,C)$, the posterior term, the belief in hypothesis given evidence and the <font color="DeepSkyBlue">background context</font>.  

### Addendum
>&#10112;A Brief Introduction to Graphical Models and Bayesian Networks, Murphy K. (1998)  
>&#10113;[Bayesian networks, Michal Horný, Technical Report No. 5, April 18, 2014](http://people.math.aau.dk/~sorenh/misc/2014-useR-GMBN/bayesnet-slides.pdf)  
>&#10114;[Bayesian Networks, Ben-Gal Irad, in Ruggeri F., Faltin F. & Kenett R., Encyclopedia of Statistics in Quality & Reliability, Wiley & Sons (2007).](http://www.eng.tau.ac.il/~bengal/BN.pdf)  
>&#10115;[Introduction to discrete probability theory and Bayesian networks, Dr. Michael Ashcroft, September 15, 2011](https://www.it.uu.se/edu/course/homepage/ai/ht11/Lecture%20Notes%20BN.pdf)  
>&#10116;[Markov blanket](https://library.bayesia.com/display/FAQ/Markov+Blankets)  

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