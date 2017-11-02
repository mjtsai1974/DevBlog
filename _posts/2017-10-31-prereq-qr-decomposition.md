---
layout: post
title: QR Decomposition
---

## QR Decomposition
<p class="message">
QR decomposition claims that A = B&sdot;X = B&sdot;D&sdot;E&sdot; X = Q&sdot;R.
This article will show you the way to prove it, we will begin from Gram-Schmit Procedure, then, briefly introduce to the projection matrix, then, migrate to triangular matrix, finally to prove the QR decomposition.    
</p>

### Gram-Schmit Procedure
>Given a set of linear independent vectors set S = {v<sub>1</sub>, v<sub>2</sub>,..., v<sub>p</sub>} &isin; R<sup>m</sup>,  
>define vectors u<sub>i</sub>, 1 &le; i &le; p by   
>u<sub>i</sub> = v<sub>i</sub> − [((v<sub>i</sub>)<sup>t</sup> &sdot; u<sub>1</sub>) ∕ ((u<sub>1</sub>)<sup>t</sup> &sdot; u<sub>1</sub>)] &sdot; u<sub>1</sub> − [((v<sub>i</sub>)<sup>t</sup> &sdot; u<sub>2</sub>) ∕ ((u<sub>2</sub>)<sup>t</sup> &sdot; u<sub>2</sub>)] &sdot; u<sub>2</sub> − [((v<sub>i</sub>)<sup>t</sup> &sdot; u<sub>3</sub>) ∕ ((u<sub>3</sub>)<sup>t</sup> &sdot; u<sub>3</sub>)] &sdot; u<sub>3</sub> − ... − [((v<sub>i</sub>)<sup>t</sup> &sdot; u<sub>i−1</sub>) ∕ ((u<sub>i−1</sub>)<sup>t</sup> &sdot; u<sub>i−1</sub>)] &sdot; u<sub>i−1</sub>  
>the set T = {u<sub>1</sub>, u<sub>2</sub>,..., u<sub>p</sub>} is a linear independent orthonormal set and aoan(S) = span(T)  
>we just have below holds:  
>u<sub>1</sub> = v<sub>1</sub>  
>u<sub>2</sub> = v<sub>2</sub> − [((v<sub>2</sub>)<sup>t</sup> &sdot; u<sub>1</sub>) ∕ ((u<sub>1</sub>)<sup>t</sup> &sdot; u<sub>1</sub>)] &sdot; u<sub>1</sub>  
>u<sub>3</sub> = v<sub>3</sub> − [((v<sub>3</sub>)<sup>t</sup> &sdot; u<sub>1</sub>) ∕ ((u<sub>1</sub>)<sup>t</sup> &sdot; u<sub>1</sub>)] &sdot; u<sub>1</sub> − [((v<sub>3</sub>)<sup>t</sup> &sdot; u<sub>2</sub>) ∕ ((u<sub>2</sub>)<sup>t</sup> &sdot; u<sub>2</sub>)] &sdot; u<sub>2</sub>  
>u<sub>4</sub> = v<sub>4</sub> − [((v<sub>4</sub>)<sup>t</sup> &sdot; u<sub>1</sub>) ∕ ((u<sub>1</sub>)<sup>t</sup> &sdot; u<sub>1</sub>)] &sdot; u<sub>1</sub> − [((v<sub>4</sub>)<sup>t</sup> &sdot; u<sub>2</sub>) ∕ ((u<sub>2</sub>)<sup>t</sup> &sdot; u<sub>2</sub>)] &sdot; u<sub>2</sub> − [((v<sub>4</sub>)<sup>t</sup> &sdot; u<sub>3</sub>) ∕ ((u<sub>3</sub>)<sup>t</sup> &sdot; u<sub>3</sub>)] &sdot; u<sub>3</sub>  
>...  
>u<sub>p</sub> = v<sub>p</sub> − [((v<sub>p</sub>)<sup>t</sup> &sdot; u<sub>1</sub>) ∕ ((u<sub>1</sub>)<sup>t</sup> &sdot; u<sub>1</sub>)] &sdot; u<sub>1</sub> − [((v<sub>p</sub>)<sup>t</sup> &sdot; u<sub>2</sub>) ∕ ((u<sub>2</sub>)<sup>t</sup> &sdot; u<sub>2</sub>)] &sdot; u<sub>2</sub> − ... − [((v<sub>p</sub>)<sup>t</sup> &sdot; u<sub>p−1</sub>) ∕ ((u<sub>p−1</sub>)<sup>t</sup> &sdot; u<sub>p−1</sub>)] &sdot; u<sub>p−1</sub>

