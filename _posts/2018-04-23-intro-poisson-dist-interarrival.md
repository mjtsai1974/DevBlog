---
layout: post
title: Introduction To The Poisson Process Inter-arrival Times
---

## Prologue To The <font color="Red">Poisson</font> Process <font color="Red">Inter-arrival Times</font>
<p class="message">
On the way to the <font color="Red">Poisson</font> distribution, the <font color="Red">inter-arrival times</font> could be easily found, and both exponential and <font color="Red">Poisson</font> distribution could be an appropriate modeling of it.  Formally, <font color="Red">inter-arrival times</font> could be distributed in gamma probability as a result of the nature of exponential distribution.  
</p>

### The <font color="Red">Inter-arrival Times</font>
>Given that $X_{1}$,$X_{2}$,...,$X_{n}$ are random variables with event outcome occurrences arrived at specific time.  To make it more formally, we take the difference $T_{i}$=$X_{i}$-$X_{i-1}$ as the <font color="Red">inter-arrival times</font>.  

### The <font color="DeepSkyBlue">Very First</font> <font color="Red">Inter-arrival Times</font> Follows <font color="DeepSkyBlue">Exponential Distribution</font>
>We start to derive the probability distribution of <font color="Red">inter-arrival times</font>, let's focus on the <font color="DeepSkyBlue">very first one</font> as the prelude.  
>&#10112;take $T_{1}$=$X_{1}$ as the very first arrival time.  
>&#10113;the probability of first arrival at time greater than t is equivalent to the probability of zero arrival within time $[0,t]$.  
><font color="DeepSkyBlue">$P(T_{1}\le t)$</font>=1-$P(T_{1}>t)$=1-$P(N_{[0,t]}=0)$=1-$e^{-\lambda\cdot t}$  
>, where $\lambda$ is the intensity, the rate of event occurrence.  
>
><font color="DeepPink">The very first inter-arrival times is itself an exponential distribution.</font>  

### The Distribution Of <font color="Red">Distinct Inter-arrival Times</font>
>If you take a close look at the random arrivals over the horizon, trivially, numerous <font color="Red">distinct inter-arrival times</font> could be found.  
>Suppose you are given two adjacent <font color="Red">inter-arrival times</font>, $T_{i}$=$s$,$T_{i+1}$=$t$.  We are asking the <font color="DeepSkyBlue">probability for we have the second arrival after time duration $t$, under the condition that we have the first arrival with regards to $T_{i}$=$s$</font>.  
>This turns into the <font color="DeepSkyBlue">conditional probability</font>.  
>$P(T_{i+1}>t|T_{i}=s)$  
>=$P(T_{i+1}>t,T_{i}=s|T_{i}=s)$  
>=$P(N_{(s,s+t]}=0,N_{[0,s]}=1|N_{[0,s]}=1)$  
>=$\frac {P(N_{(s,s+t]}=0\cap N_{[0,s]}=1)}{P(N_{[0,s]}=1)}$  
>=$\frac {P(N_{(s,s+t]}=0)\cdot P(N_{[0,s]}=1)}{P(N_{[0,s]}=1)}$...<font color="OrangeRed">independence</font>  
>=$P(N_{(s,s+t]}=0)$  
>=$e^{-\lambda\cdot(t)}$  
>
>Therefore, $P(T_{i+1}\le t|T_{i}=s)$=1-$P(T_{i+1}>t|T_{i}=s)$=1-$e^{-\lambda\cdot(t)}$  
>We can claim that each <font color="DeepPink">distinct inter-arrival times has an exponential distribution.</font>  Some textbook treat it as the <font color="Red">one-dimensional Poisson process</font>.  

