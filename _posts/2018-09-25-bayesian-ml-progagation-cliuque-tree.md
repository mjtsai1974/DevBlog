---
layout: post
title: The Bayesian Network Propagation And Clique Tree
---

## Prologue To The <font color="Red">Bayesian Network Propagation</font> And <font color="Red">Clique Tree</font>
<p class="message">
The introduction of <font color="Red">clique tree</font> algorithm aims at <font color="Red">posterior belief update</font> distributed in all variables of a network by means of <font color="Red">message propagation</font>.
</p>

### The <font color="Red">Clique Tree</font>
>A <font color="Red">clique tree</font> is an <font color="Red">undirected</font> tree, where:  
>&#10112;each node in the tree is a set of variables, called a <font color="Red">clique</font>.  
>&#10113;<font color="DeepPink">if one variable appears in 2 cliques, it must exist in all the cliques in the path between the 2 cliques</font>.  It is <font color="DeepPink">variable-connected</font>.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-invalid.png "invalid")
>This is an <font color="RosyBrown">invalid</font> clique tree, variable B should exist in all the cliques in the path in between cliques of $(B,S)$ and $(R,D,B)$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-valid.png "valid")
>This is a <font color="DeepPink">valid</font> clique tree, since it meets the criteria that a variable could be found on all cliques in the path between 2 cliques containing it.  
>
>A <font color="DeepSkyBlue">clique tree covers a Bayesian network</font> if below conditions are meet:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-bn.png "BN sample")
>&#10112;the union of the cliques is the set of the variables in the <font color="Red">Bayesian network</font>.  
>&#10113;for any variable $X$, the clique tree has one clique containing this variable with all its parent variables, such clique is called the <font color="OrangeRed">family cover clique</font> of $X$.  
>Suppose we are given above <font color="Red">Bayesian network</font>, below <font color="Red">clique tree</font> is just one such example.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-family-cover.png "valid")

