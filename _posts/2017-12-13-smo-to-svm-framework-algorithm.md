---
layout: post
title: SMO Framework And Algorithm
---

## SMO Framework And Algorithm
<p class="message"> 
SMO algorithm is the realization of updating mandatory coefficients in the objective function based on the long and tedious deduction with a hope to regularize 
by optimization in accordance to the KKT rules that can sequentially costruct the boundarys of the safeguard. 
</p>

### SMO Framework
>Let me make a brief summary of the major points from the initial idea to the end of the deduction of the objective function.  
>
>[1]Suppose we'd like to have a hyperplane with a safeguard that can classify the given data sample.  
>&#10112;we formulate our problem as:  
>$\underset w{min}\frac12w^t\cdot w$, subject to $y_i\cdot(w^t\cdot x_i-b)\geq1,\forall i$.  
>The first part is the <font color="green">target</font>, the second part is the <font color="red">constraint</font>.  
>&#10113;then, introduce $\alpha_1,\alpha_2,\dots\alpha_n$ to be the lagrange multiplier and express in below lagrangian to be our <font color="deepink">objective function</font>:  
$$L(w,b,\alpha)=\frac12w^t\cdot w-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)-1)$$  
>&#10114;next to regularize the objective function, to get the optimal $\alpha$, we should take partial derivatives of $L$ on $w$, $b$ respectively and equate them to zero.  Finally, we get:  
$$\begin{array}{l}L(w,b,\alpha)\\=-\frac12\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot(x_i^t\cdot x_j)\\+\sum_{i=1}^n\alpha_i\end{array}$$  
>where $w=\sum_{i=1}^n\alpha_i\cdot y_i\cdot x_i$.  
>
>By such design guarantees that we could have <font color="green">$\forall\alpha_i>0$</font>, one basic condition must be satisfied in SMO.  

>[2]Next to the imperfect separation with <font color="OrangeRed">noise</font>.  There exists some condition that we don't strictly enforce that <font color="OrangeRed">no</font> data points in between $H_1$ and $H_2$.  We can extend SVM to allow some <font color="OrangeRed">noise</font>(data points) in between the safeguard zone.  Thus, we want to <font color="OrangeRed">penalize</font> the data points that cross the boundaries($H_1$,$H_2$).  
>&#10112;we formulate our problem as:  
>$\underset{w,\xi_i}{min}\left[w^t\cdot w+C\cdot\sum_{i=1}^n\xi_i\right]$,  
><font color="OrangeRed">subject to</font> $y_i\cdot(w^t\cdot x_i-b)+\xi_i-1\geq0$, $\forall\xi_i\geq0$  
>Such design is to <font color="OrangeRed">shrink down</font> the distance between $H_1$ and $H_2$, thus <font color="DeepSkyBlue">to allow some noise within original margin</font>.  
>&#10113;next to build the lagrangian by introducing $\alpha_1$, $\alpha_2$,..., $\alpha_n$ and $\mu_1$, $\mu_2$,..., $\mu_n$, then:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+C\cdot\sum_{i=1}^n\xi_i\\\;\;\;\;-\sum_{i=1}^n\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)+\xi_i-1)\\\;\;\;\;-\sum_{i=1}^n\mu_i\cdot\xi_i\end{array}$$  
>The lagrangian expression turns out to be:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot w^t\cdot w+\sum_{i=1}^n(C-\alpha_i-\mu_i)\xi_i\\\;\;\;\;-\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i^t)\cdot w\\\;\;\;\;+\sum_{i=1}^n\alpha_i\cdot y_i\cdot b\\\;\;\;\;+\sum_{i=1}^n\alpha_i\end{array}$$  
>&#10114;to get the maximum of $L$ at $\alpha$ and $\xi$, below constraints must be satisfied for all $i$:  
>$\frac{\partial L}{\partial w}=0$, $\frac{\partial L}{\partial b}=0$, $\frac{\partial L}{\partial \xi}=0$.  
>We have $w=\sum_{i=1}^n(\alpha_i\cdot y_i\cdot x_i)$, $\sum_{i=1}^n\alpha_i\cdot y_i=0$,  
>and $\sum_{i=1}^nC-\alpha_i-\mu_i=0$, for all $i$, $C-\alpha_i-\mu_i=0$ just holds.  
>&#10115;to maximize $L(w,b,\xi,\alpha,\mu)$ for the <font color="DeepSkyBlue">optimal $\alpha_i$ value</font>, then, we formulate the lagrangian as:  
$$\begin{array}{l}\underset\alpha{min}L(w,b,\xi,\alpha,\mu)\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$  
>, subject to $\sum_{i=1}^n\alpha_i\cdot y_i=0$ and <font color="OrangeRed">$0\leq\alpha_i\leq C$</font> for all $i$  
>&#10116;Notes that $\alpha_i\geq0$, $\mu_i\geq0$, therefore, we have <font color="OrangeRed">$0\leq\alpha_i\leq C$</font>,  
>$\alpha_i$ is now <font color="OrangeRed">upper bounded</font> by <font color="OrangeRed">$C$</font>.  