### Prove Gram-Schmit Procedure by means of Projection Matrix
Begin by projection matrix to prove Gram-Schmit Procedure illustrated in below pic:   
![Project y onto column space of x]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-10-31-prereq-qr-decomposition-projection-matrix.png "Project y onto column space of x")

>take x &sdot; b = y<sub>proj</sub>, the projection of y onto C(x), where C(x) is the column space spanned by vector x  
>C(x) &perp; (y − x &sdot; b), then    
>=>C(x) &sdot; (y − x &sdot; b) = 0,  
>=>x<sup>t</sup> &sdot; (y − x &sdot; b) = 0,  
>=>x<sup>t</sup> &sdot; x &sdot; b =  x<sup>t</sup> &sdot; y,  
>=>b = (x<sup>t</sup> &sdot; x)<sup>−</sup> &sdot; x<sup>t</sup> &sdot; y; where (x<sup>t</sup> &sdot; x)<sup>−</sup> is the generalized inverse form,       
>=>y<sub>proj</sub> = x &sdot; (x<sup>t</sup> &sdot; x)<sup>−</sup> &sdot; x<sup>t</sup> &sdot; y       
>∵x is itself a column vector, then (x<sup>t</sup> &sdot; x)<sup>−</sup> = (x<sup>t</sup> &sdot; x)<sup>−1</sup> just holds, for the vector x is in the spanning set/basis    
>&there4;y<sub>proj</sub> = [(x<sup>t</sup> &sdot; y) ∕ (x<sup>t</sup> &sdot; x)] &sdot; x = [(y<sup>t</sup> &sdot; x) ∕ (x<sup>t</sup> &sdot; x)] &sdot; x 

To further explain Gram-Schmit Procedure in terms of Projection Matrix:
>take y as v<sub>2</sub>, x as u<sub>1</sub>, where u<sub>1</sub> = v<sub>1</sub>, then      
>u<sub>2</sub> = v<sub>2</sub> − [((u<sub>1</sub>)<sup>t</sup> &sdot; v<sub>2</sub>) ∕ ((u<sub>1</sub>)<sup>t</sup> &sdot; u<sub>1</sub>)] &sdot; u<sub>1</sub>, where the second term is just the projection of v<sub>2</sub> onto u<sub>1</sub>  
>u<sub>3</sub> = v<sub>3</sub> − Proj<sub>w<sub>2</sub></sub>(v<sub>3</sub>), where w<sub>2</sub> = Span(u<sub>1</sub>, u<sub>2</sub>)   
>&#160;&#160;&#160;&#160;&#160;= v<sub>3</sub> − Proj<sub>u<sub>1</sub></sub>(v<sub>3</sub>) − Proj<sub>u<sub>2</sub></sub>(v<sub>3</sub>)      
>&#160;&#160;&#160;&#160;&#160;= v<sub>3</sub> − [((u<sub>1</sub>)<sup>t</sup> &sdot; v<sub>3</sub>) ∕ ((u<sub>1</sub>)<sup>t</sup> &sdot; u<sub>1</sub>)] &sdot; u<sub>1</sub> − [((u<sub>2</sub>)<sup>t</sup> &sdot; v<sub>3</sub>) ∕ ((u<sub>2</sub>)<sup>t</sup> &sdot; u<sub>2</sub>)] &sdot; u<sub>2</sub>    
>the flow is exhibited by below pic:    

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-10-31-prereq-qr-decomposition-multiple-projection.png "Gram-Schmit from multi-projection")

