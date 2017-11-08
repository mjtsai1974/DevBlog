---
layout: post
title: Gradient Descendent
---

## Gradient Descendent
<p class="message">
Most widely used in machine learning with respect to linear regression, logistic regression for supervised learning.  But, the gradient descendent itself actually knows nothing when to stop!!    
</p>

### Begin from Cost Function in Simple Linear Regressoin(S.L.R)
>take the cost function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi><mo>(</mo><mi>&#x3B8;</mi><mo>)</mo><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mi>2m</mi></mstyle></mfrac><munderover><mo>&#x2211;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mo>(</mo><msub><mi>h</mi><mi>&#x3B8;</mi></msub><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msup><mo>)</mo><mo>-</mo><msup><mi>y</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msup><msup><mo>)</mo><mn>2</mn></msup></math>, where the purpose of S.L.R is to minimize <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi><mo>(</mo><mi>&#x3B8;</mi><mo>)</mo></math>.  
>given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>h</mi><mi>&#x3B8;</mi></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>&#x3B8;</mi><mi>t</mi></msup><mo>&#xB7;</mo><mi>x</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#x3B8;</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><msub><mi>&#x3B8;</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><mi>&#x3B8;</mi><mn>2</mn></mtd></mtr></mtable></mfenced></math> is the coefficients,  
><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>&#xA0;</mo><mo>=</mo><mo>&#xA0;</mo><mfenced open="[" close="]"><mtable><mtr><mtd><msub><mi>x</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><mi>x</mi><mn>2</mn></mtd></mtr></mtable></mfenced></math> is the input data  
>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn></math>, it is the intercept, or the bias term.  
>as to the divide by 2m is an artificial design:  
>&#10112;<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math> is to eliminate the power of 2 in the square, after differentiation is taken.  
>&#10113;<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>m</mi></mfrac></math> is to average all squared errors of m input rows of data.

### Step into Gradient &nabla; of J(&Theta;)
>take derivation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi><mo>(</mo><mi>&#x3B8;</mi><mo>)</mo></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#x3B8;</mi><mi>j</mi></msub></math>, then we obtain:  
><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#x2202;</mo><mi>J</mi><mo>(</mo><mi>&#x3B8;</mi><mo>)</mo></mrow><mrow><mo>&#x2202;</mo><msub><mi>&#x3B8;</mi><mi>j</mi></msub></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>m</mi></mfrac><munderover><mo>&#x2211;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mo>(</mo><msub><mi>h</mi><mi>&#x3B8;</mi></msub><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msup><mo>)</mo><mo>-</mo><msup><mi>y</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msup><mo>)</mo><mo>&#xB7;</mo><msubsup><mi>x</mi><mi>j</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msubsup></math>  
>since we are running batch gradient descendent, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>m</mi></mfrac></math> is required to average it.  
>if m = 1, then, we just have the j-th term as:  
><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#x2202;</mo><mi>J</mi><mo>(</mo><mi>&#x3B8;</mi><mo>)</mo></mrow><mrow><mo>&#x2202;</mo><msub><mi>&#x3B8;</mi><mi>j</mi></msub></mrow></mfrac><mo>=</mo><munderover><mo>&#x2211;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mo>(</mo><msub><mi>h</mi><mi>&#x3B8;</mi></msub><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msup><mo>)</mo><mo>-</mo><msup><mi>y</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msup><mo>)</mo><mo>&#xB7;</mo><msubsup><mi>x</mi><mi>j</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msubsup></math>  

### Learning Rate &alpha;

>it is used to converge the result of gradient descendent.  The smaller value would believed to have a less fluctuation.

### Put It Together

>put everything together, we will have the j-the term of &Theta;, it is inclusive of the bias term &Theta;<sub>1</sub>:  
><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#x3B8;</mi><mi>j</mi></msub><mo>=</mo><msub><mi>&#x3B8;</mi><mi>j</mi></msub><mo>-</mo><mi>&#x3B1;</mi><mo>&#xB7;</mo><mfrac><mn>1</mn><mi>m</mi></mfrac><munderover><mo>&#x2211;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mo>(</mo><msub><mi>h</mi><mi>&#x3B8;</mi></msub><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msup><mo>)</mo><mo>-</mo><msup><mi>y</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msup><mo>)</mo><mo>&#xB7;</mo><msubsup><mi>x</mi><mi>j</mi><mrow><mo>(</mo><mi>i</mi><mo>)</mo></mrow></msubsup><mo>,</mo><mo>&#xA0;</mo><mi>w</mi><mi>h</mi><mi>e</mi><mi>r</mi><mi>e</mi><mo>&#xA0;</mo><mi>j</mi><mo>=</mo><mn>1</mn><mo>&#xA0;</mo><mi>t</mi><mi>o</mi><mo>&#xA0;</mo><mi>n</mi><mo>,</mo><mo>&#xA0;</mo><mi>&#x3B8;</mi><mo>&#x2208;</mo><msup><mi>R</mi><mi>n</mi></msup></math>  
>given X &isin; M<sub>m×n</sub>, &Theta; &isin; M<sub>n×1</sub>, Y &isin; M<sub>m×1</sub>, x<sup>i</sup> &isin; M<sub>n×1</sub>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>&#xA0;</mo><mo>=</mo><mo>&#xA0;</mo><msub><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mn>1</mn><mo>)</mo></mrow></msup><msup><mo>)</mo><mi>t</mi></msup><mo>-</mo></mtd></mtr><mtr><mtd><mo>-</mo><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow></msup><msup><mo>)</mo><mi>t</mi></msup><mo>-</mo></mtd></mtr><mtr><mtd><mo>.</mo><mo>.</mo><mo>.</mo></mtd></mtr><mtr><mtd><mo>-</mo><mo>(</mo><msup><mi>x</mi><mrow><mo>(</mo><mi>m</mi><mo>)</mo></mrow></msup><msup><mo>)</mo><mi>t</mi></msup><mo>-</mo></mtd></mtr></mtable></mfenced><mrow><mi>m</mi><mi>x</mi><mi>n</mi></mrow></msub></math>
