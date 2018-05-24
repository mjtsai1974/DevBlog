---
layout: post
title: Introduction To The Bayes Theorem
---

## Prologue To Introduction To <font color="Red">The Bayes Theorem</font>
<p class="message">
<font color="Red">The Bayes theorem</font> has been developed and evolved over time <font color="DeepPink">to enhance the accuracy of conditional probability prediction result</font>, especially, when you have only a few data gathered and would like to have a convincible, plausible result.
It could be pervasively found in the machine learning, reinforcement learning, wherein the POMDP transition probability is one such model.   
</p>

### Begin From The <font color="Red">Foundamental Probability</font>
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