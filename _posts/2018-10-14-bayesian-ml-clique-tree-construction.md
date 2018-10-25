---
layout: post
title: The Clique Tree Construction
---

## Prologue To The <font color="Red">Clique Tree</font> Construction
<p class="message">
The construction of <font color="Red">clique tree</font> aims at <font color="Red">minimal cliques</font> with none of them being the subsets of their neighbors, by using <font color="Red">VE(variable elimination) in moral graph</font>.
</p>

### <font color="Red">VE</font> Versus <font color="Red">Clique Tree Propagation</font>
>In my early post [Variable Elimination Order And Moral Graph]({{ site.github.repo }}{{ site.baseurl }}/2018/07/29/bayesian-ml-net-var-elim-order-moral/), we have explored how to query <font color="DeepSkyBlue">non-directly connected</font> variables in the <font color="Red">BN</font> by means of VE and have a clear mapping in the <font color="Red">MN</font>.  In advance to construct the <font color="Red">clique tree</font>, recap the VE and make comparison with <font color="Red">clique tree propagation</font>.  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Variable elimination</font>  
>&#10112;<font color="DeepSkyBlue">answers one query at a time</font>, for query of other variables, the whole VE must be proceeded.  
>&#10113;<font color="RosyBrown">delete non-queried</font> variables during VE process.  
>&#10114;<font color="RosyBrown">no</font> computation sharing among different queries.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Clique tree propagation</font>  
>&#10112;make posterior belief update for <font color="DeepPink">all</font> variables, inclusive of these <font color="DeepPink">un-observed</font> variables.  
>&#10113;delete <font color="DeepPink">no</font> any variable in the propagation of message passing.  
>&#10114;allows <font color="Red">computation sharing</font> among different queries.  
>
>Since <font color="Red">clique tree propagation</font> could be distributed on un-observed variables, empirical results suggest to use it when we'd like to make posteriro belief update on un-observed variables.  

### <font color="Red">Clique Tree</font> Construction Algorithm
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Target</font>  
>Given a <font color="Red">BN</font>, the target would be:  
>&#10112;construct a <font color="Red">clique tree</font> that covers the <font color="Red">BN</font>, with <font color="DeepSkyBlue">its clique be the smallest</font>.  
>&#10113;<font color="DeepSkyBlue">by using VE</font> in the moral graph as the solution.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Algorithm</font>  
>There exists over a dozen of <font color="Red">clique tree</font> construction algorithm, I list one workable and rather simple workflow, from [Introduction to Bayesian Networks, Lecture 5: Inference as Message Propagation, Nevin L. Zhang, lzhang@cse.ust.hk, Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Fall 2008](http://www.cse.ust.hk/bnbook/pdf/l05.h.pdf), all related illustration in this article are under progress of this algorithm.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-alg.png "algorithm")
>In the incoming future, I might have my own version of algorithm.  
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Illustration by example</font>  
>Given the same <font color="Red">BN</font>, suppose the elimination order is $X,A,S,D,B,L,T,R$, proceed with the following steps:  
>&#10112;<font color="DeepSkyBlue">moralize</font> the <font color="Red">BN</font> to get the <font color="Red">MN</font>.
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-step-1.png "step 1")
>&#10113;eliminate variable $X$, we get the clique $(X,R)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-step-2.png "step 2")
>&#10114;eliminate variable $A$, we get the clique $(A,T)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-step-3.png "step 3")
>&#10115;eliminate variable $S$, we get the clique $(L,S,B)$, where the green line is the new pairwise connection after $S$ has been removed:    
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-step-4.png "step 4")
>&#10116;eliminate variable $D$, we get the clique $(R,D,B)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-step-5.png "step 5")
>&#10117;eliminate variable $B$, we get the clique $(L,R,B)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-step-6.png "step 6")
>&#10118;eliminate variable $L$, we get the <font color="OrangeRed">final</font> clique $(T,L,R)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-step-7.png "step 7")
>Finally, connect the cliques thus obtained in accordance to the moralized <font color="Red">MN</font>.   
>
><font color="DeepSkyBlue">[4]</font>
><font color="Red">The clique tree is not unique</font>  
>&#10112;will the different elimination order construct clique tree identical to the moralized <font color="Red">MN</font>, or the original <font color="Red">BN</font>?  
>&#10113;<font color="DeepPink">the clique tree is not unique, if we are using different elimination orders</font>.  
>
>Due to above concern, will the posterior belief update all the same in the <font color="Red">clique tree</font> thus constructed, versus <font color="Red">VE</font>?  I will prove my answer in the following sections.  

