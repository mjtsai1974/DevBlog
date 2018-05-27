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
>$1$-$P(A\vert B)$  
>=$1$-$P(A)$  
>=$P(A^{c})$  
>=$P(A^{c}\vert B)$  
>From the end to the beginning could we prove the inverse direction.  
>
><font color="RoyalBlue">[3]</font>
><font color="OrangeRed">independence of all events</font>  
>Given event $A$ is independent of event $B$, we can infer out all possible independence in between $A$, $A^{c}$, $B$, $B^{c}$.  
><font color="Brown">proof::mjtsai1974</font>  
>$P(A\vert B)$=$P(A)$  
>$\Leftrightarrow P(A^{c}\vert B)$=$P(A^{c})$  
>$\Leftrightarrow P(B\vert A^{c})$=$P(B)$  
>$\Leftrightarrow P(B^{c}\vert A^{c})$=$P(B^{c})$  
>$\Leftrightarrow P(B\vert A)$=$P(B)$  
>$\Leftrightarrow P(B^{c}\vert A)$=$P(B^{c})$  
>$\Leftrightarrow P(A\vert B^{c})$=$P(A)$  
>$\Leftrightarrow P(A^{c}\vert B^{c})$=$P(A^{c})$  
>
>We conclude <font color="DeepPink">if $A$ is independent of $B$, then $A^{c}$ is independent of $B$, $A$ is independent of $B^{c}$, $A^{c}$ is independent of $B^{c}$</font>.  
>
><font color="RoyalBlue">[4]</font>
><font color="OrangeRed">event and its complemenmt</font>  
>The prpbability of intersection of any given event and its complement is $0$,  that is $P(A\cap A^{c})$=$0$.  

### <font color="RoyalBlue">Example</font>: 2nd Head following 1st Head
>Suppose you are tossing a fair coin, the probability of head and tail are all $\frac {1}{2}$, and <font color="DeepSkyBlue">each tossing is an independent case</font>.  
>
>We'd like to ask for <font color="OrangeRed">the probability that the 2nd tossing out a head, right after the 1st tossing out a head</font>, then,  
>&#10112;take the event of 1st tossing as $A_{1}$=$\\{H,T\\}$, take the event of 2nd tossing as $A_{2}$=$\\{H,T\\}$.  
>&#10113;the sample space of these 2 tossing would be $\Omega$=$\\{HH,HT,TH,TT\\}$.  The probability of 2 contiguous heads is $\frac {1}{4}$.  
>&#10114;<font color="OrangeRed">the probability that the 2nd tossing out a head, right after the 1st tossing out a head</font> is asking for $P(A_{2}\cap A_{1})$, then  
>$\frac {1}{4}$  
>=$P(A_{2}\cap A_{1})$  
>=$P(A_{2}\vert A_{1})\cdot P(A_{1})$  
>=$\frac {1}{2}\cdot \frac {1}{2}$  
>=$P(A_{2})\cdot P(A_{1})$  
>Thus, we have $P(A_{2}\vert A_{1})$=$P(A_{2})$, it is fully compliant with the given that <font color="DeepSkyBlue">each tossing is an independent case</font>.  

### <font color="RoyalBlue">Example</font>: Illustration By Tossing A Fair Die
>Suppose you are tossing a fair die, the sample space $\Omega$=$\\{1,2,3,4,5,6\\}$.  We denote the event of numbers smaller than $4$ as $A$=$\\{1,2,3\\}$, and denote the event of even numbers as $B$=$\\{2,4,6\\}$.  
>
>To evaluate <font color="DeepSkyBlue">if event $A$ is independent of event $B$</font>:  
>&#10112;$P(A\cap B)$=$P(\\{2\\})$=$\frac {1}{6}$  
>&#10113;$P(A)\cdot P(B)$=$\frac {1}{2}\cdot \frac {1}{2}$=$\frac {1}{4}$  
>Hence, the event of numbers smaller than $4$ is <font color="DeepPink">not independent</font> of the event of even numbers.  

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