### The <font color="Red">Clique Tree</font> For <font color="Red">Variable Elimination</font>
>Supposed we are given this <font color="Red">Bayesian network</font> and would like to make the posterior belief update of <font color="Red">all</font> variables based on the observed evidence.  This paragraph will guide you through the whole process by using the <font color="Red">clique tree</font>.  
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Initialize the cliques with independence probability distribution of BN variables</font>  
>For each variable $X$ in <font color="Red">Bayesian network</font>:  
>&#10112;find the probability of $P(X\vert Pa(X))$ and attach it onto the clique containing $X$.  
>&#10113;if the clique has no probability of independence attached, set it to the <font color="Green">identity</font> function.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-ve-step-1.png "step 1")
>Trivially, the multiplication of all functions on the clique tree is equivalent to the full joint probability distribution in the <font color="Red">Bayesian network</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Instantiate the variable with the observed evidence</font>  
>Using the same <font color="Red">Bayesian network</font>, we denote the observed evidence as $E$, <font color="OrangeRed">in the real world, we can have observation of multiple variables at the same time</font>.  
>
>Suppose we have observed $A=y$ and $X=y$, to instantiate the clique tree, we associate the independence probability function containing $A$ and $X$ with the observed value $y$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-ve-step-2.png "step 2")
>If we take $\chi$ to be all unobserved variables, $P(\chi,E)$ is just the multiplication of all functions on the clique tess, which will laterly be proved.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Choose pivot for reference</font>  
>&#10112;for <font color="DeepSkyBlue">one</font> query variable case, <font color="DeepSkyBlue">choose the clique containing that variable in it to be the pivot</font>.  
>Suppose we'd like to query for $P(L\vert A=y,X=y)$, based on the observation of $A=y,X=y$, in the same example, take the <font color="Red">clique</font> $(R,L,B)$ to be the <font color="Red">pivot</font>, the $(T,L,R)$ could also be the candidate.  
>&#10113;for case of <font color="OrangeRed">two</font> query variables, then <font color="OrangeRed">combine the cliques of the queried variable together as the pivot</font>, or just <font color="OrangeRed">choose the clique containing these 2 queried variables</font>, if any exists.  
>Suppose we'd like to query for $P(T,L\vert A=y,X=y)$, we can <font color="OrangeRed">directly take the clique $(T,L,R)$ as to pivot</font>.  If we'd like to query for $P(T,B\vert A=y,X=y)$, then <font color="OrangeRed">combine the cliques $(T,L,R)$,$(R,L,B)$ just holds</font>.  
>&#10114;for multiple query variables case, follow &#10113;'s fashion, could we reach the goal.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Pass the messages from the leafs to the pivot</font>  
>When we have a clique tree constructed, <font color="OrangeRed">the messages(evidence) are passed from the leafs to the pivot node</font>.  Supposed we have such example of undirected graph, the clique is expressed by uppercase C for better understanding.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-ve-step-4-msg-passing.png "msg passing")
>This exhibition reveals the portion mostly closed to the target pivot $C_{Q}$, the messages are coming from $C_{i}$, where $i$=$1$ to $k$, such <font color="OrangeRed">message passing are triggered by the observed evidence on leaf nodes</font>, maybe far away from these $C_{i}$s.  
>&#10112;$g_{i}$ is the message from $C_{i}$ to $C$.  
>&#10113;$f_{j}$ is the function attached to $C$.  
>&#10114;the messages passed to $C$, are trsnafered to $C'$, we denote it $H$.  
>$H((C\cap C')-E)$=$\sum_{C\backslash C'\cup E}\prod_{i}g_{i}\prod_{j}f_{j}$  
>The summation over elements purely from $C$, <font color="RosyBrown">not</font> belonging to $C'$ and $E$(evidence).  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-ve-step-4-msg-passing-func.png "msg passing function")
>The term $(C\cap C')-E$ is better understood by this illustration.  Since <font color="OrangeRed">$C$ and $C'$ are independent, the intersection of the 2 nodes is null</font>.  It's the <font color="#C20000">evidence existing in the space in between $C$ and $C'$, after we minus $E$, what we want is the pure message from $C$ to $C'$</font>.  
>
><font color="DeepSkyBlue">[5]</font>
><font color="OrangeRed">Posterior belief update</font>  
>Supposed we'd like to query for $P(Q|E=e)$ in above given graph of <font color="Red">clique tree</font>, and we take $H(Q,\chi)$ to be the <font color="DeepSkyBlue">function attached or send to</font> $C_{Q}$, where $\chi$ stands for all <font color="OrangeRed">unobserved</font> variables other than $Q$ in $C_{Q}$:  
>$P(Q|E=e)$=$\frac {\sum_{\chi}H(Q,\chi)}{\sum_{Q,\chi}H(Q,\chi)}$  

### <font color="Red">Posterior Belief Update</font> Illustration In <font color="Red">Clique Tree</font>
<font color="RoyalBlue">[Question]</font>
>Using the same <font color="Red">clique tree</font>, suppose we are given the observed evidence on $A=y$ and $X=y$, we'd like to make inference on $P(L\vert A=y,X=y)$.  
<font color="DeepSkyBlue">[Answer]</font>
>Let's illustrate by this graph, similar to variable elimination process.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-bel-upd.png "bel update")
>&#10112;do the join over $A=y$ in clique $(A,T)$:  
>$f_{1}(T)$=$P(A=y)\cdot P(T\vert A=y)$  
>&#10113;directly take the only attached function in clique $(R,X)$:  
>$f_{2}(R)$=$P(X=y\vert R)$  
>&#10114;do the join over $S$ in clique $(L,S,B)$, we'd like to <font color="DeepSkyBlue">move toward the pivot</font>:  
>$f_{3}(L,B)$=$\sum_{S}P(S)\cdot P(L\vert S)\cdot P(B\vert S)$  
>&#10115;do the join over $D$ in clique $(R,D,B)$, we'd like to <font color="DeepSkyBlue">move toward the pivot</font>:  
>$f_{4}(R,B)$=$\sum_{D}P(D\vert R,B)$  
>&#10116;<font color="DeepSkyBlue">in clique $(T,L,R)$, collect the message from clique $(A,T)$ and $(R,X)$, pass it to the pivot</font>:  
>$f_{5}(L,R)$=$\sum_{T}f_{1}(T)\cdot f_{2}(R)\cdot P(R\vert T,L)$  
>This time, join over $T$.  
>&#10117;thus we have $f_{3}(L,B)$,$f_{4}(R,B)$ and $f_{5}(L,R)$, the joint probability is thus distributed and expressed as:  
>$H(R,L,B)$=$f_{3}(L,B)\cdot f_{4}(R,B)\cdot f_{5}(L,R)\cdot 1$  
>
>Finally, $P(L\vert A=y,X=y)$=$\frac {\sum_{R,B}H(R,L,B)}{\sum_{R,L,B}H(R,L,B)}$, since <font color="OrangeRed">$H(R,L,B)$ already encompass $A=y$ and $X=y$ in it</font>.  

### The <font color="Red">Clique Tree</font> Propagation Algorithm: <font color="Red">Computation Sharing</font> In All Queries
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The algorithm of two sweep message passing</font>  
>&#10112;the first sweep is <font color="DeepSkyBlue">collection</font>, from the leafs to the pivot, above posterior belief update illustration is the example.  
>&#10113;the second sweep is <font color="DeepSkyBlue">distribution</font>, from the pivot to the leafs.  Next to illustrate it.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Propagation from the pivot to the leafs</font>  
>Just like your eyes see somthing, stimulation from certain observation of evidence to the brain, next would be the inspiration from the brain central point back to each distinct parts that had joined in this message frowarding process, finally back to your eyes.  This explains why human sometimes tracks object movement, maybe.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-bel-upd-dist.png "distribution")
>Using the same example of <font color="Red">clique tree</font>, the message is distributed from the pivot $(R,L,B)$ to all other cliques in reversed direction.  
>&#10112;$f_{6}(R,L)$=$\sum_{B}f_{3}(L,B)\cdot f_{4}(R,B)\cdot 1$  
>Combine the $f_{3}(L,B)$,$f_{4}(R,B)$ by joining over $B$, could we have the function of message passing to clique $(T,L,R)$.  
>&#10113;$f_{7}(R,B)$=$\sum_{L}f_{3}(L,B)\cdot f_{5}(R,L)\cdot 1$  
>&#10114;$f_{8}(L,B)$=$\sum_{R}f_{4}(R,B)\cdot f_{5}(R,L)\cdot 1$  
>&#10115;$f_{9}(R)$=$\sum_{T,L}f_{1}(T)\cdot f_{6}(R,L)\cdot P(R\vert T,L)$  
>Combine $P(R\vert T,L)$ with $f_{1}(T)$ and $f_{6}(R,L)$, join over $T,L$, could we have such expression of the message passing to clique $(R,X)$ from the pivot.  
>&#10115;$f_{10}(T)$=$\sum_{R}f_{2}(R)\cdot f_{6}(R,L)$  
>
>Have you found that <font color="DeepPink">the function of the message from the pivot to the leafs are all expressed in terms of the variables the same as it is in the clique from which passes message to the pivot</font>.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Posterior belief update after distribution::mjtsai1974</font>  
>Suppose you'd like to infer $P(L\vert A=y,X=y)$ in $(T,L,R)$, since we have $f_{1}(T)$,$f_{2}(R)$,$f_{6}(R,L)$ send to $(T,L,R)$ and $P(R\vert T,L)$ attached to it:  
>&#10112;$I(T,L,R)$  
>=$\sum_{B}f_{1}(T)\cdot f_{2}(R)\cdot$  
>$\;\;f_{3}(L,B)\cdot f_{4}(R,B)\cdot P(R\vert T,L)$  
>=$f_{1}(T)\cdot f_{2}(R)\cdot f_{6}(R,L)\cdot P(R\vert T,L)$  
>, where $f_{6}(R,L)$ is the join of $f_{3}(L,B)$ and $f_{4}(R,B)$ over $B$.  
>&#10113;$P(L\vert A=y,X=y)$  
>=$\frac {\sum_{T,L,R}I(T,R)}{\sum_{T,L,R}I(T,L,R)}$  
>&#10114;by <font color="DeepPink">using $H(R,L,B)$ or $I(T,L,R)$ is to calculate $P(L\vert A=y,X=y)$ on the same sets of functions</font>!  
>
>This is my explain of <font color="Red">computation sharing</font>.  

### The <font color="Red">Clique Tree</font> Properties
><font color="DeepSkyBlue">Property 1:</font>
><font color="OrangeRed">The arguemnts of the functions attached or send to a clique are all veriables in the clique</font>  
>In mjtsai's explain:  
>&#10112;<font color="DeepSkyBlue">before</font> $C$ sends to $C'$, the arguments of the functions attached to $C$ or send to $C$ <font color="OrangeRed">would be passed to</font> a clique $C'$ are all variables in the clique $C$.  
>&#10113;<font color="DeepSkyBlue">after</font> $C$ sends to $C'$, the arguments of the functions attached to $C$ or send to $C$ <font color="OrangeRed">has been passed to</font> a clique $C'$ are all variables in the clique $C$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-09-25-bayesian-ml-progagation-cliuque-tree-arguments-passing.png "arguments passing")
><font color="Brown">proof::mjtsai1974</font>  
>Using the same <font color="Red">clique tree</font> in above paragraph, focus on the left pink marked part.   
>&#10112;by given we have $f_{j}$ attached to $C$ and passing message of $g_{i}$ from $C_{i}$.  
>&#10113;the function of the messgae from $C$ to $C'$ is thus defined:  
>$H((C\cap C')-E)$=$\sum_{C\backslash C'\cup E}\prod_{i}g_{i}\prod_{j}f_{j}$  
>therefore, the arguments of the functions in the passing messgae from $C$ to $C'$ are all the variables in $C$.  
>
><font color="DeepSkyBlue">Property 2:</font>
><font color="OrangeRed">Product of functions attached to or send to all un-activated cliques=$P(\chi,E=e)$, where $\chi$ stands for all unobserved variables in these un-activated cliques</font>  
>We denote <font color="DeepSkyBlue">a clique is un-activated if it has not send out messages</font>.  

### Addendum
>&#10112;[Introduction to Bayesian Networks, Lecture 5: Inference as Message Propagation, Nevin L. Zhang, lzhang@cse.ust.hk, Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Fall 2008](http://www.cse.ust.hk/bnbook/pdf/l05.h.pdf)  

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