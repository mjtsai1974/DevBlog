---
layout: post
title: Introduction To The Bayes Theorem
---

## Prologue To Introduction To The <font color="Red">Bayes Theorem</font>
<p class="message">
<font color="Red">The Bayes theorem</font> has been developed and evolved over time <font color="DeepPink">to enhance the accuracy of conditional probability prediction result</font>, especially, when you have only a few data gathered and would like to have a convincible, plausible result.
It could be pervasively found in the machine learning, reinforcement learning, wherein the POMDP transition probability is one such model.   
</p>

### Law Of <font color="Red">Total Probability</font>
>Consider in a random experiment, given below conditions:  
>&#10112;$\Omega$=$\\{B_{1},B_{2},...,B_{n}\\}$, where $B_{i}\cap B_{j}$=$0$.  
>&#10113;within the sample space, there exist another event $A$, partitioned by $B_{i}$ randomly.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-23-bayesian-ml-intro-total-prob.png "total probability")
>We have $P(A)$=$P(A\vert B_{1})\cdot P(B_{1})$+...+$P(A\vert B_{n})\cdot P(B_{n})$  
>
>proof:  
>&#10112;by intersection of $A$ and $\Omega$ could we get $A$:  
>$A$  
>=$A\cap \Omega$  
>=$A\cap (B_{1}\cup B_{2}\cup...\cup B_{n})$  
>=$(A\cap B_{1})\cup (A\cap B_{2})...\cup (A\cap B_{n})$.  
>&#10113;the <font color="Red">total probability</font> of event $A$:  
>$P(A)$  
>=$P((A\cap B_{1})\cup (A\cap B_{2})...\cup (A\cap B_{n}))$  
>=$P(A\cap B_{1})$+$P(A\cap B_{2})$+...+$P(A\cap B_{n})$  
>=$P(A\vert B_{1})\cdot P(B_{1})$+...+$P(A\vert B_{n})\cdot P(B_{n})$  

### The <font color="Red">Bayes Theorem</font>
>Given 2 distinct events $A$ and $B$, the term $P(A\cap B)$ can interconnect below 2 expression:  
>&#10112;$P(A\cap B)$=$P(A\vert B)\cdot P(B)$  
>&#10113;$P(B\cap A)$=$P(B\vert A)\cdot P(A)$  
>
><font color="DeepSkyBlue">The sequence order in intersection changes nothing:</font>  
>$P(B\vert A)\cdot P(A)$=$P(A\vert B)\cdot P(B)$, then,   
>$\;\;\;\;P(B\vert A)$=$\frac {P(A\vert B)\cdot P(B)}{P(A)}$...<font color="Red">Bayes Theorem</font>  

### The General Form of <font color="Red">Bayes Theorem</font>
>By using the law of <font color="Red">total probability</font>, the general form of <font color="Red">Bayes theorem</font> describing the probability of event $B$, given event $A$ could be expressed in below terms:  
>$\;\;\;\;P(B_{i}\vert A)$=$\frac {P(A\vert B_{i})\cdot P(B_{i})}{P(A\vert B_{1})\cdot P(B_{1})+...+P(A\vert B_{n})\cdot P(B_{n})}$  

### <font color="RoyalBlue">Example</font>: Illustration By Rainy And Sunny Days In One Week
><font color="RoyalBlue">[Question]</font>
>Suppose we have a fully record of the weather in the past one week, they are rainy and sunny periods.  Say $P(Rainy)$=$\frac {3}{7}$, $P(Sunny)$=$\frac {4}{7}$.  
>
>In the rainy period of time, assume such probability when we look into the sky, we can see sun shinning(quiet strange earth weather), $P(Sunny\vert Rainy)$=$\frac {1}{5}$, that is $\frac {1}{5}$ of the time you can see the sun shining in the rainy days.  
>
>The we'd like to know how often could we have rain drops when we are under the sun shinning.  
>
><font color="DeepSkyBlue">[Answer]</font>
>This is to ask for $P(Rainy\vert Sunny)$.  
>$P(Rainy\vert Sunny)$=$\frac {P(Sunny\vert Rainy)\cdot P(Rainy)}{P(Sunny)}$=$\frac {\frac {1}{5}\cdot\frac {3}{7}}{\frac {4}{7}}$=$\frac {3}{20}$  

### <font color="RoyalBlue">Example</font>: Illustration By Dogs And cats
>Suppose there exists 60 dos and 40 cats in the animal hospital, 20 female dogs and 10 female cats.  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">When we pick up one female animal, what's the probability it is a dog?</font>  
><font color="DeepSkyBlue">Total probability of female animals</font> should be calculated out in advance.  This is asking for $P(Dog\vert Female)$.  
>&#10112;probability of female animals:  
>$P(Female)$  
>=$P(Female \cap(Dog \cup Cat))$  
>=$P(Female \cap Dog)$+$P(Female \cap Cat)$  
>=$\frac {20}{100}$+$\frac {10}{100}$  
>=$\frac {3}{10}$  
>&#10113;$P(Dog\vert Female)$  
>=$\frac {P(Female \cap Dog)}{P(Female)}$  
>=$\frac {P(Female \vert Dog)\cdot P(Dog)}{P(Female)}$  
>=$\frac {\frac {20}{60}\cdot\frac {60}{100}}{\frac {3}{10}}$  
>=$\frac {2}{3}$  
>
><font color="RoyalBlue">The tiny skill would be to advice the given condition in the first order in the intersection term, the to be asked probability in the second term.</font>  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Back to $P(Dog\vert Female)$ again, for the term $\frac {P(Female \cap Dog)}{P(Female)}$, can we instead to express in the term $\frac {P(Dog \cap Female)}{P(Female)}$?</font>  
>Yes!  Let's expand from it to verify.  
>&#10112;$P(Dog\vert Female)$  
>=$\frac {P(Dog \cap Female)}{P(Female)}$  
>=$\frac {P(Dog \vert Female)\cdot P(Female)}{P(Female)}$  
>&#10113;trivially, <font color="DeepSkyBlue">back to $\frac {P(Dog \cap Female)}{P(Female)}$ is not incorporating anything already given to help to figure out something we don't know!!</font>  Although, we can also count it by means from the given sample space of 30 females, 20 dogs in it, to get the answer of $\frac {2}{3}$.  
>
><font color="DeepPink">The major purpose of Bayes theorem is to use known probability to figure out unknown probability in its maximum likelihood</font>, instead of manual counting in the sample space.  
>

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