---
layout: post
title: Symmetrization
---

## Prologue To The <font color="Red">Symmetrization</font>
<p class="message">
In machine, statistics, probability theory, the <font color="Red">symmetrization</font> is commonly used to <font color="OrangeRed">relate the random variables belonging to the same distribution</font>.  
</p>

### The <font color="Red">Symmetrization</font>
>Given a <font color="OrangeRed">bounded</font> random variable $Z\in\lbrack a,b\rbrack$, we perform <font color="OrangeRed">multiple</font> tests of it with instances of $Z$ <font color="OrangeRed">duplicated</font>, choose one of the clones to be $Z'$, so that $Z'\in\lbrack a,b\rbrack$ and $E\lbrack Z\rbrack$=$E\lbrack Z'\rbrack$.  
>There exists some properties:  
>[1]$E_Z\lbrack e^{Z-E\lbrack Z\rbrack}\rbrack\le E_Z\lbrack E_{Z'}\lbrack e^{Z-Z'}\rbrack\rbrack$  
>[2]$P(\left|Z-E\lbrack Z\rbrack\right|\ge t)$=$P(\left|Z-E\lbrack Z'\rbrack\right|\ge t)$  
>$\le E\lbrack e^{\lambda\cdot E\lbrack\left|Z-Z'\right|\rbrack}\rbrack\cdot e^{-\lambda\cdot t}$  
>[3]$E_Z\lbrack E_{Z'}\lbrack e^{\lambda\cdot (Z-Z')}\rbrack\rbrack\le e^{\frac {(\lambda\cdot (b-a'))^{2}}{2}}$  
>
>Proof::mjtsai  
>&#10112;by given, $E\lbrack Z\rbrack$=$E\lbrack Z'\rbrack$, then,  
>$E_Z\lbrack Z-E\lbrack Z\rbrack\rbrack$=$E_Z\lbrack Z-E\lbrack Z'\rbrack\rbrack$  
>And according to the <font color="Red">Jensen's inequality</font>, we have it that  
>$E_Z\lbrack e^{Z-E\lbrack Z\rbrack}\rbrack$  
>=$E_Z\lbrack e^{Z-E\lbrack Z'\rbrack}\rbrack$  
>$\le E_Z\lbrack E_{Z'}\lbrack e^{Z-Z'}\rbrack\rbrack$  
>&#10113;by the <font color="Red">Chernoff bounds</font>, we can have  
>$P(\left|Z-E\lbrack Z\rbrack\right|\ge t)$  
>=$P(\left|Z-E\lbrack Z'\rbrack\right|\ge t)$  
>=$P(e^{\lambda\cdot\left|Z-E\lbrack Z'\rbrack\right|}\ge e^{\lambda\cdot t})$  
>$\le E\lbrack e^{\lambda\cdot\left|Z-E\lbrack Z'\rbrack\right|}\rbrack\cdot e^{-\lambda\cdot t}$  
>$\le E\lbrack e^{\lambda\cdot E\lbrack\left|Z-Z'\right|\rbrack}\rbrack\cdot e^{-\lambda\cdot t}$  
>&#10114;given that $S\in\\{+1,-1\\}$, a <font color="Red">Rademacher</font> random variable, and <font color="DeepPink">$S\cdot (Z-Z')$ and $Z-Z'$ have the same distribution</font>, it implies that  
>$E_Z\lbrack E_{Z'}\lbrack e^{Z-Z'}\rbrack\rbrack$  
>=$E_Z\lbrack E_{Z'}\lbrack e^{S\cdot (Z-Z')}\rbrack\rbrack$  
>=$E_{Z,Z'}\lbrack E_{S}\lbrack e^{S\cdot (Z-Z')}\rbrack\rbrack$  
>Then, below holds,  
>$E_Z\lbrack E_{Z'}\lbrack e^{\lambda\cdot (Z-Z')}\rbrack\rbrack$  
>=$E_Z\lbrack E_{Z'}\lbrack e^{S\cdot\lambda\cdot (Z-Z')}\rbrack\rbrack$  
>=$E_{Z,Z'}\lbrack E_{S}\lbrack e^{S\cdot\lambda\cdot (Z-Z')}\rbrack\rbrack$  
>&#10115;by MGF, we have below holds  
>$E_{S}\lbrack e^{S\cdot\lambda\cdot (Z-Z')}\rbrack\le e^{\frac {(\lambda\cdot (Z-Z'))^{2}}{2}}$  
>Because <font color="DeepPink">$\left|Z-Z'\right|\le (b-a)$ guarantees $(Z-Z')^{2}\le (b-a)^{2}$</font> , then  
>$E_{S}\lbrack e^{S\cdot\lambda\cdot (Z-Z')}\rbrack\le e^{\frac {(\lambda\cdot (b-a'))^{2}}{2}}$  
>Therefore, $E_Z\lbrack E_{Z'}\lbrack e^{\lambda\cdot (Z-Z')}\rbrack\rbrack\le e^{\frac {(\lambda\cdot (b-a'))^{2}}{2}}$  

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
<!-- Z\in\lbrack a,b\rbrack -->
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