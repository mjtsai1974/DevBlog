---
layout: post
title: Chernoff Bounds
---

## Prologue To The <font color="Red">Chernoff Bounds</font>
<p class="message">
The <font color="Red">Chernoff bounds</font> is essential another variation based on the <font color="Red">Markov inequality</font>, it derivates the exponential deviation bounds.  
</p>

### <font color="Red">Chernoff Bounds</font>
>Let $Z$ be any random variable, then for any $t>0$,  
>$\;\;P(Z\ge E\lbrack Z\rbrack+t)\le\underset{\lambda\ge 0}{min}E\lbrack e^{\lambda\cdot (Z-E\lbrack Z\rbrack)}\rbrack\cdot e^{-\lambda\cdot t}$=$\underset{\lambda\ge 0}{min}M_{Z-E\lbrack Z\rbrack}(\lambda)\cdot e^{-\lambda\cdot t}$  
>and  
>$\;\;P(Z\le E\lbrack Z\rbrack-t)\le\underset{\lambda\ge 0}{min}E\lbrack e^{\lambda\cdot (E\lbrack Z\rbrack-Z)}\rbrack\cdot e^{-\lambda\cdot t}$=$\underset{\lambda\ge 0}{min}M_{E\lbrack Z\rbrack-Z}(\lambda)\cdot e^{-\lambda\cdot t}$  
>; where $M_{Z}(\lambda)$=$E\lbrack exp(\lambda\cdot Z)\rbrack$ is the <font color="OrangeRed">moment generating function</font> of $Z$.  
>
>Proof:  
>&#10112;for any $\lambda>0$, we have:  
>$Z\ge E\lbrack Z\rbrack+t$  
>$\Leftrightarrow e^{\lambda\cdot Z}\ge e^{\lambda\cdot (E\lbrack Z\rbrack+t)}$  
>Or equivalently,  
>$Z-E\lbrack Z\rbrack\ge t$  
>$\Leftrightarrow e^{\lambda\cdot (Z-E\lbrack Z\rbrack)}\ge e^{\lambda\cdot t}$  
>&#10113;by <font color="Red">Markov inequality</font>, below holds:  
>$P(\left|Z-E\lbrack Z\rbrack\right|\ge t)$  
>$=P(e^{\lambda\cdot (Z-E\lbrack Z\rbrack)}\ge e^{\lambda\cdot t})\le E\lbrack e^{\lambda\cdot (Z-E\lbrack Z\rbrack)}\rbrack\cdot e^{-\lambda\cdot t}$  
>&#10114;the second inequality could be proved in the similar way.  
>
>To be believed that <font color="DeepSkyBlue">a reasonable upper bound could be built by choosing appropriate $\lambda$.</font>  

### <font color="Red">Chernoff Bounds</font> <font color="DeepSkyBlue">Extension</font>
>We can further extend <font color="Red">Chernoff bounds</font> with summation of multiple random varaibles.  
>&#10112;suppose that all $Z_i$'s are independent and zero meanfor all $i$, then we have it that:  
>$\;\;M_{Z_1+...+Z_n}=\prod_{i=1}^{n}M_{Z_i}(\lambda)$  
>, which is a consequence of the <font color="OrangeRed">moment generating function</font>, because the independence of each $Z_{i}$.  
>$E\lbrack exp(\lambda\cdot\sum_{i=1}^{n}Z_{i})\rbrack$  
>=$E\lbrack \prod_{i=1}^{n}exp(\lambda\cdot Z_{i})\rbrack$  
>=$\prod_{i=1}^{n}E\lbrack exp(\lambda\cdot Z_{i})\rbrack$  
>&#10113;by <font color="Red">Chernoff inequality</font>, for any $\lambda>0$,  
>$P(\sum_{i=1}^{n}Z_{i}\ge t)\le \prod_{i=1}^{n}E\lbrack exp(\lambda\cdot Z_{i})\rbrack\cdot e^{-\lambda\cdot t}$  
>$\Leftrightarrow P(\sum_{i=1}^{n}Z_{i}\ge t)\le (E\lbrack exp(\lambda\cdot Z_{1})\rbrack)^{n}\cdot e^{-\lambda\cdot t}$  

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