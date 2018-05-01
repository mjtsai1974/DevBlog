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
>Hence, <font color="DeepPink">$\frac {1}{2}$+$\frac {1}{4}$+$\frac {1}{8}$+...converges to $1$, because $S_n\rightarrow 1$, as $a\rightarrow\infty$.</font>  
>
>[2]The <font color="RoyalBlue">limit</font> of <font color="OrangeRed">partial sum</font>  
>The <font color="DeepPink">sum of a series</font> is the <font color="DeepPink">limit of its partial sum</font>, for we can have a new idea that $\sum a_n$=$S$, where $S_n\rightarrow S$.  
>
>[3]<font color="DeepPink">Theorem:  
>If a series converges($S_n\rightarrow S$), then its terms must approach zero($a_n\rightarrow 0$).</font>  
>
>Proof:  
>By given that $S_n\rightarrow S$, it just converges,  
>then for $S_{n+1}$ of the $n+1$ terms, <font color="DeepPink">$S_{n+1}-S_n\rightarrow 0$</font> must hold to have $S_{n+1}\rightarrow S_n$, and $S_n\rightarrow S$ by given.  
>Therefore, the <font color="DeepPink">$(n+1)$th term must approaches zero!!</font>  

### Comparison Test
>[1]Comparison test: suppose that $0\le a_n\le b_n$ and $\sum b_n$ converges.  Then, $\sum a_n$ converges.  <font color="DeepPink">A series diverges, if it is above another diverged series.</font>  
>
>[2]Comparison test on harmonic series:  <font color="DeepPink">the harmonic series series $1$+$\frac {1}{2}$+$\frac {1}{3}$+$\frac {1}{4}$+...diverges to infinity.</font>  
>This section illustrates why by comparing the series with the curve $y$=$\frac {1}{x}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-01-26-series-cnvg-harmonic-diverge.png "harmonic series diverges")
>&#10112;for the rectangle <font color="OrangeRed">above</font> the curve, each rectangle area $a_n$=$\frac {1}{n}$, then:  
>$\sum a_n\ge\int_{1}^{n+1}\frac {1}{x}\operatorname dx$=$ln(n+1)$, where $\lim_{n\rightarrow\infty}ln(n+1)$=$\infty$  
>&#10113;for the area <font color="OrangeRed">below</font> the curve, we have it that:  
>$\frac {1}{2}$+$\frac {1}{3}$+$\frac {1}{4}$+...$<\int_{1}^{n}\frac {1}{x}\operatorname dx$=$ln(n)$, $\lim_{n\rightarrow\infty}ln(n)$=$\infty$  
>The reason we integrate up to $n$ only is due to that each rectangle at $x$ under the curve counts its area in the reciprocal of its next adjacent $x+1$, totally, $n-1$ rectangles.  
>Then $1$+$\frac {1}{2}$+$\frac {1}{3}$+$\frac {1}{4}$+...$<(1+ln(n))\rightarrow\infty$, as $n\rightarrow\infty$  
>
>Put it all together:  
>$ln(n+1)$<$1$+$\frac {1}{2}$+$\frac {1}{3}$+$\frac {1}{4}$+...<$1+ln(n)$  
>$\Rightarrow\infty$<$1$+$\frac {1}{2}$+$\frac {1}{3}$+$\frac {1}{4}$+...<$\infty$, as $a\rightarrow\infty$  
>
>By squeeze theorem, $1$+$\frac {1}{2}$+$\frac {1}{3}$+$\frac {1}{4}$+...$\rightarrow\infty$, it diverges!!

### Integral Test
>[1]If $y(x)$ is decreasing, and $y(n)$ agrees with $a_n$, then $a_1$+$a_2$+$a_3$+... and $\int_{0}^{\infty}y(x)\operatorname dx$ both converge or both diverge.  
>
>[2]The p-series $\frac {1}{2^p}$+$\frac {1}{3^p}$+$\frac {1}{4^p}$+$\frac {1}{5^p}$+... converges, if $p>1$.  
>proof:  
>&#10112;let $y$=$\frac {1}{x^p}$, then $\frac {1}{n^p}$<$\int_{n-1}^{n}\frac {1}{x^p}\operatorname dx$  
>&#10113;sum it up, we get:  
>$\sum_{n=2}^{\infty}\frac {1}{n^p}$<$\int_{1}^{\infty}\frac {1}{x^p}\operatorname dx$  
>$\;\;\;\;$=$\int_{1}^{\infty}x^{-p}\operatorname dx$  
>$\;\;\;\;$=$\frac {1}{-p+1}\cdot x\vert_1^\infty$  
>$\;\;\;\;$=$\frac {1}{1-p}\cdot(\infty^{-p+1}-1)$  
>&#10114;therefore, <font color="DeepSkyBlue">this series converges, if $p>1$,</font>  
>hence, $1$+$\sum_{2}^{\infty}\frac {1}{n^p}$<$1$+$\frac {1}{1-p}\cdot(0-1)$=$\frac {p}{p-1}$  

