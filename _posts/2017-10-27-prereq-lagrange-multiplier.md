---
layout: post
title: Lagrange Multiplier
---

## Why Lagrange Multiplier?
Suppose you are given a function f(x<sub>1</sub>, x<sub>2</sub>), and would like to find out its extreme, subject to a constraint function g(x<sub>1</sub>, x<sub>2</sub>) = 0; 
where g(x<sub>1</sub>, x<sub>2</sub>) = ax<sub>1</sub> &#43; bx<sub>2</sub> &#43; c = 0.

>The possible solution:  
[1]Figure out from the constraint function g(x<sub>1</sub>, x<sub>2</sub>) = 0 and express x<sub>2</sub> in terms of x<sub>1</sub>, like x<sub>2</sub> = h(x<sub>1</sub>).  
[2]Back to f(x<sub>1</sub>, x<sub>2</sub>) and replace x<sub>2</sub> with h(x<sub>1</sub>), f(x<sub>1</sub>, x<sub>2</sub>) = f(x<sub>1</sub>, h(x<sub>1</sub>)).  
[3]Take partial derivative on x<sub>1</sub> to zero, &part;f(x<sub>1</sub>, h(x<sub>1</sub>)) ∕ &part;x<sub>1</sub> = 0, the x<sub>1</sub> value thus obtained would then lead us to the extreme of f(x<sub>1</sub>, x<sub>2</sub>).  
But,  

Suppose you are given an in−sample data set with certain property &nu; to train your learning algorithm with a hope to predict an out−sample data set with unknown and to be believed existed property &mu;.
Does in−sample &nu; say anything about out−sample &mu;??  Where the in−sample and out−sample might consist of small balls in red, green, blue.  Both samples are coming from the same random generator.
We treat the distribution of colour in balls as the property. 

>[1]No!!  Possibly not, in−sample might contains only red balls, while out−sample might contains only green balls.  
[2]Yes!!  Probably yes, maybe in−sample and out−sample might contains similar high proportion of blue balls, thus, in−sample &nu; might be closed to out−sample &mu;.  

Hoeffding inequality guarantees that there exists such possibility that in−sample &nu; might be closed to out−sample &mu;, their difference is within quiet small &epsilon;, on conditions that the sample 
size is large:

<p class="message">
P(|&nu; − &mu;| &gt; &epsilon;) &le; 2 × exp(−2 × &epsilon;&sup2; × N); where N is the in|out−sample size.  
Hoeffding inequality claims &nu; = &mu; is probably approximate correct.
</p>

[1]Valid for all N and &epsilon;.  
[2]Doesn&#39;t depend on &mu;, no need to know &mu;.  
[3]Large sample size N or looser gap &epsilon;, will we have higher probability for &nu; = &mu;.  

> Above paragraph is my summary from [NTU H.T.Lin's Machine Learning Foundation](https://zh−tw.coursera.org/learn/ntumlone−mathematicalfoundations).

## Chebyshev&#39;s Inequality(law of large number)

<p class="message">
Chebyshev&#39;s inequality claims that P(|Y − E(Y)| &gt; a) &le; (1 ∕ a) × Var(Y);  
where Y is any arbitrary random variable Y and any a &gt; 0.  
</p>

>Proof:  
Var(Y) = &int;<sup>&infin;</sup><sub>−&infin;</sub>(y − &mu;)<sup>2</sup>×&fnof;<sub>Y</sub>dy  
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&ge; &int;<sup>&infin;</sup><sub>|y − &mu;| &ge; a</sub>(y − &mu;)<sup>2</sup>×&fnof;<sub>Y</sub>dy  
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&ge; &int;<sup>&infin;</sup><sub>|y − &mu;| &ge; a</sub>a<sup>2</sup>×&fnof;<sub>Y</sub>dy  
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;= a<sup>2</sup>×P(|Y − E(Y)| &gt; a), where &mu; = E(Y).  

Suppose we have  
(1)random variables X<sub>1</sub>, X<sub>2</sub>,,,,X<sub>n</sub> with expectation &mu; and variance &#948;<sup>2</sup>,  
(2)<sub>avg</sub>X<sub>n</sub> = &Sigma;<sup>n</sup><sub>i=1</sub>X<sub>i</sub> ∕ n, Var(<sub>avg</sub>X<sub>n</sub>) = &#948;<sup>2</sup> ∕ n,  
then, for any &epsilon; &gt; 0, by using Chebyshev&#39;s inequality, we have  
P(|<sub>avg</sub>X<sub>n</sub> − &mu;| &gt; &epsilon;) = P(|<sub>avg</sub>X<sub>n</sub> − E(<sub>avg</sub>X<sub>n</sub>)| &gt; &epsilon;)  
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &le; &#948;<sup>2</sup> ∕ (n × &epsilon;<sup>2</sup>), as n&rarr;&infin;, it&rarr;0.  
&#8756; lim<sub>n&rarr;&infin;</sub>P(|<sub>avg</sub>X<sub>n</sub> − &mu;| &gt; &epsilon;) = 0 ... law of large number.  

## Hoeffding Inequality &asymp; Chebyshev&#39;s Inequality

Now, we compare Hoeffding Inequality with Chebyshev&#39;s Inequality  

[1]P(|&nu; − &mu;| &gt; &epsilon;) &le; 2 × exp(−2 × &epsilon;&sup2; × N)  
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;v.s.  
[2]P(|<sub>avg</sub>X<sub>n</sub> − &mu;| &gt; &epsilon;) &le; &#948;<sup>2</sup> ∕ (n × &epsilon;<sup>2</sup>)  

>This is equivalent to compare 2 × exp(−2 × &epsilon;&sup2; × N) v.s. &#948;<sup>2</sup>∕(n × &epsilon;<sup>2</sup>)  
For [1], as N &rarr; &infin;, we will have 2 × exp(−2 × &epsilon;&sup2; × N) &rarr; 0  
For [2], as n &rarr; &infin;, we will have &#948;<sup>2</sup>∕(n × &epsilon;<sup>2</sup>) &rarr; 0  
&#8756; we just have Hoeffding Inequality &asymp; Chebyshev&#39;s Inequality, where 2 in [1] and &#948;<sup>2</sup> in [2] would just lead to probability in the same sign.