---
layout: post
title: Introduction To The Exponential Distribution
---

## Prologue To The <font color="Red">Exponential</font> Distribution
<p class="message">
In probability theory and statistics, the <font color="Red">exponential</font> distribution is the model of distribution further developed, base on the most fundamental gamma distribution.  
With the basic realization of gamma distributions, we could also treat the <font color="Red">exponential</font> distribution a <font color="DeepSkyBlue">special case of gamma</font> distribution.  
It would be greatly helpful in the evaluation of the experimental model build on your hypothesis, the power of test for the precision in the machine learning results.   
</p>

### The <font color="Red">Exponential</font> Distribution Illustration
>This article would like to guide you through a design of a simple case to generalize the <font color="Red">exponential</font> distribution.  
>
>&#10112;the experiment is proceeded with the assumption that $x$ is the <font color="DeepSkyBlue">rate</font> of event occurrence during one time interval $t$, totally, $x\cdot t$ events.  
>&#10113;suppose $V$ is the volumetric space where these events occur within.  Trivially, the success probability of event occurrence, we take it as $P_{success}$=$\frac {x\cdot t}{V}$, then the failure probability could be regarded as $P_{fail}$=$1-\frac {x\cdot t}{V}$.  
>&#10114;suppose the <font color="DeepSkyBlue">rate</font> $x$ do exist and <font color="OrangeRed">remain constant</font> over each disjoint interval for some event occurrence.  
>&#10115;each disjoint interval are of the same time length, say it $t$, and we further divide it into n subsections.  Then each subsection would have $P_{success}$=$\frac {x\cdot t}{V\cdot n}$, then the failure probability could be regarded as $P_{fail}$=$1-\frac {x\cdot t}{V\cdot n}$.  
>&#10116;we assume that <font color="DeepSkyBlue">each occurrence of the event in distinct subsection is independent</font>, the success v.s. failure probability in each subsection just matches the the Bernoulli distribution.  
>&#10117;let the random variable $T$ to be the time it takes until the very first event to occur, and the whole behavior follows the geometric distribution, if it takes time larger than time $t$ for the very first event to occur, then we have such probability:  
>$P(T>t)$=$\lim_{n\rightarrow\infty}(P_{fail})^{n}$=$\lim_{n\rightarrow\infty}(1-\frac {x\cdot t}{V\cdot n})^{n}$  
>
>$(1-\frac {x\cdot t}{V\cdot n})^{n}$  
>$=C_{0}^{n}1^{n}\cdot(-\frac {x\cdot t}{V\cdot n})^{0}$+$C_{1}^{n}1^{n-1}\cdot(-\frac {x\cdot t}{V\cdot n})^{1}$+$C_{2}^{n}1^{n-2}\cdot(-\frac {x\cdot t}{V\cdot n})^{2}$+...+$C_{n}^{n}1^{0}\cdot(-\frac {x\cdot t}{V\cdot n})^{n}$  
>
>Since $\lim_{n\rightarrow\infty}(-\frac {x\cdot t}{V\cdot n})=0$, then:  
>$P(T>t)$  
>$=\lim_{n\rightarrow\infty}(1-\frac {x\cdot t}{V\cdot n})^{n}$  
>$=\lim_{n\rightarrow\infty}1+(-\frac {x\cdot t}{V\cdot n})^{n}$  
>$\approx\lim_{n\rightarrow\infty}(1+\frac {-x\cdot t}{V\cdot n})^{n}$  
>
>Since $e$=$\lim_{n\rightarrow\infty}(1+\frac {1}{n})^{n}$, and  
>$e^{2}$=$\lim_{n\rightarrow\infty}((1+\frac {1}{n})^{n})^{2}$  
>$=\lim_{n\rightarrow\infty}((1+\frac {1}{n})^{2})^{n}$  
>$=\lim_{n\rightarrow\infty}(1+\frac {2}{n}+\frac {1}{n^{2}})^{n}$  
>$\approx\lim_{n\rightarrow\infty}(1+\frac {2}{n})^{n}$
>
>Then, $P(T>t)$=$e^{-\frac {x\cdot t}{V}}$  
>
>&#10118;therefore, $P(T\le t)$=$1-e^{-\frac {x\cdot t}{V}}$, it is the successful probability for events to occur within time $t$.  
>
>Above is just the basic illustration of the the <font color="Red">exponential</font> distribution.  Such scenario would be mostly found in chemical catalyst experiment, or fermentation test in biological laboratory.  

