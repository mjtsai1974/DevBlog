---
layout: post
title: Introduction To The Bayes Theorem
---

## Prologue To Introduction To <font color="Red">The Bayes Theorem</font>
<p class="message">
<font color="Red">The Bayes theorem</font> has been developed and evolved over time <font color="DeepPink">to enhance the accuracy of conditional probability prediction result</font>, especially, when you have only a few data gathered and would like to have a convincible, plausible result.
It could be pervasively found in the machine learning, reinforcement learning, wherein the POMDP transition probability is one such model.   
</p>

### Begin From The <font color="Red">Fundamental</font>
><font color="RoyalBlue">[1]</font>
><font color="OrangeRed">sample space</font>  
>&#10112;<font color="OrangeRed">sample space</font> is just the set of elements describing the outcomes of the test, experiment, formally, the result after execution of certain action.  
>In statistics reference text book, the letter $\Omega$ is most often used to represent the <font color="OrangeRed">sample space</font>.  
>&#10113;by flipping a coin one time, you will have two outcomes of head and tail, that is to say we associate the <font color="OrangeRed">sample space</font> with the set $\Omega$=$\\{H,T\\}$.  
>&#10114;to guess the birthday within one week, the <font color="OrangeRed">sample space</font> $\Omega$=$\\{Sun,Mon,Tue,Wed,Thu,Fri,Sat\\}$.  
>
><font color="RoyalBlue">[2]</font>
><font color="OrangeRed">event</font>  
>&#10112;subset of a sample space is treated as <font color="OrangeRed">event</font>.  
>&#10113;in the birthday in one week example, suppose we'd like to ask for the days with uppercase "S" as the prefix, then, we can denote $S$=$\\{Sun,Sat\\}$.  
>&#10114;suppose we'd like to ask for the days with uppercase "T" as the prefix, then, we can denote $T$=$\\{Tue,Thu\\}$.  
>
><font color="RoyalBlue">[3]</font>
><font color="OrangeRed">intersection, union, complement</font>  
>Suppose $A$ and $B$ are two events in the sample space $\Omega$.  
>&#10112;<font color="OrangeRed">intersection</font>, it's an event operator, denoted by $\cap$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-23-bayesian-ml-intro-intersection.png "intersection")
>&#10113;<font color="OrangeRed">union</font>, also an event operator, denoted by $\cup$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-23-bayesian-ml-intro-union.png "union")
>&#10113;<font color="OrangeRed">complement</font>, an event operator, usually denoted by lowercase $c$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-23-bayesian-ml-intro-complement.png "complement")
>
><font color="RoyalBlue">[4]</font>
><font color="OrangeRed">disjoint events</font>  
>Suppose $A$ and $B$ are two events in the sample space $\Omega$.  They are said to be <font color="DeepPink">two disjoint events if they have no intersection.  $A\cap B$=$0$</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-23-bayesian-ml-intro-disjoint.png "disjoint")
>Such events might be regarded as <font color="OrangeRed">mutually exclusive</font>.  

