---
layout: post
title: Variable Elimination In Bayesian Network
---

## Prologue To Variable Elimination In <font color="Red">Bayesian Network</font>
<p class="message">
<font color="Red">Inference</font> via <font color="Red">Bayesian Network</font> could be achieved by probabilistic marginalization, i.e. summing out over <font color="DeepSkyBlue">irrelevant</font> or <font color="DeepSkyBlue">hidden</font> variables.  
</p>

### <font color="Red">Inference</font> Via <font color="Red">Bayesian Network</font>
>Given a well-constructed BN of nodes, 2 types of inference are supported:  
>&#10112;<font color="Red">predictive</font> support(<font color="Red">top-down reasoning</font>) with the evidence nodes connected to node $X$, through its parent nodes, the same direction as predictive propagation.  
>&#10113;<font color="Red">diagnostic</font> support(<font color="Red">bottom-up reasoning</font>), with vidence nodes connected to node $X$, through its children nodes, the same direction as <font color="Red">retrospective</font> propagation.  
>
>In my Bayesian articles, I have guided you through both types of support by means of <font color="DeepSkyBlue">variable enumeration</font> over the factorized terms of full joint PDF(probability distribution function).  Most of the examples are all in small network, trivially, <font color="DeepSkyBlue">variable enumeration</font> is old, she will hold for complex model consisting of a lot random variables, resulting in high expenditure of computation efficiency.  Therefore, another technique of <font color="Red">variable elimination</font> is introduced.   

