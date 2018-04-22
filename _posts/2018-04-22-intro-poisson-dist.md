---
layout: post
title: Introduction To The Poisson Distribution
---

## Prologue To The <font color="Red">Poisson</font> Distribution
<p class="message">
In probability theory and statistics, the <font color="Red">poisson</font> distribution is the <font color="DeepSkyBlue">process</font> developed with a hope to approximate the scenario of random arrival within a given time period.  
The random variable of the <font color="DeepSkyBlue">interarrival time</font> modeled by the <font color="Red">poisson</font> process is identical to the result deduced out by the exponential distribution, we could also express the <font color="DeepSkyBlue">interarrival time</font> as kind of a <font color="DeepSkyBlue">special case of gamma</font> distribution.    
</p>

<!-- The realization of the poisson model would be greatly helpful in the evaluation of maximum likelihood estimation and the machine learning results correctness for some discrete or even the continuous cases in the future. -->

### The <font color="Red">Poisson</font> Process Illustration
>The poisson process is a simple kind of random process, describing random points distribution in time or space.  It is developedn based on be low two assumptions:  
>[1]<font color="OrangeRed">homogeneity</font>: it assumes the rate $\lambda$ of event occurrance is constant over time.  The expected unmber of random point arrivals over time period $t$ is $\lambda\cdot t$.  
>[2]<font color="OrangeRed">independence</font>: it assumes all random occurrances are independent.  This says that the number of arrivals over <font color="DeepSkyBlue">disjoint</font> time intervals are independent random variables.  
>
>Next the illustration of the procerss.  
>&#10112;suppose within a time interval $[0,t]$, the arrival of points or the occurrance of events are random and is represented by random variables $X_{1}$, $X_{2}$, $X_{3}$..., and this scenario is compliants with <font color="OrangeRed">homogeneity</font> and <font color="OrangeRed">independence</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-22-intro-poisson-dist-random-arrival.png "random arrival")
>This article denotes the total number of occurrances within $[0,t]$ as $N([0,t])$, or just abbreviating $N_{t}$ for over time length $t$.  The <font color="OrangeRed">homogeneity</font> implies that <font color="DeepSkyBlue">$E\lbrack N_{t}\rbrack$=$\lambda\cdot t$</font>.  
>&#10113;to be more precisely approximate to the distribution of such random arrivals, we <font color="DeepSkyBlue">divide the time period $t$ by $n$, to be believed that $n$ is large enough</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-22-intro-poisson-dist-time-interval-div-by-n.png "divide by n")
>Then we have each distinct subinterval of time length $\frac {1}{n}$, and <font color="DeepPink">each subinterval would just have success of $1$ arrival, or failure of $0$ arrival</font>, which itself is a <font color="OrangeRed">Bernoulli</font> distribution.  
>&#10114;each subinterval has time length $\frac {t}{n}$, the $i$-th subinterval ranges from time $\frac {(i-1)\cdot t}{n}$ to $\frac {i\cdot t}{n}$.  We take $R_{i}$ as the $i$-th event in each distinct subinterval. 
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-22-intro-poisson-dist-time-subinterval-bernoulli.png "subintervel bernoulli")
>The <font color="OrangeRed">Bernoulli</font> random variable would have <font color="DeepPink">its outcome as $1$ for success and $0$ for failure in its distribution</font>.  So the expected value of the $i$-th arrival is:  
>$E\lbrack R_{i}\rbrack$=$1\cdot P_{i}$+$0\cdot F_{i}$, where $F_{i}$=$1$-$P_{i}$ for each $i$, and $P_{i}$=$\frac {\lambda\cdot t}{n}$.  
>&#10115; we then accumulate all outcomes of all $R_{i}$, trivially, the total number of event occurrances remains the same.  
>$N_{t}$=$R_{1}$+$R_{2}$+...+$R_{i}$+...+$R_{n}$, the point is that <font color="DeepSkyBlue">each $R_{i}$ is independent</font> random variable, now <font color="DeepPink">the original random process behaves in the Binomial distribution as a whole</font>, therefor <font color="DeepPink">$N_{t}$ has Binomial distribution</font> of Bin($n$,$p$), where $p$=$\frac {\lambda\cdot t}{n}$.  
>

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- $E\lbrack X\rbrack$ -->
<!-- \overline{X_n} -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->
<!-- \lim_{t\rightarrow\infty} -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha</font> -->
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

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->