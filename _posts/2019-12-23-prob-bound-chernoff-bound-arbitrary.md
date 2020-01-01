---
layout: post
title: Chernoff Bounds For Arbitrary Random Variable
---

## Prologue To The <font color="Red">Chernoff Bounds</font> For <font color="OrangeRed">Arbitrary</font> Random Variable
<p class="message">
There are many <font color="Red">Chernoff bounds</font> as a result.  This article develops the tail bound on the <font color="OrangeRed">independent arbitrary</font> random variable with outcome ranging from 0 to 1, that is $\lbrack 0,1\rbrack$.  
</p>

### The <font color="Red">Error Probability</font> After Test
><font color="OrangeRed">[The given condition]</font>
>Suppose we are given  
>&#10112;$X_{1}$,$X_{2}$,...,$X_{n}$ to be independent random variables with values in $\lbrack 0,1\rbrack$.  
>&#10113;$X$=$X_{1}$+$X_{2}$+...+$X_{n}$  
>&#10114;$E\lbrack X \rbrack$=$\mu$  
>
>These $X_{1}$,...,$X_{n}$ needs <font color="RosyBrown">not</font> to be Bernoulli ranodm variables, but they must be <font color="OrangeRed">independent</font>.  
>
><font color="RoyalBlue">[Question]</font>
>Then, for every $\varepsilon$>$0$, what is the upper and lower bound for  
>&#10112;$P(X\geq (1+\delta)\cdot\mu)$=$P(X\geq \mu+\varepsilon)$  
>&#10113;$P(X\leq (1-\delta)\cdot\mu)$=$P(X\leq \mu-\varepsilon)$  
>, where $\varepsilon$=$\delta\cdot\mu$  

