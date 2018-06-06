---
layout: post
title: Bayes From Theorem To Practice
---

## Prologue To <font color="Red">Bayes From Theorem To Practice</font>
<p class="message">
The <font color="Red">Bayes theorem</font> is the <font color="DeepPink">quantitative critical thinking</font> rather than the <font color="RosyBrown">qualitative thinking</font> of human nature.  
<font color="#C20000">By using already known probability of feature to figure out unknown probability of interested feature in its maximum likelihood, the result would be more plausible.</font>
</p>

### You Are Given The Question
>Given a dog, with 3 weights(lb) of measurement, $13.9$,$17.5$,$14.1$ in the past 3 records.  <font color="OrangeRed">What's the exact weight of the dog?</font>  And <font color="DeepSkyBlue">the scale tells that it is weighted 14.2 lb in this concurrent measurement</font>.  
>
>This article is illustrated from the example in [How Bayesian inference works, Brandon Rohrer](https://www.youtube.com/watch?v=5NMxiOGL39M).  

### Can We Try The <font color="DeepSkyBlue">Unbiased Estimator</font>?
>Since we are given a sample of $13.9$,$17.5$,$14.1$, how about the <font color="DeepSkyBlue">unbiased estimator</font>?  
>&#10112;by $\frac {X_{1}+X_{2}+X_{3}}{3}$=$\overline{X_{3}}$, this is <font color="DeepSkyBlue">to use sample average to approximate the mean</font>.  The current drawback might be that we have sample of only a few data.  
>&#10113;next we look at <font color="Red">sample variance</font>:  
>$\frac {\sum_{i=1}^{n}(X_{i}-\overline{X_{n})^{2}}{n-1}$=$S_{n}^{2}$,  
>where $S_{n}^{2}$ is the <font color="Red">sample variance</font>.  
>&#10114;next we look at <font color="Red">standard sample deviation</font>:  
>$S_{n}$=$(\frac {\sum_{i=1}^{n}(X_{i}-\overline{X_{n})^{2}}{n-1})^{\frac {1}{2}}$ is the <font color="Red">sample standard deviation</font>, $n$=$3$ in this example.  
>&#10115;the the <font color="Red">standard error</font> term:  
>

### Addendum
>&#10112;[How Bayesian inference works, Brandon Rohrer](https://www.youtube.com/watch?v=5NMxiOGL39M)  
>&#10113;[Translated article of &#10112;](https://brohrer.mcknote.com/zh-Hant/statistics/how_bayesian_inference_works.html)  
>&#10114;[Bayes theorem and conditional probability](https://ccjou.wordpress.com/2016/02/01/%E6%A2%9D%E4%BB%B6%E6%A9%9F%E7%8E%87%E8%88%87%E8%B2%9D%E6%B0%8F%E5%AE%9A%E7%90%86/)  

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