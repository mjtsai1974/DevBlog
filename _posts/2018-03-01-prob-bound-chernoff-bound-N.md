---
layout: post
title: Chernoff Bounds For Normal Distribution
---

## Prologue To The <font color="Red">Chernoff Bounds For Normal Distribution</font>
<p class="message">
The <font color="Red">Chernoff bounds</font> is a convenient way to build the shaper bounds in exponential form for normal distributions.  
</p>

### <font color="Red">Chernoff Bounds For Normal Distribution</font>
>Given that $Z$ is a random variable, normally distributed in $Z\sim N(0,\sigma^2)$, then  
>$\;\;P(Z\ge t)\le e^{(\lambda\cdot\sigma)^{2}}\cdot e^{-\lambda\cdot t}$  
>, where $M_{Z}(\lambda)$=<font color="DeepSkyBlue">$e^{(\lambda\cdot\sigma)^{2}}$</font>  
>
>Proof::by mjtsai  
>The proof would be categorized into 4 major parts, the first part is to ask for $E\lbrack e^{\lambda\cdot Z}\rbrack$, the second part is to figure out the r-th moment, we'll make reference to the ratio test theorem in the third part, finally is the upper bounds in the <font color="Red">Chernoff Bounds</font> form.  
>[1]We begin from $E\lbrack e^{\lambda\cdot Z}\rbrack$  
>First, express the MGF of Z in terms of the Taylor series:  
>$M_{Z}(\lambda)$  
>=$E\lbrack e^{\lambda\cdot Z}\rbrack$  
>=$E\lbrack 1+\frac {\lambda\cdot Z}{1!}+\frac {(\lambda\cdot Z)^{2}}{2!}+\frac {(\lambda\cdot Z)^{3}}{3!}+...\rbrack$  
>=$1$+$\frac {\lambda}{1!}\cdot E\lbrack Z\rbrack$+$\frac {(\lambda)^{2}}{2!}\cdot E\lbrack Z^{2}\rbrack$+$\frac {(\lambda)^{3}}{3!}\cdot E\lbrack Z^{3}\rbrack$+$\frac {(\lambda)^{4}}{4!}\cdot E\lbrack Z^{4}\rbrack$+...  
[2]Next to ask for the r-th ordinary moment of each term.  
>&#10112;$E\lbrack Z^{r}\rbrack$=$\int_{0}^{\infty}\frac {z^{r}}{\sqrt {2\cdot\pi}}\cdot e^{-\frac {z^{2}}{2\cdot\sigma^{2}}}\operatorname dz$  
>; where $z\in Z$, $z$ is the events.  
>&#10113;take $x$=$\frac {z^{2}}{2\cdot\sigma^{2}}$, then  
>$z$=$\sqrt{2\cdot\sigma^{2}\cdot x}$, and  
>$\operatorname dz$=$\frac {\sigma^{2}}{z}\cdot\operatorname dx$  
>&#10114;just replace $\operatorname dz$ with $\operatorname dx$  
>$E\lbrack Z^{r}\rbrack$  
>=$\frac {1}{\sqrt {2\cdot\pi}}\int_{0}^{\infty}z^{r}\cdot e^{-x}\cdot\frac {\sigma^{2}}{z}\cdot\operatorname dx$  
>=$\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}\int_{0}^{\infty}z^{r-1}\cdot e^{-x}\operatorname dx$  
>=$\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}\cdot\Gamma(r)$  
>, where <font color="OrangeRed">$\Gamma(r)$=$\int_{0}^{\infty}z^{r-1}\cdot e^{-x}\operatorname dx$</font>, it is just the <font color="OrangeRed">Gamma</font> function in $Z$.  
>[3]We know $\Gamma(n)$=$(n-1)!$ in [Introduction To The Gamma Distribution]({{ site.github.repo }}{{ site.baseurl }}/2017/12/29/intro-gamma-dist/), then,  
>$M_{Z}(\lambda)$  
>=$1$+$\frac {\lambda}{1!}\cdot E\lbrack Z\rbrack$+$\frac {(\lambda)^{2}}{2!}\cdot E\lbrack Z^{2}\rbrack$+$\frac {(\lambda)^{3}}{3!}\cdot E\lbrack Z^{3}\rbrack$+$\frac {(\lambda)^{4}}{4!}\cdot E\lbrack Z^{4}\rbrack$+...  
>=$1$+$\frac {\lambda}{1!}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}\cdot\Gamma(1)$+$\frac {(\lambda)^{2}}{2!}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}\cdot\Gamma(2)$+$\frac {(\lambda)^{3}}{3!}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}\cdot\Gamma(3)$+$\frac {(\lambda)^{4}}{4!}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}\cdot\Gamma(4)$+...  
>=$1$+$0$+$\frac {(\lambda)^{2}}{2!}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}\cdot 1!$+$\frac {(\lambda)^{3}}{3!}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}\cdot 2!$+$\frac {(\lambda)^{4}}{4!}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}\cdot 3!$+...  
>...$\Gamma(1)$=$(1-1)!$=$0$  
>=$1$+$\frac {(\lambda)^{2}}{2}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}$+$\frac {(\lambda)^{3}}{3}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}$+$\frac {(\lambda)^{4}}{4}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}$+$\frac {(\lambda)^{5}}{5}\cdot\frac {\sigma^{2}}{\sqrt {2\cdot\pi}}$...  
>=$1$+$(\lambda\cdot \sigma)^{2}\cdot(\frac {1}{2\cdot\sqrt{2\cdot\pi}}$+$\frac {\lambda}{3\cdot\sqrt{2\cdot\pi}}$+$\frac {\lambda^{2}}{4\cdot\sqrt{2\cdot\pi}}$+$\frac {\lambda^{3}}{5\cdot\sqrt{2\cdot\pi}}$+...+$)$  
>
>Be recalled that we have convergence evaluation by the <font color="DeepPink">ratio test theorem</font> in [Series Convergence]({{ site.github.repo }}{{ site.baseurl }}/2018/01/26/series-cnvg/).  
><font color="DeepPink">If $\frac {a_{n+1}}{a_n}$ approaches a limit $L<1$, the series converges.</font>  
>&#10112;$\frac {a_2}{a_1}$=$\frac {\lambda^{3}/3}{\lambda^{2}/2}$=$\frac {2}{3}\cdot\lambda$  
>&#10113;$\frac {a_3}{a_2}$=$\frac {\lambda^{4}/4}{\lambda^{3}/3}$=$\frac {3}{4}\cdot\lambda$  
>&#10114;$\frac {a_4}{a_3}$=$\frac {\lambda^{5}/5}{\lambda^{4}/4}$=$\frac {4}{5}\cdot\lambda$  
>Trivially, $\frac {a_2}{a_1}$<$\frac {a_3}{a_2}$<$\frac {a_4}{a_3}$<...$\rightarrow 1$, the ratio is increasing and becomes much much close to $1$, <font color="DeepPink">this series would just diverge to infinity</font>, by <font color="DeepPink">ratio test theorem</font>.  
>Therefore, the whole equality becomes  
>$M_{Z}(\lambda)$  
>=$1$+$(\lambda\cdot\sigma)^{2}\cdot(\frac {1}{2\cdot\sqrt{2\cdot\pi}}$+$\frac {\lambda}{3\cdot\sqrt{2\cdot\pi}}$+$\frac {\lambda^{2}}{4\cdot\sqrt{2\cdot\pi}}$+$\frac {\lambda^{3}}{5\cdot\sqrt{2\cdot\pi}}$+...+$)$  
>$\approx 1+(\lambda\cdot\sigma)^{2}\cdot\infty$  
>$\approx\lim_{h\rightarrow 0}1+\frac {(\lambda\cdot\sigma)^{2}}{h}$  
>$\approx\lim_{h\rightarrow\infty}(1+\frac {(\lambda\cdot\sigma)^{2}}{h})^{h}$  
>=<font color="DeepSkyBlue">$e^{(\lambda\cdot\sigma)^{2}}$</font>  
>[4]By <font color="Red">Chernoff Bounds</font>, for any $\lambda>0$, then  
>$P(Z\ge t)\le \frac {E\lbrack e^{(\lambda\cdot Z)}\rbrack}{e^{\lambda\cdot t}}$  
>$\Rightarrow P(Z\ge t)\le e^{(\lambda\cdot\sigma)^{2}}\cdot e^{-\lambda\cdot t}$  

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
<!-- \\{Z\vert Z\ge t\\} -->
<!-- E\lbrack Z\rbrack -->
<!-- Var\lbrack Z\rbrack -->
<!-- \left|X\right| absolute value of X-->
<!-- \Leftrightarrow -->

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