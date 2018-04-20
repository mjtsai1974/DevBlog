---
layout: post
title: Introduction To The Gamma Distribution
---

## Prologue To The Gamma Distribution
<p class="message">
In probability theory and statistics, the gamma distribution is the most fundamental, which is based on for further development of many distributions, they are beta, exponential, F, chi-square, t distributions and still others.
With the basic intuition of gamma distribution would it be greatly helpful in the evaluation of the regression model build on your hypothesis, even more, the power of test for the precision in the machine learning results.   
</p>

### The Gamma Function <font color="Red">$\Gamma$</font>
>It is very important in the gamma distribution, first of all, we take not only a glance over it, but go through some of the major properties of it.  The gamma function comes in the definition:  
>$\Gamma(\alpha)$=$\int_0^\infty x^{\alpha-1}\cdot e^{-x}\operatorname dx$, where $\alpha>0$.  
>
>Taking advantage of <font color="DeepSkyBlue">integration by part</font>:  
>Let $u=x^{\alpha-1}$, $\operatorname dv$=$e^{-x}\operatorname dx$, then,  
>$\operatorname du$=$(\alpha-1)\cdot x^{\alpha-2}$, $v$=$-e^{-x}$.  
>
>$\Gamma(\alpha)$=$x^{\alpha-1}\cdot(-e^{-x})\vert_0^\infty$-$\int_0^\infty -e^{-x}\cdot (\alpha-1)\cdot x^{\alpha-2}\operatorname dx$  
>$\;\;\;\;\;\;\;$=$0$+$\int_0^\infty e^{-x}\cdot (\alpha-1)\cdot x^{\alpha-2}\operatorname dx$  
>$\;\;\;\;\;\;\;$=$(\alpha-1)\cdot\int_0^\infty e^{-x}\cdot x^{\alpha-2}\operatorname dx$  
>$\;\;\;\;\;\;\;$=$(\alpha-1)\cdot\Gamma(\alpha-1)$  
>
>$\Gamma(5)=4\cdot\Gamma(4)$, therefore, we can deduce it out that: 
>$\Gamma(\alpha)$=$(\alpha-1)\cdot\Gamma(\alpha-1)$  
>$\;\;\;\;\;\;\;$=$(\alpha-1)\cdot(\alpha-2)\cdot\Gamma(\alpha-2)$=$\cdots$  
>
>[1]the corollary has it that:  
>$\Gamma(n)$=$(n-1)\cdot(n-2)\cdot(n-3)\cdots\Gamma(1)$  
>,where $\Gamma(1)$=$\int_0^\infty x^0\cdot e^{-x}\operatorname dx$=$-e^{-x}\vert_0^\infty$=$1$  
>, thus, <font color="DeepPink">$\Gamma(n)=(n-1)!$</font> is obtained. 
>
>[2]<font color="DeepPink">$\Gamma(\frac{1}{2})$=$\sqrt{\mathrm\pi}$</font>  
>There exists some alternatives, either way could be:  
>proof::&#10112;  
>As we don't like $-\frac{1}{2}$, by means of <font color="DeepSkyBlue">change unit</font>,  
>let $x$=$u^2$, then, $\operatorname dx$=$2\cdot u\operatorname du$:  
>$\Gamma(\frac{1}{2})$=$\int_0^\infty x^{-\frac{1}{2}}\cdot e^{-x}\operatorname dx$  
>$\;\;\;\;\;\;\;$=$\int_0^\infty u^{-1}\cdot e^{-u^{2}}\cdot 2\cdot u\operatorname du$  
>$\;\;\;\;\;\;\;$=$2\cdot\int_0^\infty e^{-u^{2}}\operatorname du$  
>
>Take $I$=$\int_0^\infty e^{-u^{2}}\operatorname du$, then,  
>$I^2$=$\int_0^\infty e^{-x^{2}}\operatorname dx$&nbsp;$\int_0^\infty e^{-y^{2}}\operatorname dy$  
>$\;\;\;\;$=$\int_0^\infty\int_0^\infty e^{-(x^{2}+y^{2})}\operatorname dx\operatorname dy$  
>
>Guess what?  We just transform our integral to the <font color="OrangeRed">quadrant one</font>.  
>Take $r^2$=$x^2$+$y^2$, we can have below two sets of deduction:  
>&#10112;$\frac{\operatorname dr^2}{\operatorname dx}$=$\frac{\operatorname d(x^2+y^2)}{\operatorname dx}$=$2\cdot x$  
>$\Rightarrow\operatorname dr^2$=$2\cdot x\operatorname dx$  
>
>&#10113;$\frac{\operatorname dr^2}{\operatorname dr}$=$\frac{\operatorname d(x^2+y^2)}{\operatorname dr}$  
>$\Rightarrow 2\cdot r$=$\frac{\operatorname d(x^2+y^2)}{\operatorname dr}$  
>$\Rightarrow 2\cdot r\operatorname dr$=$\operatorname d(x^2+y^2)$  
>$\Rightarrow 2\cdot r\frac{\operatorname dr}{\operatorname dx}$=$2\cdot x$  
>$\Rightarrow r\operatorname dr$=$x\operatorname dx$  
>
>Replace &#10112; and &#10113; in below integral:  
>$\int_0^\infty e^{-r^{2}}\operatorname dr^2$  
>$=\int_0^\infty e^{-r^{2}}\frac{\operatorname dr^2}{\operatorname dx}\cdot\operatorname dx$  
>$=\int_0^\infty e^{-r^{2}}\cdot 2\cdot x\operatorname dx$  
>$=\int_0^\infty \cdot 2\cdot r\cdot e^{-r^{2}}\operatorname dr$  
>$=-e^{r^{2}}\vert_0^\infty$  
>$=1$    
>
>Please recall that we have our integration area in <font color="OrangeRed">quadrant one</font>, at this moment, back to $I$, let $\theta=y$ to integrate from $0$ to $\frac{\pi}{2}$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-29-intro-gamma-dist-int-quadrant-1.png "integral in quadrant 1")
>$I^2$=$\int_0^{\frac{\pi}{2}}\int_0^\infty e^{-r^{2}}\operatorname dr^2\operatorname d\theta$  
>$\;\;\;\;$=$\int_0^{\frac{\pi}{2}}\operatorname d\theta$&nbsp;$\int_0^\infty e^{-r^{2}}\cdot x\operatorname dx$  
>$\;\;\;\;$=$\frac{\pi}{2}$&nbsp;$\int_0^\infty e^{-r^{2}}\cdot r\operatorname dr$  
>$\;\;\;\;$=$\frac{\pi}{2}\cdot(-\frac{1}{2}\cdot e^{-r^{2}})\vert_0^\infty$  
>$\;\;\;\;$=$\frac{\pi}{2}\cdot(-\frac{1}{2})$  
>$\;\;\;\;$=$\frac{\pi}{4}$
>
>$\Gamma(\frac{1}{2})$=$2\cdot\int_0^\infty e^{-u^{2}}\operatorname du$=$2\cdot I$, where $I$=$\int_0^\infty e^{-u^{2}}\operatorname du$ is something we have already known.  
>Therefore, $I^2$=$\frac{\pi}{4}$, and $I$=$\frac{\sqrt\pi}{2}$, finally, we have $\Gamma(\frac{1}{2})$=$\sqrt\pi$ thus proved.  
>
>proof::&#10113;  
>$\Gamma(\frac{1}{2})$=$\int_0^\infty x^{-\frac{1}{2}}\cdot e^{-x}\operatorname dx$, here we are again.  
>Take $x$=$\frac {z^2}{2}$, then, $\frac {\operatorname dx}{\operatorname dz}$=$z$, thus, we have $\operatorname dx$=$z\operatorname dz$  
>$\int_0^\infty x^{-\frac{1}{2}}\cdot e^{-x}\operatorname dx$  
>$=\int_0^\infty (\frac {z^2}{2})^{-\frac{1}{2}}\cdot e^{-\frac {z^2}{2}}z\operatorname dz$  
>$=\int_0^\infty \sqrt2\cdot z^{-1}\cdot e^{-\frac {z^2}{2}}z\operatorname dz$  
>$=\sqrt2\int_0^\infty e^{-\frac {z^2}{2}}z\operatorname dz$  
>$=2\cdot\sqrt\pi\int_0^\infty \frac {1}{\sqrt2\cdot\pi}\cdot e^{-\frac {z^2}{2}}z\operatorname dz$  
>$=2\cdot\sqrt\pi\cdot\frac {1}{2}$  
>$=\sqrt\pi$  
>
>where <font color="DeepPink">$\int_{-\infty}^\infty \frac {1}{\sqrt2\cdot\pi}\cdot e^{-\frac {z^2}{2}}z\operatorname dz=1$</font> is the accumulative probability of <font color="DeepSkyBlue">normal distribution</font>, therefore, <font color="DeepPink">$\int_0^\infty \frac {1}{\sqrt2\cdot\pi}\cdot e^{-\frac {z^2}{2}}z\operatorname dz=\frac {1}{2}$</font>.  

