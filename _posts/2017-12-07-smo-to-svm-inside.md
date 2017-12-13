---
layout: post
title: Inside Support Minimal Optimization
---

## Inside Sequential Minimal Optimization
<p class="message">
SMO(Sequential Minimal Optimization) is the regularization process by optimization in accordance to the rule that can minimize the cost error of the objective function sequentially. 
</p>

### Departure With Noise
>We'd like to begin from the imperfect separation, since no sampling is fully qualified and could be well separated.  Given the support vector formulated problem expressed in terms of $\alpha_i$, $y_i$, $x_i$; then the objective function:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$  
>for all i, $0<\alpha_i<C$  

### Works On 2 $\alpha$'s At A Time
>The algorithm of SMO works by <font color="OrangeRed">manipulating 2 $\alpha$'s at a time(with others fixed)</font>, a little <font color="OrangeRed">hill climbing</font> alike approach.  By <font color="OrangeRed">heuristics</font> to choose 2 $\alpha$'s at a time.  
>
>In the <font color="OrangeRed">begin</font> of the whole flow, <font color="DeepSkyBlue">initialize $\alpha_i=0$ for $i=1$ to $n$</font>.  Suppose we randomly choose $\alpha_1$, $\alpha_2$ and denote it as <font color="RoyalBlue">$\alpha_1^{old}$</font>, <font color="RoyalBlue">$\alpha_2^{old}$</font>.  
>Due to $\sum_{i=1}^n\alpha_i\cdot y_i=0$, therefore we have:  
>$y_1\cdot \alpha_1+y_2\cdot \alpha_2=y_1\cdot \alpha_1^{old}+y_2\cdot \alpha_2^{old}$  
>This confines the optimization of $\alpha_1$, $\alpha_2$ is on a line.  
>
>Next to examine the relation in between of these 2 $\alpha_1$, $\alpha_2$ of <font color="RoyalBlue">old</font> or <font color="Green">new</font>.  
>&#10112;for $y_1\neq y_2$, then, $\alpha_1-\alpha_2=r$, where $r$ is a constant.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-07-smo-to-svm-inside-alphas-on-line-1.png "2 alphas on a line")
>&#10113;for $y_1=y_2$, then, $\alpha_1+\alpha_2=r$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-07-smo-to-svm-inside-alphas-on-line-2.png "2 alphas on a line")
>Take $S=y_1\cdot y_2$, multiply $y_1\cdot \alpha_1+y_2\cdot \alpha_2=const$ by $y_1$, then,  
>$\alpha_1+S\cdot \alpha_2=const$, we have:  
>$\alpha_1=const-S\cdot \alpha_2$,  
>where $\alpha_1+S\cdot \alpha_2=\alpha_1^{old}+S\cdot \alpha_2^{old}$.  
>
>Next to optimize $\alpha_1$, $\alpha_2$ with <font color="OrangeRed">other $\alpha$'s fixed</font>, the objective function could be rewritten as:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\alpha_1+\alpha_2+const\\-\frac12\cdot(part\;1+par\;2)\end{array}$$  
>  
>&#10112;we further express $part\;1$:  
$$\begin{array}{l}part\;1\\=\sum_{i,j=1,2}\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\\=\alpha_1^2\cdot y_1^2\cdot x_1^t\cdot x_1\\\;\;+\alpha_2^2\cdot y_2^2\cdot x_2^t\cdot x_2\\\;\;+2\cdot\alpha_1\cdot\alpha_2\cdot y_1\cdot y_2\cdot x_1^t\cdot x_2\end{array}$$  
>
>&#10113;we express $part\;2$ as:  
$$\begin{array}{l}part\;2\\=\sum_{i=3;j=1,2}^{j=n}\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\\\;\;+\sum_{i=1,2;j=3}^{j=n}\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\\=2\cdot(\sum_{i=3}^n\alpha_i\cdot y_i\cdot x_i^t)\cdot(\alpha_1\cdot y_1\cdot x_1+\alpha_2\cdot y_2\cdot x_2)\end{array}$$  

