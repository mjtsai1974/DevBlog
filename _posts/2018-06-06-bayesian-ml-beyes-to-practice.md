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
>Given a dog, with 3 measurement results(lb) of weight, $13.9$,$17.5$,$14.1$ in the past 3 records of measurement.  <font color="OrangeRed">What's the exact weight of the dog at this moment?</font>  And <font color="DeepSkyBlue">the scale tells that it is weighted 14.2 lb in this concurrent measurement</font>.  
>
>This article is illustrated from the example in [How Bayesian inference works, Brandon Rohrer](https://www.youtube.com/watch?v=5NMxiOGL39M).  

### Can We Try The <font color="DeepSkyBlue">Unbiased Estimator</font>?
>[1]Since we are given a sample of $13.9$,$17.5$,$14.1$, how about the <font color="DeepSkyBlue">unbiased estimator</font>?  
>&#10112;by $\frac {X_{1}+X_{2}+X_{3}}{3}$=$\overline{X_{3}}$, this is <font color="DeepSkyBlue">to use sample average to approximate the mean</font>.  The current drawback might be that we have sample of only a few data.  
>&#10113;next we look at <font color="Red">sample variance</font>:  
>$\frac {\sum_{i=1}^{n}(X_{i}-\overline{X_{n})^{2}}}{n-1}$=$S_{n}^{2}$,  
>where $S_{n}^{2}$ is the <font color="Red">sample variance</font>.  
>&#10114;next we look at <font color="Red">sample standard deviation</font>:  
>$S_{n}$=$(\frac {\sum_{i=1}^{n}(X_{i}-\overline{X_{n})^{2}}}{n-1})^{\frac {1}{2}}$ is the <font color="Red">sample standard deviation</font>, $n$=$3$ in this example.  
>&#10115;then, the the <font color="Red">standard error</font> term:  
>$se$=$(\frac {\sum_{i=1}^{n}(X_{i}-\overline{X_{n})^{2}}}{n})^{\frac {1}{2}}$, is the <font color="Red">standard error</font> in this sample.  
>
>[2]All above are major terms in modern probability and statistics, and the <font color="Red">standard error</font> term have another expression in <font color="DeepSkyBlue">linear regression</font>:  
>&#10112;suppose $Y$ is the real target, and $\widehat Y$ is the estimated value of target, in <font color="DeepSkyBlue">linear regression</font>, the term $RSS$=$\sum_{i=1}^{n} (Y_{i}-\widehat Y_{i})^{2}$ is the <font color="Red">residual sum of squares</font>.  
>&#10113;we denote $(\frac {RSS}{dof})^{\frac {1}{2}}$ as the the <font color="Red">standard error</font> in <font color="DeepSkyBlue">linear regression</font>.  In this example, $dof$ is unknown, since we have not yet build a linear regression model.  By intuition, $dof$=$2$, because there is an average $\overline{X_{3}}$ taken into account.  
>
>[3]After simple calculation, we have:  
>&#10112;$\overline{x_{3}}$=$15.167$, <font color="DeepSkyBlue">the little case of letter $x$ indicates the value</font>.  
>&#10113;$S_{n}^{2}$=$4.09333351$  
>&#10114;$S_{n}$=$2.023$  
>&#10115;$se$=$1.6519$  

### Before We Start
>[1]We'd like to evaluate the possible accurate weight.  By given, we have 3 already known weights in the sample.  <font color="DeepSkyBlue">Suppose the weights are in normal distribution.</font>  
>&#10112;by $\overline{x_{3}}$=$15.167$, $S_{n}$=$2.023$, the shape of normal distribution is exhibited below:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-06-06-bayesian-ml-beyes-to-practice-N-dist-sample.png "sample N")
>&#10113;by $\overline{x_{3}}$=$15.167$, $se$=$1.6519$, the shape of normal distribution is exhibited below:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-06-06-bayesian-ml-beyes-to-practice-N-dist-population.png "population N")
>The shape of normal distribution is more <font color="DeepSkyBlue">sharpen</font>, if we use the <font color="Red">population standard deviation(standard error)</font> to be the <font color="Red">standard deviation</font>, which is <font color="OrangeRed">smaller</font>, this indicates some bias exists in between 2 sources of <font color="Red">standard deviation</font>, they are <font color="Red">sample standard deviation</font> and the <font color="Red">population standard deviation(standard error)</font>.  
>
>[2]We have 3 already known weights in the sample, what are $P(13.9)$,$P(14.1)$ and $P(17.5)$?  
>&#10112;should we treat $P(13.9)$=$P(14.1)$=$P(17.5)$=$\frac {1}{3}$?  Since each measurement comes out with one value of weight, the occurrence of getting the weight.  
>&#10113;or by using $\frac {1}{\sigma\cdot\sqrt {2\cdot \pi}}\cdot e^{-\frac {(x-\mu)^{2}}{2\cdot\sigma^{2}}}$ to calculate the respective probability?  
><font color="RosyBrown">There is no standard answer, yet!!!</font>  

### <font color="DeepSkyBlue">Translate The Target Into The Correct Probabilistic Expression</font>
>It seems that the <font color="OrangeRed">target of accurate weight</font> is very clear, but, <font color="DeepSkyBlue">how to translate into the correct probabilistic expression</font> is the major topic.  
>We denote $w$ to represent the weight, $m$ as each measurement.  How to express the weight each time the dog is measured?  It is determinant in the <font color="Red">prior</font> and the target <font color="Red">posterior</font>.  Below lists 2 of my viewpoints:  
>[1]$P(w\vert m)$=$\frac {P(m\vert w)\cdot P(w)}{P(m)}$  
>&#10112;this is to ask <font color="DeepPink">the maximum probability of the real weight from the given measurement</font>, the target <font color="Red">posterior</font> is $P(w\vert m)$, and the $P(w)$ is the already known weight(lb), the <font color="Red">prior</font>.  
>&#10113;suppose the measurement process is under certain quality control, and we no doubt the result.  
>
>[2]$P(m\vert w)$=$\frac {P(w\vert m)\cdot P(m)}{P(w)}$  
>&#10112;this is to ask <font color="RosyBrown">the maximum probability of the accuracy of the measurement result from the given weight(to be believed such quantitative weight is verified and correct)</font>, the target <font color="Red">posterior</font> is $P(m\vert w)$, and the $P(m)$ is the already known measurement result(lb), the <font color="Red">prior</font>.  
>&#10113;the major purpose of this expression should work <font color="RosyBrown">when we'd like to evaluate the accuracy of the measurement process or result</font>, it's the condition that we doubt the measurement result, we'd like to make further enhancement in the measurement equipment or the process.  
>
>[3]Therefore, we choose <font color="DeepPink">$P(w\vert m)$=$\frac {P(m\vert w)\cdot P(w)}{P(m)}$</font> as our Bayes expression, and <font color="DeepSkyBlue">$P(m\vert w)$</font> is the <font color="Red">likelihood function</font> for <font color="DeepSkyBlue">the probability of the measurement outcomes, $13.9$,$17.5$,$14.1$, given the true weight $w$</font>.  

### A <font color="Red">Dead Corner</font> Leading To <font color="Red">Nowhere</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">We are still in a no-escape corner, why?</font>  
>By choosing $P(w\vert m)$=$\frac {P(m\vert w)\cdot P(w)}{P(m)}$ as our Bayes expression only makes it a point in intuition layer.  
>&#10112;we don't know <font color="OrangeRed">how to make $P(w)$,$P(m)$,$P(m\vert w)$ quantitative</font>.  
>&#10113;should we treat $P(m\vert w)$ to be in uniform or Gaussian distribution?  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Try to escape.</font>  
>To be compliant with the Bayes expression of our choice, let's back to the inference for the total probability $P(m)$ of the measurement.  
>&#10112;suppose the dog's weight would vary by time, thus we are given 3 different measurement results of weight.  
>$P(m)$=$P(m\vert w_{1})\cdot P(w_{1})$+$P(m\vert w_{2})\cdot P(w_{2})$+$P(m\vert w_{3})\cdot P(w_{3})$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-06-06-bayesian-ml-beyes-to-practice-N-total-prob-m.png "total prob m")
>&#10113;we believe there exists indeed a <font color="DeepSkyBlue">true value of dog's weight, $w_{real}$</font>.  Base on the total probability of these 3 measurements, we'd like to estimate out the probability of such $w_{real}$ by $P(w_{real}\vert m)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-06-06-bayesian-ml-beyes-to-practice-N-total-prob-w.png "total prob w")
>&#10114;to further <font color="OrangeRed">regularize</font> our Bayes expression, let it becomes:  
>$P(w_{real}\vert m)$=$\frac {P(m\vert w_{real})\cdot P(w)}{P(m)}$, where <font color="OrangeRed">$P(m)$ and $P(w_{real})$ are just constants</font>.  
>&#10115;we can toss out the 2 terms $P(m)$ and $P(w_{real})$.  The working model now becomes:  
>$P(w_{real}\vert m)$=$P(m\vert w_{real})$  
>
><font color="C20000">It's the possible direction we can escape away from the space non-going anywhere, as a result of the chosen Bayes expression constructed by insufficient sample data.</font>  