### <font color="RoyalBlue">Example</font>: Illustration Of <font color="Red">Variable Elimination</font>
>This example is simplified from [variable elimination, Peter Norvig](https://www.youtube.com/watch?v=qyXspkUOhGc&list=PLBF898A2F63224F39&t=0s&index=14).  
>
><font color="RoyalBlue">[Question]</font>  
>Suppose you are using a <font color="Red">Bayesian network</font> to infer the relationship in between raining, traffic and late(to office).  The probability of raining and the conditional probability of traffic jam, given raining, and being late, given traffic jam are all depicted in this graph.  What's the probability of being late?  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-ezex.png "ve ex")
><font color="DeepSkyBlue">[Answer]</font>  
>This is to ask for $P(L=t)$.  The full joint PDF would be $P(R,T,L)$=$P(L\vert T)\cdot P(T\vert R)\cdot P(R)$.  
>
>By the old <font color="DeepSkyBlue">variable enumeration</font>, $P(L=t)$=$\sum_{R}\sum_{T}P(R,T,L=t)$, the nested summation over $T$ would be proceeded inside the outer summation over $R$.  Here, we'd like to further reduce the computation complexity by means of <font color="Red">variable elimination</font>.  
>[1]The first would be to <font color="Red">join factors</font>:  
>&#10112;a <font color="OrangeRed">factor</font> is one of these tables of probability, $P(R)$, or the conditional probability, $P(T\vert R)$, $P(L\vert T)$.  By usual, they are multi-dimensional matrix.  
>&#10113;what we do is to <font color="OrangeRed">choose 2 or more</font> of these factors.  In this case, we choose $P(R)$ and $P(T\vert R)$, to <font color="OrangeRed">combine</font> them together to <font color="OrangeRed">form a new factor</font> which represents the joint probability of all variables, $R$ and $T$ in that new factor $P(R,T)$.  
>&#10114;we perform the operation of joining factors on these 2 factors, $P(R)$, $P(T\vert R)$, getting a new factor which is part of the existing network.  Below exhibits what we have now.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-ezex-join-factor.png "join factors")
>
>[2]The second is the operation of <font color="Red">elimination</font>, also called <font color="OrangeRed">summing out</font> or <font color="OrangeRed">marginalization</font>, to take the table $P(R,T)$, reduce it to $P(T)$, finally <font color="OrangeRed">combine</font> it with $P(L\vert T)$ to get $P(L)$.  
>&#10112;by now, we <font color="OrangeRed">sum out</font> or <font color="OrangeRed">marginalize</font> $P(R,T)$ over the variable $R$ to get $P(T)$ that just operates on $T$.  That is what we have in the network, by <font color="OrangeRed">summing out</font> over all values of $R$, respectively for which $T=t$ and $T=f$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-ezex-sum-out.png "sum out")
>&#10113;next, we do a <font color="OrangeRed">join</font> over $T$ and $L$, by <font color="OrangeRed">combining</font> $P(T)$ and $P(L\vert T)$ to <font color="OrangeRed">get a new factor</font> of joint probability $P(T,L)$.  
>&#10114;now, we are down to a network with a single node, $T,L$ with the joint probability table.  By <font color="OrangeRed">summing out</font> $P(T,L)$ over $T$ with respect for $L=t$ and $L=f$, finally we reach the single node $L$ with $P(L=t)$ and $P(L=f)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-ezex-final.png "final")
>
>It is <font color="DeepPink">a continued process of joining together factors to form a maybe larger factor and then eliminating variables by summing out(marginalization)</font>.  

### <font color="DeepSkyBlue">Optimal</font> <font color="Red">Order</font> For <font color="Red">Variable Elimination</font> Is <font color="DeepSkyBlue">NP-Hard</font>
>In this paragrapg, I'd like to illustrate the execution of different elimination order would probabilistically result in computational side effect.  I'm going to use an example from [Prof. Abbeel, steps through a few variable examples](https://www.youtube.com/watch?v=FDNB0A61PGE), but with my own viewpoint.  
>
><font color="RoyalBlue">[Question]</font> 
>The given BN is depicted below, what's $P(U\vert +z)$?  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-order-model.png "model")
>We are initialized with these factors, they are $P(U)$,$P(V)$,$P(W)$,$P(X\vert U,V)$,$P(Y\vert V,W)$,$P(Z\vert X,Y)$.  Asking for <font color="OrangeRed">$P(U\vert +z)$</font> is <font color="OrangeRed">to eliminate the nodes of $X$,$Y$,$V$,$W$</font> in the network.  
>
><font color="DeepSkyBlue">[Order: $X$,$Y$,$V$,$W$]</font>  
>&#10112;do the factor join over $X$ to eliminate $X$:  
>$f_{1}(+z,Y,U,V)$=$\sum_{x}P(+z\vert x,Y)\cdot P(x\vert U,V)$  
>There is a finding that <font color="#C20000">the elimination of the node with multiple parents would generate a new factor with the number of extra added variables eqivalent to the number of its parents</font>.  
>&#10113;do the factor join over $Y$ to eliminate $Y$:  
>$f_{2}(+z,U,V,W)$=$\sum_{y}f_{1}(+z,y,U,V)\cdot P(y\vert V,W)$  
>&#10114;do the factor join over $V$ to eliminate $V$:  
>$f_{3}(+z,U,W)$=$\sum_{v}f_{2}(+z,U,V,W)\cdot P(v)$  
>&#10115;do the factor join over $W$ to eliminate $W$:  
>$f_{4}(+z,U)$=$\sum_{w}f_{3}(+z,U,W)\cdot P(w)$  
>&#10116;we are left with $f_{4}(+z,U)$ and $P(U)$, then:  
>$P(U\vert +z)$=$\frac {P(U\cap +z)}{P(+z)}$, where <font color="DeepPink">$P(+z)$=$\sum_{u}f_{4}(+z,u)$</font> and <font color="DeepPink">$P(U\cap +z)$=$\sum_{u}f_{4}(+z,u)\cdot P(u)$</font>.  Be noted that this description won't be repeated in below sections.  
>&#10117;we can examine each new generated facor, inspect its <font color="DeepSkyBlue">scale</font>, the <font color="DeepSkyBlue">width</font>.  Below exhibits each distinct generated factor's number of variables.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-order-xyvw.png "xyvw")
>The maximum number in the new generated factor is 3, is such order the most optimal?  Let's continue to walk it through.  
>
><font color="DeepSkyBlue">[Order: $V$,$W$,$X$,$Y$]</font>  
>&#10112;do the factor join over $V$ to eliminate $V$:  
>$f_{1}(X,U,Y,W)$=$\sum_{v}P(X\vert U,V)\cdot P(Y\vert V,W)\cdot P(V)$  
>There is another finding that <font color="#C20000">the elimination of a node having more multiple children, then these children and their parents(if any), must be taken into computation cost</font>.  
>&#10113;do the factor join over $W$ to eliminate $W$:  
>$f_{2}(X,U,Y)$=$\sum_{w}f_{1}(X,U,Y,w)\cdot p(w)$  
>&#10114;do the factor join over $X$ to eliminate $X$:  
>$f_{3}(+z,U,Y)$=$\sum_{x}f_{2}(X,U,Y)\cdot P(+z\vert x,Y)$  
>&#10115;do the factor join over $Y$ to eliminate $Y$:  
>$f_{4}(+z,U)$=$\sum_{y}f_{3}(+z,U,y)$  
>&#10116;you can follow <font color="DeepSkyBlue">[Order: $X$,$Y$,$V$,$W$]</font>'s approach to renomalize for the answer.  
>&#10117;we then examine each new generated facor, inspect its <font color="DeepSkyBlue">scale</font>, the <font color="DeepSkyBlue">width</font>.  Below exhibits each distinct generated factor's number of variables.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-order-vwxy.png "vwxy")
>The maximum number in the new generated factor is 4, this elimination order is worse than $X$,$Y$,$V$,$W$ in computation efficiency.  Let's continue to walk it through to see if we can find another better one.  
>
><font color="DeepSkyBlue">[Order: $W$,$V$,$Y$,$X$]</font>  
>&#10112;do the factor join over $W$ to eliminate $W$:  
>$f_{1}(Y,V)$=$\sum_{w}P(Y\vert V,w)\cdot P(w)$  
>&#10113;do the factor join over $V$ to eliminate $V$:  
>$f_{2}(Y,X,U)$=$\sum_{v}f_{1}(Y,v)\cdot P(X\vert U,v)\cdot P(v)$  
>This is the same finding that <font color="#C20000">the elimination of a node having more multiple children, then these children and their parents(if any), must be taken into computation cost</font>.  
>&#10114;do the factor join over $Y$ to eliminate $Y$:  
>$f_{3}(+z,X,U)$=$\sum_{y}f_{2}(y,X,U)\cdot P(+z\vert X,y)$  
>&#10115;do the factor join over $X$ to eliminate $X$:  
>$f_{4}(+z,U)$=$\sum_{x}f_{3}(+z,X,U)$  
>&#10116;you can follow <font color="DeepSkyBlue">[Order: $X$,$Y$,$V$,$W$]</font>'s approach to renomalize for the answer.  
>&#10117;we then examine each new generated facor, inspect its <font color="DeepSkyBlue">scale</font>, the <font color="DeepSkyBlue">width</font>.  Below exhibits each distinct generated factor's number of variables.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-order-wvyx.png "wvyx")
>The maximum number in the new generated factor is 3, this elimination order is much betten than $V$,$W$,$X$,$Y$ in computation efficiency, and little better than $X$,$Y$,$V$,$W$.  Let's continue to walk it through to see if we can find another better one. 
>
><font color="DeepSkyBlue">[Order: $W$,$Y$,$V$,$X$]</font>  
>&#10112;do the factor join over $W$ to eliminate $W$:  
>$f_{1}(Y,V)$=$\sum_{w}P(Y\vert V,w)\cdot P(w)$  
>&#10113;do the factor join over $Y$ to eliminate $Y$:  
>$f_{2}(+z,X,V)$=$\sum_{y}f_{1}(y,V)\cdot P(+z\vert X,y)$  
>&#10114;do the factor join over $V$ to eliminate $V$:  
>$f_{3}(+z,X,U)$=$\sum_{v}f_{2}(+z,X,v)\cdot P(X\vert U,v)\cdot P(v)$  
>&#10115;do the factor join over $X$ to eliminate $X$:  
>$f_{4}(+z,U)$=$\sum_{x}f_{3}(+z,X,U)$  
>&#10116;you can follow <font color="DeepSkyBlue">[Order: $X$,$Y$,$V$,$W$]</font>'s approach to renomalize for the answer.  
>&#10117;we then examine each new generated facor, inspect its <font color="DeepSkyBlue">scale</font>, the <font color="DeepSkyBlue">width</font>.  Below exhibits each distinct generated factor's number of variables.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-order-wyvx.png "wyvx")
>The maximum number in the new generated factor is 2, this elimination order is much betten than all previous orders.  Let's continue one more to see if we can find another better one.  
>
><font color="DeepSkyBlue">[Order: $W$,$Y$,$X$,$V$]</font>  
>&#10112;do the factor join over $W$ to eliminate $W$:  
>$f_{1}(Y,V)$=$\sum_{w}P(Y\vert V,w)\cdot P(w)$  
>&#10113;do the factor join over $Y$ to eliminate $Y$:  
>$f_{2}(+z,X,V)$=$\sum_{y}f_{1}(y,V)\cdot P(+z\vert X,y)$  
>&#10114;do the factor join over $X$ to eliminate $X$:  
>$f_{3}(+z,U,V)$=$\sum_{x}f_{2}(+z,X,V)\cdot P(x\vert U,V)$  
>&#10115;do the factor join over $V$ to eliminate $V$:  
>$f_{4}(+z,U)$=$\sum_{v}f_{3}(+z,U,V)\cdot P(v)$  
>&#10116;you can follow <font color="DeepSkyBlue">[Order: $X$,$Y$,$V$,$W$]</font>'s approach to renomalize for the answer.  
>&#10117;we then examine each new generated facor, inspect its <font color="DeepSkyBlue">scale</font>, the <font color="DeepSkyBlue">width</font>.  Below exhibits each distinct generated factor's number of variables.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-order-wyxv.png "wyxv")
>The maximum number in the new generated factor is 2, this elimination order is the same good as $W$,$Y$,$V$,$X$, much betten than all other orders.  There exists total $4\cdot 3\cdot 2\cdot 1$ combinations.  So far, we reduce the scale(width) to 2 variables in the new generated factor should be confident to stop, since there should exist no factor ocntaining only 1 variable in this case!!  

### Addendum
>&#10112;[Variable elimination, CS228, Stefano Ermon ](http://kuleshov.github.io/cs228-notes/inference/ve/)  
>&#10113;[Prof. Abbeel, steps through a few variable examples](https://www.youtube.com/watch?v=FDNB0A61PGE)  
>&#10114;[Variable elimination, Peter Norvig](https://www.youtube.com/watch?v=qyXspkUOhGc&list=PLBF898A2F63224F39&t=0s&index=14)  
>&#10115;[Bayesian Networks, Ben-Gal Irad, in Ruggeri F., Faltin F. & Kenett R., Encyclopedia of Statistics in Quality & Reliability, Wiley & Sons (2007).](http://www.eng.tau.ac.il/~bengal/BN.pdf)  

<!-- Γ -->
<!-- \Omega -->
<!-- \cap intersection -->
<!-- \cup union -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- \vert_{0.5}^{\infty} -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- $E\lbrack X\rbrack$ -->
<!-- \overline{X_n} -->
<!-- \underset{Succss}P -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->
<!-- \lim_{t\rightarrow\infty} -->
<!-- \int_{0}^{a}\lambda\cdot e^{-\lambda\cdot t}\operatorname dt -->
<!-- \Leftrightarrow -->
<!-- \prod_{v\in V} -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus, mathematic expression</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha, quiz, example</font> -->
<!-- <font color="Green">new alpha</font> -->

<!-- <font color="#C20000">conclusion, finding</font> -->
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

<!-- ### <font color="RoyalBlue">Example</font>: Illustration By Rainy And Sunny Days In One Week -->
<!-- <font color="RoyalBlue">[Question]</font> -->
<!-- <font color="DeepSkyBlue">[Answer]</font> -->

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->