### Express $\alpha_1$ In Terms Of $\alpha_2$
>Next to express $\alpha_1$ in terms of $\alpha_2$, this is a quiet painful and confused process, it took me some while, now I'd like to share you with my viewpoint in each step in the deduction.  
>
>From current objective function, some symptoms could be found that $x_i$ is associasted with $x_j$.  
>Thus, we take $K_{11}=x_1^t\cdot x_1$, $K_{22}=x_2^t\cdot x_2$, $K_{12}=x_1^t\cdot x_2$.  
>
>Recall that it is deduced out by removing the <font color="RoyalBlue">old</font> $\alpha_1$, $\alpha_2$ associated terms from the term $w$, here comes the question, can we relate the <font color="RoyalBlue">old</font> $w$ to the <font color="Green">new evolved</font> $\alpha_1$, $\alpha_2$?  
$$\begin{array}{l}V_j=\sum_{i=3}^n\alpha_i\cdot y_i\cdot x_i^t\cdot x_j\\=(w^{old})^t\cdot x_j-\alpha_1^{old}\cdot y_1\cdot x_1^t\cdot x_j\\\;\;\;\;-\alpha_2^{old}\cdot y_2\cdot x_2^t\cdot x_j\\=(w^{old})^t\cdot x_j-b^{old}+b^{old}\\\;\;\;\;-\alpha_1^{old}\cdot y_1\cdot x_1^t\cdot x_j\\\;\;\;\;-\alpha_2^{old}\cdot y_2\cdot x_2^t\cdot x_j\\=U_j+b^{old}\\\;\;\;\;-\alpha_1^{old}\cdot y_1\cdot x_1^t\cdot x_j\\\;\;\;\;-\alpha_2^{old}\cdot y_2\cdot x_2^t\cdot x_j\end{array}$$  
>
>where $U_j=(w^{old})^t\cdot x_j-b^{old}$ is the output of $x_j$ under the old parameters, $w^{old}$, $b^{old}$.  Expression in this way with a hope to refine original objective function.  
>
>In order to make it the point, the subscript of the term indicates the index, usually in this proof, they are $i$,$j$ or $1$,$2$..., the superscript is ued for the identity of <font color="RoyalBlue">old</font> or <font color="Green">new clipped</font> term.  
>
>For the simplicity of the deduction and understanding, if no any word like <font color="RoyalBlue">old</font>, <font color="Green">new</font> in the superscript, then, the term is treated as <font color="Green">new</font> term.  Why by default is the term of new version?  Because the nature design in SMO algorithm works by clipping 2 <font color="Green">new</font> terms of $\alpha$'s at a time, the objective function would then be refined as the expression of 2 <font color="Green">new</font> terms of $\alpha$'s.  
>
>&#10112;deduce by replacing above terms in the objective function:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)=\alpha_1+\alpha_2+const-\frac12\cdot(\\\;\;\;\;K_{11}\cdot\alpha_1^2+K_{22}\cdot\alpha_2^2+2\cdot S\cdot K_{12}\cdot\alpha_1\cdot\alpha_2+\\\;\;\;\;2\cdot\alpha_1\cdot y_1\cdot V_1+2\cdot\alpha_2\cdot y_2\cdot V_2)\end{array}$$  
>&#10113;next to replace $\alpha_1$ with $\alpha_2$, more precisely, replace the <font color="Green">new</font> $\alpha_1$ with the <font color="Green">new</font> $\alpha_2$:  
$$\begin{array}{l}=(r-S\cdot\alpha_2)+\alpha_2+const\\\;\;\;\;-\frac12\cdot(K_{11}\cdot(r-S\cdot\alpha_2)^2+K_{22}\cdot\alpha_2^2+\\\;\;\;\;2\cdot S\cdot K_{12}\cdot(r-S\cdot\alpha_2)\cdot\alpha_2+\\\;\;\;\;2\cdot y_1\cdot V_1\cdot(r-S\cdot\alpha_2)+2\cdot\alpha_2\cdot y_2\cdot V_2)\end{array}$$  
>&#10114;<font color="DeepSkyBlue">toss out the $r$ in the term $(r-S\cdot\alpha_2)$</font>(or we just put it in the term $const$), since <font color="DeepSkyBlue">it is just a constant and no association with it</font>, as to the $r$ associated in the remaining terms, it should be retained.  
$$\begin{array}{l}=(1-S)\cdot\alpha_2+const\\\;\;\;\;-\frac12\cdot(K_{11}\cdot(r-S\cdot\alpha_2)^2+K_{22}\cdot\alpha_2^2+\\\;\;\;\;2\cdot S\cdot K_{12}\cdot(r-S\cdot\alpha_2)\cdot\alpha_2+\\\;\;\;\;2\cdot y_1\cdot V_1\cdot(r-S\cdot\alpha_2)+2\cdot\alpha_2\cdot y_2\cdot V_2)\end{array}$$  
>&#10115;expand in terms of $\alpha_2$:  
$$\begin{array}{l}=(1-S)\cdot\alpha_2+const\\\;\;\;\;-\frac12\cdot K_{11}\cdot r^2+K_{11}\cdot r\cdot S\cdot\alpha_2-\frac12\cdot K_{11}\cdot S^2\cdot\alpha_2^2\\\;\;\;\;-\frac12\cdot K_{22}\cdot\alpha_2^2\\\;\;\;\;-S\cdot K_{12}\cdot r\cdot\alpha_2+S^2\cdot K_{12}\cdot\alpha_2^2\\\;\;\;\;-y_1\cdot V_1\cdot r+y_1\cdot V_1\cdot S\cdot\alpha_2-y_2\cdot V_2\cdot\alpha_2\end{array}$$  
>&#10116;since we'd like to express $\alpha_1$ in terms of $\alpha_2$ in the new evolved objective function, it might be a good idea to <font color="DeepSkyBlue">put the $r$ non-associated with $\alpha_2$ into the $const$ term</font>, where $S^2=1$ and the $-\frac12\cdot K_{11}\cdot r^2$, $-y_1\cdot V_1\cdot r$ should be tossed out:  
$$\begin{array}{l}=(1-S)\cdot\alpha_2+const\\\;\;\;\;+K_{11}\cdot r\cdot S\cdot\alpha_2-\frac12\cdot K_{11}\cdot S^2\cdot\alpha_2^2\\\;\;\;\;-\frac12\cdot K_{22}\cdot\alpha_2^2\\\;\;\;\;-S\cdot K_{12}\cdot r\cdot\alpha_2+S^2\cdot K_{12}\cdot\alpha_2^2\\\;\;\;\;+y_1\cdot V_1\cdot S\cdot\alpha_2-y_2\cdot V_2\cdot\alpha_2\end{array}$$  
>&#10117;it seems that the objective function has been well refined with only $\alpha_2$ in it, but, take a look at the term $y_1\cdot V_1\cdot S\cdot\alpha_2$, it consists of $y_1$ and $\alpha_2$, whereas, $y_1$ is the signal of $\alpha_1$, and $\alpha_2$ should be associated with $y_2$, here comes the tricky factor $S=y_1\cdot y_2$:  
$$\begin{array}{l}y_1\cdot V_1\cdot S\cdot\alpha_2\\=y_1\cdot V_1\cdot y_1\cdot y_2\cdot\alpha_2\\=V_1\cdot y_2\cdot\alpha_2\end{array}$$  
>where $y_1^2=1$, thus, the regularized objective function in this paragraph would be:  
$$\begin{array}{l}=(1-S)\cdot\alpha_2+const\\\;\;\;\;+K_{11}\cdot r\cdot S\cdot\alpha_2-\frac12\cdot K_{11}\cdot S^2\cdot\alpha_2^2\\\;\;\;\;-\frac12\cdot K_{22}\cdot\alpha_2^2\\\;\;\;\;-S\cdot K_{12}\cdot r\cdot\alpha_2+S^2\cdot K_{12}\cdot\alpha_2^2\\\;\;\;\;+y_2\cdot V_1\cdot\alpha_2-y_2\cdot V_2\cdot\alpha_2\end{array}$$  
>&#10118;now, we save with only the <font color="Green">$\alpha_2^{new}$</font> and <font color="Green">$(\alpha_2^{new})^2$</font> are left:  
$$\begin{array}{l}=\frac12\cdot(2K_{12}-K_{11}-K_{22})\cdot(\alpha_2^{new})^2\\\;\;\;\;+(1-S+S\cdot K_{11}\cdot r-S\cdot K_{12}\cdot r\\\;\;\;\;+y_2\cdot V_1-y_2\cdot V_2)\cdot\alpha_2^{new}\end{array}$$  

