---
layout: post
title: Hoeffding Bounds
---

## Prologue To The <font color="Red">Hoeffding Bounds</font>
<p class="message">
The <font color="Red">Hoeffding lemma</font> and <font color="Red">Hoeffding inequality</font> are pervasively found in tremendous papers 
and lectures in machine learning, statistics, probability theory, such inequality <font color="OrangeRed">relates the random variables 
belonging to the same distribution</font>, to facilitate <font color="DeepSkyBlue">stepping toward the minimum bias with the suggested sampling size</font>.  
</p>

### The <font color="Red">Mjtsai1974 Upper Bound</font>
>Before stepping into the major topic, make ourself a tiny break in a corner with a rather simple inequality, constrain still the same random variable as <font color="Red">Hoeffding lemma</font>.  It's just the trivial finding during my proof in these <font color="Red">Hoeffding bounds</font>.  I nicknamed it the <font color="Red">Mjtsai1974 Upper Bound</font>.  
>
>Given $X\in\lbrack a,b\rbrack$, it's a random variable with $E\lbrack x\rbrack$=$0$, then for any $s>0$, we have  
>$E\lbrack e^{s\cdot X}\rbrack\le e^{s\cdot(a-b)}$  
>
>Proof::mjtsai
>

### The <font color="Red">Hoeffding Lemma</font>
>
>

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