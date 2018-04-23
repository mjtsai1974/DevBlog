---
layout: post
title: Introduction To The Poisson Distribution
---

## Prologue To The <font color="Red">Poisson</font> Distribution
<p class="message">
In probability theory and statistics, the <font color="Red">Poisson</font> distribution is the <font color="DeepSkyBlue">process</font> developed with a hope to approximate the scenario of random arrival within a given time period.  
The random variable of the <font color="DeepSkyBlue">interarrival time</font> modeled by the <font color="Red">Poisson</font> process is identical to the result deduced out by the exponential distribution, we could also express the <font color="DeepSkyBlue">interarrival time</font> as kind of a <font color="DeepSkyBlue">special case of gamma</font> distribution.    
</p>

<!-- The realization of the Poisson model would be greatly helpful in the evaluation of maximum likelihood estimation and the machine learning results correctness for some discrete or even the continuous cases in the future. -->

### The <font color="Red">Poisson</font> Process Illustration
>The Poisson process is a simple kind of random process, describing random points distribution in time or space.  It is developedn based on be low two assumptions:  
>[1]<font color="OrangeRed">homogeneity</font>: it assumes the rate $\lambda$ of event occurrence is constant over time.  The expected unmber of random point arrivals over time period $t$ is $\lambda\cdot t$.  
>[2]<font color="OrangeRed">independence</font>: it assumes all random occurrences are independent.  This says that the number of arrivals over <font color="DeepSkyBlue">disjoint</font> time intervals are independent random variables.  
>
>Next the illustration of the procerss.  
>&#10112;suppose within a time interval $[0,t]$, the arrival of points or the occurrence of events are random and is represented by random variables $X_{1}$, $X_{2}$, $X_{3}$..., and this scenario is compliants with <font color="OrangeRed">homogeneity</font> and <font color="OrangeRed">independence</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-22-intro-poisson-dist-random-arrival.png "random arrival")
>This article denotes the total number of occurrences within $[0,t]$ as $N([0,t])$, or just abbreviating $N_{t}$ for over time length $t$.  The <font color="OrangeRed">homogeneity</font> implies that <font color="DeepSkyBlue">$E\lbrack N_{t}\rbrack$=$\lambda\cdot t$</font>.  
>&#10113;to be more precisely approximate to the distribution of such random arrivals, we <font color="DeepSkyBlue">divide the time period $t$ by $n$, to be believed that $n$ is large enough</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-22-intro-poisson-dist-time-interval-div-by-n.png "divide by n")
>Then we have each distinct subinterval of time length $\frac {1}{n}$, and <font color="DeepPink">each subinterval would just have success of $1$ arrival, or failure of $0$ arrival</font>, which itself is a <font color="OrangeRed">Bernoulli</font> distribution.  
>&#10114;each subinterval has time length $\frac {t}{n}$, the $i$-th subinterval ranges from time $\frac {(i-1)\cdot t}{n}$ to $\frac {i\cdot t}{n}$.  We take $R_{i}$ as the $i$-th event in each distinct subinterval. 
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-22-intro-poisson-dist-time-subinterval-bernoulli.png "subintervel bernoulli")
>The <font color="OrangeRed">Bernoulli</font> random variable would have <font color="DeepPink">its outcome as $1$ for success and $0$ for failure in its distribution</font>.  So the expected value of the $i$-th arrival is:  
>$E\lbrack R_{i}\rbrack$=$1\cdot P_{i}$+$0\cdot F_{i}$, where $F_{i}$=$1$-$P_{i}$ for each $i$, and $P_{i}$=$\frac {\lambda\cdot t}{n}$.  
>&#10115;we then accumulate all outcomes of all $R_{i}$, trivially, the total number of event occurrences remains the same.  
>$N_{t}$=$R_{1}$+$R_{2}$+...+$R_{i}$+...+$R_{n}$, the point is that <font color="DeepSkyBlue">each $R_{i}$ is independent</font> random variable, now <font color="DeepPink">the original random process behaves in the Binomial distribution as a whole</font>, therefor <font color="DeepPink">$N_{t}$ has Binomial distribution</font> of Bin($n$,$p$), where $p$=$\frac {\lambda\cdot t}{n}$.  
>&#10116;$C_{k}^{n}(\frac {\lambda\cdot t}{n})^{k}\cdot(1-\frac {\lambda\cdot t}{n})^{n-k}$ is the probability we have $k$ arrivals in the Binomial distribution, and <font color="OrangeRed">the value of $n$ really matters</font>.  To get rid of this concern, we treat $n$ as <font color="DeepSkyBlue">infinity</font>.  
>$\lim_{n\rightarrow\infty}C_{k}^{n}(\frac {\lambda\cdot t}{n})^{k}\cdot(1-\frac {\lambda\cdot t}{n})^{n-k}$  
>=$\lim_{n\rightarrow\infty}C_{k}^{n}(\frac {1}{n})^{k}\cdot(\lambda\cdot t)^{k}\cdot(1-\frac {\lambda\cdot t}{n})^{n-k}$  
>&#10117;$\lim_{n\rightarrow\infty}C_{k}^{n}(\frac {1}{n})^{k}$  
>=$\lim_{n\rightarrow\infty}\frac {n}{n}\cdot\frac {n-1}{n}\cdot\frac {n-2}{n}\cdot\cdot\cdot\frac {n-k+1}{n}\cdot\frac {1}{k!}$  
>=$\frac {1}{k!}$...by using some algebra  
>&#10118;$\lim_{n\rightarrow\infty}(1-\frac {\lambda\cdot t}{n})^{n-k}$  
>=$\lim_{n\rightarrow\infty}(1-\frac {\lambda\cdot t}{n})^{n}\cdot(1-\frac {\lambda\cdot t}{n})^{k}$  
>=$e^{-\lambda\cdot t}$  
>where by calculus, <font color="DeepPink">$\lim_{n\rightarrow\infty}(1-\frac {\lambda\cdot t}{n})^{n}$=$e^{-\lambda\cdot t}$</font>,  
>and $\lim_{n\rightarrow\infty}(1-\frac {\lambda\cdot t}{n})^{k}$=$1$.  
>&#10119;thus <font color="DeepSkyBlue">the probability we have $k$ random arrivals</font> is deduced out below:  
><font color="OrangeRed">$P(N_{t}=k)$</font>  
>=$\lim_{n\rightarrow\infty}C_{k}^{n}(\frac {\lambda\cdot t}{n})^{k}\cdot(1-\frac {\lambda\cdot t}{n})^{n-k}$  
>=$\lim_{n\rightarrow\infty}C_{k}^{n}(\frac {1}{n})^{k}\cdot(\lambda\cdot t)^{k}\cdot(1-\frac {\lambda\cdot t}{n})^{n-k}$  
>=<font color="DeepPink">$\frac {(\lambda\cdot t)^{k}}{k!}\cdot e^{-\lambda\cdot t}$</font>  

