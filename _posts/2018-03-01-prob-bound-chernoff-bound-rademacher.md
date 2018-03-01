---
layout: post
title: Chernoff Bounds For Rademacher Random Variable
---

## Prologue To The <font color="Red">Chernoff Bounds</font> For <font color="Red">Rademacher</font> Random Variable
<p class="message">
The <font color="Red">Chernoff bounds</font> is a convenient way to build the shaper bounds in exponential form for the <font color="Red">Rademacher</font> random variable.  
It could efficiently relate the sample size to the error bias fits within the desired probability.  
</p>

### The <font color="Red">Rademacher</font> Random Variable
>It is also called the random sign variable.  Let S be a <font color="Red">Rademacher</font> random variable, its events are given $\\{1,-1\\}$, each with probability $\frac {1}{2}$.  
>
>Then, it has the basic property that $E\lbrack S^{k}\rbrack$=$0$, for $k$ is odd, while $E\lbrack S^{k}\rbrack$=$1$, for $k$ is even.  
>&#10112;$E\lbrack S^{1}\rbrack$=$\frac {1}{2}\cdot 1$+$\frac {1}{2}\cdot (-1)$=$0$  
>&#10113;$E\lbrack S^{3}\rbrack$=$\frac {1}{2}\cdot 1^{3}$+$\frac {1}{2}\cdot (-1)^{3}$=$0$  
>&#10114;$E\lbrack S^{2}\rbrack$=$\frac {1}{2}\cdot 1^{2}$+$\frac {1}{2}\cdot (-1)^{2}$=$1$  
>&#10115;$E\lbrack S^{4}\rbrack$=$\frac {1}{2}\cdot 1^{4}$+$\frac {1}{2}\cdot (-1)^{4}$=$1$  

### <font color="Red">Chernoff Bounds</font> For <font color="Red">Rademacher</font> Random Variable
>Given $S$ is a <font color="Red">Rademacher</font> random variable, then  
>$\;\;P(Z\ge t)\le exp(\frac {n\cdot\lambda^{2}}{2})\cdot e^{-\lambda\cdot t}$  
>, where $Z$=$\sum_{i=1}^{n}S_{i}$  
>Proof:  
>&#10112;begin by Taylor series of exponential function.  
>$E\lbrack e^{\lambda\cdot S}\rbrack$  
>=$E\lbrack\sum_{k=0}^{\infty}\frac {(\lambda\cdot S)^{k}}{k!}\rbrack$  
>=$\sum_{k=0}^{\infty}\frac {\lambda^{k}\cdot E\lbrack S^{k}\rbrack}{k!}$  
>=$\sum_{k=0,2,4,...}^{\infty}\frac {\lambda^{k}}{k!}$  
>=$\sum_{k=0}^{\infty}\frac {\lambda^{2\cdot k}}{2\cdot k!}$  
>&#10113;next to find the closest upper bound, specifically, in exponential form.  
>since $2\cdot k!\ge 2^{k}\cdot k!$, we have  
>$E\lbrack e^{\lambda\cdot S}\rbrack$  
>=$\sum_{k=0}^{\infty}\frac {\lambda^{2\cdot k}}{2\cdot k!}$  
>$\le \sum_{k=0}^{\infty}\frac {\lambda^{2\cdot k}}{2^{k}\cdot k!}$  
>=$\sum_{k=0}^{\infty}(\frac {\lambda^{2}}{2})^{k}/k!$  
>=$e^{(\frac {\lambda^{2}}{2})}$  
>&#10114;by given $Z$=$\sum_{i=1}^{n}S_{i}$, we have  
>$P(Z\ge t)$  
>$\le \frac {E\lbrack Z\rbrack}{t}$...<font color="Red">Markov inequality</font>  
>=$\frac {E\lbrack\sum_{i=1}^{n}S_{i}\rbrack}{t}$  
>=$\frac {E\lbrack e^{\lambda\cdot\sum_{i=1}^{n}S_{i}}\rbrack}{e^{\lambda\cdot t}}$......<font color="Red">Chernoff bounds</font>  
>=$\frac {E^{n}\lbrack e^{\lambda\cdot S_{1}}\rbrack}{e^{\lambda\cdot t}}$  
>$\le (e^{(\frac {\lambda^{2}}{2})})^{n}\cdot e^{-\lambda\cdot t}$  
>$\Rightarrow P(Z\ge t)\le e^{(\frac {n\cdot\lambda^{2}}{2})}\cdot e^{-\lambda\cdot t}$  

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