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
>&#10112;$B_{i}$ is the <font color="OrangeRed">prior probability</font>, the already known probability.  
>&#10113;$P(A\vert B_{i})$ is the <font color="OrangeRed">likelihood function</font>, by intuition the <font color="RosyBrown">qualitative</font> term, its major effect is the estimation of <font color="DeepSkyBlue">the possible likely probability of the occurrence of target event of interest $A$, under the given condition/partition $B_{i}$ of sample space</font>.  
>&#10114;the <font color="OrangeRed">total probability</font> also called the <font color="OrangeRed">marginal probability</font>, it is the summation over the distribution of each distinct $B_{i}$ with regards to the specific $A$, that means there could be infinite numbers of $A$.  
>&#10115;$P(B_{i}\vert A)$ is the <font color="OrangeRed">posterior probability</font>, by intuition the <font color="DeepPink">quantative</font> target, now <font color="DeepSkyBlue">the sample space is the target event of interest $A$</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-28-bayesian-ml-significance-4-factors.png "4 factors")

### <font color="RoyalBlue">Example</font>: 3 Red And 2 White Balls
><font color="RoyalBlue">[Question]</font>
>Given that there are 3 red and 2 white balls in a bow.  Suppose you pick up 2 balls sequentially.  What's the probability of picking up the 2nd white ball <font color="OrangeRed">and</font> the 1st one is the red ball?  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-28-bayesian-ml-significance-3r-2w.png "3 R, 2 W")
><font color="DeepSkyBlue">[Answer]</font>
>This is asking for $P(W_{2}\cap R_{1})$.  Denote $R_{i}$,$W_{i}$ as the i-th picking the red, white ball up.  
>&#10112;when we pick up the very first ball, $\Omega$=$\\{r_{1},r_{2},r_{3},w_{1},w_{2}\\}$.  
>$P(R_{1})$=$\frac {3}{5}$, the probability that the 1st ball is a red ball.  
>&#10113;when we pick up the second ball, $\Omega$=$\\{r_{2},r_{3},w_{1},w_{2}\\}$.  
>$P(W_{2}\vert R_{1})$=$\frac {2}{4}$, the probability that the 2nd ball is a white ball, given that the first one is the red ball.  
>&#10114;$P(W_{2}\cap R_{1})$=$P(W_{2}\vert R_{1})\cdot P(R_{1})$=$\frac {6}{20}$.  
>
><font color="#C20000">[More details]</font>
>&#10112;$P(R_{1})$ is the <font color="OrangeRed">prior priority</font>.  
>&#10113;$P(W_{2}\vert R_{1})$ is the <font color="OrangeRed">likelihood function</font> to estimate the probability that the 2nd ball is a white ball, given that the first one is the red ball.  
>&#10114;$P(W_{2}\vert R_{1})\cdot P(R_{1})$ is the <font color="OrangeRed">joint probability</font> of the coexistence of $W_{2}$ and $R_{1}$, since <font color="DeepSkyBlue">we are asking for the probability of picking up the 2nd white ball <font color="OrangeRed">and</font> the 1st one is the red ball</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-28-bayesian-ml-significance-3r-2w-sample-space.png "sample space")

### <font color="RoyalBlue">Example</font>: <font color="DeepPink">quantative</font> versus <font color="RosyBrown">qualitative</font>
><font color="RoyalBlue">[Question]</font>
>Suppose the statistical population distribution in the Hsin-Chu science park area reports that $\\%8$ of the population is the managers, $\\%32$ is the marketing sales, $\\%38$ is the manufacturing engineers, $\\%22$ is the IC design engineers.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-28-bayesian-ml-significance-q-q.png "quantative vs qualitative")
>Given that Albert is a man, when you see him, his behavior is <font color="OrangeRed">a little shy</font>, talktive with strangers for road seeking, and is not talktive in political topics.  
>
>According to recent statistical research that given a manager, $0.1$ probability being shy; given a marketing sales, $0.24$ probability being shy; given a manufacturing engineer, $0.47$ probability being shy; given an IC design engineer, %0.29% probability being shy.  
><font color="OrangeRed">Under such condition, given that Albert is a shy man, what kind of identity has the maximum probability?</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-28-bayesian-ml-significance-q-q-shy.png "q-q-shy")
><font color="DeepSkyBlue">[Answer]</font>  
>&#10112;take $P(Mgr)$=$0.08$, $P(Sales)$=$0.32$, $P(M_{eng})$=$0.38$, $P(I_{eng})$=$0.22$ for probability of being managers, marketing sales, manufacture engineers, IC design engineers, which are all the <font color="OrangeRed">prior probability</font>.  
>&#10113;take $P(Shy\vert Mgr)$=$0.1$, $P(Shy\vert Sales)$=$0.24$, $P(Shy\vert M_{eng})$=$0.47$, $P(Shy\vert I_{eng})$=$0.29$ for given a manager, a marketing sales, a manufacturing engineer, IC design engineer, the probability being shy respectively, which are all the <font color="OrangeRed">likelihood function</font>, the <font color="RosyBrown">qualitative</font> term.  
>&#10114;the question asks for the maximum in between $P(Mgr\vert Shy)$, $P(Sales\vert Shy)$, $P(M_{eng}\vert Shy)$, $P(I_{eng}\vert Shy)$.  Trivially, we need the <font color="OrangeRed">total probability</font> of being shy.  
>$P(Shy)$  
>=$P(Shy\vert Mgr)\cdot P(Mgr)$+  
>$\;\;\;\;P(Shy\vert Sales)\cdot P(Sales)$+  
>$\;\;\;\;P(Shy\vert M_{eng})\cdot P(M_{eng})$+  
>$\;\;\;\;P(Shy\vert I_{eng})\cdot P(I_{eng})$  
>=$0.1\cdot 0.08$+$0.24\cdot 0.32$+$0.47\cdot 0.38$+$0.29\cdot 0.22$  
>=$0.3272$  
>&#10115;finally, the <font color="OrangeRed">posterior probability</font>:  
>$P(Mgr\vert Shy)$=$\frac {P(Shy\vert Mgr)\cdot P(Mgr)}{P(Shy)}$=$\frac {0.1\cdot 0.08}{0.3272}$=$0.0244$  
>$P(Sales\vert Shy)$=$\frac {P(Shy\vert Sales)\cdot P(Sales)}{P(Shy)}$=$\frac {0.24\cdot 0.32}{0.3272}$=$0.2347$  
>$P(M_{eng}\vert Shy)$=$\frac {P(Shy\vert M_{eng})\cdot P(M_{eng})}{P(Shy)}$=$\frac {0.47\cdot 0.38}{0.3272}$=$0.5458$  
>$P(I_{eng}\vert Shy)$=$\frac {P(Shy\vert I_{eng})\cdot P(I_{eng})}{P(Shy)}$=$\frac {0.29\cdot 0.22}{0.3272}$=$0.1949$
>  
>By means of <font color="DeepPink">quantative posterior</font>, we found that $P(M_{eng}\vert Shy)$ has the <font color="OrangeRed">largest posterior probability</font> and implies the maximum possibility that Albert is a shy man, he is a manufacture engineer.  

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

<!-- <font color="#C20000">conclusion, finding, more details</font> -->
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