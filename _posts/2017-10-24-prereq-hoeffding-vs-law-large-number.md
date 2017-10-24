---
layout: post
title: Hoeffding Inequality v.s. Law of Large Number
---

## Hoeffding Inequality

Suppose you are given an in-sample data set with certain property &nu; to train your learning algorithm with a hope to predict an out-sample data set with unknown and to be believed existed property &mu;.
Does in-sample &nu; say anything about out-sample &mu;??  Where the in-sample and out-sample might consist of small balls in red, green, blue.  Both samples are coming from the same random generator.
We treat the distribution of colour in balls as the property. 

> No!!  Possibly not, in-sample might contains only red balls, while out-sample might contains only green balls.  

> Yes!!  Probably yes, maybe in-sample and out-sample might contains similar high proportion of blue balls, thus, in-sample &nu; might be closed to out-sample &mu;.  

Hoeffding inequality guarantees that there exists such possibility that in-sample &nu; might be closed to out-sample &mu;, their difference is within quiet small &epsilon;, on conditions that the sample 
size is large:

<p class="message">
P(|&nu; &minus; &mu;| &gt; &epsilon;) &le; 2 &times; exp(-2 &times; &epsilon;&sup2; &times; N); where N is the in|out-sample size.
Hoeffding inequality claims &nu; &equals; &mu; is probably approximate correct.
</p>

[1]Valid for all N and &epsilon;.  

[2]Doesn&#39;t depend on &mu;, no need to know &mu;.  

[3]Large sample size N or looser gap &epsilon;, will we have higher probability for &nu; &#61; &mu;.  

> Above paragraph is my summary from [NTU H.T.Lin's Machine Learning Foundation](https://zh-tw.coursera.org/learn/ntumlone-mathematicalfoundations).

## Hoeffding Inequality &asymp; Chebyshev&#39;s Inequality

<p class="message">
Chebyshev&#39;s inequality claims that P(|Y &minus; E(Y)| &gt; a) &le; (1 &#8725; a) &times; Var(Y);<br />
where Y is any arbitrary random variable Y and any a &gt; 0.<br />

Proof:<br />
Var(Y) &#61; &int;<sup>&infin;</sup><sub>&minus;&infin;</sub>(y &minus; &mu;)<sup>2</sup>&times;&fnof;<sub>Y</sub>dy<br />
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&ge; &int;<sup>&infin;</sup><sub>|y &minus; &mu;| &ge; a</sub>(y &minus; &mu;)<sup>2</sup>&times;&fnof;<sub>Y</sub>dy<br />
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&ge; &int;<sup>&infin;</sup><sub>|y &minus; &mu;| &ge; a</sub>a<sup>2</sup>&times;&fnof;<sub>Y</sub>dy<br />
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#61; a<sup>2</sup>&times;P(|Y &minus; E(Y)| &gt; a), where &mu; &#61; E(Y).  

Suppose we have random variables X<sub>1</sub>, X<sub>2</sub>,,,,X<sub>n</sub> with expectation &mu; and variance &‌delta;<sup>2</sup>,<br />
take <sub>avg</sub>X<sub>n</sub> &#61; &Sigma;<sup>n</sup><sub>i=1</sub>X<sub>i</sub>&#8725;n, Var(avg</sub>X<sub>avg</sub>) &#61; &‌delta;<sup>2</sup>&#8725;n,<br />
then, for any &epsilon; &gt; 0, by using Chebyshev&#39;s inequality, we have<br />
P(|<sub>avg</sub>X<sub>n</sub> &minus; &mu;| &gt; &epsilon;) &#61; P(|<sub>avg</sub>X<sub>n</sub> &minus; E(<sub>avg</sub>X<sub>n</sub>)| &gt; &epsilon;)<br />
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &le; &#61; &‌delta;<sup>2</sup>&#8725;n, as n&rarr;&infin;, it&rarr;0.<br />
</p>