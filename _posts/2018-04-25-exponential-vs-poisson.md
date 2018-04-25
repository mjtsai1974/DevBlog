---
layout: post
title: Exponential versus Poisson Distribution
---

## Prologue To <font color="Red">Exponential</font> versus <font color="Red">Poisson</font> Distribution
<p class="message">
In the world of <font color="OrangeRed">stochasticity</font>, pass and failure evaluation often been proceeded under <font color="DeepSkyBlue">the assumption that the intensity of event occurrence is constant over time</font>, which is debatable.  
When we involve the reinforcement learning issues, or the statistics regression topics, although the discrete case is easily constructed and simulated by bootstrapping algorithm in conjunction with the maximum likelihood estimation, the migration to continuous case would be just to split the test horizon into many, many, uncountable subintervals.  
Then, that connects the <font color="Red">Poisson</font> distribution to the <font color="Red">exponential</font> distribution, and the <font color="DeepPink">random arrivals probability could be modelled by gamma distribution as a result of the nature of exponential distribution</font>.  
</p>

### Overview The Similarities And Differences
>[1]the Poisson distribution  
>&#10112;we have an assumption that the intensity of event occurrence over time is invariant for Poisson process.  
>&#10113;suppose it is $\lambda$=$\frac {event\;counts}{time\;length}$  
Below exhibits the case where $\lambda$=$\frac {1}{time length}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-25-exponential-vs-poisson-lambda-for-1-evt.png "1 event")
This is the case where $\lambda$=$\frac {k}{time length}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-25-exponential-vs-poisson-lambda-for-k-evts.png "k events")
>&#10114;it takes up time length of $\frac {k}{\lambda}$ to have $k$ random arrivals, for $\lambda$=$\frac {k}{time\;length}$.  So, it holds to say that the adjacent two events of random arrival would just take time $\frac {1}{\lambda}$, which is the ideal inter-arrival times.  
>&#10115;each distinct inter-arrival times could then be modelled by random variable distributed in exponential probability.  
>&#10116;the joint distribution of random arrivals would be modelled by gamma distribution.  
>&#10117;<font color="DeepPink">the Poisson process has $n$ random arrivals in time inteerval $[a,b]$, the locations of these points are independent distributed, and each of them has a uniform distribution.</font>  
>
>[2]the exponential distribution  
>&#10112;suppose $X$ is the rate of event occurrences during time period $t$.  
>&#10113;suppose $V$ is the space where events take place within, then the <font color="DeepSkyBlue">success probability</font> over time period $t$ is <font color="DeepSkyBlue">$\underset{Succss}P$=$\frac {X\cdot t}{V}$</font>, and the <font color="DeepSkyBlue">failure probability</font> is <font color="DeepSkyBlue">$\underset{Fail}P$=$1$-$\frac {X\cdot t}{V}$</font>.  
>&#10114;we divide time period $t$ by $n$, where $n\rightarrow\infty$, then <font color="OrangeRed">success probability</font> over time period $t$ becomes <font color="OrangeRed">$\underset{Succss}P$=$\frac {X\cdot t}{V\cdot n}$</font>, and the <font color="OrangeRed">failure probability</font> becomes <font color="OrangeRed">$\underset{Fail}P$=$1$-$\frac {X\cdot t}{V\cdot n}$</font>.  
>After time period $t$, what is the probability for no event occurrence? Equivalently, it is asking the probability for the very first event taking place after time period $t$.  
>&#10115;<font color="DeepPink">This presumes that each subinterval $\frac {t}{n}$ is a failure case of the event</font>, then:
><font color="DeepSkyBlue">$P(T>t)$</font>  
>=$\lim_{n\rightarrow\infty}(\underset{Fail}P)^{n}$  
>=$\lim_{n\rightarrow\infty}(1-\frac {X\cdot t}{V\cdot n})^{n}$  
>$\approx e^{-\frac {X\cdot t}{V}}$    
>&#10116;the success probability within time period $t$ could be expressed:  
>$\underset{Succss}P$=$1$-$e^{-\frac {X\cdot t}{V}}$=$P(T\le t)$  
>&#10117;take $\lambda$=$\frac {X}{V}$, then, $P(T\le t)$=$1$-$e^{-\lambda\cdot t}$  
>$f_{T}(t)$=$D_{t}(1-e^{-\lambda\cdot t})$=$\lambda\cdot e^{-\lambda\cdot t}$  
>, where $lambda$ is the intensity, the rate of success, or of event occurrence.  

### <font color="RoyalBlue">Example</font>: Illustration Of The Similarities And Differences
>

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
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

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->