>u<sub>4</sub> = v<sub>4</sub> − Proj<sub>w<sub>3</sub></sub>(v<sub>4</sub>), where w<sub>3</sub> = Span(u<sub>1</sub>, u<sub>2</sub>, u<sub>3</sub>)  
>&#160;&#160;&#160;&#160;&#160;= v<sub>4</sub> − [((u<sub>1</sub>)<sup>t</sup> &sdot; v<sub>4</sub>) ∕ ((u<sub>1</sub>)<sup>t</sup> &sdot; u<sub>1</sub>)] &sdot; u<sub>1</sub> − [((u<sub>2</sub>)<sup>t</sup> &sdot; v<sub>4</sub>) ∕ ((u<sub>2</sub>)<sup>t</sup> &sdot; u<sub>2</sub>)] &sdot; u<sub>2</sub>  − [((u<sub>3</sub>)<sup>t</sup> &sdot; v<sub>4</sub>) ∕ ((u<sub>3</sub>)<sup>t</sup> &sdot; u<sub>3</sub>)] &sdot; u<sub>3</sub>  
>...  
>finally, we can reach      
>u<sub>p</sub> = v<sub>p</sub> − [((u<sub>1</sub>)<sup>t</sup> &sdot; v<sub>p</sub>) ∕ ((u<sub>1</sub>)<sup>t</sup> &sdot; u<sub>1</sub>)] &sdot; u<sub>1</sub> − [((u<sub>2</sub>)<sup>t</sup> &sdot; v<sub>p</sub>) ∕ ((u<sub>2</sub>)<sup>t</sup> &sdot; u<sub>2</sub>)] &sdot; u<sub>2</sub>  − ... −  [((u<sub>p−1</sub>)<sup>t</sup> &sdot; v<sub>p</sub>) ∕ ((u<sub>p−1</sub>)<sup>t</sup> &sdot; u<sub>p−1</sub>)] &sdot; u<sub>p−1</sub>

Further refine the notation in Gram-Schmit and Formula Representation:
>take S = {v<sub>1</sub>, v<sub>2</sub>,..., v<sub>p</sub>} to be S = {a<sub>1</sub>, a<sub>2</sub>,..., a<sub>p</sub>}  
>take T = {u<sub>1</sub>, u<sub>2</sub>,..., u<sub>p</sub>} to be T = {b<sub>1</sub>, b<sub>2</sub>,..., b<sub>p</sub>}  
>b<sub>1</sub> = a<sub>1</sub>  
>b<sub>2</sub> = a<sub>2</sub> − [((b<sub>1</sub>)<sup>t</sup> &sdot; a<sub>2</sub>) ∕ ((b<sub>1</sub>)<sup>t</sup> &sdot; b<sub>1</sub>)] &sdot; b<sub>1</sub>  
>b<sub>3</sub> = a<sub>3</sub> − [((b<sub>1</sub>)<sup>t</sup> &sdot; a<sub>3</sub>) ∕ ((b<sub>1</sub>)<sup>t</sup> &sdot; b<sub>1</sub>)] &sdot; b<sub>1</sub> − [((b<sub>2</sub>)<sup>t</sup> &sdot; a<sub>3</sub>) ∕ ((b<sub>2</sub>)<sup>t</sup> &sdot; b<sub>2</sub>)] &sdot; b<sub>2</sub>  
>b<sub>4</sub> = a<sub>4</sub> − [((b<sub>1</sub>)<sup>t</sup> &sdot; a<sub>4</sub>) ∕ ((b<sub>1</sub>)<sup>t</sup> &sdot; b<sub>1</sub>)] &sdot; b<sub>1</sub> − [((b<sub>2</sub>)<sup>t</sup> &sdot; a<sub>4</sub>) ∕ ((b<sub>2</sub>)<sup>t</sup> &sdot; b<sub>2</sub>)] &sdot; b<sub>2</sub> − [((b<sub>3</sub>)<sup>t</sup> &sdot; a<sub>4</sub>) ∕ ((b<sub>3</sub>)<sup>t</sup> &sdot; b<sub>3</sub>)] &sdot; b<sub>3</sub>  
>...  
>b<sub>p</sub> = a<sub>p</sub> − [((b<sub>1</sub>)<sup>t</sup> &sdot; a<sub>p</sub>) ∕ ((b<sub>1</sub>)<sup>t</sup> &sdot; b<sub>1</sub>)] &sdot; b<sub>1</sub> − [((b<sub>2</sub>)<sup>t</sup> &sdot; a<sub>p</sub>) ∕ ((b<sub>2</sub>)<sup>t</sup> &sdot; b<sub>2</sub>)] &sdot; b<sub>2</sub> − [((b<sub>3</sub>)<sup>t</sup> &sdot; a<sub>p</sub>) ∕ ((b<sub>3</sub>)<sup>t</sup> &sdot; b<sub>3</sub>)] &sdot; b<sub>3</sub> − ... − [((b<sub>p−1</sub>)<sup>t</sup> &sdot; a<sub>p</sub>) ∕ ((b<sub>p−1</sub>)<sup>t</sup> &sdot; b<sub>p−1</sub>)] &sdot; b<sub>p−1</sub>  
>At this moment, the proof has validated Gram-Schmit by the projection matrix

