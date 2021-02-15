---
layout: post
title: Introduction To The Beta Distribution
---

## Prologue To The <font color="Red">Beta</font> Distribution
<p class="message">
In probability theory and statistics, base on the most fundamental gamma distribution, <font color="Red">beta</font> distribution is one of the many models of distributions further developed.  
With the basic realization of gamma distributions, we could also treat the <font color="Red">beta</font> function a <font color="DeepSkyBlue">special combination of gamma</font> functions.  
The beta function is important in calculus and analysis due to its close connection to the gamma function, which is itself a generalization of the factorial function, and would be greatly 
helpful in the evaluation, the power of test for the regression model build on your hypothesis, the precision in the machine learning results.  
</p>

### Begin From The <font color="Red">Beta</font> Function
>The beta function, also known as Euler's integral of the first kind.  We formulate the <font color="Red">beta</font> function in below two expressions:  
>$\beta(x,y)$=$\int_{0}^{\infty}t^{x-1}\cdot(1+t)^{-x-y}\operatorname dt$...(1);  
>$\beta(x,y)$=$\int_{0}^{1}t^{x-1}\cdot(1-t)^{y-1}\operatorname dt$...(2);  
>Where (1)=(2), next to prove it.  
>
>proof:  
>&#10112;to change from $\int_{0}^{\infty}$ to $\int_{0}^{1}$, we focus on $t$:  
>$\int_{0}^{\infty}t^{x-1}\cdot(1+t)^{-x-y}\operatorname dt$  
>$=\int_{0}^{\infty}t^{x-1}\cdot(\frac {1}{1+t})^{x+y}\operatorname dt$  
>$=\int_{0}^{\infty}(\frac {t}{1+t})^{x-1}\cdot(\frac {1}{1+t})^{y+1}\operatorname dt$
>
>&#10113;take $w$=$\frac {t}{1+t}$, then $1-w$=$\frac {1}{1+t}$  
>$w$=$1-\frac {1}{1+t}$=$1-(1+t)^{-1}$  
>$\Rightarrow\frac {\operatorname dw}{\operatorname dt}$=$(\frac {1}{1+t})^{2}$  
>$\Rightarrow \operatorname dw$=$(\frac {1}{1+t})^{2}\cdot\operatorname dt$=$(1+t)^{-2}\cdot\operatorname dt$  
>$\Rightarrow \operatorname dt$=$(1+t)^{2}\cdot\operatorname dw$  
>
>&#10114;<font color="DeepPink">$\lim_{t\rightarrow\infty}\frac t{1+t}=1$</font>, therefore <font color="DeepSkyBlue">$\int_{0}^{\infty}\operatorname dt$ transforms to $\int_{0}^{1}\operatorname dw$ is reasonable</font>, it says that integration from $0$ to $\infty$ could be changed to integration from $0$ to $1$.  
>
>$\int_{0}^{\infty}(\frac {t}{1+t})^{x-1}\cdot(\frac {1}{1+t})^{y+1}\operatorname dt$  
>$=\int_{0}^{1}w^{x-1}\cdot(1-w)^{y+1}\cdot(1+t)^{2}\operatorname dw$  
>
>, where $1-w$=$(1+t)^{-1}$, and we have it that:  
>$(1+t)^{2}$=$((1+t)^{-1})^{-2}$=$(1-w)^{-2}$  
>therefore,  
>$=\int_{0}^{1}w^{x-1}\cdot(1-w)^{y+1}\cdot(1-w)^{-2}\operatorname dw$  
>$=\int_{0}^{1}w^{x-1}\cdot(1-w)^{y-1}\operatorname dw$  
>
>In some textbooks or web articles, they intend to use the form:  
>$\beta(x,y)$=$\int_{0}^{1}t^{x}\cdot(1-t)^{y}\operatorname dt$  
>The tiny difference mainly in the input parameters, $x\ge 1$, $y\ge 1$.  

