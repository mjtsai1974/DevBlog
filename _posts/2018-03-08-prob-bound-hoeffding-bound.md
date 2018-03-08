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

### The <font color="Red">Mjtsai1974 Light Weight Upper Bound</font>
>Before stepping into the major topic, make ourself a tiny break in a corner with a rather simple inequality, constrain still the same random variable as <font color="Red">Hoeffding lemma</font>.  It's just the trivial finding during my proof in these <font color="Red">Hoeffding bounds</font>.  I nicknamed it the <font color="Red">Mjtsai1974 Light Weight Upper Bound</font>.  
>
>Given $X\in\lbrack a,b\rbrack$, it's a random variable with $E\lbrack x\rbrack$=$0$, then for any $s>0$, we have $E\lbrack e^{s\cdot X}\rbrack\le e^{s\cdot(a-b)}$  
>
>Proof::mjtsai  
>&#10112;by given $X\in\lbrack a,b\rbrack$, take $\lambda$=$\frac {x-a}{b-a}$,  
>we just have $x$=$(1-\lambda)\cdot a$+$\lambda\cdot b$.  
>&#10113;since $g(E\lbrack s\cdot X\rbrack)\le E\lbrack g(s\cdot X)\rbrack$ by <font color="Red">Jensen's inequality</font> for any convex function $g(X)$=$e^{X}$, then  
>$e^{(1-\lambda)\cdot s\cdot a+\lambda\cdot s\cdot b}\le (1-\lambda)\cdot e^{s\cdot a}+\lambda\cdot e^{s\cdot b}$  
>$\Rightarrow E\lbrack e^{(1-\lambda)\cdot s\cdot a+\lambda\cdot s\cdot b}\rbrack\le E\lbrack (1-\lambda)\cdot e^{s\cdot a}+\lambda\cdot e^{s\cdot b}\rbrack$  
>&#10114;that is to say, for any $x\in X$, we have  
>$E\lbrack e^{s\cdot x}\rbrack$  
>$\le E\lbrack (1-\lambda)\cdot e^{s\cdot a}+\lambda\cdot e^{s\cdot b}\rbrack$  
>=$E\lbrack (\lambda+(1-\lambda)\cdot e^{s\cdot a-s\cdot b})\cdot e^{s\cdot b}\rbrack$  
>=$E\lbrack (\frac {x-a}{b-a}+(\frac {b-x}{b-a})\cdot e^{s\cdot a-s\cdot b})\cdot e^{s\cdot b}\rbrack$  
>=$(\frac {-a}{b-a}+(\frac {b}{b-a})\cdot e^{s\cdot (a-b)})\cdot e^{s\cdot b}$...$E\lbrack x\rbrack$=$0$  
>, which is equivalent to ask for its approximation.   
>&#10115;take $p$=$\frac {-a}{b-a}$, then $1-p$=$\frac {b}{b-a}$.  From the two equalities, we can deduce out two expressions for $b$:  
>$b$=$\frac {a\cdot (p-1)}{p}$ and $b$=$(1-p)\cdot (b-a)$  
>Choose $b$=$(1-p)\cdot (b-a)$ to express $b$, then above inequality becomes  
>$E\lbrack e^{s\cdot x}\rbrack$  
>$\le (\frac {-a}{b-a}+(\frac {b}{b-a})\cdot e^{s\cdot (a-b)})\cdot e^{s\cdot b}$  
>=$((1-p)\cdot e^{s\cdot (a-b)}+p)\cdot e^{s\cdot (1-p)\cdot (b-a)}$  
>=$((1-p)\cdot e^{s\cdot (a-b)}+p)\cdot e^{s\cdot (p-1)\cdot (a-b)}$  
>The reason we choose such $b$ expression is to simplify the inequality.  
>&#10116;take $u$=$a-b$,$\theta(u)$=$((1-p)\cdot e^{s\cdot u}+p)\cdot e^{s\cdot (p-1)\cdot u}$, then  
>$ln\theta(u)$  
>=$ln((1-p)\cdot e^{s\cdot u}+p)$+$s\cdot (p-1)\cdot u$  
>$\le ln((1-p)\cdot e^{s\cdot u}+p)$...since $p-1\le 0$  
>$\le ln((1-p)\cdot e^{s\cdot u})$...since $p\le 1$    
>$\le ln(e^{s\cdot u})$  
>=$s\cdot u$  
>, then <font color="DeepPink">$\theta(u)\le e^{s\cdot u}$</font>  
>Therefore, $E\lbrack e^{s\cdot X}\rbrack\le e^{s\cdot(a-b)}$ is thus proved, this is a simple, light weight inequality, I denote it <font color="Red">Mjtsai1974 Light Weight Upper Bound</font>.  