### <font color="Red">Ratio Test Theorem</font>
><font color="DeepPink">If $\frac {a_{n+1}}{a_n}$ approaches a limit $L<1$, the series converges.</font>  
>proof:  
>There is a hint that we can <font color="DeepSkyBlue">compare $a_1$+$a_2$+$a_3$+... with $1$+$x$+$x^2$+...</font>  
>&#10112;choose $L$<$x$<$1$, then we just have:  
>$\frac {a_{n+1}}{a_n}$<$x$,$\frac {a_{n+2}}{a_{n+1}}$<$x$,$\frac {a_{n+3}}{a_{n+2}}$<$x$,...  
>&#10113;multiply each inequality, we have:  
>$\frac {a_{n+1}}{a_n}$<$x$,$\frac {a_{n+2}}{a_{n}}$<$x^2$,$\frac {a_{n+3}}{a_{n}}$<$^3x$,...  
>$\Rightarrow a_{n+1}<a_{n}\cdot x$,$a_{n+2}<a_{n}\cdot x^2$,$a_{n+3}<a_{n}\cdot x^{3}$,...  
>$\Rightarrow a_{n+1}$+$a_{n+2}$+$a_{n+3}$+...<$a_n\cdot(x+x^2+x^3+...)$  
>$\Rightarrow a_{n+1}$+$a_{n+2}$+$a_{n+3}$+...<$a_n\cdot x\cdot(1+x+x^2+...)$  
>&#10114;since <font color="DeepPink">$x$<$1$, compare with the geometric series, $\sum a_n$ just converges.</font> 

### Root Test Theorem
><font color="DeepPink">If the n term in root $(a_n)^{\frac {1}{n}}$ approaches $L$<$1$, the series just converges.</font>  
>proof:  
>&#10112;$\lim_{n\rightarrow\infty}(a_n)^{\frac {1}{n}}\rightarrow L<1$...by given  
>$\Rightarrow(\lim_{n\rightarrow\infty}(a_n)^{\frac {1}{n}})^{n}\rightarrow L^n<1^n$  
>$\Rightarrow\lim_{n\rightarrow\infty}(a_n)\rightarrow L^n<1$  
>&#10113;then for the n+1 term, we just have it hold:  
>$\lim_{n\rightarrow\infty}(a_{n+1})\rightarrow L^{n+1}<1$  
>&#10114;$\lim_{n\rightarrow\infty}\frac {a_{n+1}}{a_n}\rightarrow\frac {L^{n+1}}{L^{n}}=L<1$, therefore, this series just converges.    

### Theorem: Limit Comparison Test
><font color="DeepPink">If the ratio $\frac {a_n}{b_n}$ approaches a positive limit $L$, then $\sum a_n$,$\sum b_n$ either diverge or converge.</font>  
>proof:  
>$\lim_{n\rightarrow\infty}\frac {a_n}{b_n}\rightarrow L>0$...by given  
>$\Rightarrow\lim_{n\rightarrow\infty}\frac {a_{n+1}}{b_{n+1}}\rightarrow L>0$, also holds  
>, which implies that $\sum a_n$,$\sum b_n$ are two very closed series, if one converges, another would surely does; for divergence, it is the same.  

### Convergence Tests: <font color="Red">All</font> Series
>[1]Definition of absolute convergence:  
><font color="DeepPink">The series $\sum a_n$ is absolutely convergent, if $\left|\sum a_n\right|$ converges.</font>  
>Why? This is because <font color="DeepSkyBlue">changing from $a_n$ to $\left|a_n\right|$ increases the sum.  Thus, the smaller $a_n$ is surely to converge, if $\left|\sum a_n\right|$ converges.</font>    
>
>[2]Alternating series:  
>$a_1$-$a_2$+$a_3$-$a_4$+$a_5$-$a_6$+..., in which the signs alternate between plus and minus.  
>The series $1$-$\frac {1}{2}$+$\frac {1}{3}$-$\frac {1}{4}$+$\frac {1}{5}$-$\frac {1}{6}$+... converges, why?  
>&#10112;the terms decreasing to zero  
>&#10113;it decreasing to zero with alternating signs, that is $a_n\rightarrow 0^{+}$,$a_{n+1}\rightarrow 0^{-}$,  
>hence, $a_n+(-a_{n+1})\rightarrow 0$, where $a_n>a_{n+1}$, the series converges.  
>
>[3]An alternating series <font color="DeepPink">$a_1$-$a_2$+$a_3$-$a_4$+$a_5$-$a_6$+...converges, if every $a_{n+1}\le a_{n}$ and $a_{n}\rightarrow 0$.</font>  
><font color="Brown">proof::mjtsai1974</font>  
>&#10112;by given that $a_n\ge a_{n+1}$,$a_n\rightarrow 0$, as $a\rightarrow\infty$, we define $b_i$=$a_i-a_{i+1}$  
>&#10113;then, $b_n\rightarrow 0$, as $a\rightarrow\infty$ also holds.  
>&#10114;and $a_n\ge a_{n+1}$ implies that $\frac {a_{n+1}}{a_n}\rightarrow L_a\le 1$, as $n\rightarrow\infty$.  
>for $L_a=1$, we have $a_n$-$a_{n+1}$=$b_n$=$0$  
>for $L_a<1$, we have $b_n\rightarrow 0$ also holds.  
>&#10115;thus, $b_n$ is either zero or decreasing to zero, and $\frac {b_{n+1}}{b_n}\rightarrow L_b$, as $n\rightarrow\infty$, where $L_b\rightarrow 1$ must hold, if $L_a<1$.

### Addendum
>&#10112;[MIT OCW Calculus On-line Textbook by Gilbert Strange](https://ocw.mit.edu/ans7870/resources/Strang/Edited/Calculus/Calculus.pdf)  
>&#10113;[MIT OCW Calculus by Gilbert Strange](https://ocw.mit.edu/resources/res-18-005-highlights-of-calculus-spring-2010/)  

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