### Relate <font color="Green">$\alpha_2^{new}$</font> Back To <font color="RoyalBlue">$\alpha_2^{old}$</font>
>The major spirit of SMO is to optimize 2 $\alpha$'s at a time, by transiting from the <font color="RoyalBlue">old</font> $\alpha$'s to the <font color="Green">new</font> $\alpha$'s, more precisely, from $\alpha_1^{old}$ to $\alpha_1^{new}$, and from $\alpha_2^{old}$ to $\alpha_2^{new}$.  Now, we focus on $\alpha_2^{new}$, and laterly, by the relationship in between these 2 $\alpha$'s:  
>&#10112;$\alpha_1+\alpha_2=r$  
>&#10113;$\alpha_1-\alpha_2=r$  
>above equality holds for both the <font color="RoyalBlue">old</font> $\alpha$'s to the <font color="Green">new</font> $\alpha$'s, we can get the $\alpha_1^{new}$ after we get $\alpha_2^{new}$.  
>
>To link <font color="Green">$\alpha_2^{new}$</font> back to <font color="RoyalBlue">$\alpha_2^{old}$</font> ,we start below procedure.  
>&#10112;now, we focus on the <font color="OrangeRed">coefficient</font> of <font color="Green">$\alpha_2^{new}$</font>, expand from $r$ and $V_1$ and $V_2$:  
$$\begin{array}{l}1-S+S\cdot K_{11}\cdot r-S\cdot K_{12}\cdot r+y_2\cdot V_1-y_2\cdot V_2\\=1-S+S\cdot K_{11}\cdot(\alpha_1^{old}+S\cdot\alpha_2^{old})\\\;\;\;\;-S\cdot K_{12}\cdot(\alpha_1^{old}+S\cdot\alpha_2^{old})\\\;\;\;\;+y_2\cdot(U_1^{old}+b^{old}-\alpha_1^{old}\cdot y_1\cdot K_{11}-\alpha_2^{old}\cdot y_2\cdot K_{12})\\\;\;\;\;-y_2\cdot(U_2^{old}+b^{old}-\alpha_1^{old}\cdot y_1\cdot K_{12}-\alpha_2^{old}\cdot y_2\cdot K_{22})\end{array}$$  
>&#10113;further expand:  
$$\begin{array}{l}=1-S+S\cdot K_{11}\cdot\alpha_1^{old}+S\cdot K_{11}\cdot S\cdot\alpha_2^{old}\\\;\;\;\;-S\cdot K_{12}\cdot\alpha_1^{old}-S\cdot K_{12}\cdot S\cdot\alpha_2^{old}\\\;\;\;\;+y_2\cdot U_1^{old}+y_2\cdot b^{old}-y_2\cdot\alpha_1^{old}\cdot y_1\cdot K_{11}-y_2\cdot\alpha_2^{old}\cdot y_2\cdot K_{12}\\\;\;\;\;-y_2\cdot U_2^{old}-y_2\cdot b^{old}+y_2\cdot\alpha_1^{old}\cdot y_1\cdot K_{12}+y_2\cdot\alpha_2^{old}\cdot y_2\cdot K_{22}\end{array}$$  
>&#10114;eliminate these terms $S\cdot K_{11}\cdot \alpha_1^{old}$, $S\cdot K_{12}\cdot \alpha_1^{old}$ and $y_2\cdot b^{old}$:
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-07-smo-to-svm-inside-eliminate-1.png "eliminate")
>&#10115;we obtain below equality:  
$$\begin{array}{l}=1-S+(K_{11}-2\cdot K_{12}+K_{22})\cdot\alpha_2^{old}\\\;\;\;\;+y_2\cdot(U_1^{old}-U_2^{old})\end{array}$$  
>, where $U_j^{old}=(w^{old})^t\cdot x_j-b^{old}$.  
>&#10116;enrich the equation with terms that is related to $\alpha_2$ might be helpful:  
$$\begin{array}{l}=(y_2)^2-y_1\cdot y_2+(K_{11}-2\cdot K_{12}+K_{22})\cdot\alpha_2^{old}\\\;\;\;\;+y_2\cdot(U_1^{old}-U_2^{old})\end{array}$$  
>, where $(y_2)^2=1$ and $y_1\cdot y_2=S$.  

