---
layout: post
title: Lagrange Multiplier
---

## Why Lagrange Multiplier?
Suppose you are given a function f(x<sub>1</sub>, x<sub>2</sub>), and would like to find out its extreme, subject to a constraint function g(x<sub>1</sub>, x<sub>2</sub>) = 0;  
where g(x<sub>1</sub>, x<sub>2</sub>) = ax<sub>1</sub> + bx<sub>2</sub> + c = 0, with a, b, c to be any scalar.

>The possible solution:  
[1]Figure out from the constraint function g(x<sub>1</sub>, x<sub>2</sub>) = 0 and express x<sub>2</sub> in terms of x<sub>1</sub>, like x<sub>2</sub> = h(x<sub>1</sub>)  
[2]Back to f(x<sub>1</sub>, x<sub>2</sub>) and replace x<sub>2</sub> with h(x<sub>1</sub>), f(x<sub>1</sub>, x<sub>2</sub>) = f(x<sub>1</sub>, h(x<sub>1</sub>))  
[3]Take partial derivative on x<sub>1</sub> to zero, &part;f(x<sub>1</sub>, h(x<sub>1</sub>)) ∕ &part;x<sub>1</sub> = 0, the x<sub>1</sub> value thus obtained would then lead us to the extreme of f(x<sub>1</sub>, x<sub>2</sub>)  

Here comes the problem that not all objective parameters could be expressed in terms of other objective parameters in the constraint function.  

### The Regularized Formula for Lagrange Multiplier
We thus step further into the lagrange multiplier, usually, we will see:

<p class="message">
&#8466;(x<sub>1</sub>, x<sub>2</sub>, λ) = f(x<sub>1</sub>, x<sub>2</sub>) + λ(x<sub>1</sub>, x<sub>2</sub>) ... (1),  
where λ is the lagrange multiplier, and &#8466;(x<sub>1</sub>, x<sub>2</sub>, λ) is the maximum likelihood function for us to come out with the λ that can optimize the extreme value of &#8466;
</p>

To get the most optimal solution, &part;&#8466; ∕ &part;x<sub>1</sub> = 0, &part;&#8466; ∕ &part;x<sub>2</sub> = 0, &part;&#8466; ∕ &part;λ = 0 must be mandatory!

Before proceed any further, we'd like to realize why (1) is the regularized formula for Lagrange Multiplier.  

[1]Expand f by means of Taylor Series:
>take f(x<sub>1</sub>, x<sub>2</sub>,..., x<sub>n</sub>) to be a continuous and differentiable function in R<sup>n</sup>,  
take x = [x<sub>1</sub>, x<sub>2</sub>,..., x<sub>n</sub>]<sup>t</sup> &isin; R<sup>n</sup>,  
then, begin from lim<sub>x&rarr;a</sub>f(x) = f(a), where x, a &isin; R<sup>n</sup>,  
express lim<sub>x&rarr;a</sub>f(x) in terms of Taylor Series:  
f(a) = f(x) + f&prime;(x)(x − a) + (1 ∕ (2!))f&Prime;(x)(x − a)<sup>2</sup> + (1 ∕ (6!))f&prime;&Prime;(x)(x − a)<sup>3</sup> + ...  
f(a) &asymp; f(x) + f&prime;(x)(x − a); ignore the second derivative term,  
then, f&prime;(x) = &part;f(x) ∕ &part;x = [&part;f(x) ∕ &part;x<sub>1</sub> &part;f(x) ∕ &part;x<sub>2</sub> ... &part;f(x) ∕ &part;x<sub>n</sub>]<sup>t</sup> = &nabla;f,  
f(a) &asymp; f(x) + (&nabla;f)<sup>t</sup>(x − a)<sub>n×1</sub>  

[2]Next, we discuss single constraint condition:
>=>suppose we are asking for min/max f(x), subject to g(x) = 0, x &isin; R<sup>n</sup>,  where g(x) = 0 is a hypersurface on R<sup>n</sup> and g(x) is continuous, differentiable,  
=>express lim<sub>x&rarr;a</sub>g(x) = g(a) in terms of Taylor Series, then:  
g(a) &asymp; g(x) + g&prime;(x)(x − a)  
&#160;&#160;&#160;&#160;&#160;= g(x) + (&nabla;g)<sup>t</sup>(x − a)<sub>n×1</sub>  
=>if a is also the point on the hypersurface, then, g(x) = g(a) = 0, we can treat (x − a) &rarr; 0, since x is very closed to a and conclude that (&nabla;g)<sup>t</sup>(x − a)<sub>n×1</sub> = 0  
=>that is to say (&nabla;g)<sup>t</sup> is the normal vector orthogonal to the hypersurface at the point a, where we can have:  
(&nabla;g)<sup>t</sup> &asymp; lim<sub>x&rarr;a</sub>[(g(x) − g(a)) ∕ (x − a)]  
=>cautions must be made that level curve of function f might hit onto the hypersurface of function g at the point x, with an infinitesimal distance to the point a, say it &epsilon;, where x + &epsilon; = a  
=>then, &nabla;f might not be full parallel to &nabla;g, we should have:  
&Delta; = &nabla;f − Proj<sub>&nabla;g</sub>(&nabla;f) ... &ne; 0  
&#160;&#160;&#160;&#160; = &nabla;f − (((&nabla;f)<sup>t</sup> &sdot; &nabla;g) ∕ ||&nabla;g||<sup>2</sup>) &sdot; &nabla;g  
 &‌#8757;&epsilon;&rarr;0, x&rarr;a, we thus have &Delta; &asymp; 0  
&there4;&Delta; = &nabla;f − λ&nabla;g &asymp; 0, where λ = (((&nabla;f)<sup>t</sup> &sdot; &nabla;g) ∕ ||&nabla;g||<sup>2</sup>)  
or, we can directly say that &nabla;f &isin; span{&nabla;g}  
=>if your AI algorithm works well, then &epsilon;&rarr;0, such that &nabla;f = λ&nabla;g could hold  



