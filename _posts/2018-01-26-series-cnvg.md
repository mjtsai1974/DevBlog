---
layout: post
title: Series Convergence
---

## Prologue To The Series <font color="DeepPink">Convergence</font>
<p class="message">
Series is a collection of the data ordered by indices, maybe in a time sequence manner, pervasively by monotonic increasing numbers.  This article will inspect the <font color="DeepPink">convergence</font> versus <font color="RosyBrown">divergence</font> of a given series.
<font color="DeepSkyBlue">The convergence of series</font> could be a key factor in some topics in reinforcement learning, usually in a <font color="DeepSkyBlue">discounted representation of value function</font> deduction.
</p>

### Begin By <font color="OrangeRed">Geometric Series</font>
>&#10112;this is a geometric series, $1$,$x$,$x^2$,$x^3$,..., when you sum them up, then $1$+$x$+$x^2$+$x^3$+...=$\frac {1-x^{n+1}}{1-x}$, and why?  
>Since $1+x$=$\frac {1-x^2}{1-x}$,$1+x+x^2$=$\frac {1-x^3}{1-x}$,...,then, $1+x+x^2+...+x^{n-1}$=$\frac {1-x^n}{1-x}$  
>
>&#10113;what $1$+$x$+$x^2$+$x^3$+...finally becomes?  
>This equates to the discussion of the case when n approaches infinity:  
>When <font color="DeepPink">$\left|x\right|<1$</font>, it <font color="DeepPink">converges</font> and $\lim_{n\rightarrow\infty}\frac {1-x^n}{1-x}$=$\lim_{n\rightarrow\infty}\frac {1}{1-x}$  
>When <font color="RosyBrown">$\left|x\right|>1$</font>, it <font color="RosyBrown">divergence</font> and $\lim_{n\rightarrow\infty}\frac {1-x^n}{1-x}$=$\lim_{n\rightarrow\infty}\frac {1-x^n}{1-x}$  
>
>&#10114;by directly dividing, we have:
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-26-series-cnvg-direct-divide.png "direct div for geometric series")
>This says $1+x+x^2+...+x^{n-1}$=$\frac {1}{1-x}$  

### What's The Function Of $1$-$x$+$x^2$-$x^3$+$x^4$-$x^5$+...?
>Let $f(x)$=$1$-$x$+$x^2$-$x^3$+$x^4$-$x^5$+..., then their first, second, third, forth order derivative are below:  
>$f^{(1)}(x)$=$-1$+$2\cdot x$-$3\cdot x^2$+$4\cdot x^3$-$5\cdot x^4$+...  
>$f^{(2)}(x)$=$2$-$6\cdot x$+$12\cdot x^2$-$20\cdot x^3$+...  
>$f^{(3)}(x)$=$-6$+$24\cdot x$-$60\cdot x^2$+...  
>$f^{(4)}(x)$=$24$-$120\cdot x$+...  
>
>Departure from $x$=$0$, where $\triangle x\rightarrow 0$, thus:  
>$\lim_{\triangle x\rightarrow 0}f(x+\triangle x)$  
>$\approx\lim_{\triangle x\rightarrow 0}f(\triangle x)$  
>$=f(0)$+$f^{(1)}(0)\cdot\triangle x$+$\frac {1}{2}\cdot f^{(2)}(0)\cdot(\triangle x)^2$+$\frac {1}{6}\cdot f^{(3)}(0)\cdot(\triangle x)^3$+...  
>$=1$-$\triangle x$+$(\triangle x)^2$-$(\triangle x)^3$+$(\triangle x)^4$-$(\triangle x)^5$+...
>
><font color="DeepSkyBlue">Replace $\triangle x$ by $x$, we finally have $f(x)$</font>, then:  
>&#10112;let $f(x)$=$\frac {1}{x}$, then $f(0)$=$\infty$, boom!  
>&#10113;let $f(x)$=$\frac {1}{x-1}$, then $f(0)$=$-1$, a contradiction!  
>&#10114;let $f(x)$=$\frac {1}{1-x}$, then:  
>$f(0)$=$1$  
>$f^{(1)}(0)$=$-(1-x)^{-2}$=$-1$  
>$f^{(2)}(0)$=$-2\cdot(1-x)^{-3}$=$-2$, boom!  
>&#10115;let $f(x)$=$\frac {1}{1+x}$, then:  
>$f(0)$=$1$  
>$f^{(1)}(0)$=$-(1+x)^{-2}$=$-1$  
>$f^{(2)}(0)$=$2\cdot(1+x)^{-3}$=$2$, looks good    
>$f^{(3)}(0)$=$-6\cdot(1+x)^{-4}$=$-6$, still holds  
>$f^{(4)}(0)$=$24\cdot(1+x)^{-5}$=$24$, wow, that's it  
>
>Thus, $f(x)$=$\frac {1}{1+x}$ just satisfies this series.  