### Introduction Of $\eta$
>Take a look at above &#10116;, there exists a term $(K_{11}-2\cdot K_{12}+K_{22})$ quiet similar with the term $(2K_{12}-K_{11}-K_{22})$, which is the coefficient of the term <font color="Green">$(\alpha_2^{new})^2$</font>.  
>
>Next is to further refine the objective funection by introducing $\eta$.  
>
>Take $\eta=2K_{12}-K_{11}-K_{22}$, then, the above &#10116; becomes:  
$$\begin{array}{l}=(y_2)^2-y_1\cdot y_2-\eta\cdot\alpha_2^{old}\\\;\;\;\;+y_2\cdot(U_1^{old}-U_2^{old})\end{array}$$
$$=y_2\cdot(y_2-y_1+U_1^{old}-U_2^{old})-\eta\cdot\alpha_2^{old}$$  
$$=y_2\cdot(U_1^{old}-y_1-(U_2^{old}-y_2))-\eta\cdot\alpha_2^{old}$$  
$$=y_2\cdot(E_1^{old}-E_2^{old})-\eta\cdot\alpha_2^{old}$$  
>where $E_1^{old}=Err_{(x_1,y_1)}^{old}=(w^{old})^t\cdot x_1-b^{old}-y_1$,  
>and $E_2^{old}=Err_{(x_2,y_2)}^{old}=(w^{old})^t\cdot x_2-b^{old}-y_2$.  
>They are just the error caused by the $w^{old}$, when <font color="RoyalBlue">$\alpha_1^{old}$</font> and <font color="RoyalBlue">$\alpha_2^{old}$</font> in it.  
>
>Now, we formularize our problem in objective function of $\eta$, <font color="Green">$\alpha_2^{new}$</font>, <font color="RoyalBlue">$\alpha_2^{old}$</font>, $E_1^{old}$, $E_2^{old}$:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=L(\alpha_2^{new})\\=\frac12\cdot\eta\cdot(\alpha_2^{new})^2\\\;\;\;\;+(y_2\cdot(E_1^{old}-E_2^{old})-\eta\cdot\alpha_2^{old})\cdot\alpha_2^{new}\\\;\;\;\;+const\end{array}$$  
>
><font color="DeepPink">Transform from $L(w,b,\xi,\alpha,\mu)$ to $L(\alpha_2^{new})$ is much simpler in its optimization</font>, since, <font color="DeepPink">only $\alpha_2^{new}$ is left to be optimized</font>, the regularization cost of computation is greatly reduced!!!
>
>Now we come to the <font color="OrangeRed">validity of $\eta$</font>, to get the most optimal vale of <font color="Green">$\alpha_2^{new}$</font>:  
>&#10112;$\frac{\partial L}{\partial\alpha_2^{new}}=\eta\cdot\alpha_2^{new}+y_2\cdot(E_1^{old}-E_2^{old})-\eta\cdot\alpha_2^{old}=0$  
>&#10113;$\frac{\partial L}{\partial{(\alpha_2^{new})^2}}=\frac12\cdot\eta$, where we have $\eta=2K_{12}-K_{11}-K_{22}$.  
>
>By &#10112;, this coincides with our departure point in the section relate <font color="Green">$\alpha_2^{new}$</font> back to <font color="RoyalBlue">$\alpha_2^{old}$</font>, we just make the point.  We have:  
$$\alpha_2^{new}=\alpha_2^{old}-\frac{y_2\cdot(E_1^{old}-E_2^{old})}\eta$$  
>Further refine, we can have:  
$$\alpha_2^{new}=\alpha_2^{old}+\frac{y_2\cdot(E_2^{old}-E_1^{old})}\eta$$  
>
><font color="DeepPink">$\eta\leq0$ is the validity of $\eta$</font> and must hold:  
$$\begin{array}{l}\eta=2\cdot K_{12}-K_{11}-K_{22}\\\;\;\;=-\left\|x_1-x_2\right\|^2\leq0\end{array}$$  
><font color="OrangeRed">For computation, $\eta$ should be less than $0$</font>, although it might be approaching to $0$.

