---
layout: post
title: Markov Inequality
---

## Prologue To The <font color="Red">Markov Inequality</font>
<p class="message">
On our way to the learning theorem, the sampling size and the confidence level are the major key factors that can lead your test result to a reject or still pondering.  
The <font color="Red">Markov inequality</font> is a rahter simple probabilistic inequality, that is also a preliminary to allow us to make very strong claims on sums of random variables.   
</p>

### <font color="Red">Markov Inequality</font> Theorem
>Given that $Z$ is a non-negative random variable, then for all $t\ge 0$, we have $P(Z\ge t)\le \frac {E\lbrack Z\rbrack}{t}$  
>
>Proof::by mjtsai  
>&#10112;let's begin by the definition of expect value of a random variable.  
>$E\lbrack Z\rbrack$=$\sum(P(Z\ge t)\cdot\\{Z\vert Z\ge t\\}$+$P(Z<t)\cdot\{Z\vert Z<t\})$  
>, where we denote $\{Z\vert Z\ge t\}$=$1$,$\{Z\vert Z<t\}$=$1$  
>&#10113;then:  
>$E\lbrack Z\rbrack\ge\sum P(Z\ge t)\cdot\{Z\vert Z\ge t\}$...this must hold  
>$\;\;\;\;\;\;\;$=$P(Z\ge t)\cdot\sum \{Z\vert Z\ge t\}$  
>&#10114;choose $Q_t$=$\sum \{Z\vert Z\ge t\}$ to be the total number of events in $\{Z\vert Z\ge t\}$, then:  
>$\frac {E\lbrack Z\rbrack}{Q_t}\ge P(Z\ge t)$, where $Q_t$=$0$,$1$,$2$,...  
>&#10115;take $Q_t=t$ could also hold to have 
>$\frac {E\lbrack Z\rbrack}{t}\ge P(Z\ge t)$  
>We just prove that $P(Z\ge t)\le \frac {E\lbrack Z\rbrack}{t}$  

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