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
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Incorporating the background context</font>  
>Below is an intuitive <font color="Red">Bayesian network</font>:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-11-bayesian-ml-net-profound-bayes-background.png "Bayes with C")
>We can deduce the posterior by incorporating the <font color="DeepSkyBlue">background context</font> in the <font color="Red">Bayes theorem</font> expression:  
>$\;\;P(H\vert E,C)$=$\frac {P(E\vert H,C)\cdot P(H\vert C)}{P(E\vert C)}$  
>
>&#10112;$C$, the <font color="DeepSkyBlue">background context</font>.  
>&#10113;$P(H\vert C)$, the <font color="Red">hypothesis</font> or <font color="Red">prior</font> term, based on the <font color="DeepSkyBlue">background context</font>.  
>&#10114;$P(E\vert H,C)$, the <font color="Red">likelihood</font> term, for the evidence, given the hypothesis and the <font color="DeepSkyBlue">background context</font>.  
>&#10115;$P(E\vert C)$, the <font color="Red">total probability</font> of evidence given the <font color="DeepSkyBlue">background context</font>, and is independent of the hypothesis.  It is the <font color="OrangeRed">normalizing</font> or <font color="OrangeRed">scaling</font> factor.  
>&#10116;$P(H\vert E,C)$, the <font color="Red">posterior</font> term, the belief in hypothesis given evidence and the <font color="DeepSkyBlue">background context</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Update probabilities of Bayesian network</font>  
>In my prior post [The Bayesian Inference Exploitation]({{ site.github.repo }}{{ site.baseurl }}/2018/06/17/bayesian-ml-bayesian-inf-exploit/), I have exploited the process to update the prior(hypothesis) from the posterior.  
>
>New information about one or more nodes in the network updates the probability distributions over the possible values of each node.  There are two ways in which information can propagate in a Bayesian network:  
>&#10112;<font color="DeepSkyBlue">predictive</font> propagation, it is straightforward, just by following the direction by the arrows.  Once new information changes the probability of a node, the node will pass the information to its children, which in turn pass to its children, and so on.  
>&#10113;<font color="DeepSkyBlue">retrospective</font> propagation, it is an inverse of <font color="DeepSkyBlue">predictive</font> propagation.  Under <font color="DeepSkyBlue">retrospective</font> propagation, when a node is updated, it will pass the information to its child node.  But, if it is updated from the childe node, the information is passed to its parent node, and in turn pass to its parent node, and so on.  
>
>You can think of the update of information from one node to another is <font color="DeepPink">simultaneous</font>(maybe <font color="DeepPink">atomic</font>), if one node has multiple children, or parents.  

