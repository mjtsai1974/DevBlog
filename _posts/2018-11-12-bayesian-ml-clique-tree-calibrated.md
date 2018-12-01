---
layout: post
title: The Calibrated Clique Tree
---

## Prologue To The <font color="Red">Calibrated Clique Tree</font>
<p class="message">
The quantitative evaluation of messages from one clique to its adjacent clique and from this adjacent clique to itself would be a <font color="DeepPink">equilibrium</font> in a <font color="Red">calibrated clique tree</font>.
</p>

### Before We Go Any Farther
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Recap: variable-elimination constructed clique tree</font>  
>Remember that my prior post [The Clique Tree Construction]({{ site.github.repo }}{{ site.baseurl }}/2018/10/14/bayesian-ml-clique-tree-construction/) has proved that <font color="DeepPink">slight different and very different elimination order constructed clique tree makes the same propagation</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Recap: message passing in the clique tree</font>  
>Still in another prior post of mine, [The Bayesian Network Propagation And Clique Tree]({{ site.github.repo }}{{ site.baseurl }}/2018/09/25/bayesian-ml-progagation-cliuque-tree/):  
>&#10112;the message propagation in the <font color="Red">clique tree</font> is proceeded in two stage operations with the former the <font color="DeepSkyBlue">collection</font>(from leaf nodes to the pivot node) and the next is the <font color="DeepSkyBlue">distribution</font>(from pivot node to the leaf nodes).  
>&#10113;<font color="Red">computation sharing</font> in all queries that <font color="#C20000">the function of the message from the pivot to the leafs are all expressed in terms of the variables the same as it is in the clique from which passes message to the pivot</font>.  
>&#10114;given clique $C$ and $C'$ in adjacent, there exists $C_{i}$ for $i$=$1$ to $k$ to be $C$'s neighbors, $g_{i}$ is the message from $C_{i}$ to $C$, and $f_{j}$ is the $j$-th function attached to clique $C$, the message from $C$ to $C'$ is denoted as $H$, expressed as:  
>$H((C\cap C')-E)$=$\sum_{C\backslash C'\cup E}\prod_{i}g_{i}\prod_{j}f_{j}$, with $E$ to be the evidence.  
>
><font color="DeepPink">The summation over elements purely from $C$</font>, <font color="RosyBrown">not</font> belonging to $C'$ and $E$(evidence), then:  
>$H((C\cap C')-E)$=$\sum_{C\backslash C\cap C'}\prod_{i}g_{i}\prod_{j}f_{j}$ also holds for it sums out the variables only in $C$!!
>The term $(C\cap C')-E$ illustrates that the message purely propagates from $C$ to $C'$, exclusive of the intermediate noise.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Notes</font>  
>The <font color="Red">clique tree</font> is also called a <font color="Red">junction tree</font> or a <font color="Red">join tree</font>.  

### What Is The <font color="Red">Calibrated Clique Tree</font>?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Run message passing with each clique in the tree as the pivot(root)</font>  
>Suppose you have a well constructed <font color="Red">clique tree</font>:  
>&#10112;take one <font color="Red">clique</font> that <font color="RosyBrown">neither</font> has been used as a pivot <font color="RosyBrown">nor</font> all its containing variables has been belief updated.  
>&#10113;run message passing from leave nodes to this pivot node with one variable chosen for <font color="DeepSkyBlue">belief update</font>(such variable must <font color="RosyBrown">not</font> have been propagated with message in this clique).  
>&#10114;in the message passing from one clique to another, marginalizes over variables other than &#10113; chosen variable, thus to have the final factor containing only this variable in it.  
>&#10115;repeat &#10112; until each clique and all variables in it has been <font color="DeepSkyBlue">belief updated</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The calibrated clique tree</font>  
>After each clique with all its variables has been <font color="DeepSkyBlue">belief updated</font>, we will have a <font color="Red">calibrated clique tree</font> if below condition is satisfied:  
>$\;\;\sum_{C_{i}\backslash S_{i,j}}Bel_{i}$=$\sum_{C_{j}\backslash S_{i,j}}Bel_{j}$  
>where,  
>&#10112;we denote $Bel_{i}$ for the belief update on clique $i$.  
>&#10113;we take $S_{i,j}$=$C_{i}\cap C_{j}$ as the edge in between $C_{i}$ and $C_{j}$.  
>&#10114;$C_{i}$ and $C_{j}$ are any two <font color="DeepSkyBlue">adjacent</font> cliques in the tree.  
>&#10115;we say that $C_{i}$ and $C_{j}$ are <font color="Red">calibrated</font>.  
>
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-11-12-bayesian-ml-clique-tree-calibrated-cliques.png "calibration")
>We can also use $Bel_{i}(X)$ to be the <font color="DeepSkyBlue">posterior belief update</font> of variable $X$ in clique $i$; for the simplicity, the <font color="DeepSkyBlue">belief update</font> would be proceeded in the unit of each distinct clique in this article.  

### Illustrtation Of The <font color="Red">Calibrated Clique Tree</font>::<font color="Brown">by mjtsai1974</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">From BN to MN</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-11-12-bayesian-ml-clique-tree-calibrated-illustration-bn.png "BN")
>Suppose we are given this BN, with probability distributed over each variable:  
>&#10112;the total joint probability would be  
>$P(A,B,C,D,E,F)$  
>=$P(F\vert C,D)\cdot P(E\vert C)\cdot P(D)$  
>$\;\;P(C\vert A,B)\cdot P(B)\cdot P(A)$  
>&#10113;we'd like to query for $P(A,B,C\vert d,e,f)$=$\frac {P(A,B,C,d,e,f)}{\sum_{A,B,C}P(A,B,C,d,e,f)}$, under the observation(evidence) that $D$=$d$,$E$=$e$,$F$=$f$.  
>&#10114;moralize it, we get below MN.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-11-12-bayesian-ml-clique-tree-calibrated-illustration-mn.png "MN")
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Construct the clique tree</font>  
>By using the variable elimination order $A,B,E,F,D,C$, we construct this clique tree:  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-11-12-bayesian-ml-clique-tree-calibrated-illustration-ct.png "CT")
>&#10112;we choose the clique $(A,B,C)$ as the pivot, for the 1st phase of <font color="DeepSkyBlue">collection</font>:  
>$f_{2}(C)$=$\sum_{E}P(E\vert C)$  
>$f_{3}(C)$=$\sum_{D,F}P(D)\cdot P(F\vert C,D)$  
>$f_{1}(A,B,C)$=$P(A)\cdot P(B)\cdot P(C\vert A,B)$  
>$f_{0}(A,B,C)$=$f_{3}(C)\cdot f_{2}(C)\cdot f_{1}(A,B,C)$  
>, where $f_{0}(A,B,C)$ is the final collected messages in the clique $(A,B,C)$.  
>&#10113;in the 2nd phase of <font color="DeepSkyBlue">distribution</font>, from the pivot to the leafs:  
>$f_{4}(C,E)$=$f_{3}(C)\cdot(\sum_{A,B}f_{1}(A,B,C)\cdot P(E\vert C))$  
>$f_{5}(C,D,F)$=$P(D)\cdot P(F\vert C,D)$  
>$\;\;\cdot(\sum_{A,B}f_{1}(A,B,C)\cdot f_{2}(C))$  
>, where $f_{4}(C,E)$ is the message from pivot to $(C,E)$, and $f_{5}(C,D,F)$ is the message from pivot to $(C,D,F)$.  
>
>$f_{0}(A,B,C)$ in the <font color="DeepSkyBlue">collection</font> phase, $f_{4}(C,E)$ and $f_{5}(C,D,F)$ in the <font color="DeepSkyBlue">distribution</font> phase are all operating over the same factors.  
>
><font color="DeepPink">Although the computation of $f_{0}(A,B,C)$, $f_{4}(C,E)$ and $f_{5}(C,D,F)$ are using the same factors, the marginalizations in these 2 phase are proceeded over different variables, which <font color="RosyBrown">doesn't</font> guarantee to have the equivalent posterior belief</font>.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">The proof of the calibrated clique tree</font>  
>When $C_{i}$ and $C_{j}$ are <font color="Red">calibrated</font>, $\sum_{C_{i}\backslash S_{i,j}}Bel_{i}$=$\sum_{C_{j}\backslash S_{i,j}}Bel_{j}$.  
>
><font color="Brown">proof::mjtsai1974</font>  
>Succeesding to above:  
>&#10112;take $Bel_{1}$=$f_{0}(A,B,C)$ for the belief updated in clique $C_{1}$.  
>&#10113;take $Bel_{2}$=$f_{4}(C,E)$ for the belief updated in clique $C_{2}$.  
>&#10114;take $Bel_{3}$=$f_{5}(C,D,F)$ for the belief updated in clique $C_{3}$.  
>&#10115;then we have below equilibrium holds:  
>$\sum_{A,B}Bel_{1}$=$\sum_{E}Bel_{2}$  
>$\sum_{A,B}Bel_{1}$=$\sum_{D,F}Bel_{3}$  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">The expression of the calibrated message</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-11-12-bayesian-ml-clique-tree-calibrated-message.png "calibrated message")
>&#10112;take $\mu_{i,j}$ to be the <font color="Red">calibrated</font> message from clique $i$ to clique $j$.  
>&#10113;still using the same example, $\mu_{1,2}$ is the <font color="Red">calibrated</font> message from clique $1$ to clique $2$, then  
>$\mu_{1,2}$  
>=$\sum_{A,B}Bel_{1}$  
>=$\sum_{A,B}f_{3}(C)\cdot f_{2}(C)\cdot f_{1}(A,B,C)$  
>=$\sum_{A,B}f_{3}(C)\cdot f_{1}(A,B,C)\cdot f_{2}(C)$  
>=$(\sum_{A,B}f_{3}(C)\cdot f_{1}(A,B,C))\cdot (\sum_{E}P(E\vert C))$  
>=$\delta_{1,2}\cdot\delta_{2,1}$  
>, where $delta_{i,j}$ is the <font color="Red">before-calibrated</font> message propagated from clique $i$ to clique $j$.  
>&#10114;$\mu_{1,3}$=$\delta_{1,3}\cdot\delta_{3,1}$ could also be proved, by mathematics induction, we can claim that <font color="DeepPink">$\mu_{i,j}$=$\delta_{i,j}\cdot\delta_{j,i}$</font>.  
>
><font color="#C20000">The <font color="DeepPink">calibrated message</font> from clique $i$ to clique $j$ is the joint probability function of the <font color="DeepPink">before-calibrated</font> message from clique $i$ to clique $j$ and the <font color="DeepPink">before-calibrated</font> message from clique $j$ to clique $i$</font>.  
>
><font color="DeepSkyBlue">[5]</font>
><font color="OrangeRed">The generalization of the calibrated message</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-11-12-bayesian-ml-clique-tree-calibrated-message-generalized.png "generalized")
><font color="Brown">proof::mjtsai1974</font>  
>&#10112;take $neighbor(C)$=$\{C"\}\cup\{C'\}$  
>&#10113;take $\mu_{S=C\cap C'}$ te be the <font color="DeepPink">calibrated</font> message from clique $C$ to $C'$(or $C'$ to $C$), then  
>$\mu_{S=C\cap C'}$  
>=$\sum_{C\backslash S}\prod f_{j}\prod_{C"\in neighbor(C)}\delta_{C"\rightarrow C}$  
>=$\sum_{C\backslash S}\prod f_{j}\prod_{C"\in neighbor(C)\backslash C'}\delta_{C"\rightarrow C}$  
>$\;\;\cdot \delta_{C'\rightarrow C}$  
>=$\delta_{C\rightarrow C'}\cdot \delta_{C'\rightarrow C}$  
>, where $f_{j}$ is the function attached to clique $C$.  
>&#10114;if we choose the calibrated message from clique $C$ to $C'$, then we have  
>$\mu_{C,C'}$  
>=$\delta_{C\rightarrow C'}\cdot \delta_{C'\rightarrow C}$  
>and, it also hods for below  
>$\mu_{C',C}$  
>=$\delta_{C'\rightarrow C}\cdot \delta_{C\rightarrow C'}$  

### Before The End Of <font color="Red">Bayesian Network</font> Begin@20181201
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Brief summary</font>  
>Using <font color="Red">Bayesian network</font> to compute probability of the query in the form of $P(X\vert E)$ is called <font color="Red">inference</font>, where $E$ is the observed evidence variable(s), $X$ is the query variable(s) in the network.  
>
>The <font color="Red">Bayesian networks</font> are useful for these tasks:  
>&#10112;<font color="Red">diagnosis</font> of the form $P(causes\vert symptom)$, the <font color="Red">quantitative</font> thinking.  
>&#10113;<font color="Red">predict</font> of the form $P(symptom\vert causes)$, the <font color="OrangeRed">qualitative</font> thinking.  
>&#10114;<font color="Red">classification</font> of the form $\underset{class}{max}P(class\vert data)$.  
>&#10115;<font color="Red">decision making</font> by given/develop certain kind of cost function in a subsystem.  
>
>I have &#10112; and &#10113; involved in a lot of my previous posts, in the incoming future, I expect myself to investigate &#10114; and &#10115;, you can find some future direction in p.11~43 of [A Tutorial on Inference and Learning in Bayesian Networks, Irina Rish, IBM T.J.Watson Research Center](http://www.ee.columbia.edu/~vittorio/Lecture12.pdf).  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Time to back to Reinforcement Learning</font>  
>In the early May of 2018, I was struggling over <font color="Red">reinforcement learning</font> in <font color="Red">exploitation versus exploration</font>, for some terminology, <font color="DeepSkyBlue">prior</font> or <font color="DeepSkyBlue">posterior</font> alike, I explore to the <font color="Red">Bayesian network</font>, after months of <font color="Red">exploitation</font>, I should resume my <font color="Red">reinforcement learning</font> and explore to next station of unknow, maybe sooner or later involved in the <font color="Red">Bayesian network</font> due to this deep <font color="Red">exploitation</font> in these days.  
>
>Finally, <font color="DeepPink">the Bayesian network network is a network of multiple variables, while reinforcement learning is a network of only one variable iterating over multiple states.</font>  

### Addendum
>&#10112;[Graphical Models - Lecture 11: Clique Trees, Andrew McCallum, mccallum@cs.umass.edu](https://people.cs.umass.edu/~mccallum/courses/gm2011/11-clique-trees.pdf)  
>&#10113;[A Tutorial on Inference and Learning in Bayesian Networks, Irina Rish, IBM T.J.Watson Research Center](http://www.ee.columbia.edu/~vittorio/Lecture12.pdf)  

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