### The <font color="Red">Probability</font>
><font color="RoyalBlue">[1]</font>
><font color="OrangeRed">why do we need the probability?</font>  
>In order <font color="DeepSkyBlue">to express how likely it is that an event will occur</font>, during the experiment, by assigning probability to each <font color="DeepSkyBlue">distinct event</font> would be common.  To distribute the probability accurately would not be an easy task.  
>
><font color="RoyalBlue">[2]</font>
><font color="OrangeRed">the probability function</font>  
>Since each event would be associated with a probability, then we are in need of <font color="OrangeRed">the probability function</font>.  
>&#10112;the uppercase "P" is <font color="OrangeRed">the probability function</font> on a sample space $\Omega$ to assign the event $A$ in $\Omega$ a number $P(A)$ in $[0,1]$.  <font color="DeepSkyBlue">The number $P(A)$ is the probability of the occurrence of event $A$</font>.  
>&#10113;wherein $P(\Omega)$=$1$  
>&#10114;<font color="DeepPink">$P(A\cup B)$=$P(A)$+$P(B)$-$P(A\cap B)$</font>, where <font color="OrangeRed">$P(A\cap B)$=$0$</font> for $A$ and $B$ are <font color="OrangeRed">disjoint</font>. 
>If $A$,$B$,$C$ are disjoint events, then $P(A\cup B\cup C)$=$P(A)$+$P(B)$+$P(C)$.  
>
><font color="RoyalBlue">[3]</font>
><font color="DeepPink">the probability is defined on events, not on outcomes</font>  
>&#10112;tossing a coin one time would we have $\Omega$=$\\{H,T\\}$, then $P(\\{H\\})$=$\frac {1}{2}$, $P(\\{T\\})$=$\frac {1}{2}$, under the assumption that head and tail chances are coming to an equilibrium.  
>&#10113;given cards of read, blue, green colours.  The permutation of all the possible orders of cards would be $\Omega$=$\\{RGB$,$RBG$,$GRB$,$GBR$,$BRG$,$BGR\\}$.  
>$P(\\{RGB\\})$=$P(\\{RBG\\})$=$P(\\{GRB\\})$=$P(\\{GBR\\})$=$P(\\{BRG\\})$=$P(\\{BGR\\})$=$\frac {1}{6}$...the same probability for each distinct event.  
>&#10114;the same example as above, the probability of the event that green card is in the middle would be $P(\\{RGB,BGR\\})$=$\frac {1}{3}$.  
>The $\\{RGB,BGR\\}$ is such event we desire, wherein the $\\{RGB\\}$ and $\\{BGR\\}$ are the outcomes described by $\Omega$.  
>
><font color="RoyalBlue">[4]</font>
><font color="OrangeRed">additivity of probability</font>  
>&#10112;using the same card example, the probability of the event that green card is in the middle could be $P(\\{XGX\\})$=$P(\\{RGB\\})$+$P(\\{BGR\\})$=$\frac {1}{3}$.  
>This implies that <font color="DeepPink">the probability of an event could be obtained by summing over the probabilities of the outcomes belonging to the same event</font>.  
>&#10113;given $A$ is an event, then $P(A)$+$P(A^{c})$=$P(\Omega)$=$1$.  
>&#10114;if $A$, $B$ are <font color="OrangeRed">not</font> disjoint, then $A$=$(A\cap B)\cup(A\cap B^{c})$, this is a disjoint union.  
>Therefore, $P(A)$=$P(A\cap B)$+$P(A\cap B^{c})$.  

### <font color="Red">Product</font> Of Sample Space
><font color="RoyalBlue">[1]</font>
><font color="OrangeRed">run the same test over multiple times</font>  
>To justify the experiment result, one single test would be executed over multiple times.  
>&#10112;suppose we flip the same coin over 2 times, the sample space $\Omega$=$\\{H,T\\}$x$\\{H,T\\}$.  
>It is now $\Omega$=$\\{HH,HT,TH,TT\\}$.  Total 4 outcomes in it, we can take one outcome as one event, then $P(\\{HH\\})$=$P(\\{HT\\})$=$P(\\{TH\\})$=$P(\\{TT\\})$=$\frac {1}{4}$, under the assumption that $P(\\{H\\})$=$P(\\{T\\})$ in each single tossing of coin.  
>
><font color="RoyalBlue">[2]</font>
><font color="OrangeRed">combine the sample space from different tests</font>  
>&#10112;given that 2 sample spaces with respect to 2 different tests' outcomes, they are $\Omega_{1}$,$\Omega_{2}$, where sizeof($\Omega_{1}$)=$r$, sizeof($\Omega_{2}$)=$s$.  
>&#10112;then $\Omega$=$\Omega_{1}$x$\Omega_{2}$, sizeof($\Omega$)=$r\cdot s$.  If we treat each distinct combination in the sample space as one single event, the probability of such distinct event is <font color="OrangeRed">$\frac {1}{r\cdot s}$</font>.  The $\frac {1}{r}$,$\frac {1}{s}$ are the probability for the occurrences of outcomes in the $\Omega_{1}$ and $\Omega_{2}$ with respect to test 1 and test 2.  

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

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha, quiz, example</font> -->
<!-- <font color="Green">new alpha</font> -->

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

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->