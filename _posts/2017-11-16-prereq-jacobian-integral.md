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

>&#10114;we can say that the $Dh(y)$ is the ratio from $\operatorname dx$ to $\operatorname dy$, it is the jacobian.

### Normalize The Jacobian
>Next, this article would enter into the field a little bit deeper.  