### The Integral Of Series
>&#10112;by given that $1+x+x^2+...+x^{n-1}$=$\frac {1}{1-x}$, as $n\rightarrow\infty$  
>Then, $\int 1+x+x^2+...\operatorname dx$=$\int\frac {1}{1-x}\operatorname dx$  
>$\Rightarrow x+\frac {1}{2}\cdot x^2+\frac {1}{3}\cdot x^3+...$=$-ln(1-x)$  
>&#10113;by given that $1$-$x$+$x^2$-$x^3$+$x^4$-$x^5$+...+$(x)^{n-1}$=$\frac {1}{1+x}$, as $n\rightarrow\infty$  
>then, $\int 1-x+x^2-x^3+x^4-x^5+...\operatorname dx$=$\int\frac {1}{1+x}$  
>$\Rightarrow x-\frac {1}{2}\cdot x^2+\frac {1}{3}\cdot x^3-\frac {1}{4}\cdot x^4+\frac {1}{5}\cdot x^5...$=$ln(1+x)$  
>&#10114;$\int 1+x+x^2+...\operatorname dx$+$\int 1-x+x^2-x^3+x^4-x^5+...\operatorname dx$  
>$\;\;$=$x+\frac {1}{2}\cdot x^2+\frac {1}{3}\cdot x^3+...$+$x-\frac {1}{2}\cdot x^2+\frac {1}{3}\cdot x^3...$  
>$\;\;$=$2\cdot(x+\frac {1}{3}\cdot x^3+\frac {1}{5}\cdot x^5...)$  
>$\;\;$=$-ln(1-x)$+$ln(1+x)$  
>$\;\;$=$ln(1+x)$-$ln(1-x)$  
>$\;\;$=$ln\frac {1+x}{1-x}$...magic  

### <font color="DeepPink">Convergence</font> Test
>[1]Definition of <font color="OrangeRed">partial sum</font>  
>The <font color="OrangeRed">partial sum $S_n$</font> of the series $a_1$+$a_2$+$a_3$+... stops at $a_n$, then <font color="OrangeRed">the sum of the first n tems</font> is $S_n$=$a_1$+$a_2$+$a_3$+...+$a_n$.  
>Thus, <font color="OrangeRed">$S_n$</font> is part of the total sum.  
>
>Ex. the series $\frac {1}{2}$+$\frac {1}{4}$+$\frac {1}{8}$+...has partial sums:  
>$S_1$=$\frac {1}{2}$,$S_2$=$\frac {3}{4}$,$S_3$=$\frac {7}{8}$,...,$S_n$=$1-\frac {1}{2^n}$  
>$\frac {1}{2}$+$\frac {1}{4}$+$\frac {1}{8}$+...converges to $1$, because $S_n\rightarrow 1$, as $a\rightarrow\infty$.  


<!-- Γ -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- \overline{X_n} -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->
<!-- \lim_{t\rightarrow\infty} -->
<!-- \begin{array}{l}f'(x)\\f''(x)\\f'''(x)\\f''''(x)\end{array} -->

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