### The <font color="DeepSkyBlue">Maximum Likelihood</font> For $P(w_{real}\vert m)$
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The working model filled with given data</font>  
>$P(w_{real}\vert m)$=$P(m\vert w_{real})$ leads us to the maximum likely possible real weight.  
>&#10112;fill in what we are given:  
>$P(w_{real}\vert m=\\{13.9,14.1,17.5\\})$  
>=$P(m=\\{13.9,14.1,17.5\\}\vert w_{real})$  
>&#10113;next to interpret $P(m\vert w_{real})$ by the <font color="Red">Gaussian normal distribution</font>.  
>
>Because this is <font color="DeepSkyBlue">fully compliant with the assumption that the accuracy of measurement result of weight is of no concern, and the weight varies by time, thus come out with different results</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The way to do the maximum likelihood estimation</font>  
>&#10112;it is to be proceeded <font color="DeepSkyBlue">with a given possible real weight, to generate the maximum value</font> of $P(m=\\{13.9,14.1,17.5\\}\vert w_{real})$, and <font color="DeepSkyBlue">such $w_{real}$ will yield the largest probability</font> of $P(w_{real}\vert m=\\{13.9,14.1,17.5\\})$.  
>&#10113;$\underset{w_{real}}{maxarg}P(m=\\{13.9,14.1,17.5\\}\vert w_{real})$  
>=$\underset{w_{real}}{maxarg}P(m=\\{13.9\\}\vert w_{real})$  
>$\;\;\;\;\cdot P(m=\\{14.1\\}\vert w_{real})$  
>$\;\;\;\;\cdot P(m=\\{17.5\\}\vert w_{real})$  
>This is just the maximum likelihood estimation for $w_{real}$.  
>&#10114;to have more probability and be centralized toward the $\overline{X_{3}}$, this article choose $\overline{x_{3}}$=$15.167$, $se$=$1.6519$ to build the Gaussian normal distribution.  
>Take $w_{real}\in\\{\overline{X_{3}}\pm se\\}$, ranges from $13.5151$ to $16.8189$.  
>&#10115;it's not inclusive of the given measurement result $17.5$, to make it more complete:  
>$w_{real}$=$\\{13,...,18\\}$  
>&#10116;<font color="DeepPink">let the data or the experiment result speaks!!</font>  
>
>In my [Python simulator](https://mjtsai1974.github.io/DevBlog/template/BayesInferForDogWeightByMLE.py), the maximum likelihood estimation of $w_{real}$ is $15.126$, for whatever sample or population standard deviation we choose to make the normal distribution.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-06-06-bayesian-ml-beyes-to-practice-N-dist-compare.png "std compare")
>The estimated $w_{real}$=$15.126$, which is very close to $\overline{x_{3}}$=$15.167$, <font color="RoyalBlue">is this the most appropriate value?</font>  

### Make The <font color="DeepPink">Bayes Inference With The Given Prior</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The Bayes inference should begin with the given prior</font>  
>Please recall that <font color="DeepSkyBlue">the scale tells the dog is weighted $14.2$ lb in this concurrent measurement</font>, and this is the <font color="Red">prior</font> to make Bayes inference with.  
>&#10112;assumed the given <font color="Red">prior</font> $P(w_{real})$=$14.2$ is true.  
>&#10113;since $14.2$ is within the existing sample space, we can just take $\mu$=$14.2$ and the same sample or population standard deviation to build the normal distribution.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Refine the working model</font>  
>$P(w_{real}\vert m)$=$P(m\vert w_{real})\cdot P(w_{real})$  
>&#10112;<font color="OrangeRed">the Bayes inference should begin with the given prior</font>, that's why we put the term P(w_{real}) at the right side.  
>&#10113;the term $P(m)$ is just a constant, could be safely tossed out.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Design the new flow</font>  
>We'll still use the maximum likelihood estimation for the real weight, there will be some flow change:  
>&#10112;take $\mu$=$14.2$ and the same sample or population standard deviation to build the normal distribution to <font color="OrangeRed">simulate</font> the real weight.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-06-06-bayesian-ml-beyes-to-practice-N-dist-compare-prior.png "std compare")  
>The red solid line is the normal distribution of sample standard deviation, the dashed blue line is the version of population standard deviation.  
>&#10113;iterate through each measured weight in the sample space.  
>&#10114;take the current iterated measured weight as $\mu$ to build a new normal distribution, centrally distributed in accordance with it.  
>&#10115;calculate the $P(w_{cur})$ with regards to the normal probability distributed in the normal distribution build in &#10112;.  
>&#10116;calculate the sample and population standard deviation in this new build normal distribution.  
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
<!-- \widehat X -->
<!-- \overline{X_n} -->
<!-- \underset{w_{real}}{maxarg} -->
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
<!-- http://www.astroml.org/book_figures/chapter3/fig_gaussian_distribution.html -->