### The <font color="Red">PDF</font> of Gamma Distribution
>Next we inspect the PDF(probability density function) of the gamma distribution.  The $f(x)$ of PDF is expressed as:  
>$f(x)=\frac {1}{\beta^{\alpha}\cdot\Gamma(\alpha)}\cdot x^{\alpha-1}\cdot e^{-\frac{x}{\beta}}$  
>$\;\;\;\;\;\;=\frac {1}{\beta\cdot\Gamma(\alpha)}\cdot (\frac{x}{\beta})^{\alpha-1}\cdot e^{-\frac{x}{\beta}}$  
>$\;\;\;\;\;\;=\frac {\frac {1}{\beta}\cdot(\frac{x}{\beta})^{\alpha-1}\cdot e^{-\frac{x}{\beta}}}{\Gamma(\alpha)}$  
>, where $\alpha>0$, $\beta>0$  
>
>By taking $\lambda=\frac{1}{\beta}$, then, we just have it that:  
>$f(x)=\frac {\lambda\cdot(\lambda\cdot x)^{\alpha-1}\cdot e^{-\lambda\cdot x}}{\Gamma(\alpha)}$ 
>
>What do we mean by the parameters $\alpha$, $\beta$, $\lambda$?  
>&#10112;$\alpha$ is for the <font color="DeepSkyBlue">sharpness</font> of the distribution.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-29-intro-gamma-dist-pdf-alpha.png "alpha for sharpness")
>&#10113;the <font color="DeepSkyBlue">spread</font> or <font color="DeepSkyBlue">dissemination</font> of the distribution could be resort to $\beta$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-29-intro-gamma-dist-pdf-beta.png "alpha for spread")
>&#10114;$\lambda$ is for the <font color="DeepSkyBlue">intensity</font>, that is, the <font color="DeepSkyBlue">rate</font>, <font color="DeepSkyBlue">frequency</font>, in the form of $\frac {count}{time unit}$.  