### Express Gram-Schmit Procedure in Matrix Product
Advance one step to represent Gram-Schmit Procedure by matrix product:
>if we take X<sub>i,j</sub> = ((b<sub>i</sub>)<sup>t</sup> &sdot; a<sub>j</sub>) ∕ ((b<sub>i</sub>)<sup>t</sup> &sdot; b<sub>i</sub>), then, we could have:  
>b<sub>1</sub> = a<sub>1</sub>  
>b<sub>2</sub> = a<sub>2</sub> − X<sub>1,2</sub> &sdot; b<sub>1</sub>  
>b<sub>3</sub> = a<sub>3</sub> − X<sub>1,3</sub> &sdot; b<sub>1</sub> − X<sub>2,3</sub> &sdot; b<sub>2</sub>  
>b<sub>4</sub> = a<sub>4</sub> − X<sub>1,4</sub> &sdot; b<sub>1</sub> − X<sub>2,4</sub> &sdot; b<sub>2</sub> − X<sub>3,4</sub> &sdot; b<sub>3</sub>  
>...  
>b<sub>p</sub> = a<sub>p</sub> − X<sub>1,p</sub> &sdot; b<sub>1</sub> − X<sub>2,p</sub> &sdot; b<sub>2</sub> − X<sub>3,p</sub> &sdot; b<sub>3</sub> − ... − X<sub>p−2,p</sub> &sdot; b<sub>p−2</sub> − X<sub>p−1,p</sub> &sdot; b<sub>p−1</sub>  

Then, express a<sub>i</sub> in terms of b<sub>i</sub>&prime;s:
>a<sub>1</sub> = b<sub>1</sub>  
>a<sub>2</sub> = b<sub>2</sub> + X<sub>1,2</sub> &sdot; b<sub>1</sub>  
>a<sub>3</sub> = b<sub>3</sub> + X<sub>1,3</sub> &sdot; b<sub>1</sub> + X<sub>2,3</sub> &sdot; b<sub>2</sub>  
>a<sub>4</sub> = b<sub>4</sub> + X<sub>1,4</sub> &sdot; b<sub>1</sub> + X<sub>2,4</sub> &sdot; b<sub>2</sub> + X<sub>3,4</sub> &sdot; b<sub>3</sub>  
>...  
>a<sub>p</sub> = b<sub>p</sub> + X<sub>1,p</sub> &sdot; b<sub>1</sub> + X<sub>2,p</sub> &sdot; b<sub>2</sub> + X<sub>3,p</sub> &sdot; b<sub>3</sub> + ... + X<sub>p−2,p</sub> &sdot; b<sub>p−2</sub> + X<sub>p−1,p</sub> &sdot; b<sub>p−1</sub>  

