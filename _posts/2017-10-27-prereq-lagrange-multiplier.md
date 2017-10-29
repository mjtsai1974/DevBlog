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

[1]Expand f by means of Taylor Series
>&#10112;take f(x<sub>1</sub>, x<sub>2</sub>,..., x<sub>n</sub>) to be a continuous and differentiable function in R<sup>n</sup>,  
&#10113;take x = [x<sub>1</sub>, x<sub>2</sub>,..., x<sub>n</sub>]<sup>t</sup> &isin; R<sup>n</sup>,  
&#10114;then, begin from lim<sub>x&rarr;a</sub>f(x) = f(a), where x, a &isin; R<sup>n</sup>,  
express lim<sub>x&rarr;a</sub>f(x) in terms of Taylor Series:  
f(a) = f(x) + f&prime;(x)(x − a) + (1 ∕ (2!))f&Prime;(x)(x − a)<sup>2</sup> + (1 ∕ (6!))f&prime;&Prime;(x)(x − a)<sup>3</sup> + ...  
f(a) &asymp; f(x) + f&prime;(x)(x − a); ignore the second derivative term,  
then, f&prime;(x) = &part;f(x) ∕ &part;x = [&part;f(x) ∕ &part;x<sub>1</sub> &part;f(x) ∕ &part;x<sub>2</sub> ... &part;f(x) ∕ &part;x<sub>n</sub>]<sup>t</sup> = &nabla;f,  
f(a) &asymp; f(x) + (&nabla;f)<sup>t</sup>(x − a)<sub>n×1</sub>  

[2]Next, we discuss single constraint condition
>&#10112;suppose we are asking for min/max f(x), subject to g(x) = 0, x &isin; R<sup>n</sup>,  where g(x) = 0 is a continuous, differentiable hypersurface on R<sup>n</sup>  
&#10113;express lim<sub>x&rarr;a</sub>g(x) = g(a) in terms of Taylor Series, then:  
g(a) &asymp; g(x) + g&prime;(x)(x − a) = g(x) + (&nabla;g)<sup>t</sup> &sdot;(x − a) <sub>n×1</sub>  
&#10114;if a is also the point on the hypersurface, then, g(x) = g(a) = 0, we can treat (x − a) &rarr; 0, since x is very closed to a and conclude that (&nabla;g)<sup>t</sup>(x − a)<sub>n×1</sub> = 0  
&#10115;that is to say (&nabla;g)<sup>t</sup> is the normal vector orthogonal to the hypersurface at the point a, where we can have:  
(&nabla;g)<sup>t</sup> &asymp; lim<sub>x&rarr;a</sub>[(g(x) − g(a)) ∕ (x − a)]<sup>t</sup>  
&#10116;cautions must be made that level curve of function f might hit onto the hypersurface of function g at the point x, with an infinitesimal distance to the point a, say it &epsilon;, where x + &epsilon; = a  
&#10117;then, &nabla;f might not be full parallel to &nabla;g, we should have:  
&Delta; = &nabla;f − Proj<sub>&nabla;g</sub>(&nabla;f) ... &ne; 0  
&#160;&#160;&#160;&#160; = &nabla;f − (((&nabla;f)<sup>t</sup> &sdot; &nabla;g) ∕ ||&nabla;g||<sup>2</sup>) &sdot; &nabla;g  
∵&epsilon;&rarr;0, x&rarr;a, we thus have &Delta; &asymp; 0  
&there4;&Delta; = &nabla;f − λ&nabla;g &asymp; 0, where λ = (((&nabla;f)<sup>t</sup> &sdot; &nabla;g) ∕ ||&nabla;g||<sup>2</sup>)  
or, we can directly say that &nabla;f &isin; span{&nabla;g}  
&#10118;if your AI algorithm works well, then &epsilon;&rarr;0, such that &nabla;f = λ&nabla;g could hold, we illustrate this concept of projecting &nabla;f onto &nabla;g, see below pic(the picture is just by intuition).  

![Project &nabla;f onto &nabla;g]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-10-27-prereq-lagrange-multiplier-projection.png "if &epsilon;&rarr;0, then &nabla;f = λ&nabla;g")