### The <font color="Red">Joint</font> Distribution Of <font color="Red">Random Arrivals</font>::mjtsai1974
>Due to the nature of the exponential distribution, we can then derive the <font color="Red">joint</font> distribution of numerous <font color="Red">random arrivals</font> in the unit of each <font color="Red">distinct inter-arrival times</font> as a whole.  
>By one-dimensional Poisson process, we know that all $T_{i}$'s are independent and each has an $Exp(\lambda\cdot t)$ distribution, where $t$ is the <font color="Red">inter-arrival times</font>.  Let me state below claim:  
>&#10112;$T_{i}$=$X_{i}$-$X_{i-1}$  
>&#10113;$X_{i}$=$T_{i}$+$T_{i-1}$  
>&#10114;where &#10112;,&#10113;is the rule for each new arrival, $T_{0}$=$X_{0}$=$0$ by default.  
>Then, $F_{T_{i}}$=$P(T_{i}\le t)$=1-$e^{-\lambda\cdot t}$, for $i$=$1$,$2$,$3$,...  
>I'd like to prove that the <font color="DeepPink">joint distribution of random arrivals is just a gamma distribution.</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-23-intro-poisson-dist-interarrival.png "inter-arrival times")
>proof::mjtsai1974  
>[1]begin by time tick at $0$, say we use $X_{1}$ as the random variable to represent the first one arrival within whatever time length $t$ is, denote time period $[0,t]$ as $T_{1}$.  
>&#10112;$F_{X_{1}}(t)$=$F_{T_{1}+T_{0}}(t)$=$P(T_{1}\le t)$=1-$e^{-\lambda\cdot t}$, where $T_{0}$=$0$  
>&#10113;$f_{X_{1}}(t)$=<font color="DeepPink">$\lambda\cdot e^{-\lambda\cdot t}$</font>  
>Trivially, by previous section, each $X_{i}$ just has an exponential distribution.  
>[2]for whatever $T_{1}$ is, after that, say we'd like to have the second arrival within time length $t$, and use the $X_{2}$ as the random variable for the second arrival.  
>&#10112;$T_{2}$=$X_{2}$-$X_{1}$ and $X_{2}$=$T_{2}$+$T_{1}$  
>&#10113;$F_{X_{2}}(t)$  
>=$F_{T_{2}+T_{1}}(t)$  
>=$P(T_{2}+T_{1}\le t)$...take $Y$=$T_{1}$,$X$=$T_{2}$  
>=$\int_{0}^{t}\int_{0}^{t-y}f_{X}(x)\cdot f_{Y}(y)\operatorname dx\operatorname dy$  
>=$\int_{0}^{t}F_{X}(t-y)\cdot f_{Y}(y)\operatorname dy$  
>&#10114;differentiate $F_{X_{2}}(t)$ with respect to its current variable, say $t$.  
>$f_{X_{2}}(t)$  
>=$\int_{0}^{t}f_{X}(t-y)\cdot f_{Y}(y)\operatorname dy$  
>=$\int_{0}^{t}\lambda\cdot e^{-\lambda\cdot(t-y)}\cdot\lambda\cdot e^{-\lambda\cdot y}\operatorname dy$  
>=$\lambda^{2}\cdot e^{-\lambda\cdot t}\int_{0}^{t}\operatorname dy$  
>=<font color="DeepPink">$\lambda^{2}\cdot t\cdot e^{-\lambda\cdot t}$</font>  
>
>If you set $X$=$T_{1}$,$Y$=$T_{2}$ in deduction, still the same result you can get.  
>[3]for whatever $T_{2}$ is, after that, we use the $X_{3}$ as the random variable for the third arrival, and would like to have it within time length $t$.  
>&#10112;$X_{3}$=$T_{3}$+$T_{2}$+$T_{1}$  
>&#10113;$F_{X_{3}}(t)$  
>=$F_{T_{3}+T_{2}+T_{1}}(t)$  
>=$P(T_{3}+T_{2}+T_{1}\le t)$...take $Y$=$T_{2}$+$T_{1}$,$X$=$T_{3}$  
>=$\int_{0}^{t}\int_{0}^{t-y}f_{X}(x)\cdot f_{Y}(y)\operatorname dx\operatorname dy$  
>=$\int_{0}^{t}F_{X}(t-y)\cdot f_{Y}(y)\operatorname dy$  
>&#10114;differentiate $F_{X_{3}}(t)$ with respect to its current variable, say $t$.  
>$f_{X_{3}}(t)$  
>=$\int_{0}^{t}f_{X}(t-y)\cdot f_{Y}(y)\operatorname dy$  
>=$\int_{0}^{t}\lambda\cdot e^{-\lambda\cdot(t-y)}\cdot(\lambda)^{2}\cdot y\cdot e^{-\lambda\cdot y}\operatorname dy$  
>=$\lambda^{3}\cdot e^{-\lambda\cdot t}\int_{0}^{t}y\operatorname dy$  
>=<font color="DeepPink">$\frac {1}{2}\cdot\lambda^{3}\cdot t^{2}\cdot e^{-\lambda\cdot t}$</font>  
>
>If you set $X$=$T_{2}$+$T_{1}$,$Y$=$T_{3}$ in deduction, still the same result you can get.  
>[4]repeat above procedure until $n\rightarrow\infty$, we will have $F_{X_{n}}(t)$ holds to have its derivative $f_{X_{n}}(t)$=$\frac {\lambda\cdot(\lambda\cdot t)^{n-1}\cdot e^{-\lambda\cdot t}}{(n-1)!}$, for $n$=$1$,$2$,..., where $\Gamma(n)$=$(n-1)!$.  
>[5]by means of mathematics induction, we can conclude that the <font color="DeepPink">joint distribution of random arrivals is just a gamma distribution.</font>  Be recalled that <font color="DeepSkyBlue">$f_{X_{n}}(t)$=$\frac {\lambda\cdot(\lambda\cdot t)^{n-1}\cdot e^{-\lambda\cdot t}}{(n-1)!}$ is a gamma probability function</font> in [Introduction To The Gamma Distribution]({{ site.github.repo }}{{ site.baseurl }}/2017/12/29/intro-gamma-dist/).  

