---
layout: post
title: The Bayes Theorem Significance
---

## Prologue To The <font color="Red">Bayes Theorem Significance</font>
<p class="message">
<font color="#C20000">The most optimized effect of Bayes theorem is to use already known probability to figure out the maximum unknown probability in its likelihood</font>, instead of manual counting in the sample space.  
The <font color="Red">Bayes theorem</font> is the weapon for <font color="DeepPink">quantative critical thinking</font> to overcome the drawback of <font color="RosyBrown">qualitative thinking</font> of human nature.  
</p>

### The <font color="Red">Bayes Theorem Significance</font>
>$\;\;\;\;P(B_{i}\vert A)$=$\frac {P(A\vert B_{i})\cdot P(B_{i})}{P(A\vert B_{1})\cdot P(B_{1})+...+P(A\vert B_{n})\cdot P(B_{n})}$  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The general form of Bayes theorem embedes a total probability expression in its denominator part.</font>  
>&#10112;such <font color="OrangeRed">total probability</font> is the <font color="DeepSkyBlue">linear combination of the events in the sample space</font> with the probability $P(A\vert B_{i})$, the occurrence of <font color="OrangeRed">the target condition $A$</font>, under the given partitioned sample space $B_{i}$ as it's <font color="OrangeRed">weighting</font>.  
>&#10113;usually, $A$ is the <font color="OrangeRed">qualitative</font> feature of interest.  
>&#10114;$\Omega$=$\\{B_{1},B_{2},...,B_{n}\\}$, where $B_{i}$ is the partition os the sample space.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The general form of Bayes theorem has joint probability expression in its nominator part.</font>  
>&#10112;the <font color="DeepSkyBlue">joint probability</font> is expressed in terms of $P(A\vert B_{i})\cdot P(B_{i})$.  
>&#10113;$P(A\vert B_{i})\cdot P(B_{i})$=$P(A\cap B_{i})$, is to calculate the <font color="OrangeRed">possible likelihood</font> of the probability of the coexistence of $A$ and $B_{i}$.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Take the Bayes theorem into parts</font>  
>There exists 4 factors in the Bayes theorem expression.  
>&#10112;$B_{i}$ is the <font color="OrangeRed">prior</font> probability, the already known probability.  
>&#10113;$P(A\vert B_{i})$ is the <font color="OrangeRed">likelihood function</font>, by intuition the <font color="DeepSkyBlue">qualitative</font> term, its major effect is the estimation of <font color="DeepSkyBlue">the possible likely probability of the occurrence of target event of interest $A$, under the given condition/partition $B_{i}$ of sample space</font>.  
>&#10114;the <font color="OrangeRed">total probability</font> also called the <font color="OrangeRed">marginal probability</font>, it is the summation over the distribution of each distinct $B_{i}$ with regards to the specific $A$, that means there could be infinite numbers of $A$.  
>&#10115;$P(B_{i}\vert A)$ is the <font color="OrangeRed">posterior probability</font>, by intuition the <font color="DeepSkyBlue">quantative</font> target, now the sample space is the target event of interest $A$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-28-bayesian-ml-significance-4-factors.png "4 factors")


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