[3]Lagrangian representation in most application design
>In most application design, Lagrange Multiplier likelihood function is expressed as:  
&#8466;(x, λ) = f(x) + λg(x), x &isin; R<sup>n</sup>,  
&part;&#8466; ∕ &part;x = &nabla;f + λ&nabla;g ... (a)  
&part;&#8466; ∕ &part;λ = 0 ... (b)  
=>Resolve above two equations (a), (b) to get λ:  
&#10112;if λ = 0, then, &nabla;f = 0 means that &nabla;f(x<sup>*</sup>) = 0 and g(x<sup>*</sup>) = 0 just satisfy the constraint function, where  
g(x) = a<sub>1</sub>x<sub>1</sub><sup>d1</sup> + a<sub>2</sub>x<sub>2</sub><sup>d2</sup> + ... + a<sub>n</sub>x<sub>n</sub><sup>dn</sup> + C = 0, x &isin; R<sup>n</sup>  
&#10113;if λ &ne; 0, then, &nabla;f = -λ&nabla;g, it implies that &nabla;f and &nabla;g are inverse parallel, where f(x) has a extreme(min/max) at this point x<sup>*</sup>(so does g(x))  

[4]Why &nabla;f and &nabla;g are inverse parallel?
>∵the regularization by using the lagrange multiplier would further reduce the magnitude of &nabla;f, the final &nabla;f would be normal vector with small magnitude(length), thus the small error when we project sample data onto &nabla;f.  
This design expects a minimum magnitude of the gradient after regularization at the tangent point where the level curve and the hypersurface of the constraint function.

![Inverse Parallel]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-10-27-prereq-lagrange-multiplier-inverse-parallel.png "to have a minimum magnitude of the regularization")

### What to choose in between &#8466;(x, λ) = f(x) + λg(x) v.s. &#8466;(x, λ) = f(x) − λg(x)
>It depends on exactly your design of regularization algorithm and how good you believe your regularization can work.  If you aims at reducing the prediction error(&Delta;),
then, &#8466;(x, λ) = f(x) − λg(x) might be the most appropriate, whereas, inverse parallel version of &#8466;(x, λ) = f(x) + λg(x) would make the point on minimizing the magnitude of &nabla;f which is orthogonal to the hyperplane.  Both guarantee the projecting
sample data onto &nabla;f would we have the minimal error(see below pic for intuition).  
One thing interest is that by choosing &#8466;(x, λ) = f(x) + λg(x), the λ is negative; nevertheless, &#8466;(x, λ) = f(x) − λg(x) would come out with positive λ, concluded from the 2 combination, we should have the lagrgarian in a more regularized expression:  
&#8466;(x, λ) = f(x) + sign(λ)λg(x), where sign(λ) is negative.

![Just Works]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-10-27-prereq-lagrange-multiplier-just-works.png "They both work")

### The Lagrange Multiplier and Multiple Constraints
>&#10112;succeeding to conclusion in above paragraph, suppose we are asking for min/max f(x), subject to g<sub>k</sub>(x) = 0, x &isin; R<sup>n</sup>,  k = 1 to m, and g<sub>k</sub>(x) is continuous and differentiable,  
where &nabla;f = -&sum;<sub>k=1</sub><sup>m</sup>λ<sub>k</sub>&nabla;g<sub>k</sub>  
&hArr; &nabla;f &isin; span{&nabla;g<sub>1</sub>, &nabla;g<sub>2</sub>,..., &nabla;g<sub>m</sub>}  
&#10113;refine Lagrange Multiplier likelihood function, we have:  
&#8466;(x, {λ<sub>k</sub>}) = f(x) + &sum;<sub>k</sub>λ<sub>k</sub>g<sub>k</sub>(x), for k = 1 to m  
&#10114;to find the extreme value(min/max), we need:  
&nabla;<sub>x</sub>&#8466; = &nabla;f + &sum;<sub>k=1</sub><sup>m</sup>λ<sub>k</sub>&nabla;g<sub>k</sub> = 0 ... (c)  
&nabla;<sub>λ<sub>k</sub></sub>&#8466; = g<sub>k</sub>(x) = 0 for k = 1 to m ... (d)  