### <font color="RoyalBlue">Example</font>: Illustrate The <font color="Red">Poisson Probability</font> For <font color="DeepSkyBlue">Points Distribution</font>
>Suppose you are given $n$ points randomly generated within an interval, how to evaluate the <font color="DeepSkyBlue">points location</font>?  Just <font color="DeepSkyBlue">treat the inter-arrival times as the location info</font>, it suffice to evaluate the probability of points arrival by means of <font color="Red">Poisson</font> distribution.  
>
>Let's say the interval is $[0,a]$, explore one arrival case within this interval as a beginning.  
>[1]assume $0<s<a$, we now know one arrival occurred within $[0,a]$, the probability of this one arrival occurrence within $s$, under the condition that this occurrence is within $[0,a]$:  
><font color="DeepSkyBlue">$P(X_{1}\le s|N_{[0,a]}=1)$</font>  
>=$P(X_{1}\le s,N_{[0,a]}=1|N_{[0,a]}=1)$  
>=$P(N_{(0,s]}=1,N_{[0,a]}=1|N_{[0,a]}=1)$  
>=<font color="DeepSkyBlue">$P(N_{(0,s]}=1,N_{[s,a]}=0|N_{[0,a]}=1)$</font>  
>=$\frac {\lambda\cdot s\cdot e^{-\lambda\cdot s}\cdot e^{-\lambda\cdot(a-s)}}{\lambda\cdot a\cdot e^{-\lambda\cdot a}}$  
>=$\frac {s}{a}$  
>
>$X_{1}$ is uniformly distributed within $[0,a]$, given the event ${N_{[0,a]}=1}$ as the condition, since $\sum_{i=1}^{s}\frac {1}{a}$=$\frac {s}{a}$  
>[2]suppose that there are two arrivals in $[0,a]$, that is $N_{[0,a]}=2$, and given $0<s<t<a$, we can show $P(X_{1}\le s,X_{2}\le t|N_{[0,a]}=2)$=$\frac {t^{2}-(t-s)^{2}}{a^{2}}$.  
>proof::mjtsai1974  
>&#10112;this is to ask out the probability that first arrival falls within $[0,s]$, the second arrival falls within $(s,t]$.  Below graph exhibits the possible cases.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-23-intro-poisson-dist-interarrival-prob-2-events.png "2 events")
>&#10113;by above table, we just need to accumulate the probability of the case (1) and (2), which is equivalent to <font color="DeepSkyBlue">substract the probability of two event occurrences in $(s,t]$ from the probability that two event arrivals in $[0,t]$.</font>  
>$P(X_{1}\le s,X_{2}\le t|N_{[0,a]}=2)$  
>=$\frac {P(X_{1}\le s,X_{2}\le t\cap N_{[0,a]}=2)}{P(N_{[0,a]}=2)}$  
>=$\frac {P(X_{1},X_{2}\le t)-P(s<X_{1},X_{2}\le t)}{P(N_{[0,a]}=2)}$  
>=$\frac {P(N_{[0,t]}=2)\cdot P(N_{(t,a]}=0)-P(N_{[0,s)}=0)\cdot P(N_{[s,t]}=2)\cdot P(N_{(t,a]}=0)}{P(N_{[0,a]}=2)}$  
>=$\frac {\frac {(\lambda\cdot t)^{2}}{2!}\cdot e^{-\lambda\cdot t}\cdot\frac {(\lambda\cdot(a-t))^{0}}{0!}\cdot e^{-\lambda\cdot(a-t)}-\frac {(\lambda\cdot s)^{0}}{0!}\cdot e^{-\lambda\cdot s}\cdot\frac {(\lambda\cdot(t-s))^{2}}{2!}\cdot e^{-\lambda\cdot(t-s)}\cdot\frac {(\lambda\cdot(a-t))^{0}}{0!}\cdot e^{-\lambda\cdot(a-t)}}{\frac {(\lambda\cdot a)^{2}}{2!}\cdot e^{-\lambda\cdot a}}$  
>=$\frac {\frac {(\lambda\cdot t)^{2}}{2!}\cdot e^{-\lambda\cdot t}-\frac {(\lambda\cdot(t-s))^{2}}{2!}\cdot e^{-\lambda\cdot(t-s)-\lambda\cdot s-\lambda\cdot(a-t)}}{\frac {(\lambda\cdot a)^{2}}{2!}\cdot e^{-\lambda\cdot a}}$  

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

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->