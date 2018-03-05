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
>Then,  
>
>Proof:
>&#10112;by known, $E\lbrack Z\rbrack$=$E\lbrack Z'\rbrack$, then,  
>$P(Z-E\lbrack Z\rbrack)$=$P(Z-E\lbrack Z'\rbrack)$, which implies that  
>$E_Z\lbrack Z-E\lbrack Z\rbrack\rbrack$=$E_Z\lbrack Z-E\lbrack Z'\rbrack\rbrack$  
>&#10113;by <font color="Red">Jensen's inequality</font>, we have it that  
>$P(e^{Z-E\lbrack Z\rbrack})$  
>=$P(e^{Z-E\lbrack Z'\rbrack})$  
>$\le P(E\lbrack e^{Z-Z'}\rbrack)$  
>, which in turns implies that  
>$E_Z\lbrack e^{Z-E\lbrack Z\rbrack}\rbrack$  
>=$E_Z\lbrack e^{Z-E\lbrack Z'\rbrack}\rbrack$  
>$\le E_Z\lbrack E_{Z'}\lbrack e^{Z-Z'}\rbrack\rbrack$  

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