Further refine:
>take X<sub>i,i</sub> = 1, that is  
>a<sub>1</sub> = X<sub>1,1</sub> &sdot; b<sub>1</sub>  
>a<sub>2</sub> = X<sub>1,2</sub> &sdot; b<sub>1</sub> + X<sub>2,2</sub> &sdot; b<sub>2</sub>  
>a<sub>3</sub> = X<sub>1,3</sub> &sdot; b<sub>1</sub> + X<sub>2,3</sub> &sdot; b<sub>2</sub> + X<sub>3,3</sub> &sdot; b<sub>3</sub>  
>a<sub>4</sub> = X<sub>1,4</sub> &sdot; b<sub>1</sub> + X<sub>2,4</sub> &sdot; b<sub>2</sub> + X<sub>3,4</sub> &sdot; b<sub>3</sub> + X<sub>4,4</sub> &sdot; b<sub>4</sub>  
>...  
>a<sub>p</sub> = X<sub>1,p</sub> &sdot; b<sub>1</sub> + X<sub>2,p</sub> &sdot; b<sub>2</sub> + X<sub>3,p</sub> &sdot; b<sub>3</sub> + ... + X<sub>p−2,p</sub> &sdot; b<sub>p−2</sub> + X<sub>p−1,p</sub> &sdot; b<sub>p−1</sub> + X<sub>p,p</sub> &sdot; b<sub>p</sub>  

><div class="code_responsive"><pre class="programlisting">
take X as an upper unit triangular matrix where X<sub>i,i</sub> = 1 
X = 
X<sub>1,1</sub> X<sub>1,2</sub> X<sub>1,3</sub> X<sub>1,4</sub> .... X<sub>1,p</sub>  
 0    X<sub>2,2</sub> X<sub>2,3</sub> X<sub>2,4</sub> .... X<sub>2,p</sub>
 0     0   X<sub>3,3</sub> X<sub>3,4</sub> .... X<sub>3,p</sub>
 0     0    0   X<sub>4,4</sub> .... X<sub>4,p</sub>
   ..................
 0     0    0   0  ....   X<sub>p,p</sub></pre></div>
>then,  
>A<sub>m×p</sub> = [a<sub>1</sub>|a<sub>2</sub>|...|a<sub>p</sub>], where a<sub>i</sub> &isin; R<sup>m</sup>,  
>B<sub>m×p</sub> = [b<sub>1</sub>|b<sub>2</sub>|...|b<sub>p</sub>], where b<sub>i</sub> &isin; R<sup>m</sup>,    
>
>take D = diag(||b<sub>1</sub>||<sup>−1</sup>, ||b<sub>2</sub>||<sup>−1</sup>, ||b<sub>3</sub>||<sup>−1</sup>,...,||b<sub>p</sub>||<sup>−1</sup>)  
>take Q = B &sdot; D = diag(b<sub>1</sub> ∕ ||b<sub>1</sub>||, b<sub>2</sub> ∕ ||b<sub>2</sub>||, b<sub>3</sub> ∕  ||b<sub>3</sub>||,..., b<sub>p</sub> ∕ ||b<sub>p</sub>||)  
>take E = diag(||b<sub>1</sub>||, ||b<sub>2</sub>||, ||b<sub>3</sub>||,...,||b<sub>p</sub>||)...to eliminate D  
>take R = E &sdot; X = [(||b<sub>1</sub>|| &sdot; X<sub>1</sub>)|(||b<sub>2</sub>|| &sdot; X<sub>2</sub>)|(||b<sub>3</sub>|| &sdot; X<sub>3</sub>)|,...,|(||b<sub>p</sub>|| &sdot; X<sub>p</sub>)]...upper triangular matrix  
>then, A = B &sdot; X = B &sdot; D &sdot; E &sdot; X = Q &sdot; R ...QR decomposition, where such Q  &sdot; R is unique, ∵B &sdot; X is also unique, too.