>[3]Then, we make introduction to the <font color="Red">KKT</font> conditions:  
>&#10112;$\alpha_i=0$, $R_i\geq0$  
>&#10113;$0<\alpha_i<C$, $R_i\approx0$  
>&#10114;$\alpha_i=C$, $R_i\leq0$  
>Above <font color="Red">KKT</font> cases are evaluated by below constraints under <font color="OrangeRed">$0\leq\alpha_i\leq C$</font>:  
>&#10112;$\frac{\partial L}{\partial \xi}=C-\alpha_i-\mu_i=0$  
>&#10113;$\alpha_i\cdot(y_i\cdot(w^t\cdot x_i-b)+\xi_i-1)=0$  
>
>Also, we give the <font color="OrangeRed">KKT violating cases</font>:  
>&#10112;$\alpha_i<C$ and $R_i<0$  
>&#10113;$\alpha_i>0$ and $R_i>0$  
>&#10114;$\alpha_i=0$ and $R_i>0$...by mjtsai  

>[4]Departure from noise  
>So far, we have our objective function as:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\sum_{i=1}^n\alpha_i-\frac12\cdot\sum_{i,j=1}^n\alpha_i\cdot\alpha_j\cdot y_i\cdot y_j\cdot x_i^t\cdot x_j\end{array}$$  
>for all i, <font color="OrangeRed">$0<\alpha_i<C$</font>, the <font color="OrangeRed">non-boundary</font> case.    

>[5]Works on 2 $\alpha$'s at a time  
>The algorithm of SMO works by <font color="OrangeRed">manipulating 2 $\alpha$'s at a time(with others fixed)</font>, a little <font color="OrangeRed">hill climbing</font> alike approach.  By <font color="OrangeRed">heuristics</font> to choose 2 $\alpha$'s at a time.  
>To optimize $\alpha_1$, $\alpha_2$ with <font color="OrangeRed">other $\alpha$'s fixed</font>, the objective function could be rewritten as:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\alpha_1+\alpha_2+const\\-\frac12\cdot(part\;1+par\;2)\end{array}$$  
>All deduction is based on below equality:  
>$\alpha_1+S\cdot \alpha_2=const$, 
>$\alpha_1=const-S\cdot \alpha_2$,  
>where $\alpha_1+S\cdot \alpha_2=\alpha_1^{old}+S\cdot \alpha_2^{old}$.  

>[6]Express $\alpha_1$ in terms Of $\alpha_2$  
>The major purpose is to express the objective function in terms of single $\alpha_2^{new}$, this is quiet a paintful process.  
>We'd like to toss out almost everything non-related with $\alpha_2^{new}$ and put it it the $const$ term.  The objective function becomes:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=\frac12\cdot(2K_{12}-K_{11}-K_{22})\cdot(\alpha_2^{new})^2\\\;\;\;\;+(1-S+S\cdot K_{11}\cdot r-S\cdot K_{12}\cdot r\\\;\;\;\;+y_2\cdot V_1-y_2\cdot V_2)\cdot\alpha_2^{new}\end{array}$$  

