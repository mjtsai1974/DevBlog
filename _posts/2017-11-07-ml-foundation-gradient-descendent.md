---
layout: post
title: Gradient Descendent
---

## Gradient Descendent
<p class="message">
Most widely used in machine learning with respect to linear regression, logistic regression for supervised learning.  But, the gradient descendent itself actually knows nothing when to stop!!    
</p>

### Begin from Cost Function in Simple Linear Regressoin(S.L.R)
>take the cost function J(&Theta;) = (1 ∕ (2m))&sum;<sub>i</sub>(h<sub>&Theta;</sub>(x<sup>(i)</sup>) − y<sup>(i)</sup>)<sup>2</sup>, where the purpose of S.L.R is to minimize J(&Theta;).  
>given h<sub>&Theta;</sub>(x) = &Theta;<sup>t</sup> &sdot; x, where &Theta; = [&Theta;<sub>1</sub> &Theta;<sub>2</sub>]<sup>t</sup> is the coefficients, x = [x<sub>1</sub> x<sub>2</sub>]<sup>t</sup> is the input data and x<sub>1</sub> = 1, it is the intercept, or the bias term.  
>as to the divide by 2m is an artificial design:  
>&#10112;1 ∕ 2 is to eliminate the power of 2 in the square, after differentiation is taken.  
>&#10113;1 ∕ m is to average all squared errors of m input rows of data.

### Step into Gradient &nabla; of J(&Theta;)
>take derivation of J(&Theta;) on &Theta;<sub>j</sub>, then we obtain:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-07-ml-found-gradient-descendent-size-m.png "m records of input data")

>since we are running batch gradient descendent, 1 ∕ m is required to average it.  
>if m = 1, then, we just have the j-th term as:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-07-ml-found-gradient-descendent-size-1.png "single input data")

### Learning Rate &alpha;

>it is used to converge the result of gradient descendent.  The smaller value would believed to have a less fluctuation.

### Put It Together

>put everything together, we will have the j-the term of &Theta;, it is inclusive of the bias term &Theta;<sub>1</sub>:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-07-ml-found-gradient-descendent-size-1.png "j-th term of &Theta;")

>given X &isin; M<sub>m×n</sub>, &Theta; &isin; M<sub>n×1</sub>, Y &isin; M<sub>m×1</sub>, x<sup>i</sup> &isin; M<sub>n×1</sub>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>&#xA0;</mo><mo>=</mo><mo>&#xA0;</mo><msub><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mn>1</mn><mo>)</mo></mrow></msup><msup><mo>)</mo><mi>t</mi></msup><mo>-</mo></mtd></mtr><mtr><mtd><mo>-</mo><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow></msup><msup><mo>)</mo><mi>t</mi></msup><mo>-</mo></mtd></mtr><mtr><mtd><mo>.</mo><mo>.</mo><mo>.</mo></mtd></mtr><mtr><mtd><mo>-</mo><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mi>m</mi><mo>)</mo></mrow></msup><msup><mo>)</mo><mi>t</mi></msup><mo>-</mo></mtd></mtr></mtable></mfenced><mrow><mi>m</mi><mi>x</mi><mi>n</mi></mrow></msub></math>