### The Upper Bound On Error Probability
>Still, it is asking the upper bound on error probability, when target value $X$ is greater than the expect value $\mu$, and we'd like to bound it on the upper side.  
>
>The major difference is that these random variables fall within $\lbrack 0,1\rbrack$, <font color="RosyBrown">not</font> the Bernoulli values $0$ or $1$.  Here is the idea:  
>&#10112;take $Y_{i}$=$X_{i}$-$E\lbrack X_{i} \rbrack$  
>&#10113;take $X$=$\sum_{1}^{n}X_{i}$,$E\lbrack X \rbrack$=$\mu$=$\sum_{1}^{n}E\lbrack X_{i} \rbrack$  
>&#10114;take $Y$=$\sum_{1}^{n}Y_{i}$  
>&#10115;$P(X\geq\mu+\varepsilon)$  
>=$P(X-\mu\geq\varepsilon)$  
>=$P(\sum_{1}^{n}(X_{i}-E\lbrack X_{i} \rbrack)\geq\varepsilon)$  
>=$P(Y\geq\varepsilon)$  
>=$P(e^{t\cdot Y}\geq e^{t\cdot\varepsilon})$...for any $t>0$  
>$\leq\frac {E\lbrack e^{t\cdot Y}\rbrack}{e^{t\cdot\varepsilon}}$, and $E\lbrack Y_{i}\rbrack$=$0$  
>
>Further expand  
>$E\lbrack e^{t\cdot Y}\rbrack$  
>=$E\lbrack e^{\sum_{1}^{n} t\cdot Y_{i}}\rbrack$  
>=$E\lbrack \prod_{1}^{n} e^{t\cdot Y_{i}}\rbrack$  
>=$\prod_{1}^{n}E\lbrack e^{t\cdot Y_{i}}\rbrack$  
>
>Thus, $P(X\geq \mu+\varepsilon)\leq\frac {\prod_{1}^{n}E\lbrack e^{t\cdot Y_{i}}\rbrack}{e^{t\cdot\varepsilon}}$ is left to bound the term $E\lbrack e^{t\cdot Y_{i}}\rbrack$.  
>&#10112;$D_{y}e^{t\cdot Y_{i}}$=$t\cdot e^{t\cdot Y_{i}}>0$  
>&#10113;$D_{y}t\cdot e^{t\cdot Y_{i}}$=$t^{2}\cdot e^{t\cdot Y_{i}}>0$  
>$e^{t\cdot Y_{i}}$ is a <font color="OrangeRed">convex</font> function, it <font color="OrangeRed">concaves up</font>, by the 2nd derivative greater than 0.  
>
>Suppose there exists a line $a+b\cdot y$ passing through the curve of $e^{t\cdot Y_{i}}$ at the points $(1,e^{t})$ and $(-1,e^{-t})$, that is  
>$a$+$b$=$e^{t}$  
>$a$-$b$=$e^{-t}$  
>$\Rightarrow$solve above equation, could we obtain $a$=$\frac {e^{t}+e^{-t}}{2}$, $b$=$\frac {e^{t}-e^{-t}}{2}$  
>
>We can claim that within $\lbrack -1,1\rbrack$   
>$e^{t\cdot Y_{i}}\leq a+b\cdot Y_{i}$  
>$\Rightarrow E\lbrack e^{t\cdot Y_{i}}\rbrack\leq E\lbrack a+b\cdot Y_{i}\rbrack$  
>$\Rightarrow E\lbrack e^{t\cdot Y_{i}}\rbrack\leq a + b\cdot E\lbrack Y_{i}\rbrack$  
>$\Rightarrow E\lbrack e^{t\cdot Y_{i}}\rbrack\leq a + b\cdot 0$, where $E\lbrack Y_{i}\rbrack$=$0$  
>$\Rightarrow E\lbrack e^{t\cdot Y_{i}}\rbrack\leq a$  
>$\Rightarrow E\lbrack e^{t\cdot Y_{i}}\rbrack\leq \frac {e^{t}+e^{-t}}{2}$  
>
>By using <font color="Red">Taylor expansion</font> of $e^{t}$, we can simplify the bounding:  
>$e^{x}$=$1$+$\frac {x^{1}}{1!}$+$\frac {x^{2}}{2!}$+$\frac {x^{3}}{3!}$+..., then  
>$\frac {e^{t}+e^{-t}}{2}$  
>=$\frac {1}{2}\cdot\lbrack$+$1$+$\frac {t^{1}}{1!}$+$\frac {t^{2}}{2!}$+$\frac {t^{3}}{3!}$+$\frac {t^{4}}{4!}$+...
>+$1$+$\frac {(-t)^{1}}{1!}$+$\frac {(-t)^{2}}{2!}$+$\frac {(-t)^{3}}{3!}$+$\frac {(-t)^{4}}{4!}$+...+$\rbrack$  
>=$1$+$\frac {t^{2}}{2!}$+$\frac {t^{4}}{4!}$+$\frac {t^{6}}{6!}$+...  
>$\leq 1$+$\frac {t^{2}}{2\cdot 1!}$+$\frac {t^{4}}{2^{2}\cdot 2!}$+$\frac {t^{6}}{2^{3}\cdot 3!}$+...  
>$\leq 1$+$\frac {\frac {t^{2}}{2}}{1!}$+$\frac {(\frac {t^{2}}{2})^{2}}{2!}$+$\frac {(\frac {t^{2}}{2})^{3}}{3!}$+...  
>$\leq e^{\frac {t^{2}}{2}}$  
>
>Therefore, $e^{t\cdot Y_{i}}\leq e^{\frac {t^{2}}{2}}$,  
>$\prod_{1}^{n}E\lbrack e^{t\cdot Y_{i}}\rbrack$  
>=$E\lbrack e^{t\cdot (Y_{1}+Y_{2}+...+Y_{n})}\rbrack$  
>=$E\lbrack e^{n\cdot t\cdot Y_{i}}\rbrack$  
>$\leq E\lbrack e^{\frac {t^{2}}{2}}\rbrack$  
>
>Back to the inequality:  
>$P(X\geq \mu+\varepsilon)$  
>$\leq\frac {\prod_{1}^{n}E\lbrack e^{t\cdot Y_{i}}\rbrack}{e^{t\cdot\varepsilon}}$  
>$\leq\frac {E\lbrack e^{\frac {t^{2}}{2}}\rbrack}{e^{t\cdot\varepsilon}}$  
>$\leq e^{\frac {t^{2}}{2}-t\cdot\varepsilon}$  
>
>Next would be:  
>&#10112;ask for the maximum value of $\frac {t^{2}}{2}-t\cdot\varepsilon$, <font color="OrangeRed">take its 1st order differentiation, set it to 0, figure out such $t$</font>:  
>$D_{t}(\frac {t^{2}}{2}-t\cdot\varepsilon)$=$0$  
>$\Rightarrow n\cdot t-\varepsilon$=$0$  
>$\Rightarrow t$=$\frac {\varepsilon}{n}$  
>
>&#10113;take $t$=$\frac {\varepsilon}{n}$ in $e^{\frac {t^{2}}{2}-t\cdot\varepsilon}$, then  
>$e^{\frac {n\cdot \frac {\varepsilon^{2}}{n^{2}}}{2}-\frac {\varepsilon}{n}\cdot\varepsilon}$  
>=$e^{\frac {\varepsilon^{2}}{2n}-\frac {\varepsilon^{2}}{n}}$  
>=$e^{-\frac {\varepsilon^{2}}{2n}}$  
>
>Finally, we prove $P(X\geq \mu+\varepsilon)\leq e^{-\frac {\varepsilon^{2}}{2n}}$ in this upper bound for error probability.  