### Feasible Rangle Of New $\alpha$ Value
>Suppose we are working under $\eta<0$ in this equality, and it is correct:  
$$\alpha_2^{new}=\alpha_2^{old}+\frac{y_2\cdot(E_2^{old}-E_1^{old})}\eta$$  
>Then, the <font color="Green">$\alpha_2^{new}$</font> thus obtained might be <font color="OrangeRed">unconstrainted</font> maximum value.  <font color="OrangeRed">The feasible range of $\alpha_2^{new}$ must be checked</font>.  
>
>We'd like to examine 4 cases, begin from below 3 equality:  
>&#10112;$S=y_1\cdot y_2$.  
>&#10113;$\alpha_1^{old}+S\cdot \alpha_2^{old}=r=\alpha_1^{new}+S\cdot \alpha_2^{new}$.  
>&#10114;$0\leq\alpha_i\leq C$, this should be inequality.  
>
>[Case 1]$S=1$, $\alpha_1+\alpha_2=r$, $r>C$, then, max($\alpha_2$)=$C$, min($\alpha_2$)=$r-C$  
>[Case 2]$S=1$, $\alpha_1+\alpha_2=r$, $r<C$, then, max($\alpha_2$)=$r$, min($\alpha_2$)=$0$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-07-smo-to-svm-inside-feasible-alpha-case-1-2.png "feasible range")
>Where the case 1 and case 2 are found to have $y_1=y_2$, we'd like to get the low threshold by max($0$, $r-c$), denote it as L; the hight threshold by min($r$, $C$), denote it as H.  
>[Case 3]$S=-1$, $\alpha_1-\alpha_2=r$, $r>0$, then, max($\alpha_2$)=$C-r$, min($\alpha_2$)=$0$  
>[Case 4]$S=-1$, $\alpha_1-\alpha_2=r$, $r<0$, then, max($\alpha_2$)=$C$, min($\alpha_2$)=$-r$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-07-smo-to-svm-inside-feasible-alpha-case-3-4.png "feasible range")
>Where the case 3 and case 4 are found to have $y_1\neq y_2$, we'd like to get the low threshold by max($0$, $-r$), denote it as L; the hight threshold by min($C$, $C+r$), denote it as H.  
>
>Take the <font color="OrangeRed">minimum</font> feasible of <font color="Green">$\alpha_2^{new}$</font> be <font color="OrangeRed">L</font>, the <font color="OrangeRed">maximum</font> feasible of <font color="Green">$\alpha_2^{new}$</font> be <font color="OrangeRed">H</font>, then:  
$$\alpha_2^{new,clipped}=\left\{\begin{array}{l}L,if\;\alpha_2^{new}<L\\\alpha_2^{new},if\;L<\alpha_2^{new}<H\\H,if\;\alpha_2^{new}>H\end{array}\right.$$  

### Clip New $\alpha$
>Succeeding to above section, in this paragraph, I'd like to summarize the process to clip <font color="Green">$\alpha_2^{new}$</font>, then, <font color="Green">$\alpha_1^{new}$</font>.  
>
>Begin by given $y_1$, $y_2$, $K_{11}$, $K_{22}$, $K_{12}$, $E_1^{old}$, $E_2^{old}$, where $E_i^{old}=w^{old}\cdot x_i-b^{old}-y_i$.  
>&#10112;take $\eta=2\cdot K_{12}-K_{11}-K_{22}$, then $\eta\leq 0$ <font color="OrangeRed">must hold</font>.  
>
>&#10113;if $\eta<0$, by prior induction, we have:  
$$\alpha_2^{new}=\alpha_2^{old}+\frac{y_2\cdot(E_2^{old}-E_1^{old})}\eta$$  
>Take $\triangle\alpha_2=\frac{y_2\cdot(E_2^{old}-E_1^{old})}\eta$  
>Please recall that <font color="DeepPink">$\alpha_1=r-S\cdot \alpha_2$, it holds for both new and old</font>.  Therefore,  
$$\lim_{\triangle\rightarrow0}\frac{(\alpha_1+\triangle)-\triangle}\triangle=\lim_{\triangle\rightarrow0}\frac{r-S\cdot(\alpha_2+\triangle)-(r-S\cdot\alpha_2)}\triangle$$  
$$\Rightarrow\triangle\alpha_1=-S\cdot\lim_{\triangle\rightarrow0}\frac{(\alpha_2+\triangle)-\alpha_2}\triangle$$  
$$\Rightarrow\triangle\alpha_1=-S\cdot\triangle\alpha_2$$  
>, where $\triangle\alpha_1$, $\triangle\alpha_2$ are the differentials or derivatives of $\alpha_1$, $\alpha_2$.  
>
>&#10114;if <font color="OrangeRed">$\eta=0$</font>, most SMO dosument, just commends to evaluate the objective function at the 2 end points and set $\alpha_2^{new}$ to the one that can make the <font color="OrangeRed">larger</font> objective function, thus, <font color="DeepPink">$\alpha_2^{new}$ would be more closed to boundary</font>!!!  
>
>Recap the objective function is now:  
$$\begin{array}{l}L(\alpha_2^{new})\\=\frac12\cdot\eta\cdot(\alpha_2^{new})^2\\\;\;\;\;+(y_2\cdot(E_1^{old}-E_2^{old})-\eta\cdot\alpha_2^{old})\cdot\alpha_2^{new}\\\;\;\;\;+const\end{array}$$  
>
>Where mjtsai think, <font color="DeepSkyBlue">for $\eta=0$, alternative would be to abandom and switch to next set of 2 points</font>, since the current evaluated 2 points might just be the <font color="OrangeRed">duplicated</font> or the <font color="OrangeRed">overlapped</font> cases(Coursera, M.L professor ANG's SMO sample code does this).  
>
>As to the <font color="OrangeRed">mirrored</font> case, should <font color="DeepSkyBlue">keep them in the mutual exclusive list for later manipulation, once new iteration would like to choose the new 2 candidates, already paired 2 points should not be paired again</font>, also by mjtsai.  

### SMO Updating
>We now have the concept that $\alpha_1^{new}$, $\alpha_2^{new}$ are updated by $\triangle\alpha_1$, $\triangle\alpha_2$, this section would like to guide you to update $E_i$, $F_i$, $w$ and $b$.  
>
>[Updating $b$]  
>Take $E(x,y)=\sum_{i=1}^n\alpha_i\cdot y_i\cdot\ x_i^t\cdot x-y-b$ to be the predict error:  
>$\triangle E(x,y)=\triangle\alpha_1\cdot y_1\cdot x_1^t\cdot x+\triangle\alpha_2\cdot y_2\cdot x_2^t\cdot x-\triangle b$ just holds to be the change in $E$.  
>
>If <font color="DeepPink">$0<\alpha_1^{new}<C$, then, we can treat the new value of $E_1$ be zero, that is $E_1^{new}=0$</font>, since it is <font color="OrangeRed">not the boundary case</font>.  Recall in the <font color="Red">KKT case 2</font>, it is <font color="OrangeRed">not at boundary</font>, we have $R_i=y_i\cdot E_i=0$.  Thus, we can reinforce the new value of $E$ to be $0$.  
>
>$E(x,y)$  
>$=E(x,y)^{old}+\triangle E(x,y)$  
>$=E(x,y)^{old}+\triangle\alpha_1\cdot y_1\cdot x_1^t\cdot x+\triangle\alpha_2\cdot y_2\cdot x_2^t\cdot x-\triangle b$    
>$=0$  
>
>Then, we have $\triangle b$ in below expression:  
$$\triangle b=E(x,y)^{old}+\triangle\alpha_1\cdot y_1\cdot x_1^t\cdot x+\triangle\alpha_2\cdot y_2\cdot x_2^t\cdot x$$    
>
>Take $\triangle b=b^{new}-b^{old}$, then:  
$$b^{new}=E(x,y)^{old}+\triangle\alpha_1\cdot y_1\cdot x_1^t\cdot x+\triangle\alpha_2\cdot y_2\cdot x_2^t\cdot x+b^{old}$$  
>
>We can further deduce out that:  
$$b_1^{new}=E(x_1,y_1)^{old}+\triangle\alpha_1\cdot y_1\cdot x_1^t\cdot x_1+\triangle\alpha_2\cdot y_2\cdot x_2^t\cdot x_1+b^{old}$$  
$$b_2^{new}=E(x_2,y_2)^{old}+\triangle\alpha_1\cdot y_1\cdot x_1^t\cdot x_2+\triangle\alpha_2\cdot y_2\cdot x_2^t\cdot x_2+b^{old}$$  
>
>where  
$$\triangle b_1=b_1^{new}-b^{old}$$  
$$\triangle b_2=b_2^{new}-b^{old}$$  
>&#10112;when <font color="Green">$\alpha_1^{new}$</font> (and, or, <font color="Green">$\alpha_2^{new}$</font>) is <font color="OrangeRed">not</font> at <font color="OrangeRed">boundary</font>, $0<\alpha_1^{new},\alpha_2^{new}<C$, by above deduction, we have $E(x_i,y_i)^{new}=0$, for $i=1,2$, that is to say:  
$$R_i=y_i\cdot E_i^{new}=y_i\cdot ((w^{new})^t\cdot x_i-b-y_i)\approx0$$  
>it holds for $y_i=\pm$, therefore, there should be no change in $b$, we can treat $\triangle b=0$.  
>$\triangle b=0$  
>$\;\;\;\;=b_1^{new}-b_1^{old}$  
>$\;\;\;\;=b_2^{new}-b_2^{old}$, further proof of this:  
>let $b_1^{new}$, $b_2^{new}$ the bias term after iteration  
>$(w^{new})^t\cdot x_1-b_1^{new}\approx0$  
>$(w^{new})^t\cdot x_2-b_2^{new}\approx0$, where <font color="DeepPink">non-boundary case guarantees</font>:  
><font color="DeepPink">$\left|(w^{new})^t\cdot x_i-y_i\right|\leq\varepsilon$</font>, for $i=1,2$, and $\varepsilon$ is a rather tiny quantity.  
>therefore, $\varepsilon-b_1^{new}\approx\varepsilon-b_2^{new}$  
>hence, we have <font color="DeepPink">$b_1^{new}\approx b_2^{new}$</font> as the result.  
>
>&#10113;when <font color="Green">$\alpha_1^{new}$</font>, <font color="Green">$\alpha_2^{new}$</font> are all at different boundary, one at $0$, one at $C$, where $L\neq H$, then, the interval in between $b_1^{new}$ and $b_2^{new}$ are all constrained by the KKT case 1 and 3, respectively.  
>
>Be recalled that <font color="Red">KKT case 1</font> has it that <font color="Red">$\alpha_i=0$, $R_i\geq0$</font>; and <font color="Red">KKT case 3</font> has it that <font color="Red">$\alpha_i=C$, $R_i\leq0$</font>, the <font color="Red">intersection with KKT case 2</font> is the equality of $0$, <font color="Red">$R_i\approx0$</font>, to reinforce these 2 points entering into the support vector, we can just come out with $E(x,y)^{new}=0$.  Therefore, we take $b^{new}=\frac{b_1^{new}+b_2^{new}}{2}$, such that the next $b^{new}$ would be stable in this way, the very next time, for current evaluated or other points to be iterated over, it would be much easier to move toward the boundary than current.  
>
>On our way to update $b$, in the meanwhile, we update $E_i$.  
>
>[Updating $F_i$]  
>We have it that:  
>$F(x,y)$  
>$=w^t\cdot x-y$  
>$=\sum_{i=1}^{n}\alpha_i\cdot y_i\cdot x_i^t\cdot x-y$  
>
>Trivially, we also have it that:  
>$\triangle F(x,y)$  
>$=\triangle\alpha_1\cdot y_1\cdot x_1^t\cdot x+\triangle\alpha_2\cdot y_2\cdot x_2^t\cdot x$    
>
>[Updating $w$]  
>Under the assumption that we are using linear kernel,  
>begin from $w=\sum_{i=1}^{n}\alpha_i\cdot y_i\cdot x_i$,  
>we can have it that:  
$\triangle w=\triangle\alpha_1\cdot y_1\cdot x_1+\triangle\alpha_2\cdot y_2\cdot x_2$  

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha</font> -->
<!-- <font color="Green">new alpha</font> -->

<!-- <font color="DeepPink">positive conclusion, finding</font> -->
<!-- <font color="DimGray">negative conclusion, finding</font> -->

<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->

<!-- http://web.cs.iastate.edu/~honavar/smo-svm.pdf -->
<!-- http://cs229.stanford.edu/notes/cs229-notes3.pdf -->
<!-- https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-14.pdf -->

<!-- https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/ -->
<!-- https://machinelearningmastery.com/support-vector-machines-for-machine-learning/ -->