### <font color="LightCoral">Slight Different</font> <font color="DeepPink">Elimination Order Constructed Clique Tree Makes The Same Propagation</font>::<font color="Brown">by mjtsai1974</font>
>In this section, I'd like to prove that constructing <font color="Red">clique tree</font> by using <font color="LightCoral">slight different</font> elimination order would just make the same propagation.  
><font color="RoyalBlue">[Question]</font>  
>Suppose we are give the same above <font color="Red">BN</font>, this time, the elimination order is $X,A,S,B,D,L,T,R$, with the <font color="Red">clique tree</font> thus constructed, we are asked for the same $P(L\vert X=y,A=y)$, what's it?  
><font color="DeepSkyBlue">[1]</font>
><font color="Red">Clique tree construction</font>  
>Suppose we are give the same above <font color="Red">BN</font>, with $X,A,S,B,D,L,T,R$ as the elimination order, proceed with the following steps:  
>&#10112;<font color="DeepSkyBlue">moralize</font> the <font color="Red">BN</font> to get the <font color="Red">MN</font>.  
>&#10113;eliminate variable $X$, we get the clique $(X,R)$.  
>&#10114;eliminate variable $A$, we get the clique $(A,T)$.  
>&#10115;eliminate variable $S$, we get the clique $(L,S,B)$, where the green line is the new pairwise connection after $S$ has been removed:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-slight-diff-e-o-step-4.png "step 4")
>&#10116;eliminate variable $B$, we get the clique $(R,L,D,B)$, where the green line is the new pairwise connection after $B$ has been removed:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-slight-diff-e-o-step-5.png "step 5")
>&#10117;eliminate variable $D$, we get the clique $(R,L,D)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-slight-diff-e-o-step-6.png "step 6")
>&#10118;eliminate variable $L$, we get the <font color="OrangeRed">final</font> clique $(T,L,R)$:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-slight-diff-e-o-step-7.png "step 7")
>Finally, connect the cliques thus obtained in accordance to the moralized <font color="Red">MN</font>(<font color="DeepSkyBlue">This might not be a perfect clique tree</font>).  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">What is $P(L\vert X=y,A=y)$?</font>  
>Choose $(R,L,D)$ as the pivot:  
>&#10112;$f_{1}$ and $f_{2}$ are the same:  
>$f_{1}(T)$=$P(A=y)\cdot P(T\vert A=y)$  
>$f_{2}(R)$=$P(X=y\vert R)$  
>&#10113;$f_{3}(L,R)$=$\sum_{T}P(R\vert T,L)\cdot f_{1}(T)\cdot f_{2}(R)$  
>&#10114;$f_{4}(L,B)$=$\sum_{S}P(S)\cdot P(L\vert S)\cdot P(B\vert S)$  
>&#10115;$f_{5}(R,D)$=$\sum_{B}P(D\vert R,B)$  
>&#10116;take $H_{\alpha}(R,L,D)$  
>=$\sum_{B}f_{3}(L,R)\cdot f_{4}(L,B)\cdot f_{5}(R,D)\cdot 1$ as the joint probability function in <font color="#6100A8">this</font> clique tree.  
>&#10117;compare with the $H(R,L,B)$ in [The Bayesian Network Propagation And Clique Tree]({{ site.github.repo }}{{ site.baseurl }}/2018/09/25/bayesian-ml-progagation-cliuque-tree/), we turn $f_{5}(R,D)$ into $f_{5.5}(R,B)$:  
>$f_{5.5}(R,B)$=$\sum_{D}P(D\vert R,B)$, therefore,  
>$H_{\alpha}(R,L,D)$  
>=$\sum_{B}f_{3}(L,R)\cdot f_{4}(L,B)\cdot f_{5}(R,D)\cdot 1$  
>=$f_{3}(L,R)\cdot f_{4}(L,B)\cdot f_{5.5}(R,B)\cdot 1$  
>=$H_{\alpha}(R,L,B)$ in <font color="#6100A8">this</font> clique tree.  
>=$H(R,L,B)$ in [The Bayesian Network Propagation And Clique Tree]({{ site.github.repo }}{{ site.baseurl }}/2018/09/25/bayesian-ml-progagation-cliuque-tree/)  
><font color="DeepPink">The answer of $P(L\vert X=y,A=y)$ would just be the same!!!</font>
>
>The clique trees are compared in below graph, the <font color="#6100A8">new</font> tree is under the <font color="#FFAC12">original</font> tree:    
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-slight-diff-e-o-compare.png "compare")
>The functions associated with <font color="#FFAC12">original clique tree</font> are listed below:  
>$f_{1}(T)$=$P(A=y)\cdot P(T\vert A=y)$  
>$f_{2}(R)$=$P(X=y\vert R)$  
>$f_{3}(L,B)$=$\sum_{S}P(S)\cdot P(L\vert S)\cdot P(B\vert S)$  
>$f_{4}(R,B)$=$\sum_{D}P(D\vert R,B)$  
>$f_{5}(L,R)$=$\sum_{T}f_{1}(T)\cdot f_{2}(R)\cdot P(R\vert T,L)$  
>$H(R,L,B)$=$f_{3}(L,B)\cdot f_{4}(R,B)\cdot f_{5}(L,R)\cdot 1$  