### The Lower Bound On Error Probability
>It is asking the error probability when target value $X$ is less than the expect value $\mu$, and we'd like to bound it on the lower side.  
>$P(X\leq \mu-\varepsilon)$  
>=$P(X-\mu\leq -\varepsilon)$  
>=$P(-X+\mu\geq \varepsilon)$  
>=$P(-X\geq -\mu+\varepsilon)$  
>
>It is much similar to the upper bound expression, here is the idea again:  
>&#10112;take $Y_{i}^{\'}$=$E\lbrack X_{i} \rbrack$-$X_{i}$  
>&#10113;take $X$=$\sum_{1}^{n}X_{i}$,$E\lbrack X \rbrack$=$\mu$=$\sum_{1}^{n}E\lbrack X_{i} \rbrack$  
>&#10114;take $Y^{\'}$=$\sum_{1}^{n}Y_{i}^{\'}$  
>&#10115;$P(X\leq \mu-\varepsilon)$  
>=$P(-X\geq -\mu+\varepsilon)$  
>=$P(Y^{\'}\geq \varepsilon)$  
>=$P(e^{t\cdot Y^{\'}}\geq e^{t\cdot\varepsilon})$...for any $t>0$  
>$\leq\frac {E\lbrack e^{t\cdot Y^{\'}}\rbrack}{e^{t\cdot\varepsilon}}$  
>
>With similar deduction in upper bound would we obtain the same expression for lower bound:  
>$P(X\leq \mu-\varepsilon)\leq e^{-\frac {\varepsilon^{2}}{2n}}$  
>
>By <font color="OrangeRed">symmetrical</font> distribution, $P(X-\mu\leq -\varepsilon)$ is the opposite direction to $P(X-\mu\geq \varepsilon)$, its lower bound of error probability would be <font color="RosyBrown">no more</font> than $e^{\frac {t^{2}}{2}-t\cdot\varepsilon}$  
>$P(X\leq \mu-\varepsilon)$  
>=$P(X-\mu\leq -\varepsilon)$  

### Illustration: <font color="Red">Chernoff bound</font> For <font color="Red">Bernoulli</font> versus <font color="OrangeRed">arbitrary</font> Random Variables::mjtsai1974
><font color="DeepSkyBlue">[The major point]</font>
><font color="OrangeRed">Why the proof in Chernoff bound for Bernoulli is inadequate in arbitrary random variables?</font>  
><font color="RoyalBlue">Can we use the proof in Chernoff bound for Bernoulli in arbitrary random variable?</font>  If not, why?  
>
>The Bernoulli random variable has only two values, $0$ and $1$, while arbitrary random variable has values falling withing $\lbrack 0,1\rbrack$.  It seems that <font color="OrangeRed">probabilistic error tolerance</font> in arbitrary random variables requires much more precision concern in approximation, which would be shown in my next proof.  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The fault tolerance $\delta$ of upper and lower bound</font>  
>From the proof in [Chernoff Bounds For Bernoulli Random Variable]({{ site.baseurl }}/2019/12/09/prob-bound-chernoff-bound-bernoulli/), we see that  
>&#10112;$P(X>(1+\delta)\cdot\mu)$<$e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$  
>&#10113;$P(X<(1-\delta)\cdot\mu)$<$e^{(-1-t\cdot\delta)\cdot\mu}$  
>
>Next would be to inspect the fault tolerance $\delta$ in <font color="Red">Chernoff</font> bounds for <font color="Red">Bernoulli</font> random variable for any given $t$>$0$, based on <font color="DeepSkyBlue">the convex property used in the proof of Chernoff bounds for arbitrary random variable</font>.  
>
><font color="DeepSkyBlue">[1.1]</font>
><font color="OrangeRed">The fault tolerance $\delta$ of upper bound</font>  
>&#10112;$D_{t}e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$  
>=$(e^{t}-(1+\delta))\cdot\mu\cdot e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$  
>&#10113;$D_{t}^{2}e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$  
>=$(e^{t}\cdot\mu+(e^{t}-(1+\delta))^{2})\cdot e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$  
>
>Since <font color="OrangeRed">$D_{t}^{2}e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}\geq 0$ alswys holds</font>, this upper bound of $e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$ in <font color="Red">Chernoff</font> bounds for <font color="Red">Bernoulli</font> random variable is a <font color="Red">convex</font> function, which concaves up.  
>
>&#10114;suppose $c$+$d\cdot t$ pass through $e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$ at $(0,1)$ and $(1,e^{e-2-\delta})$...for $t$>$0$  
>$c$+$d\cdot 0$=$1$...$t$=$0$  
>$c$+$d$=$e^{e-2-\delta}$...$t$=$1$  
>$\Rightarrow c=1$ and $d$=$e^{e-2-\delta}$-$1$, thus it is  
>$1$+$(e^{e-2-\delta}-1)\cdot t$  
>
>&#10115;$D_{t}(1+(e^{e-2-\delta}-1)\cdot t)$=$0$  
>$\Rightarrow e^{e-2-\delta}-1$=$0$  
>$\Rightarrow e^{e-2-\delta}$=$1$  
>$\Rightarrow e-2-\delta$=$0$  
>$\Rightarrow \delta$=$e-2$...$e$=$2.71828182...$  
>$\Rightarrow \delta$=$0.71828182...$  
>
>For whatever $0<t\leq 1$ we are using, the fault tolerance expressed by $\delta$ could be probabilistically up to almost $0.718$, <font color="OrangeRed">might not be an inappropriate choice</font>.  
>
><font color="DeepSkyBlue">[1.2]</font>
><font color="OrangeRed">The fault tolerance $\delta$ of lower bound</font>  
>&#10112;$D_{t}e^{(-1-t\cdot\delta)\cdot\mu}$=$-\delta\cdot\mu\cdot e^{(-1-t\cdot\delta)\cdot\mu}$  
>&#10113;$D_{t}^{2}e^{(-1-t\cdot\delta)\cdot\mu}$=$(-\delta\cdot\mu)^{2}\cdot e^{(-1-t\cdot\delta)\cdot\mu}$  
>
>Since <font color="OrangeRed">$(-\delta\cdot\mu)^{2}\cdot e^{(-1-t\cdot\delta)\cdot\mu}\geq 0$ always holds</font>, this lower bound of $e^{(-1-t\cdot\delta)\cdot\mu}$ in <font color="Red">Chernoff</font> bounds for <font color="Red">Bernoulli</font> random variable is a <font color="Red">convex</font> function, which concaves up.  
>
>&#10114;suppose $c$+$d\cdot t$ pass through $e^{(-1-t\cdot\delta)\cdot\mu}$ at $(0,e^{-\mu})$ and $(1,e^{(-1-\delta)\cdot\mu})$, then  
>$c$+$d\cdot 0$=$e^{-\mu}$...$t$=$0$  
>$c$+$d$=$e^{(-1-\delta)\cdot\mu}$  
>$\Rightarrow c$=$e^{-\mu}$ and $d$=$e^{(-1-\delta)\cdot\mu}$-$e^{-\mu}$, thus it is  
>$e^{-\mu}$+$(e^{(-1-\delta)\cdot\mu}-e^{-\mu})\cdot t$  
>
>&#10115;$D_{t}(e^{-\mu}+(e^{(-1-\delta)\cdot\mu}-e^{-\mu})\cdot t)$=$0$  
>$\Rightarrow e^{(-1-\delta)\cdot\mu}-e^{-\mu}$=$0$  
>$\Rightarrow e^{(-1-\delta)\cdot\mu}$=$e^{-\mu}$  
>$\Rightarrow (-1-\delta)\cdot\mu$=$-\mu$  
>$\Rightarrow \delta$=$0$  
>
>For whatever $0<t\leq 1$ we are using, the fault tolerance expressed by $\delta$ could only be to $0$, <font color="RosyBrown">might be an inappropriate choice</font> in error probability evaluation.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The existence of $t$ in upper and lower bound</font>  
>Succeeding to above section, this article would like to ask for $t$, such that we can have an ideal upper/lower bound, for $\delta$ in $\lbrack -1,1\rbrack$:  
>&#10112;$P(X>(1+\delta)\cdot\mu)$<$e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$  
>&#10113;$P(X<(1-\delta)\cdot\mu)$<$e^{(-1-t\cdot\delta)\cdot\mu}$  
>
><font color="DeepSkyBlue">[2.1]</font>
><font color="OrangeRed">The validity of $t$ in upper bound</font>  
>&#10112;$D_{\delta}^{2}e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}\geq 0$  
>$e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$ is a <font color="Red">convex</font> function.  
>
>&#10113;suppose $c$+$d\cdot\delta$ pass through $e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$ at $(-1,e^{(e^{t}-1)\cdot\mu})$ and $(1,e^{(e^{t}-1-2\cdot t)\cdot\mu})$, then:  
>$c$=$\frac {e^{(e^{t}-1-2\cdot t)\cdot\mu}+e^{(e^{t}-1)\cdot\mu}}{2}$  
>$d$=$\frac {e^{(e^{t}-1-2\cdot t)\cdot\mu}-e^{(e^{t}-1)\cdot\mu}}{2}$  
>
>&#10114;$D_{\delta}(c+d\cdot\delta)$=$0$  
>$\Rightarrow d$=$0$  
>$\Rightarrow \frac {e^{(e^{t}-1-2\cdot t)\cdot\mu}-e^{(e^{t}-1)\cdot\mu}}{2}$=$0$  
>$\Rightarrow e^{(e^{t}-1-2\cdot t)\cdot\mu}$=$e^{(e^{t}-1)\cdot\mu}$  
>$\Rightarrow (e^{t}-1-2\cdot t)\cdot\mu$=$(e^{t}-1)\cdot\mu$  
>$\Rightarrow e^{t}-1-2\cdot t$=$(e^{t}-1)$  
>$\Rightarrow t$=$0$, which is a <font color="RosyBrown">contradiction</font>, for <font color="RosyBrown">$t>0$ is the must be condition</font> in proof.  
>
><font color="DeepSkyBlue">[2.2]</font>
><font color="OrangeRed">The validity of $t$ in lower bound</font>  
>&#10112;$D_{\delta}^{2}e^{(-1-t\cdot\delta)\cdot\mu}\geq 0$  
>$e^{(-1-t\cdot\delta)\cdot\mu}$ is a <font color="Red">convex</font> function.  
>
>&#10113;suppose $c$+$d\cdot\delta$ pass through $e^{(-1-t\cdot\delta)\cdot\mu}$ at $(-1,e^{(-1+t)\cdot\mu})$ and $(1,e^{(-1-t)\cdot\mu})$, then:  
>$c$=$\frac {e^{(-1-t)\cdot\mu}+e^{(-1+t)\cdot\mu}}{2}$  
>$d$=$\frac {e^{(-1-t)\cdot\mu}-e^{(-1+t)\cdot\mu}}{2}$  
>
>&#10114;$D_{\delta}(c+d\cdot\delta)$=$0$  
>$\Rightarrow d$=$0$  
>$\Rightarrow e^{(-1-t)\cdot\mu}$=$e^{(-1+t)\cdot\mu}$  
>$\Rightarrow -1-t$=$-1+t$  
>$\Rightarrow t$=$0$, which is a <font color="RosyBrown">contradiction</font>, for <font color="RosyBrown">$t>0$ is the must be condition</font> in proof.  
>
>We have the generalized $t$=$0$ for both upper and lower bound in <font color="Red">Chernoff</font> bounds for <font color="Red">Bernoulli</font> random variable by using the <font color="Red">convex property</font> in the proof of <font color="Red">Chernoff</font> bounds for <font color="OrangeRed">arbitrary</font> random variable, and found it an inappropriate value, because $t$ should be any positive value, at least greater than zero.  
>
><font color="Brown">[Notes::mjtsai1974]</font>
>As a result of above indication, we can claim that <font color="RosyBrown">the inequality in <font color="Red">Chernoff</font> bounds for <font color="Red">Bernoulli</font> random variable:</font>  
>&#10112;$P(X>(1+\delta)\cdot\mu)$<$e^{((e^{t}-1)-t\cdot (1+\delta))\cdot\mu}$  
>&#10113;$P(X<(1-\delta)\cdot\mu)$<$e^{(-1-t\cdot\delta)\cdot\mu}$  
><font color="RosyBrown">is inappropriate in <font color="Red">Chernoff</font> bounds for <font color="OrangeRed">arbitrary</font> random variable.</font>  

<!-- Γ -->
<!-- \Omega -->
<!-- \cap intersection -->
<!-- \cup union -->
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
<!-- \Leftrightarrow -->
<!-- \prod_{v\in V} -->
<!-- \subset -->
<!-- \subseteq -->
<!-- \varnothing -->
<!-- \perp -->
<!-- \overset\triangle= -->
<!-- \left|X\right| -->
<!-- \xrightarrow{r_t} -->
<!-- \left\|?\right\| => ||?||-->
<!-- \left|?\right| => |?|-->
<!-- \lbrack BQ\rbrack => [BQ] -->
<!-- \subset -->
<!-- \subseteq -->
<!-- \widehat -->
<!-- \int_{}^{}{}\operatorname d{} -->

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

<!-- ### <font color="RoyalBlue">Example</font>: Illustration By Rainy And Sunny Days In One Week -->
<!-- <font color="RoyalBlue">[Question]</font> -->
<!-- <font color="DeepSkyBlue">[Answer]</font> -->

<!-- <font color="Brown">Notes::mjtsai1974</font> -->

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!--
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Why at this moment, the Poisson and exponential probability come out with different result?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->