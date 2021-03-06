---
layout: post
title: Exponential versus Poisson Distribution::mjtsai1974
---

## Prologue To <font color="Red">Exponential</font> versus <font color="Red">Poisson</font> Distribution::mjtsai1974
<p class="message">
In the world of <font color="OrangeRed">stochasticity</font>, pass and failure evaluation often been proceeded under <font color="DeepSkyBlue">the assumption that the intensity of event occurrence is constant over time</font>, which is debatable.  
When we involve the reinforcement learning issues, or the statistics regression topics, although the discrete case is easily constructed and simulated by bootstrapping algorithm in conjunction with the maximum likelihood estimation, the migration to continuous case would be just to split the test horizon into many, many, uncountable subintervals.  
Then, that connects the <font color="Red">Poisson</font> distribution to the <font color="Red">exponential</font> distribution, and the <font color="DeepPink">random arrivals probability could be modelled by gamma distribution as a result of the nature of exponential distribution</font>.  
</p>

### Overview The Similarities And Differences
><font color="RoyalBlue">[1]</font>
><font color="OrangeRed">the Poisson distribution</font>  
>&#10112;we have an assumption that the intensity of event occurrence over time is invariant for Poisson process.  
>&#10113;suppose it is $\lambda$=$\frac {event\;counts}{time\;length}$  
Below exhibits the case where $\lambda$=$\frac {1}{time\;length}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-25-exponential-vs-poisson-lambda-for-1-evt.png "1 event")
This is the case where $\lambda$=$\frac {k}{time\;length}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-04-25-exponential-vs-poisson-lambda-for-k-evts.png "k events")
>&#10114;it takes up time length of $\frac {k}{\lambda}$ to have $k$ random arrivals, for $\lambda$=$\frac {k}{time\;length}$.  So, it holds to say that the adjacent two events of random arrival would just take time $\frac {1}{\lambda}$, which is the ideal inter-arrival times.  
>&#10115;each distinct inter-arrival times could then be modelled by random variable distributed in exponential probability.  
>&#10116;the joint distribution of random arrivals would be modelled by gamma distribution.  
>&#10117;<font color="DeepPink">the Poisson process has $n$ random arrivals in time interval $[a,b]$, the locations of these points are independent distributed, and each of them has a uniform distribution.</font>  
>
><font color="RoyalBlue">[2]</font>
><font color="OrangeRed">the exponential distribution</font>  
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
>, where $\lambda$ is the intensity, the rate of success, or of event occurrence.  

### <font color="RoyalBlue">Example</font>: Illustration Of The Similarities And Differences
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
>&#10112;by <font color="OrangeRed">exponential</font> distribution, we take $\lambda$=$6$ ($\frac {vehicles}{1\;minute}$), its PDF is $f_{exp}(t)$=$6\cdot e^{-6\cdot t}$, where $t>0$.  
>No cars within $30$ seconds asks for no car within $0.5$ minute, and we are figuring out <font color="DeepSkyBlue">the probability that $t>0.5$ will we just have the very first car come in</font>, then:  
>$F_{exp}(t>0.5)$  
>=$\int_{0.5}^{\infty}6\cdot e^{-6\cdot t}\operatorname dt$  
>=$-e^{-6\cdot t}\vert_{0.5}^{\infty}$  
>=$e^{-3}$  
>&#10113;by <font color="OrangeRed">Poisson</font> distribution, we can still use $\lambda$=$6$ ($\frac {vehicles}{1\;minute}$), its PDF is $f_{Pois}(x,t)$=$\frac {(6\cdot t)^{x}}{x!}\cdot e^{-6\cdot t}$, $t$ is now $0.5$.  
>Therefore, $f_{Pois}(0,0.5)$=$\frac {(6\cdot 0.5)^{0}}{0!}\cdot e^{-6\cdot 0.5}$=$e^{-3}$  
>
>We have found that the probability for no vehicles within the dedicated time interval is <font color="DeepPink">the same in both exponential and Poisson distribution</font>.  This is fully compliant with the claim that <font color="DeepPink">the very first inter-arrival times is itself an exponential distribution</font> in [Introduction To The Poisson Process Inter-arrival Times]({{ site.github.repo }}{{ site.baseurl }}/2018/04/23/intro-poisson-dist-interarrival/).
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Still using the same rate that $6$ vehicles pass through a highway toll station per minute, then, what is the probability that all 6 cars crossing the toll station within 30 seconds?</font>  
>&#10112;from <font color="OrangeRed">exponential</font> distribution view point, this is asking <font color="DeepSkyBlue">the success probability within 30 seconds</font>.  
>$F_{exp}(0.5)$  
>=$P_{exp}(t\le 0.5)$  
>=$\int_{0}^{0.5}6\cdot e^{-6\cdot t}\operatorname dt$  
>=$1$-$e^{-6\cdot 0.5}$=$0.950$  
>&#10113;for <font color="OrangeRed">Poisson</font> distribution, this is to calculate the probability of distribution on the number $6$, which is the number of the requested target crossing vehicle counts within $0.5$ minute.  
>$P_{Pois}(x)$=$\frac {(\lambda\cdot t)^{x}}{x!}\cdot e^{-\lambda\cdot t}$...the Poisson PMF.  
>Now $t$=$0.5$, $x$=$6$, $P_{Pois}(6)$=$\frac {3^6}{6!}\cdot e^{-3}$=$0.168$  
>
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Why at this moment, the Poisson and exponential probability come out with different result?</font>  
>&#10112;as a result of the fact that we treat the pass probability as a whole by integration from each distinct exponential probability from $t$=$0$ to $t$=$0.5$, whereas we only calculate the Poisson probability distributed on the number $6$.  
>&#10113;if we accumulate the distinct Poisson probability distributed on the numbers from $0$ to $6$, that is $\sum_{x=0}^{6}\frac {(\lambda\cdot t)^{x}}{x!}\cdot e^{-\lambda\cdot t}$, in this example, we get the probability $0.96649146...$, and the bias of $0.01$ could then be found.  
><font color="DeepSkyBlue">By accumulating the distinct Poisson probability distribution from $0$ to $6$ is just to answer different question asking the probability of the number of cars passing by up to 6.</font>  