### <font color="LightSalmon">Very Different</font> <font color="DeepPink">Elimination Order Constructed Clique Tree Makes The Same Propagation</font>::<font color="Brown">by mjtsai1974</font>
>In this section, I'd like to prove that by using <font color="LightSalmon">very different</font> elimination order in <font color="Red">clique tree</font> construction process will you get the <font color="DeepPink">identical</font> propagation of message passing for the same given <font color="Red">BN</font>.  
><font color="RoyalBlue">[Question]</font>  
>Suppose we are give the same above <font color="Red">BN</font>, this time, the elimination order is $X,A,T,R,B,D,L,S$, with the <font color="Red">clique tree</font> thus constructed, we are asked for the same $P(L\vert X=y,A=y)$, what's it?  
><font color="DeepSkyBlue">[1]</font>
><font color="Red">Clique tree construction</font>  
>Assume we are give the same above <font color="Red">BN</font>, the elimination order is $X,A,T,R,B,D,L,S$, proceed with the following steps:
>&#10112;<font color="DeepSkyBlue">moralize</font> the <font color="Red">BN</font> to get the <font color="Red">MN</font>.  
>&#10113;eliminate variable $X$, we get the clique $(X,R)$.  
>&#10114;eliminate variable $A$, we get the clique $(A,T)$.  
>&#10115;eliminate variable $T$, we get the clique $(T,L,R)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-very-diff-e-o-step-4.png "step 4")
>&#10116;eliminate variable $R$, we get the clique $(R,L,D,B)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-very-diff-e-o-step-5.png "step 5")
>&#10117;eliminate variable $B$, we get the clique $(B,S,D)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-very-diff-e-o-step-6.png "step 6")
>&#10118;eliminate variable $D$, we get the clique $(L,S,D)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-very-diff-e-o-step-7.png "step 7")
>Finally, connect the cliques thus obtained in accordance to the moralized <font color="Red">MN</font>(<font color="DeepSkyBlue">This might not be a perfect clique tree</font>).  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">What is $P(L\vert X=y,A=y)$?</font>  
>Choose $(T,L,R)$ as the pivot:  
>&#10112;$f_{1}$ and $f_{2}$ are the same:  
>$f_{1}(T)$=$P(A=y)\cdot P(T\vert A=y)$  
>$f_{2}(R)$=$P(X=y\vert R)$  
>&#10113;$f_{3}(L,D)$=$\sum_{S}P(L\vert S)\cdot P(S)$  
>&#10114;$f_{4}(B,D)$=$\sum_{S}P(B\vert S)\cdot P(S)$  
>&#10115;$f_{5}(R)$=$\sum_{B,D}P(D\vert R,B)\cdot f_{3}(L,D)\cdot f_{4}(B,D)$  
>&#10116;take $H_{\beta}(T,L,R)$  
>=$P(R\vert T,L)\cdot f_{1}(T)$  
>$\;\;\cdot f_{2}(R)\cdot f_{5}(R)$ as the joint probability function in <font color="#6100A8">this</font> clique tree.  
>&#10117;compare with the $H(R,L,B)$ in [The Bayesian Network Propagation And Clique Tree]({{ site.github.repo }}{{ site.baseurl }}/2018/09/25/bayesian-ml-progagation-cliuque-tree/), we turn $f_{5}(R)$ into $f_{5.5}(R,B)$:  
>$f_{5.5}(R,B)$=$\sum_{D}P(D\vert R,B)\cdot f_{3}(L,D)\cdot f_{4}(B,D)$, therefore,  
>$H_{\beta}(T,L,R)$  
>=$P(R\vert T,L)\cdot f_{1}(T)$  
$\;\;\cdot f_{2}(R)\cdot f_{5}(R)$  
>=$\sum_{T}P(R\vert T,L)\cdot f_{1}(T)$  
$\;\;\cdot f_{2}(R)\cdot f_{5.5}(R,B)$  
>=$H_{\beta}(R,L,B)$  
>=$H(R,L,B)$ in [The Bayesian Network Propagation And Clique Tree]({{ site.github.repo }}{{ site.baseurl }}/2018/09/25/bayesian-ml-progagation-cliuque-tree/)  
><font color="DeepPink">The answer of $P(L\vert X=y,A=y)$ would just be the same!!!</font>
>
>The clique trees are compared in below graph, the <font color="#6100A8">new</font> tree is under the <font color="#FFAC12">original</font> tree:    
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-very-diff-e-o-compare.png "compare")
>The functions associated with <font color="#FFAC12">original clique tree</font> could be found in prior section.  

