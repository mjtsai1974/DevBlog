---
layout: post
title: Jensen's Inequality
---

## Prologue To The <font color="Red">Jensen's Inequality</font>
<p class="message">
The <font color="Red">Jensen's inequality</font> is an important inequality in the proof of many famous lemmas, theorems,   
it reveals that equality, <font color="RosyBrown">$E\lbrack g(X)\rbrack$=$g(E\lbrack X\rbrack)$ rarely occur for nonlinear function g.</font>  
Without actually computing the distribution of $g(X)$, we can easily relate $E\lbrack g(X)\rbrack$ to $g(E\lbrack X\rbrack)$.  
</p>

### <font color="Red">Jensen's Inequality</font>
>Let $g$ be a <font color="DeepSkyBlue">convex</font> function, and let $X$ be any random variable, then  
>$\;\;g(E\lbrack X\rbrack)\le E\lbrack g(X)\rbrack$  
>
>&#10112;why focus on the <font color="DeepSkyBlue">convex</font> function?  
>Be recalled that the second derivative of convex function is positive, that is $g″(X)\ge 0$.  The curve would be in a bowl shape.  
>&#10113;suppose $X$=$\\{e_1,e_2\\}$ is a random variable, containing 2 events with event $e_1$ the probability $\frac {4}{7}$, and event $e_2$ the probability $\frac {3}{7}$.  
>You can treat the 2 events as the inputs.  
><font color="DeepPink">Convexity of $g$ forces all line segments connecting 2 points on the curve lie above the part of the curve segment in between.</font>  
>&#10114;if we choose the line ranging from $(a,g(a))$ to $b,g(b)$, then  
>$(E\lbrack X\rbrack,E\lbrack g(X)\rbrack)$  
>=$(\frac {4}{7}\cdot a+\frac {3}{7}\cdot b,\frac {4}{7}\cdot g(a)+\frac {3}{7}\cdot g(b))$    
>=$\frac {4}{7}\cdot (a,g(a))+\frac {3}{7}\cdot (b,g(b))$  
>This point $(E\lbrack X\rbrack,E\lbrack g(X)\rbrack)$ must lie above the point $(E\lbrack X\rbrack,g(E\lbrack X\rbrack))$.  
>Therefore, we have proved $g(E\lbrack X\rbrack)\le E\lbrack g(X)\rbrack$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-03-02-prob-bound-jensen-inequality.png "g(E[X])<=E[g(X)]")

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