### Definition Of The <font color="Red">Exponential</font> Distribution
>Succeeding to the last paragraph, for the simplicity, we take $\lambda$=$\frac {x}{V}$ to be the <font color="DeepSkyBlue">rate</font>, the <font color="DeepSkyBlue">intensity</font>.  The CDF could be easily defined as below:  
>$F_{T}(t)$=$1-e^{-\lambda\cdot t}$=$P(T\le t)$  
>
>Derivate $F_{T}(t)$ on $t$, we then get its PDF below:  
>$f_{T}(t)$=$\frac{\operatorname d{F_{T}(t)}}{\operatorname d{t}}$=$\lambda\cdot e^{-\lambda\cdot t}$  
>
>To validate it,  
>$P(T\le a)$  
>$=\int_{0}^{a}\lambda\cdot e^{-\lambda\cdot t}\operatorname dt$  
>$=-e^{-\lambda\cdot t}\vert_{0}^{a}$  
>$=1-e^{-\lambda\cdot a}$, take $t$=$a$  

### Relationship With The Gamma Distribution
>Be recalled that the PDF of [the gamma distribution]({{ site.github.repo }}{{ site.baseurl }}/2017/12/29/intro-gamma-dist/):  
>$f_{X}(x)=\frac {1}{\beta^{\alpha}\cdot\Gamma(\alpha)}\cdot x^{\alpha-1}\cdot e^{-\frac{x}{\beta}}$  
>
>Take $\alpha$=$1$, $\lambda$=$\frac {1}{\beta}$, you can easily find that the <font color="Red">exponential</font> distribution a <font color="DeepSkyBlue">special case of gamma</font> distribution. Change $X$ to $T$, $x$ to $t$, they are exactly the same thing!!!  
>
>Below chart exhibits its PDF with regards to $\lambda$ set to $0.5$,$0.333$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-24-intro-exp-dist-pdf.png "exp dist pdf")
>Next chart illustrate the cumulative distribution with $\lambda$ set to $0.5$,$0.333$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-24-intro-exp-dist-cdf.png "exp dist cdf")

### Moments Of The <font color="Red">Exponential</font> Distribution
>The most efficient way to get the expect value and variance would be the moments.  
>&#10112;take $\alpha$=$1$, $\lambda$=$\frac {1}{\beta}$, we will have the moments below:  
>$\mu_{r}$=$E\lbrack X^{r}\rbrack$=$\frac {1}{\beta}\int_{0}^{\infty}x^{r}\cdot e^{-\frac {x}{\beta}}\operatorname dx$  
>
>&#10113;let $y$=$\frac {x}{\beta}$, $\operatorname dy$=$\frac {1}{\beta}\cdot\operatorname dx$, then:  
>$\mu_{r}$=$\frac {1}{\beta}\int_{0}^{\infty}(\beta\cdot y)^{r}\cdot e^{-y}\cdot\beta\cdot\operatorname dy$  
>$\;\;\;\;$=$\beta^{r}\int_{0}^{\infty}(y)^{r}\cdot e^{-y}\operatorname dy$  
>$\;\;\;\;$=$\beta^{r}\cdot\Gamma(r+1)$  
>
>Therefore, we have $\mu_1$=$\beta\cdot\Gamma(2)$=$\beta$  
>And $\mu_2$=$\beta^{2}\cdot\Gamma(3)$=$\beta^{2}\cdot 2\cdot\Gamma(2)$=$2\cdot\beta^{2}$  
>
>Finally, the expect value $\mu_{1}$=$E\lbrack X\rbrack$=$\beta$  
>The variance $Var\lbrack X\rbrack$=$E\lbrack X^2\rbrack$-$E^2\lbrack X\rbrack$=$\beta^{2}$  
>Recall that we take $\lambda$=$\frac {1}{\beta}$, hence, $E\lbrack X\rbrack$=$\frac {1}{\lambda}$, $Var\lbrack X\rbrack$=$(\frac {1}{\lambda})^2$  

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
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