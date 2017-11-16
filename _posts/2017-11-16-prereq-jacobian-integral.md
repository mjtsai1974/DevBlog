---
layout: post
title: Jacobian and Integral
---

## Jacobian
<p class="message">
Just like lagrange multiplier as a great add-in of constraint in differential to reach the local optimal.  Jacobian is treated as a ratio in between two coordinate system of references transformed in calculus integration process by often.  
Before proceeding any further, take a good look in this article would be quiet helpful.
</p>

### What Is Jacobian?
>&#10112;Begin by a simple example, given $\int_a^bf(x)\operatorname dx$:  
$$\begin{array}{l}take\;x=h(y),\;differntiae\;x\;on\;y,\\\Rightarrow\frac{\operatorname dx}{\operatorname dy}=Dh(y),\\\Rightarrow x=h(y)=Dh(y)\cdot\operatorname dy\\\end{array}$$

<!-- don't know why, it doesn't work::Begin -->
<!-- because ' -->
<!-- $$\begin{array}{l}take\;x=h(y),\;differntiate\;on\;y,\\we\;have\frac{\operatorname dx}{\operatorname dy}=h^'(y),\\then,\;x=h(y)=h^'(y)\cdot\operatorname dy\end{array}$$ -->
<!-- don't know why, it doesn't work::End -->

>&#10113;then, we have below deduction:  
$$\begin{array}{l}\int_a^bf(x)\operatorname dx=\int_c^df(h(y))\cdot Dh(y)\operatorname dy,\\where\;c=h(a),d=h(b),\operatorname dx=Dh(y)\cdot\operatorname dy\end{array}$$

>&#10114;we can say that the $Dh(y)$ is the ratio from $\operatorname dx$ to $\operatorname dy$, it is the <font color="red">jacobian</font>.

### Normalize The Jacobian
>Next, this article would enter into the field a little bit deeper by double integral to prove the formula and $\left|J\right|$:  

$$\iint\limits_Rf(x,y)\operatorname dx\operatorname dy=\iint\limits_Sf(h(u,v),k(u,v))\cdot\left|J\right|\operatorname du\operatorname dv$$

>Let me give you a hint this proof is just to relate two sides of above equation with $\left|J\right|$, which is just a ratio due to system of coordinate of reference transformation from $x$, $y$ to $u$, $v$.  
>proof:  
>Take $x=h(u,v)$ and $y=k(u,v)$, we will prove by illustration:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-16-prereq-jacobian-integral-coordinate-transform.png "system of coordinate of reference transform")

>Suppose we are transforming from coordinate system <$x$, $y$> to <$u$, $v$>, and the surface area $R$ should be equal to the surface area $S$.
>We just have $area(R)=area(S)=\overset\rightharpoonup{MN}\otimes\overset\rightharpoonup{MQ}$, where $\otimes$ means the cross product.  
$$\begin{array}{l}\overset\rightharpoonup{MN}=\left\langle h(u+\triangle u,v)-h(u,v),k(u+\triangle u,v)-k(u,v)\right\rangle;\\where\;\triangle u\approx0,then\;we\;have\\\lim_{\triangle u\rightarrow0}\frac{h(u+\triangle u,v)-h(u,v)}{\triangle u}=\frac{\partial{h(u,v)}}{\partial u}\\\lim_{\triangle u\rightarrow0}\frac{k(u+\triangle u,v)-k(u,v)}{\triangle u}=\frac{\partial{k(u,v)}}{\partial u}\end{array}$$

>To get back to $\overset\rightharpoonup{MN}$, we need to multiply by $\triangle u$ for both $h$ and $k$ terms.  Then, we have:  
$$\overset\rightharpoonup{MN}=\left\langle\frac{\partial{h(u,v)}}{\partial u}\cdot\triangle u,\frac{\partial{k(u,v)}}{\partial u}\cdot\triangle u\right\rangle$$

>Above deduction holds for $\overset\rightharpoonup{MQ}$, apply it would we get similar result:  
$$\overset\rightharpoonup{MQ}=\left\langle\frac{\partial{h(u,v)}}{\partial v}\cdot\triangle v,\frac{\partial{k(u,v)}}{\partial v}\cdot\triangle v\right\rangle$$

>Thus, take the absolute value of $area(R)=area(S)=\overset\rightharpoonup{MN}\otimes\overset\rightharpoonup{MQ}$.  
>Continue to illustrate by geometric cross product:  
$$\begin{array}{l}\begin{vmatrix}i&j&k\\\frac{\partial{h(u,v)}}{\partial u}\cdot\triangle u&\frac{\partial{k(u,v)}}{\partial u}\cdot\triangle u&0\\\frac{\partial{h(u,v)}}{\partial v}\cdot\triangle v&\frac{\partial{k(u,v)}}{\partial v}\cdot\triangle v&0\end{vmatrix}\\=\frac{\partial{h(u,v)}}{\partial u}\cdot\triangle u\cdot\frac{\partial{k(u,v)}}{\partial v}\cdot\triangle v-\frac{\partial{h(u,v)}}{\partial v}\cdot\triangle v\cdot\frac{\partial{k(u,v)}}{\partial u}\cdot\triangle u\\=\begin{bmatrix}\frac{\partial{h(u,v)}}{\partial u}\cdot\frac{\partial{k(u,v)}}{\partial v}-\frac{\partial{h(u,v)}}{\partial v}\cdot\frac{\partial{k(u,v)}}{\partial u}\end{bmatrix}\cdot\triangle u\cdot\triangle v\end{array}$$

>Make one more step, we can take the first part to be $\left|J\right|$ expressed in terms of $2\times2$ determinant:  
$$\begin{array}{l}\begin{bmatrix}\frac{\partial{h(u,v)}}{\partial u}\cdot\frac{\partial{k(u,v)}}{\partial v}-\frac{\partial{h(u,v)}}{\partial v}\cdot\frac{\partial{k(u,v)}}{\partial u}\end{bmatrix}\\={\begin{vmatrix}\frac{\partial{h(u,v)}}{\partial u}&\frac{\partial{k(u,v)}}{\partial u}\\\frac{\partial{h(u,v)}}{\partial v}&\frac{\partial{k(u,v)}}{\partial v}\end{vmatrix}}_{2\times2\;detmiant}\\=\begin{vmatrix}J\end{vmatrix}\end{array}$$

>Finally, we have conclusion below:  
$$\begin{array}{l}area(R)\\=\triangle x\cdot\triangle y\\\cong\operatorname dx\cdot\operatorname dy\\\cong\left|J\right|\cdot\triangle u\cdot\triangle v\\\cong\left|J\right|\cdot\operatorname du\cdot\operatorname dv\\=area(S)\end{array}$$

>At this ending of proof, we can also treat $\left|J\right|$ to be the ratio from $area(R)$ to $area(S)$,  
>where $$area(R)=\left|J\right|\cdot area(S)$$.
