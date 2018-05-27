---
layout: post
title: Event Independence versus Conditional Probability
---

## Prologue To <font color="Red">Event Independence</font> versus <font color="DeepSkyBlue">Conditional Probability</font>
<p class="message">
In the disciplines of probability, <font color="Red">event independence</font> is quiet an important concept.  
The inference from <font color="DeepSkyBlue">conditional probability</font> come out with the result that one event occurrence is said to <font color="OrangeRed">not related</font> to another event, if the two events are <font color="OrangeRed">independent</font>.  
</p>

### Definition: <font color="Red">Event Independence</font>
>An event $A$ is said independent of event $B$, if  
>$\;\;\;\;P(A\vert B)$=$P(A)$.  

### <font color="Red">Event Independence</font> <font color="DeepSkyBlue">Equivalence</font>
>By the definition of <font color="Red">event independence</font>, we can have an equivalence of expression from <font color="DeepSkyBlue">conditional probability</font>:  
>$P(A\vert B)$=$\frac {P(A\cap B)}{P(B)}$=$P(A)$  
>$\Leftrightarrow P(A\cap B)=P(A)\cdot P(B)$  
>
>Below lists the basic properties:  
>&#10112;$P(A\cap B)$=$P(A)\cdot P(B)$ indicates event $A$ is independent of event $B$.  
>&#10113;by its symmetry, $P(A)\cdot P(B)$=$P(B)\cdot P(A)$=$P(B\cap A)$, event $B$ is independent of event $A$.  
>&#10114;$P(A\vert B)$=$P(A)$ and $P(B\vert A)$=$P(B)$.  

### <font color="Red">Event Independence</font> <font color="DeepSkyBlue">Extension</font>
><font color="RoyalBlue">[1]</font>
><font color="OrangeRed">multiple events independence</font>  
>$P(N_{1}\cap N_{2}\cap...\cap N_{m})$  
>=$P(N_{1})\cdot P(N_{2})\cdot ...\cdot P(N_{m-1})\cdot P(N_{m})$, given that all events $N_{i}$ are all independent.  
><font color="Brown">proof::mjtsai1974</font>  
<!-- >$P(N_{1}\cap N_{2}\cap...\cap N_{m})$  
>=$P(N_{1}\vert (N_{2}\cap N_{3}\cap ...\cap N_{m}))$  
>$\;\;\;\;\cdot P(N_{2}\vert (N_{3}\cap ...\cap N_{m}))$  
>$\;\;\;\;\...$  
>$\;\;\;\;\cdot P(N_{m-1}\vert N_{m})$  
>$\;\;\;\;\cdot P(N_{m})$  
>=$\frac {P(N_{1}\cap (N_{2}\cap N_{3}\cap ...\cap N_{m}))}{P(N_{2}\cap N_{3}\cap ...\cap N_{m})}$  
>$\;\;\;\;\cdot \frac {P(N_{2}\cap (N_{3}\cap ...\cap N_{m}))}{P(N_{3}\cap ...\cap N_{m})}$  
>$\;\;\;\;\...$  
>$\;\;\;\;\cdot \frac {P(N_{m-1}\cap N_{m})}{P(N_{m})}$  
>$\;\;\;\;\cdot P(N_{m})$  
>=$P(N_{1})\cdot P(N_{1})\cdot ...\cdot P(N_{m-1})\cdot P(N_{m})$  
>$\Rightarrow$!-->
>&#10112;$P(N_{m-1}\vert N_{m})$=$\frac {P(N_{m-1}\cap N_{m})}{P(N_{m})}$=$P(N_{m-1})$  
>Then $P(N_{m-1}\cap N_{m})$  
>=$P(N_{m-1})\cdot P(N_{m})$.  
>&#10113;$P(N_{m-2}\vert (N_{m-1}\cap N_{m}))$=$\frac {P(N_{m-2}\cap (N_{m-1}\cap N_{m}))}{P(N_{m-1}\cap N_{m})}$=$P(N_{m-2})$  
>Then $P(N_{m-2}\cap (N_{m-1}\cap N_{m}))$  
>=$P(N_{m-2})\cdot P(N_{m-1})\cdot P(N_{m})$.  
>&#10114;by mathematics induction, could we finally have the equivalence of expression.  
>
><font color="RoyalBlue">[2]</font>
><font color="OrangeRed">independence equivalence relation</font>  
>Event $A$ is independent of event $B$  
>$\Leftrightarrow$ event $A^{c}$ is independent of event $B$  
><font color="Brown">proof::mjtsai1974</font>  
>&#10112;$\Rightarrow$  
>$1$-$P(A\vert B)$  
>=$1$-$P(A)$  
>=$P(A^{c})$  
>=$P(A^{c}\vert B)$  
>&#10113;$\Leftarrow$  
>$P(A^{c}\vert B)$  
>=$P(A^{c})$  
>=$1$-$P(A)$  
>$1$-$P(A\vert B)$  

<!-- Γ -->
<!-- \Omega -->
<!-- \subset -->
<!-- \cap intersection -->
<!-- \cup union -->
<!-- P(A\vert C) -->
<!-- \Rightarrow -->
<!-- \Leftarrow -->
<!-- \Leftrightarrow -->
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

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha, quiz, example</font> -->
<!-- <font color="Green">new alpha</font> -->

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

<!-- <font color="Brown">proof::mjtsai1974</font> -->

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->