### Expect Value And Variance Of Gamma Distribution
>As we know that it is the PDF of the gamma distribution:  
>$f(x)=\frac {1}{\beta^{\alpha}\cdot\Gamma(\alpha)}\cdot x^{\alpha-1}\cdot e^{-\frac{x}{\beta}}$  
>
>Next to figure out the expect value and variance of the gamma distribution.  The suggestion would be made that we should take advantage of the <font color="Red">moment</font> in [Introduction To The Moment Generating Function]({{ site.github.repo }}{{ site.baseurl }}/2017/12/28/intro-mgf/).  
>
>$E\lbrack X^k\rbrack$=$\frac{1}{\beta^{\alpha}\cdot\Gamma(\alpha)}\int_0^{\infty}x^{k}\cdot x^{\alpha-1}\cdot e^{-\frac{x}{\beta}}\operatorname dx$  
>Let $y=\frac{x}{\beta}$, and we can have, $\operatorname dy=\frac{1}{\beta}\operatorname dx$, then:  
>$E\lbrack X^k\rbrack$=$\frac{1}{\beta^{\alpha}\cdot\Gamma(\alpha)}\int_0^{\infty}x^{k+\alpha-1}\cdot e^{-\frac{x}{\beta}}\operatorname dx$  
>$\;\;\;\;\;\;\;\;=\frac{1}{\beta^{\alpha}\cdot\Gamma(\alpha)}\int_0^{\infty}(\beta\cdot y)^{k+\alpha-1}\cdot e^{-y}\cdot\beta\operatorname dy$  
>$\;\;\;\;\;\;\;\;=\frac{\beta^{k+\alpha-1}\cdot\beta}{\beta^{\alpha}\cdot\Gamma(\alpha)}\int_0^{\infty}(y)^{k+\alpha-1}\cdot e^{-y}\operatorname dy$  
>$\;\;\;\;\;\;\;\;=\frac{\beta^{k}}{\Gamma(\alpha)}\int_0^{\infty}(y)^{k+\alpha-1}\cdot e^{-y}\operatorname dy$  
>$\;\;\;\;\;\;\;\;=\frac{\beta^{k}}{\Gamma(\alpha)}\cdot\Gamma(k+\alpha)$  
>
>&#10112;$E\lbrack X\rbrack$=$\mu_1$, the first ordinary moment, by taking $k=1$, we can have the expected value expressed as:  
>$E\lbrack X\rbrack$=$\frac{\beta}{\Gamma(\alpha)}\cdot\Gamma(1+\alpha)$=$\beta\cdot\alpha$  
>&#10113;$Var\lbrack X\rbrack=E\lbrack X^2\rbrack-E^2\lbrack X\rbrack$, by taking $k=2$, we can obtain $E\lbrack X^2\rbrack$=$\mu_2$, the second ordinary moment, and have the expression of the variance:  
>$Var\lbrack X\rbrack$=$\frac{\beta^{2}}{\Gamma(\alpha)}\cdot\Gamma(2+\alpha)$-$(\beta\cdot\alpha)^2$  
>$\;\;\;\;\;\;=\beta^{2}\cdot(\alpha+1)\cdot(\alpha)$-$(\beta\cdot\alpha)^2$  
>$\;\;\;\;\;\;=\beta^2\cdot\alpha\cdot(\alpha-1-\alpha)$  
>$\;\;\;\;\;\;=\beta^2\cdot\alpha$  

<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha</font> -->
<!-- <font color="Green">new alpha</font> -->

<!-- <font color="DeepPink">positive conclusion, finding</font> -->
<!-- <font color="DimGray">negative conclusion, finding</font> -->

<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->