### The <font color="Red">Hoeffding Lemma</font>
>Given $X\in\lbrack a,b\rbrack$, it's a random variable with $E\lbrack x\rbrack$=$0$, then for any $s>0$, we have $E\lbrack e^{s\cdot X}\rbrack\le e^{\frac {s^2\cdot(b-a)^2}{8}}$  
>
>Proof::mjtsai  
>We would inherit from &#10116; in the proof of <font color="Red">Mjtsai1974 Light Weight Upper Bound</font>, begin from $ln\theta(u)$=$ln((1-p)\cdot e^{s\cdot u}+p)$+$s\cdot (p-1)\cdot u$, where $u$=$a-b$,$\theta(u)$=$((1-p)\cdot e^{s\cdot u}+p)\cdot e^{s\cdot (p-1)\cdot u}$.  
>&#10112;take $M(u)$=$ln\theta(u)$, by <font color="OrangeRed">Taylor theorem</font>, for $w\in\lbrack u,0\rbrack$, where in this case $u\le 0$, we have  
>$\lim_{w\rightarrow u}M(w)$  
>$\approx ln\theta(u)$+$\frac {ln^{′}\theta(u)}{1!}\cdot (w-u)$+$\frac {ln^{″}\theta(u)}{2!}\cdot (w-u)^2$+$\frac {ln^{′″}\theta(u)}{3!}\cdot (w-u)^3$+...  
>$\le ln\theta(0)$+$\frac {ln^{′}\theta(0)}{1!}\cdot (0-u)$+$\frac {ln^{″}\theta(0)}{2!}\cdot (0-u)^2$+$\frac {ln^{′″}\theta(0)}{3!}\cdot (0-u)^3$+...  
>&#10113;from above, we must make first, second derivatives, they are  
>$ln^{′}\theta(u)$=$(p+(1-p)\cdot e^{s\cdot u})^{-1}\cdot ((1-p)\cdot s\cdot e^{s\cdot u})$+$s\cdot(p-1)$  
>$ln^{″}\theta(u)$=$-1\cdot (p+(1-p)\cdot e^{s\cdot u})^{-2}\cdot ((1-p)\cdot s\cdot e^{s\cdot u})^{2}$  
>$\;\;\;\;\;\;\;\;+(p+(1-p)\cdot e^{s\cdot u})^{-1}\cdot ((1-p)\cdot s^2\cdot e^{s\cdot u})$  
>And, $ln\theta(0)$=$0$, $ln^{′}\theta(0)$=$0$,  
>$ln^{″}\theta(0)$=$-1\cdot((1-p)\cdot s)^2$+$(1-p)\cdot s^2$=$p\cdot (1-p)\cdot s^2$  
>&#10114;therefore, we'd like to <font color="DeepSkyBlue">maximum the term $ln^{″}\theta(u)$</font>,  
>take $z$=$e^{s\cdot u}$, $s$=$\frac {ln(z)}{u}$, then  
>$ln^{″}\theta(u)$...further regularized  
>=$\frac {p\cdot (1-p)\cdot s^2\cdot e^{s\cdot u}}{(p+(1-p)\cdot e^{s\cdot u})^{2}}$  
>=$\frac {p\cdot (1-p)\cdot (\frac {ln(z)}{u})^2\cdot z}{(p+(1-p)\cdot z)^{2}}$  
>$\le \frac {p\cdot (1-p)\cdot z}{(p+(1-p)\cdot z)^{2}}$...$(\frac {ln(z)}{u})^2\le 1$  
>&#10115;take $N(z)$=$\frac {p\cdot (1-p)\cdot z}{(p+(1-p)\cdot z)^{2}}$, and <font color="DeepSkyBlue">$ln^{″}\theta(u)$=$s^2\cdot N(z)$</font>, <font color="OrangeRed">this is equivalent to ask for the maximum of $N(z)$</font>, the formal procedure would be to take its first derivative and set it to $0$, next to get the possible $z$ expressed in terms of $p$, in this case.  
>$N′(z)$=$\frac {p^{2}\cdot (1-p)-p\cdot (1-p)^{2}\cdot z}{(p+(1-p)\cdot z)^{3}}$=$0$  
>After we solve it, we get $z$=$\frac {p}{1-p}$ is the <font color="DeepSkyBlue">critical point</font>.  
>&#10116;take $z$=$\frac {p}{1-p}$ in $N(z)$  
>$N(z)$=$\frac {p\cdot (1-p)\cdot\frac {p}{1-p}}{(p+(1-p)\cdot\frac {p}{1-p})^{2}}$=$\frac {p^{2}}{4\cdot p^{2}}$=$\frac {1}{4}$  
>Be recalled that <font color="DeepSkyBlue">$ln^{″}\theta(u)$=$s^2\cdot N(z)$</font>, back to the <font color="OrangeRed">Taylor expansion</font> in &#10113;, we have  
>$ln\theta(u)$  
>=$M(u)$  
>$\le \frac {ln^{″}\theta(0)}{2!}\cdot(u)^{2}$  
>=$\frac {s^{2}\cdot N(z)}{2!}\cdot (u)^2$  
>$\le \frac {1}{2!}\cdot s^{2}\cdot\frac {1}{4}\cdot u^{2}$  
>=$\frac {1}{8}\cdot s^{2}\cdot u^{2}$  
>Therefore, $\theta(u)\le e^{\frac {1}{8}\cdot s^{2}\cdot u^{2}}$  
>&#10117;finally, we just proved that  
>$E\lbrack e^{s\cdot X}\rbrack\le \theta(u)\le e^{\frac {1}{8}\cdot s^{2}\cdot u^{2}}$=$e^{\frac {s^{2}\cdot (a-b)^{2}}{8}}$=$e^{\frac {s^{2}\cdot (b-a)^{2}}{8}}$  

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
<!-- \ln\left(\right)-->

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