### The Definition Of The <font color="Red">Beta</font> Function
>Next come to visit the definition of the <font color="Red">beta</font> function.  
>$\beta(x,y)$=$\frac {\Gamma(x)\cdot\Gamma(y)}{\Gamma(x+y)}$...by definition  
>
>proof:  
>&#10112;  
>$\Gamma(x)\cdot\Gamma(y)$  
>$=\int_{0}^{\infty}u^{x-1}\cdot e^{-u}\operatorname du\cdot\int_{0}^{\infty}v^{y-1}\cdot e^{-v}\operatorname dv$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}u^{x-1}\cdot v^{y-1}\cdot e^{-u-v}\operatorname du\operatorname dv$  
>
>&#10113;take $u$=$v\cdot t$, then $\operatorname du$=$v\cdot\operatorname dt$  
>why? <font color="OrangeRed">Because gamma function focus on the parameter of power, not integral itself</font>. Expand from &#10112;:  
>
>$\int_{0}^{\infty}\int_{0}^{\infty}u^{x-1}\cdot v^{y-1}\cdot e^{-(u+v)}\operatorname du\operatorname dv$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}v\cdot (v\cdot t)^{x-1}\cdot v^{y-1}\cdot e^{-(v\cdot t+v)}\operatorname dt\operatorname dv$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}t^{x-1}\cdot v^{x+y-1}\cdot e^{-(v\cdot t+v)}\operatorname dt\operatorname dv$  
>
>&#10114;take $w$=$v\cdot t+v$, then we have:  
>$v$=$\frac {w}{1+t}$, $\operatorname dv$=$\frac {1}{1+t}\cdot\operatorname dw$  
>
>$\int_{0}^{\infty}\int_{0}^{\infty}t^{x-1}\cdot v^{x+y-1}\cdot e^{-(v\cdot t+v)}\operatorname dt\operatorname dv$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}t^{x-1}\cdot (\frac {w}{1+t})^{x+y-1}\cdot e^{-w}\operatorname dt\frac {1}{1+t}\cdot\operatorname dw$  
>$=\int_{0}^{\infty}\int_{0}^{\infty}t^{x-1}\cdot (\frac {1}{1+t})^{x+y}\cdot w^{(x+y-1)}\cdot e^{-w}\operatorname dt\operatorname dw$  
>$=\int_{0}^{\infty}w^{(x+y-1)}\cdot e^{-w}\operatorname dw\cdot\int_{0}^{\infty}t^{x-1}\cdot(\frac {1}{1+t})^{x+y}\operatorname dt$  
>$=\Gamma(x+y)\cdot\int_{0}^{\infty}t^{x-1}\cdot (1+t)^{-x-y}\operatorname dt$  
>$=\Gamma(x+y)\cdot\beta(x,y)$  
>
>Finally, we just have it proved:  
>$\Gamma(x)\cdot\Gamma(y)$  
>$=\Gamma(x+y)\cdot\int_{0}^{\infty}t^{x-1}\cdot (1+t)^{-x-y}\operatorname dt$  
>$=\Gamma(x+y)\cdot\beta(x,y)$  
>$\Rightarrow\beta(x,y)=\frac {\Gamma(x)\cdot\Gamma(y)}{\Gamma(x+y)}$  

### <font color="DeepPink">Symmetry</font> Of The <font color="Red">Beta</font> Function
>$\beta(x,y)$=$\beta(y,x)$...$\beta$ is symmetric.  
>
>proof:  
>&#10112;begin by definition,  
>$\beta(x,y)$=$\int_{0}^{1}t^{x-1}\cdot(1-t)^{y-1}\operatorname dt$  
>
>&#10113;take $v$=$1-t$, then $t$=$1-v$  
>therefore, $\operatorname dv$=$-\operatorname dt$, $\operatorname dt$=$-\operatorname dv$  
>and $0\le t\le 1$, $-1\le -v\le 0$  
>
>&#10114;expand from <font color="Red">beta</font> function:  
>$\beta(x,y)$  
>$=\int_{0}^{1}t^{x-1}\cdot(1-t)^{y-1}\operatorname dt$  
>$=\int_{-1}^{0}(1-v)^{x-1}\cdot(v)^{y-1}(\operatorname -dv)$  
>$=\int_{-1}^{0}(1-v)^{x-1}\cdot(v)^{y-1}\operatorname d(-v)$...$\operatorname -dv=\operatorname d(-v)$  
>$=\int_{0}^{1}(1-v)^{x-1}\cdot(v)^{y-1}\operatorname dv$  
>$=\beta(y,x)$  
>
><font color="DeepPink">$\beta$ function is symmetric</font> is thus proved.  