### The Target: <font color="Red">Minimal Clique Trees</font>
>A <font color="DeepPink">clique tree is minimal if none of its cliques are subsets of their neighbors</font>, the ideal version after variable elimination should be <font color="DeepPink">minimal</font>.  
>Below exhibits different <font color="Red">VE</font> leads to different <font color="Red">clique trees</font>(<font color="DeepSkyBlue">non-minimal</font>):  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-diff-ve.png "diff ve")
>The ideal <font color="Red">minimal clique tree</font> would the illustration:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-minimal.png "minimal")
>Current introduced buildCliqueTree() algorithm might not guarantee to have the minimal result, in the incoming future, I might develop a new algorithm for this. (to be conti...)  

### <font color="DeepPink">Clique Tree Is Variable-Connected</font>
>The <font color="Red">clique tree</font> by buildCliqueTree() from the un-connected <font color="Red">MN</font> is <font color="DeepPink">variable-connected</font>.  
><font color="Brown">proof::mjtsai1974</font>  
>By using mathematics induction fashion, we can prove it.  
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">the case of $1$ clique</font>  
>Suppose <font color="DeepSkyBlue">only one</font> clique in the tree, this just holds.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">the case of $n$ cliques</font>  
>Suppose it holds for $n$ cliques in the tree $\tau'$, next to prove it holds for $n+1$ cliques in the tree $\tau$. 
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-vc-n.png "n cliques")
>Below is the pre-requisite to next prove step:  
>&#10112;the tree $\tau'$ contains cliques $C_{1}$ and $C_{2}$ with variable $X$ in it.  
>&#10113;since $\tau'$ is the <font color="Red">clique tree</font>, variable $X$ exists in all the cliques of the path in between $C_{1}$ and $C_{2}$.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">the case of $n+1$ cliques</font>  
>We'd like to show $X$ exists in all the cliques of the path in between $C_{1}$ and $C_{2}$ in tree of $n+1$ cliques.  
>To create tree $\tau$, we make below assumption:  
>&#10112;$C_{1}$ is the clique by removing variable $Z$, where variable $X$ is not $Z$(since $X\in C_{1}\cap C_{2}$), therefore $X\in S$.  
>&#10113;$\tau'$ is the tree obtained after &#10112;.  
>&#10114;suppose $S'$ is obtained by removing some other node in $S$(not $X$), then $S' \subseteq S$.  
>&#10115;or suppose $S'$ is obtained by removing some other variables <font color="DeepSkyBlue">in adjacent to</font> all variables in $S$, then $S'$=$S$.  
>&#10116;for bothe case $S' \subseteq S$ or $S'$=$S$, then $X\in S$ and $X\in S'$ must all hold.  By taking $\tau$=$C_{1}$+$\tau'$, trivially, the variable exists in the cliques of the path in between $C_{1}$ and $C_{2}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-vc-n1.png "n+1 cliques")
>
>Evenmore, for the condition that keeping &#10112;,&#10113; the same, where $S'$ is obtained by removing variable $X$ from $S$, then $S' \subset S$, that is to say $C'$=$S'\cup X$.  By taking $\tau$=$C_{1}$+$\tau'$, we also find it true that the variable exists in the cliques of the path in between $C_{1}$ and $C_{2}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-10-14-bayesian-ml-clique-tree-construction-vc-n1_2.png "n+1 cliques")

### Addendum
>&#10112;[Introduction to Bayesian Networks, Lecture 5: Inference as Message Propagation, Nevin L. Zhang, lzhang@cse.ust.hk, Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Fall 2008](http://www.cse.ust.hk/bnbook/pdf/l05.h.pdf)  
>&#10113;[Clique Tree Algorithm - Computation](https://zh-tw.coursera.org/lecture/probabilistic-graphical-models-2-inference/clique-tree-algorithm-computation-Jm0AM)  
>&#10114;[Clique Trees, Amr Ahmed, CS CMU, October 23, 2008](http://www.cs.cmu.edu/~guestrin/Class/10708/recitations/r7/Clique_Trees_2slides.pdf)  
>&#10115;[Graphical Models - Lecture 11: Clique Trees, Andrew McCallum, mccallum@cs.umass.edu](https://people.cs.umass.edu/~mccallum/courses/gm2011/11-clique-trees.pdf)  

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
<!-- \subset -->
<!-- \subseteq -->
<!-- \varnothing -->
<!-- \perp -->
<!-- \overset\triangle= -->

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

<!--
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Why at this moment, the Poisson and exponential probability come out with different result?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->