### <font color="RoyalBlue">Example</font>: Illustration Of <font color="OrangeRed">Random Arrivals</font>
><font color="DeepSkyBlue">[1]</font>
><font color="Black">Still using the same intensity, the rate that $6$ vehicles pass through a highway toll station per minute, then, <font color="OrangeRed">what's the probability of the $8$-th vehicle passing through the toll station?</font></font>  
>&#10112;<font color="DeepSkyBlue">random arrivals doesn't reinforce the occurrence of specific event at dedicated time interval</font>, in distinct time interval unit with regard to the given rate, which is $\frac {1}{rate}$, event outcome might just be true or false.  Then, the k-th car should pass by after time length of $k\cdot\frac {1}{rate}$, if all goes well, just right at the k-th moment.  
>&#10113;this involves <font color="DeepSkyBlue">the distribution of inter-arrival times</font>, which is in <font color="DeepSkyBlue">exponential distribution</font> itself, and <font color="DeepSkyBlue">the accumulation of which would leads to the gamma distribution</font>, see [Introduction To The Poisson Process Inter-arrival Times]({{ site.github.repo }}{{ site.baseurl }}/2018/04/23/intro-poisson-dist-interarrival/).  
>&#10114;in this question, <font color="DeepSkyBlue">the most beautiful k-th random arrival takes place at the k-th moment of time interval unit.  We need to transform the correct interval unit from the reciprocal value of the given rate.</font>  
>The time interval unit would be $\frac {1}{\lambda}$.  The k-th random arrival takes place at the k-th time interval unit, $\frac {k}{\lambda}$, in this example is $\frac {8}{6}$.  
>&#10115;we have already proved that <font color="DeepPink">$f_{X_{n}}(t)$=$\frac {\lambda\cdot(\lambda\cdot t)^{n-1}\cdot e^{-\lambda\cdot t}}{(n-1)!}$, for $n$=$1$,$2$,..., where $\Gamma(n)$=$(n-1)!$</font>.  Then the probability of the <font color="OrangeRed">8-th vehicle</font> passing through the toll station at the <font color="OrangeRed">8-th time interval unit</font> would be calculated in this way.  
>$f_{X_{8}}(\frac {8}{6})$  
>=$\frac {6\cdot(6\cdot \frac {8}{6})^{7}\cdot e^{-6\cdot \frac {8}{6}}}{(7)!}$  
>=$0.8375191$  
>
><font color="DeepSkyBlue">[2]</font>
><font color="Black">What is the probability of the $8$-th, $12$-th, $16$-th car passing by at the $3$-rd time interval unit?</font>  
>&#10112;$f_{X_{8}}(\frac {3}{6})$  
>=$\frac {6\cdot(6\cdot \frac {3}{6})^{7}\cdot e^{-6\cdot \frac {3}{6}}}{(7)!}$  
>=$0.12962418871490290869$  
>&#10113;$f_{X_{12}}(\frac {3}{6})$  
>=$\frac {6\cdot(6\cdot \frac {3}{6})^{11}\cdot e^{-6\cdot \frac {3}{6}}}{(11)!}$  
>=$0.00132570193003877975$  
>&#10114;$f_{X_{16}}(\frac {3}{6})$  
>=$\frac {6\cdot(6\cdot \frac {3}{6})^{15}\cdot e^{-6\cdot \frac {3}{6}}}{(15)!}$  
>=$0.00000327783444240358$  
>
>We can easily tell, <font color="DeepPink">the arrivals in the time interval unit of the order less than it, the probability would just decrease almost to $0$ as the order of arrival increases</font>.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="Black">What is the probability of the $5$-th, $4$-th car passing by at the $5$-th, $4$-th time interval unit?</font>  
>&#10112;$f_{X_{5}}(\frac {5}{6})$  
>=$\frac {6\cdot(6\cdot \frac {5}{6})^{4}\cdot e^{-6\cdot \frac {5}{6}}}{(4)!}$  
>=$1.05280421860710423385$  
>&#10113;$f_{X_{4}}(\frac {4}{6})$  
>=$\frac {6\cdot(6\cdot \frac {4}{6})^{3}\cdot e^{-6\cdot \frac {4}{6}}}{(3)!}$  
>=$1.1722008888789875388$  
>
>There exists <font color="DeepSkyBlue">no probability larger than $1.0$</font>, above answer from gamma PDF just guarantees that <font color="DeepSkyBlue">$5$-th, $4$-th car passing by at the $5$-th, $4$-th time interval unit would definitely happen</font>.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="Black">All we have done is by assuming that <font color="RosyBrown">each i-th event arrival occurrs at the i-th time interval unit, this is not the normal case</font>!!!</font>  
>&#10112;we can have a more random question about the probability of $10$-th car passing by after 10 minutes.  
>$f_{X_{10}}(10)$  
>=$\frac {6\cdot(6\cdot 10)^{9}\cdot e^{-6\cdot 10}}{(9)!}$  
>=$0.00000000000000145908$  
>This is <font color="OrangeRed">quiet small</font> probability for the $10$-th car passing by after 10 minutes, given that 6 cars would just across every one minute is the constant rate.  
>&#10113;we then regularize the question by the probability of $60$-th car passing by after 10 minutes.  
>$f_{X_{60}}(10)$  
>=$\frac {6\cdot(6\cdot 10)^{59}\cdot e^{-6\cdot 10}}{(59)!}$  
>=$0.30859046994207513678$  
>This is a <font color="OrangeRed">much higher</font> probability than the probability for $10$-th car passing by after 10 minutes.  
>&#10113;we then ask the question by the probability of $59$-th car passing by after 10 minutes.  
>$f_{X_{59}}(10)$  
>=$\frac {6\cdot(6\cdot 10)^{58}\cdot e^{-6\cdot 10}}{(58)!}$  
>=$0.30344729544304055116$  
>It's a <font color="DeepSkyBlue">little</font> smaller.  
>&#10114;we then ask the question by the probability of $25$-th car passing by after 10 minutes.  
>$f_{X_{25}}(10)$  
>=$\frac {6\cdot(6\cdot 10)^{24}\cdot e^{-6\cdot 10}}{(24)!}$  
>=$0.00000040124226676254$  
>It's <font color="OrangeRed">much</font> smaller.  
>
>As we can tell that <font color="DeepPink">the most optimized probability of random arrival by means of the gamma distribution would be the order of arrival is in 100 percent proportional to the time length it takes, given that the rate is a constant over time!!</font>  
>&#10115;soon we verify it with the case the $25$-th arrival at $25$-th time interval unit, that is  
>$f_{X_{25}}(\frac {25}{6})$  
>=$\frac {6\cdot(6\cdot \frac {25}{6})^{24}\cdot e^{-6\cdot \frac {25}{6}}}{(24)!}$  
>=$0.4771377088083926763$  
>Next, compare it with the $15$-th arrival at $25$-th time interval unit, that is  
>$f_{X_{15}}(\frac {25}{6})$  
>=$\frac {6\cdot(6\cdot \frac {25}{6})^{14}\cdot e^{-6\cdot \frac {25}{6}}}{(14)!}$  
>=$0.03560745811847304799$  
>Here we concrete above conclusion.  
>
><font color="DeepSkyBlue">[5]</font>
><font color="Black">We are here with below probability as a summary</font> for the final finding.  
>$f_{X_{8}}(\frac {8}{6})$=$0.8375191$  
>$f_{X_{25}}(\frac {25}{6})$=$0.4771377088083926763$  
>$f_{X_{60}}(10)$=$0.30859046994207513678$, where $10$=$\frac {60}{6}$  
>
><font color="DeepSkyBlue">As the event arrives at the time interval unit of appropriate proportion, which is also more closed to $1$, like $\frac {8}{6}$, it will just have higher probability by using the gamma distribution for a prediction.</font>  

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