### The <font color="Red">Poisson</font> Distribution Definition
>By the illustration step &#10119;, we have <font color="DeepPink">$\frac {(\lambda\cdot t)^{k}}{k!}\cdot e^{-\lambda\cdot t}$</font> as <font color="DeepSkyBlue">the probability of $k$ random arrivals</font>, we have below formal claim the definition of the <font color="Red">Poisson</font> distribution, as a result of the fact that <font color="DeepPink">$e^{-\lambda\cdot t}\cdot\sum_{k=0}^{\infty}\frac {(\lambda\cdot t)^{k}}{k!}$=$1$</font>.  
>
><font color="OrangeRed">[Definition]</font>  
>For any discrete random variable X with parameter $\mu$, it is said to have a <font color="Red">Poisson</font> distribution if its <font color="DeepSkyBlue">probability mass function</font> is given by  
>$P(X=k)$=$\frac {(\mu)^{k}}{k!}\cdot e^{-\mu}$, for $k$=$0$,$1$,$2$,..., denote it as $Pois(\mu)$, where  
>&#10112;$\mu$=$\lambda\cdot t$, and $\lambda$ is a constant event occurrence rate in the format of (event counts)/(time unit).  
>&#10113;$t$ is the period of time in the unit with respect to the time unit of the rate by $\lambda$.  
>
>Please recall that we use the term <font color="DeepSkyBlue">probability mass function</font>, since this random process is deducing from a rather <font color="OrangeRed">discrete</font> distributed case.

### Expect Value And Variance Of The <font color="Red">Poisson</font> Distribution
>Succeeding to above paragraphs, we know that probability for each distinct $R_{j}$ to have event occurrence is $\frac {\lambda\cdot t}{n}$, which is a great add-in and a short-cut to the expect value and variance.  
>[1]<font color="OrangeRed">expect value</font>  
>$E\lbrack N_{t}\rbrack$  
>=$E\lbrack\sum_{i=1}^{n}R_{i}\rbrack$  
>=$\sum_{i=1}^{n}E\lbrack R_{i}\rbrack$  
>=$n\cdot\frac {\lambda\cdot t}{n}$  
>=$\lambda\cdot t$...hold for $n\rightarrow\infty$  
>[2]<font color="OrangeRed">variance</font>::mjtsai  
>&#10112;begin from the Binomial variance.  
>$Var\lbrack N_{t}\rbrack$  
>=$Var\lbrack\sum_{i=1}^{n}R_{i}\rbrack$  
>=$Var\lbrack R_{1}+R_{2}+...+R_{n}\rbrack$  
>=$Var\lbrack R_{1}\rbrack$+$Var\lbrack R_{2}\rbrack$+...+$Var\lbrack R_{n}\rbrack$  
>&#10113;for each $i$,  
>$Var\lbrack R_{i}\rbrack$  
>=$E\lbrack R_{i}^{2}\rbrack$-$E^{2}\lbrack R_{i}\rbrack$  
>=$1^{2}\cdot p+0^{2}\cdot(1-p)$-$p^{2}$  
>=$p$-$p^{2}$, where <font color="DeepSkyBlue">$p$ is the success probability</font>  
>=$p\cdot(1-p)$, take <font color="DeepSkyBlue">$p$=$\frac {\lambda\cdot t}{n}$</font>  
>&#10114;go to the <font color="Red">Poisson</font> case $n\rightarrow\infty$:  
>$\lim_{n\rightarrow\infty}Var\lbrack N_{t}\rbrack$  
>=$\lim_{n\rightarrow\infty}n\cdot p\cdot(1-p)$  
>=$\lim_{n\rightarrow\infty}n\cdot \frac {\lambda\cdot t}{n}\cdot(1-\frac {\lambda\cdot t}{n})$  
>=$\lambda\cdot t$, where $\lim_{n\rightarrow\infty}(1-\frac {\lambda\cdot t}{n})$=$1$  
>
>We found that <font color="DeepPink">the Poisson distribution has the same expect value and variance.</font>  
>You can also see [Poisson variance proof on WiKi](https://proofwiki.org/wiki/Variance_of_Poisson_Distribution)

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