### The <font color="Red">Beta</font> Distribution PDF
>For <font color="DeepPink">$0<x<1$</font> and <font color="DeepPink">$X$ is a random variable of beta distribution</font>, where <font color="DeepPink">$x\in X$</font>, the <font color="DeepPink">PDF</font> of <font color="Red">beta</font> distribution is defined below:  
><font color="DeepPink">$f_{X}(x)$=$\frac {1}{\beta(a,b)}\cdot x^{a-1}\cdot(1-x)^{b-1}$</font>
>
>Caution must be made that <font color="OrangeRed">$f_{X}(x)=0$ for the case $x\not\in [0,1]$</font>.  Next we go to prove it.  
>
>proof:  
>&#10112;departure from integrating its PDF from negative to positive infinity.  
>$\int_{-\infty}^{\infty}f_{X}(x)\operatorname dx$  
>$=\int_{-\infty}^{\infty}\frac {1}{\beta(a,b)}\cdot x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\int_{-\infty}^{\infty}x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>
>&#10113;suppose the definition of its PDF is true, we can integrate, ranging from $0$ to $1$:  
>$\frac {1}{\beta(a,b)}\int_{0}^{1}x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\beta(a,b)$  
>$=1$  
>
>Be recalled that <font color="OrangeRed">$f_{X}(x)=0$ for the case $x\not\in [0,1]$</font>  
>Below we exhibit the PDF of $\beta(1,4)$, $\beta(2,5)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-16-intro-beta-dist-pdf-1.png "the beta PDF 1")
>Then exhibit the PDF of $\beta(4,1)$, $\beta(5,2)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-16-intro-beta-dist-pdf-2.png "the beta PDF 2")
>Finally, the exhibition of PDF of $\beta(2,2)$, $\beta(4,4)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-16-intro-beta-dist-pdf-3.png "the beta PDF 3")
>You can find it more approximate normal distribution for we input parameters with $a=b$, and the graph would be right skew for $a<b$, and left skew for $a>b$.  

### The <font color="Red">Beta</font> Distribution CDF
>The CDF of <font color="Red">beta</font> distribution is defined below:  
><font color="DeepPink">$F_{X}(k)$=$\frac {\beta(k,a,b)}{\beta(a,b)}$=$\frac {\int_{0}^{k}x^{a-1}\cdot(1-x)^{b-1}}{\beta(a,b)}$</font>  
>
>proof:  
><font color="DeepPink">$F_{X}(k)$</font>  
>$=\int_{-\infty}^{k}f_X(x)\operatorname dx$  
>$=\int_{0}^{k}\frac {1}{\beta(a,b)}\cdot x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\int_{0}^{k}x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>
>, where we take $\beta(k,a,b)$=$\int_{0}^{k}x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>
>In general, two CDFs could be further defined:  
>&#10112;<font color="OrangeRed">lower</font> CDF, $\frac {\int_{0}^{k}x^{a-1}\cdot(1-x)^{b-1}}{\beta(a,b)}$, where $k\le 1$.  
>&#10113;<font color="OrangeRed">upper</font> CDF, $\frac {\int_{k}^{1}x^{a-1}\cdot(1-x)^{b-1}}{\beta(a,b)}$  

### Expect Value Of The <font color="Red">Beta</font> Distribution
>For any <font color="OrangeRed">valid</font> random variable X of <font color="Red">beta</font> distribution, the expect value is given:  
>$E\lbrack X\rbrack$=$\frac {a}{a+b}$  
>
>proof:  
>$E\lbrack X\rbrack$  
>$=\int_{0}^{\infty}x\cdot\frac {1}{\beta(a,b)}\cdot x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\int_{0}^{\infty}x^{a}\cdot(1-x)^{b-1}\operatorname dx$  
>$=(\frac {\Gamma(a)\cdot\Gamma(b)}{\Gamma(a+b)})^{-1}\cdot\beta(a+1,b)$  
>$=\frac {\Gamma(a+b)}{\Gamma(a)\cdot\Gamma(b)}\cdot\frac {\Gamma(a+1)\cdot\Gamma(b)}{\Gamma(a+b+1)}$  
>$=\frac {\Gamma(a+b)}{\Gamma(a)\cdot\Gamma(b)}\cdot\frac {a\cdot\Gamma(a)\cdot\Gamma(b)}{(a+b)\cdot\Gamma(a+b)}$  
>$=\frac {a}{a+b}$  