### <font color="Red">Factorization</font> In <font color="Red">Bayesian Network</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Definition of DAG</font>  
>According to the [Introduction into Bayesian networks, p.6, Mgr. Libor Vaněk](http://www.fit.vutbr.cz/study/courses/VPD/public/0809VPD-Vanek.pdf), we can define DAG as $G$=$(V,E)$, $V$ for the <font color="DeepSkyBlue">set of indices to random variables</font>, $E$ for the <font color="DeepSkyBlue">edges</font>, and $X$=$\\{X_{v}: v\in V\\}$ to be the <font color="DeepSkyBlue">set of random variables indexed by $v$</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Factorization definition</font>  
>$X$ is a <font color="Red">Bayesian network</font> with respect to $G$, if the model's <font color="OrangeRed">full</font> joint probability density function could be expressed as a <font color="OrangeRed">product</font> of a series of the random variables' PDFs(probability density functions), with each PDF having its probability <font color="OrangeRed">conditionally depending on its parents</font>:  
>$\;\;P(X)$=$\prod_{v\in V}P(X_{v}\vert pa(X_{v}))$, where $pa(X_{v})$ is the <font color="OrangeRed">set of parents</font> of $X_{v}$.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Compare chain rule with conditional independence</font>  
>Suppose $X$ has $n$ nodes in its network:  
>&#10112;$P(X_{1}=x_{1},...,X_{n}=x_{n})$...by <font color="Red">chain rule</font>  
>=$\prod_{v=1}^{n}P(X_{v}=x_{v}\vert X_{v+1}=x_{v+1},...,X_{n}=x_{n})$  
>=$P(X_{1}=x_{1}\vert X_{2}=x_{2},...,X_{n}=x_{n})$  
>$\;\;\cdot P(X_{2}=x_{2}\vert X_{3}=x_{3},...,X_{n}=x_{n})$  
>$\;\;...$  
>$\;\;\cdot P(X_{n-1}=x_{n-1}\vert X_{n}=x_{n})$  
>&#10113;$P(X_{1}=x_{1},...,X_{n}=x_{n})$...by <font color="Red">factorization</font>  
>=$\prod_{v=1}^{n}P(X_{v}\vert (X_{i1},X_{i2},X_{i3},...))$  
>; where $pa(X_{v})$=$\\{X_{i1},X_{i2},X_{i3},...\\}$  
>
>These 2 expressions differ in that <font color="#C20000">the factorization of conditional independence for any descendant takes only its parents as the conditioning events</font>, as I have shown it in the section "The Joint Probability Distribution Of Bayesian Network" in [Introduction To The Bayesian Network]({{ site.github.repo }}{{ site.baseurl }}/2018/07/08/bayesian-ml-net-intro/).

### <font color="RoyalBlue">Example</font>: The Possible Causes To Computer Failure
>This is an example from [Bayesian networks, Michal Horný, Technical Report No. 5, April 18, 2014](https://www.bu.edu/sph/files/2014/05/bayesian-networks-final.pdf), which in turn simplified from Cowel et al, (1999).  This example is illustrated here provided that I have a full implementation and explaination with the consistent result.  
><font color="RoyalBlue">[Scene 1: the prior probability distribution, before evidence]</font>  
>We are given a question of infering the possible root cause of computer failure(M), suppose the experiment comes with two possible suspects, electricity failure(E), computer malfunction(M):  
>&#10112;the given prior, $P(E)$, $P(M)$ and the likelihoods of $P(C=t\vert E,M)$ are exhibited with the estimated probability for computer failure, $P(C)$ in below graph.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-11-bayesian-ml-net-profound-emc-prior.png "emc-prior")
>&#10113;$P(C=t)$  
>=$\sum_{E,M}P(C\vert E,M)\cdot P(E,M)$  
>=$\sum_{E,M}P(C\vert E,M)\cdot P(E)\cdot P(M)$  
>=$1\cdot 0.1\cdot 0.2$+$1\cdot 0.1\cdot 0.8$+$0\cdot 0.9\cdot 0.8$+$0.5\cdot 0.9\cdot 0.2$  
>=$0.02$+$0.08$+$0$+$0.09$  
>=$0.19$...the estimated probability of computer failure  
>
><font color="RoyalBlue">[Scene 2: the posterior probability distribution, after evidence]</font>  
>Assume we have been updated by the observation of physical computer failure, by the <font color="DeepSkyBlue">retrospective</font> propagation, we could <font color="DeepSkyBlue">infer</font> the possible root cause.  
>&#10112;$P(E=t\vert C=t)$  
>=$\sum_{M}P(E=t,M\vert C=t)$  
>=$\frac {\sum_{M}P(C=t\vert E=t,M)\cdot P(E=t)\cdot P(M)}{P(C=t)}$  
>=$\frac {1\cdot 0.1\cdot 0.2+1\cdot 0.1\cdot 0.8}{0.19}$  
>=$0.526315789$  
$\approx 0.53$  
>&#10113;$P(M=t\vert C=t)$  
>=$\sum_{E}P(M=t,E\vert C=t)$  
>=$\frac {\sum_{E}P(C=t\vert E,M=t)\cdot P(E)\cdot P(M=t)}{P(C=t)}$  
>=$\frac {1\cdot 0.1\cdot 0.2+0.5\cdot 0.9\cdot 0.2}{0.19}$  
>=$0.578947368$  
>$\approx 0.58$  

### Addendum
>&#10112;[Bayesian networks, Michal Horný, Technical Report No. 5, April 18, 2014](https://www.bu.edu/sph/files/2014/05/bayesian-networks-final.pdf)  
>&#10113;[Bayesian Networks, Ben-Gal Irad, in Ruggeri F., Faltin F. & Kenett R., Encyclopedia of Statistics in Quality & Reliability, Wiley & Sons (2007).](http://www.eng.tau.ac.il/~bengal/BN.pdf)  
>&#10114;[Introduction to discrete probability theory and Bayesian networks, Dr. Michael Ashcroft, September 15, 2011](https://www.it.uu.se/edu/course/homepage/ai/ht11/Lecture%20Notes%20BN.pdf)  
>&#10115;[Markov blanket](https://library.bayesia.com/display/FAQ/Markov+Blankets)  
>&#10116;[What are Bayesian belief networks?(part 1)](https://www.probabilisticworld.com/bayesian-belief-networks-part-1/)  
>&#10117;[Introduction into Bayesian networks, Mgr. Libor Vaněk](http://www.fit.vutbr.cz/study/courses/VPD/public/0809VPD-Vanek.pdf)  
>&#10118;Cowel R. G., Dawid A. P., Lauritzen S. L., Spiegelhalter D. J. (1999): Probabilistic Networks and Expert Systems. Springer-Verlag New York. ISBN 0-387-98767-3.

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