>[7]<font color="DeepPink">Transform from $L(w,b,\xi,\alpha,\mu)$ to $L(\alpha_2^{new})$</font>  
>The major spirit of SMO is to optimize 2 $\alpha$'s at a time, by transiting from the <font color="RoyalBlue">old</font> $\alpha$'s to the <font color="Green">new</font> $\alpha$'s, more precisely, from $\alpha_1^{old}$ to $\alpha_1^{new}$, and from $\alpha_2^{old}$ to $\alpha_2^{new}$.  First, we focus on $\alpha_2^{new}$, and laterly, get the $\alpha_1^{new}$ after we get $\alpha_2^{new}$.  
>&#10112;relate <font color="Green">$\alpha_2^{new}$</font> Back To <font color="RoyalBlue">$\alpha_2^{old}$</font>  
>&#10113;introduction Of $\eta$ by taking $\eta=2K_{12}-K_{11}-K_{22}$, <font color="DeepPink">$\eta\leq0$ is the validity of $\eta$.</font>    
>Now, we formularize our problem in objective function of $\eta$, <font color="Green">$\alpha_2^{new}$</font>, <font color="RoyalBlue">$\alpha_2^{old}$</font>, $E_1^{old}$, $E_2^{old}$:  
$$\begin{array}{l}L(w,b,\xi,\alpha,\mu)\\=L(\alpha_2^{new})\\=\frac12\cdot\eta\cdot(\alpha_2^{new})^2\\\;\;\;\;+(y_2\cdot(E_1^{old}-E_2^{old})-\eta\cdot\alpha_2^{old})\cdot\alpha_2^{new}\\\;\;\;\;+const\end{array}$$  
><font color="DeepPink">It is much simpler in its optimization, <font color="DeepPink">only $\alpha_2^{new}$ is left to be optimized.</font>  