### Variance Of The <font color="Red">Beta</font> Distribution
>For any <font color="OrangeRed">valid</font> random variable X of <font color="Red">beta</font> distribution, the variance is given:  
>$Var\lbrack X\rbrack$=$\frac {a\cdot b}{(a+b+1)\cdot(a+b)^{2}}$  
>
>proof:  
>$Var\lbrack X\rbrack$=$E\lbrack X^{2}\rbrack$-$E^{2}\lbrack X\rbrack$, to figure out the variance, the term $E\lbrack X^{2}\rbrack$ should be come out.  
>
>$E\lbrack X^{2}\rbrack$  
>$=\int_{0}^{\infty}x^{2}\cdot\frac {1}{\beta(a,b)}\cdot x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\int_{0}^{\infty}\frac {1}{\beta(a,b)}\cdot x^{a+1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\int_{0}^{\infty}x^{a+1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\beta(a+2,b)$  
>
>$Var\lbrack X\rbrack$  
>$=\frac {1}{\beta(a,b)}\cdot\beta(a+2,b)$-$(\frac {a}{a+b})^{2}$  
>...after deduction...  
>$=\frac {a\cdot b}{(a+b+1)\cdot(a+b)^{2}}$  

### <font color="OrangeRed">k-th Moment</font> Of <font color="Red">Beta</font> Random Variable
><font color="OrangeRed">$\mu_{k}$</font>  
>$=E\lbrack X^{k}\rbrack$  
>$=\frac {\beta(a+k,b)}{\beta(a,b)}$  
>$={\textstyle\prod_{n=0}^{k-1}}\frac{a+n}{a+b+n}$  
>
>proof:  
>$E\lbrack X^{k}\rbrack$  
>$=\int_{0}^{\infty}x^{k}\cdot\frac {1}{\beta(a,b)}\cdot x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\int_{0}^{\infty}x^{a+k-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {\Gamma(a+b)}{\Gamma(a)\cdot\Gamma(b)}\cdot\frac {\Gamma(a+k)\cdot\Gamma(b)}{\Gamma(a+b+k)}$  
>$=\frac {\Gamma(a+b)}{\Gamma(a)\cdot\Gamma(b)}\cdot\frac {(a+k-1)\cdot(a+k-2)...a\cdot\Gamma(a)\cdot\Gamma(b)}{(a+b+k-1)\cdot(a+b+k-2)...(a+b)\cdot\Gamma(a+b)}$  
>$=\frac {a\cdot(a+1)\cdot(a+2)...(a+k-2)\cdot(a+k-1)}{(a+b)\cdot(a+b+1)...(a+b+k-2)\cdot(a+b+k-1)}$  
>$={\textstyle\prod_{n=0}^{k-1}}\frac{a+n}{a+b+n}$  
>
>Where $X$ is any <font color="Red">beta</font> random variable, $x\in X$.  

### <font color="OrangeRed">Moment Generating Function</font> Of <font color="Red">Beta</font> Random Variable
><font color="OrangeRed">$M_{X}(t)$</font>  
>$=\sum_{k=0}^{\infty}\frac {t^{k}}{k!}\cdot\frac {\beta(a+k,b)}{\beta(a,b)}$  
>$=1+\sum_{k=1}^{\infty}\frac {t^{k}}{k!}\cdot\frac {\beta(a+k,b)}{\beta(a,b)}$  
>
>proof:  
><font color="OrangeRed">$M_{X}(t)$</font>  
>$=\int_{0}^{1}e^{x\cdot t}\cdot\frac {x^{a-1}\cdot(1-x)^{b-1}}{\beta(a,b)}\operatorname dx$...MGF's definition  
>$=\frac {1}{\beta(a,b)}\cdot\int_{0}^{1}e^{x\cdot t}\cdot x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\int_{0}^{1}(\sum_{k=0}^{\infty}\frac {(x\cdot t)^{k}}{k!})\cdot x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\sum_{k=0}^{\infty}\int_{0}^{1}\frac {(x\cdot t)^{k}}{k!}\cdot x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\sum_{k=0}^{\infty}\frac {t^{k}}{k!}\int_{0}^{1}x^{k}\cdot x^{a-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\sum_{k=0}^{\infty}\frac {t^{k}}{k!}\int_{0}^{1}x^{a+k-1}\cdot(1-x)^{b-1}\operatorname dx$  
>$=\frac {1}{\beta(a,b)}\cdot\sum_{k=0}^{\infty}\frac {t^{k}}{k!}\cdot\beta(a+k,b)$  
>$=\sum_{k=0}^{\infty}\frac {t^{k}}{k!}\frac {beta(a+k,b)}{\beta(a,b)}$  
>$=1+\sum_{k=1}^{\infty}\frac {t^{k}}{k!}\cdot\mu_{k}$  
>$=1+\sum_{k=1}^{\infty}\frac {t^{k}}{k!}\cdot E\lbrack X^{k}\rbrack$  
>$=1+\sum_{k=1}^{\infty}\frac {t^{k}}{k!}\cdot{\textstyle\prod_{n=0}^{k-1}}\frac{a+n}{a+b+n}$  
>  
>Where $X$ is any <font color="Red">beta</font> random variable, $x\in X$.  

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- \overline{X_n} -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->

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

<!-- http://keisan.casio.com/ -->
<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://homepage.tudelft.nl/11r49/documents/wi4006/gammabeta.pdf -->