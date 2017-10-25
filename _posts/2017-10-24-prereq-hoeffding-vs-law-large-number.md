−−−
layout: post
title: Hoeffding Inequality v.s. Law of Large Number
−−−

## Hoeffding Inequality

Suppose you are given an in−sample data set with certain property &nu; to train your learning algorithm with a hope to predict an out−sample data set with unknown and to be believed existed property &mu;.
Does in−sample &nu; say anything about out−sample &mu;??  Where the in−sample and out−sample might consist of small balls in red, green, blue.  Both samples are coming from the same random generator.
We treat the distribution of colour in balls as the property. 

> No!!  Possibly not, in−sample might contains only red balls, while out−sample might contains only green balls.  
> Yes!!  Probably yes, maybe in−sample and out−sample might contains similar high proportion of blue balls, thus, in−sample &nu; might be closed to out−sample &mu;.  

Hoeffding inequality guarantees that there exists such possibility that in−sample &nu; might be closed to out−sample &mu;, their difference is within quiet small &epsilon;, on conditions that the sample 
size is large:

<p class="message">
P(|&nu; − &mu;| &gt; &epsilon;) &le; 2 × exp(−2 × &epsilon;&sup2; × N); where N is the in|out−sample size.
Hoeffding inequality claims &nu; &equals; &mu; is probably approximate correct.
</p>

[1]Valid for all N and &epsilon;.  
[2]Doesn&#39;t depend on &mu;, no need to know &mu;.  
[3]Large sample size N or looser gap &epsilon;, will we have higher probability for &nu; = &mu;.  

> Above paragraph is my summary from [NTU H.T.Lin's Machine Learning Foundation](https://zh−tw.coursera.org/learn/ntumlone−mathematicalfoundations).

## Chebyshev&#39;s Inequality(law of large number)

<p class="message">
Chebyshev&#39;s inequality claims that P(|Y − E(Y)| &gt; a) &le; (1 ∕ a) × Var(Y);<br />
where Y is any arbitrary random variable Y and any a &gt; 0.<br />

Proof:<br />
Var(Y) = &int;<sup>&infin;</sup><sub>−&infin;</sub>(y − &mu;)<sup>2</sup>×&fnof;<sub>Y</sub>dy<br />
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&ge; &int;<sup>&infin;</sup><sub>|y − &mu;| &ge; a</sub>(y − &mu;)<sup>2</sup>×&fnof;<sub>Y</sub>dy<br />
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&ge; &int;<sup>&infin;</sup><sub>|y − &mu;| &ge; a</sub>a<sup>2</sup>×&fnof;<sub>Y</sub>dy<br />
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;= a<sup>2</sup>×P(|Y − E(Y)| &gt; a), where &mu; = E(Y).<br />
<br />
Suppose we have 
(1)random variables X<sub>1</sub>, X<sub>2</sub>,,,,X<sub>n</sub> with expectation &mu; and variance &#948;<sup>2</sup>,<br />
(2)<sub>avg</sub>X<sub>n</sub> = &Sigma;<sup>n</sup><sub>i=1</sub>X<sub>i</sub>∕n, Var(<sub>avg</sub>X<sub>n</sub>) = &#948;<sup>2</sup>∕n,<br />
then, for any &epsilon; &gt; 0, by using Chebyshev&#39;s inequality, we have<br />
P(|<sub>avg</sub>X<sub>n</sub> − &mu;| &gt; &epsilon;) = P(|<sub>avg</sub>X<sub>n</sub> − E(<sub>avg</sub>X<sub>n</sub>)| &gt; &epsilon;)<br />
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &le; &#948;<sup>2</sup> ∕ (n × &epsilon;<sup>2</sup>), as n&rarr;&infin;, it&rarr;0.<br />
&#8756; lim<sub>n&rarr;&infin;</sub>P(|<sub>avg</sub>X<sub>n</sub> − &mu;| &gt; &epsilon;) = 0 ... law of large number.<br />
</p>

## Hoeffding Inequality &asymp; Chebyshev&#39;s Inequality

Now, we compare Hoeffding Inequality with Chebyshev&#39;s Inequality  

[1]P(|&nu; − &mu;| &gt; &epsilon;) &le; 2 × exp(−2 × &epsilon;&sup2; × N)  
<a>                      v.s.</a>  
[2]P(|<sub>avg</sub>X<sub>n</sub> − &mu;| &gt; &epsilon;) &le; &#948;<sup>2</sup> ∕ (n × &epsilon;<sup>2</sup>)  

>This is equivalent to compare 2 × exp(−2 × &epsilon;&sup2; × N) v.s. &#948;<sup>2</sup>∕(n × &epsilon;<sup>2</sup>)
>>For [1], as N &rarr; &infin;, we will have 2 × exp(−2 × &epsilon;&sup2; × N) &rarr; 0
>>For [2], as n &rarr; &infin;, we will have &#948;<sup>2</sup>∕(n × &epsilon;<sup>2</sup>) &rarr; 0
>>>&#8756; we just have Hoeffding Inequality &asymp; Chebyshev&#39;s Inequality, where 2 in [1] and &#948;<sup>2</sup> in [2] would just lead to probability in the same sign.