---
layout: post
title: Unbiased Estimator And Random Sample
---

## Prologue To <font color="Red">Unbiased Estimator</font> And Random Sample
<p class="message">
<font color="Red">Unbiased estimator</font> is a device or method to estimate the quantity of interesting features in a model distribution.  Such estimation is made on the dataset from <font color="DeepSkyBlue">random samples</font>.
</p>

### <font color="Red">Random Sample</font> And <font color="Red">Sample Statistic</font>
>&#10112;a random sample is <font color="DeepSkyBlue">a collection of random variables</font>, say $X_1$,$X_2$,...,$X_n$, they have <font color="OrangeRed">the same probability distribution</font> and are assumed to be <font color="OrangeRed">mutually independent</font>.  Those random variables thus constitute a random sample of <font color="DeepSkyBlue">population</font>.  
>&#10113;<font color="DeepSkyBlue">sampling is the behavior of taking samples from a population</font>, it must be representative to the population from which it is obtained.  
>&#10114;whereas, <font color="DeepSkyBlue">datasets</font> are usually modelled as <font color="DeepSkyBlue">the realization of random samples</font>, $X_1$,...,$X_n$.  
>&#10115;<font color="red">sample statistic</font> is an object, which depends on the random samples, $X_1$,...,$X_n$.  To be more formally, the sample average $\overline {X_n}$ is just one of the commonly referenced <font color="red">sample statistic</font>.  
>
>You can also <font color="DeepSkyBlue">take one distinct random random variable $X$ as a random sample</font>; although we often expect multiple random variables in a set of random sample.  

### <font color="Red">Estimate</font> versus <font color="Red">Estimator</font>
>&#10112;the <font color="Red">estimate</font> is <font color="DeepSkyBlue">the pure quantity obtained by means of the estimator</font>.  
>&#10112;the <font color="Red">estimator</font> is an <font color="DeepSkyBlue">artificial designed random variable by taking parameters constituting to a model distribution</font>.  
>
><font color="DeepPink">The value of $\overline {X_n}$ is the estimate, $\frac {X_1+X_2+...+X_n}{n}$ is just the estimator.</font>  

### <font color="Red">Unbiased Estimator</font> And <font color="DeepSkyBlue">Sampling Distribution</font>
>&#10112;assume <font color="Red">the random variable $T$ is an estimator</font> based on random sample consisting of $X_1$,$X_2$,...,$X_n$ for the quantity of features of interest, <font color="DeepSkyBlue">the distribution of the estimator $T$ is the sampling distribution of $t$</font>.  
>&#10113;the random variable $T$ is an <font color="Red">unbiased estimator</font> of the feature, denoted it as $\theta$, if and only if <font color="DeepSkyBlue">$E\lbrack T\rbrack$=$\theta$</font>, for any value of $\theta$.  

### <font color="Red">Unbiased Estimator</font> For <font color="DeepSkyBlue">Sample Expectation</font>
>This section focus on the quantity of interest, the expect value of random sample.  
><font color="OrangeRed">Irrelevant of the original probabilistic distribution</font> of the random sample, <font color="DeepSkyBlue">$\overline {X_n}$=$\frac {X_1+X_2+...+X_n}{n}$ is an unbiased estimator for the sample expectation</font>, given that the sample is consisting of $X_1$,...,$X_n$, with $\mu$ and $\sigma^2$ as its <font color="OrangeRed">finite</font> expectation and variance.  
>
>proof:  
>$E\lbrack \overline {X_n}\rbrack$  
>=$E\lbrack \frac {X_1+X_2+...+X_n}{n}\rbrack$  
>=$\sum_{i=1}^{n}\frac {E\lbrack X_i\rbrack}{n}$  
>=$\sum_{i=1}^{n}\frac {\mu}{n}$  
>=$\mu$  
>
>This proof is rather trivial.  

### <font color="Red">Unbiased Estimator</font> For <font color="DeepSkyBlue">Sample Variance</font>
>This section focus on the quantity of interest, the variance of random sample.  
><font color="OrangeRed">Irrelevant of the original probabilistic distribution</font> of the random sample, <font color="DeepSkyBlue">$S_n^{2}$=$\frac {1}{n-1}\cdot\sum_{i=1}^{n}(X_i-\overline {X_n})^{2}$ is an unbiased estimator for the sample variance</font>, given that the sample is consisting of $X_1$,...,$X_n$, with $\mu$ and $\sigma^2$ as its <font color="OrangeRed">finite</font> expectation and variance.  
>
>proof:  
>&#10112;we begin by the most basic definition of variance.  
>$E\lbrack \sum_{i=1}^{n}(X_i-\overline {X_n})^{2}\rbrack$  
>=$E\lbrack \sum_{i=1}^{n}(X_i-\mu+\mu-\overline {X_n})^{2}\rbrack$  
>=$E\lbrack \sum_{i=1}^{n}((X_i-\mu)-(\overline {X_n}-\mu))^{2}\rbrack$  
>&#10113;expand the summation term.  
>$\sum_{i=1}^{n}((X_i-\mu)-(\overline {X_n}-\mu))^{2}$  
>=$\sum_{i=1}^{n}(X_i-\mu)^{2}$-$2\cdot\sum_{i=1}^{n}(X_i-\mu)\cdot(\overline {X_n}-\mu)$+$\sum_{i=1}^{n}(\overline {X_n}-\mu)^{2}$  
>; where $\sum_{i=1}^{n}(\overline {X_n}-\mu)^{2}$=$n\cdot(\overline {X_n}-\mu)^{2}$, and  
>$\sum_{i=1}^{n}(X_i-\mu)\cdot(\overline {X_n}-\mu)$  
>=$(\overline {X_n}-\mu)\cdot\sum_{i=1}^{n}(X_i-\mu)$  
>=$(\overline {X_n}-\mu)\cdot(\sum_{i=1}^{n}X_i-n\cdot\mu)$  
>=$(\overline {X_n}-\mu)\cdot(n\cdot\overline {X_n}-n\cdot\mu)$  
>=$n\cdot (\overline {X_n}-\mu)^{2}$  
>&#10114;therefore,  
>$E\lbrack \sum_{i=1}^{n}(X_i-\overline {X_n})^{2}\rbrack$  
>=$E\lbrack \sum_{i=1}^{n}(X_i-\mu)^{2}$-$2\cdot\sum_{i=1}^{n}(X_i-\mu)\cdot(\overline {X_n}-\mu)$+$\sum_{i=1}^{n}(\overline {X_n}-\mu)^{2}\rbrack$  
>=$E\lbrack \sum_{i=1}^{n}(X_i-\mu)^{2}$-$2\cdot n\cdot (\overline {X_n}-\mu)^{2}$+$n\cdot(\overline {X_n}-\mu)^{2}\rbrack$  
>=$E\lbrack \sum_{i=1}^{n}(X_i-\mu)^{2}$-$n\cdot (\overline {X_n}-\mu)^{2}\rbrack$  
>=$E\lbrack \sum_{i=1}^{n}(X_i-\mu)^{2}\rbrack$-$n\cdot E\lbrack (\overline {X_n}-\mu)^{2}\rbrack$  
>=$E\lbrack \sum_{i=1}^{n}(X_i-\mu)^{2}\rbrack$-$n\cdot E\lbrack (\overline {X_n}-$E\lbrack \overline {X_n}\rbrack$)^{2}\rbrack$  

<!-- Γ -->
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