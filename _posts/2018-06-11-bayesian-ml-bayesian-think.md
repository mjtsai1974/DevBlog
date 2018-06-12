---
layout: post
title: The Bayesian Thinking
---

## Prologue To The <font color="Red">Bayesian Thinking</font>
<p class="message">
<font color="Red">Bayesian thinking</font> is an approach <font color="DeepPink">to systematizing reasoning under uncertainty</font> by means of the <font color="Red">Bayes theorem</font>.
</p>

### The <font color="DeepSkyBlue">Intuition</font> Behind The <font color="Red">Bayes Theorem</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">ReCap the Bayes theorem</font>  
>![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-28-bayesian-ml-significance-4-factors.png "4 factors")
>The detailed explanation of 4 factors are in my prior post, [The Bayes Theorem Significance](({{ site.github.repo }}{{ site.baseurl }}/2018/05/28/bayesian-ml-significance/)).  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The intuition behind the theorem</font>  
>![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-06-11-bayesian-ml-bayesian-think-intuition.png "intuition")
>The intuition behind encourages you to make further inference.  
>&#10112;the <font color="Red">hypothesis</font>, mapped to the <font color="DeepSkyBlue">prior</font>, which are all probabilities.  
>&#10113;the <font color="DeepSkyBlue">likelihood function</font> related to prior is expressed as the probability of the event occurrence of the <font color="Red">observation</font> given the event occurrence of <font color="Red">hypothesis</font>.  
>&#10114;the <font color="Red">total probability of the observation</font> is more well regularized.  
>&#10115;the <font color="Red">posterior is the probability of the hypothesis, given the observation</font>.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">The Bayesian inference</font>  
>&#10112;at the first glance, we make an <font color="Red">observation</font> in the real world.  
>&#10113;we'd like to identify it by making certain <font color="Red">hypothesis</font> of some classification.  
>&#10114;the <font color="Red">likelihood function</font> estimates the possible probability of the observation given the hypothesis.  
>&#10115;finally, the <font color="Red">posterior</font> is the probability of the <font color="Red">hypothesis</font> given the <font color="Red">observation</font>.  
>Such process is called the <font color="Red">Bayesian inference</font>, full compliant with the classification of an observed object, which the hypothesis is made all about.  
>
>By the way, <font color="#C20000">observation, hypothesis, likelihood function are all based on the <font color="RosyBrown">qualitative</font> belief, the total probability of the observation and the posterior are the <font color="DeepPink">quantitative</font> outcomes</font>.  

### Addendum
>&#10112;[Introduction to Bayesian Thinking: from Bayes theorem to Bayes networks, Felipe Sanchez](https://towardsdatascience.com/will-you-become-a-zombie-if-a-99-accuracy-test-result-positive-3da371f5134)  
>&#10113;[The Bayesian trap, Veritasium channel](https://www.youtube.com/watch?v=R13BD8qKeTg&vl=en)

<!--
[1]What is a Bayesian network?
Bayes theorem offers a fundamental mechanism for changing your opinion in the light of evidence. This is what Bayesian networks are about.

https://www.quora.com/What-is-a-Bayesian-network

[2]What are the relationships of Bayes' theorem, Bayesian inference, Naive Bayes, and Bayesian network (in simple English)?
[2.1]Bayesianism is an approach to systematizing reasoning under uncertainty.
[2.2]We can characterize how one’s beliefs ought to change when new information is gained.
[2.3]If we observe the truth or falsity of a relevant event, we can then use Bayes’ theorem to revise our probability assessment for other related events. This is called Bayesian inference.
[2.4]If we are thinking about a complex situation, in which our probability for events depend upon various others, we can use a Bayesian network (also called Bayes net) to represent what we believe. 
[2.5]In a Bayes net, there are nodes connected by arrows. Each node is the probability of an event. An arrow from event A to event B means that our probability of B depends on our probability of A. 
[2.6]Naive Bayes refers to a particularly simple form of a Bayes net, where your event of interest depends on other things, but none of them depends on one another.

https://www.quora.com/What-are-the-relationships-of-Bayes-theorem-Bayesian-inference-Naive-Bayes-and-Bayesian-network-in-simple-English

[3]How does Bayesian networks work?
[3.1]A Bayesian network is good at classifying based on observations.
[3.2]Therefore you can make a network that models relations between events in the present situation, symptoms of these and potential future effects. The BN would then be able to classify the present situation and hence predict future events with a probability.
[3.3]You can do unsupervised learning with a BN from a dataset and allow the learning algorithm to find both structure and probabilities.
[3.4]you can also do supervised learning with a BN, aiding the learning algorithm with a priori knowledge about relations and probabilities in the model. Here, results should become better than ANN and SVM.
[3.5]A BN is a white box approach where you can represent and evaluate the structure of the model explicitly whereas ANN and SVM are black box approaches where you really don't know why you get your results. This puts a limit to how good they can become.

https://www.quora.com/How-does-Bayesian-networks-work

[4]What is Bayesian machine learning?
[4.1]Machine learning is a set of methods for creating models that describe or predicting something about the world. It does so by learning those models from data.
[4.2]Bayesian machine learning allows us to encode our prior beliefs about what those models should look like, independent of what the data tells us. This is especially useful when we don’t have a ton of data to confidently learn our model.

https://www.quora.com/What-is-Bayesian-machine-learning

[5]What does Bayesian networks mean in Machine Learning?
[5.1]A Bayesian network essentially has random variables, and a graph structure that encodes the dependencies between the variables.
[5.2]A Bayesian network is a statistical model which connects random variables with their conditional probabilities. Bayes' theorem is used for the computation of probabilities in the network.

https://www.quora.com/What-does-Bayesian-networks-mean-in-Machine-Learning
-->

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