>[8]Examine the feasible rangle of new $\alpha$ value  
><font color="OrangeRed">For computation, $\eta$ should be less than $0$</font>, although it might be approaching to $0$.  We have the new $\alpha_2$ expressed in below:  
>$$\alpha_2^{new}=\alpha_2^{old}+\frac{y_2\cdot(E_2^{old}-E_1^{old})}\eta$$  
>Then, the <font color="Green">$\alpha_2^{new}$</font> thus obtained might be <font color="OrangeRed">unconstrainted</font> maximum value.  <font color="OrangeRed">The feasible range of $\alpha_2^{new}$ must be checked</font>.  
>Take the <font color="OrangeRed">minimum</font> feasible of <font color="Green">$\alpha_2^{new}$</font> be <font color="OrangeRed">L</font>, the <font color="OrangeRed">maximum</font> feasible of <font color="Green">$\alpha_2^{new}$</font> be <font color="OrangeRed">H</font>, then:  
$$\alpha_2^{new,clipped}=\left\{\begin{array}{l}L,if\;\alpha_2^{new}<L\\\alpha_2^{new},if\;L<\alpha_2^{new}<H\\H,if\;\alpha_2^{new}>H\end{array}\right.$$  
>We can finally go to clip the new $\alpha_1$, $\alpha_2$ value with sequantial updating in $b$ and $w$.  
>
>Take $\triangle\alpha_2=\frac{y_2\cdot(E_2^{old}-E_1^{old})}\eta$  
>Recall that <font color="DeepPink">$\alpha_1=r-S\cdot \alpha_2$, it holds for both new and old</font>.  Therefore,  
$$\lim_{\triangle\rightarrow0}\frac{(\alpha_1+\triangle)-\triangle}\triangle=\lim_{\triangle\rightarrow0}\frac{r-S\cdot(\alpha_2+\triangle)-(r-S\cdot\alpha_2)}\triangle$$  
$$\Rightarrow\triangle\alpha_1=-S\cdot\lim_{\triangle\rightarrow0}\frac{(\alpha_2+\triangle)-\alpha_2}\triangle$$  
$$\Rightarrow\triangle\alpha_1=-S\cdot\triangle\alpha_2$$  
>, where $\triangle\alpha_1$, $\triangle\alpha_2$ are the differentials or derivatives of $\alpha_1$, $\alpha_2$.  
>
>This is a quiet tedious, complicated process, but a beautiful framework!!    

### SMO Algorithm
>We all have been given the concept that SMO is the process by <font color="OrangeRed">randomly</font> picking 2 $\alpha$'s at a time, such behavior is called <font color="Red">SMO heuristics</font>.  The implementation or even algorithm flow could be found the existence of a lot variety.  In this section, I'd like to review the algorithm in SMO original design.  By usual, you can find one outer loop and one inner loop in the whole flow.  
>
>[First <font color="Red">heuristic</font>]  
>It is the outer loop for $\alpha_1$.  
>&#10112;iterates all training set, if an example is examined as <font color="Red">KKT violated</font>; it is eligible for optimization.  
>&#10113;search the entire training set for <font color="OrangeRed">non-boundary</font> examples, whose $\alpha\neq0$, $\alpha\neq C$, and $0<\alpha<C$; if such example was found, it is treated as <font color="Red">KKT violated</font>, it is eligible for optimization.  
>&#10114;keep seraching <font color="OrangeRed">non-boundary</font> examples, until all <font color="OrangeRed">non-boundary</font> examples obey KKT conditions <font color="DeepSkyBlue">within $\varepsilon=0.001$</font>.  
>
>Where <font color="DeepPink">non-boundary case guarantees</font>:  
><font color="DeepPink">$\left|(w^{new})^t\cdot x_i-y_i\right|\leq\varepsilon$</font>, for $i=1,2$, and $\varepsilon$ is a rather tiny quantity.  
>
><font color="DeepPink">By above &#10112;, &#10113;, &#10114;, examples at boundary are likely to stay at boundary; examples at non-boundary are likely to move toward boundary as they have been optimized.</font>  Why?  
>Because iteration focus on <font color="OrangeRed">non-boundary</font> cases and <font color="DeepPink">$\alpha_1^{new}=\alpha_1-S\cdot \triangle\alpha_2$</font> will move this example(<font color="Green">$\alpha_1^{new}$</font>) toward boundary.  
>
>&#10115;after &#10112;, &#10113;, &#10114; completed, SMO algorithm will start to search boundary case and optimize it <font color="OrangeRed">if the case has been KKT violated due to non-boundary subset optimization</font>.  

>[Second <font color="Red">heuristic</font>]  
>It is the inner loop for $\alpha_2$.  
>Once $\alpha_1$ has been chosen, $\alpha_2$ would be chosen based on the criteria to maximize the step size in each iteration:  
>$\underset{i,j}{max}\left|E_i-E_j\right|$, where $i$, $j$ would be $1$, $2$.  why?  
>Because <font color="DeepPink">it could speed up the converge from non-boundary location to the boundary side</font>, where:  
>&#10112;$\alpha_2^{new}=\alpha_2^{old}+\frac{y_2\cdot(E_2^{old}-E_1^{old})}\eta$;  
>&#10113;$\alpha_1^{new}=\alpha_1-S\cdot \triangle\alpha_2$  
>

>Before the ending of SVM algorithm, <font color="DeepPink">positive progress</font> means <font color="DeepPink">from $0<\alpha_i<C$ to $\alpha_i\rightarrow0$ or $\alpha_i\rightarrow C$</font>.  From the non-boundary case, then, back to whole training set for optimization by random pick.  
>At the end, this article would like to remind that <font color="OrangeRed">not all iteration makes positive progress</font>, if $x_i=x_j$, then $\eta=0$!!!  Skip to other case is the recommendation from some code snippet.  

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
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