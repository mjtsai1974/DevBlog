---
layout: post
title: Introduction To The Conditional Probability
---

## Prologue To Introduction To The <font color="Red">Conditional Probability</font>
<p class="message">
<font color="DeepSkyBlue">Based on the probability of some already occurred event, we can infer or reassess the probability of another event</font>, which is the major effect of the <font color="Red">conditional probability</font>.
</p>

### Definition: <font color="Red">Conditional Probability</font>
>Given the probability $P(C)$ of the <font color="OrangeRed">already occurred event</font> $C$, we can compute another event $A$'s probability $P(A\vert C)$.  The <font color="Red">conditional probability</font> is defined:  
>$\;\;\;\;P(A\vert C)$=$\frac {P(A\cap C)}{P(C)}$, provided that $P(C)>0$.  
>
>This implies that <font color="DeepSkyBlue">the conditonal probability could help to find out the fraction of the probability of event $C$ <font color="OrangeRed">is also</font> in event $A$</font>, which is <font color="OrangeRed">$P(A\cap C)$</font>.  

### <font color="Red">Conditional Probability</font> <font color="DeepSkyBlue">Properties</font>
>Given that $P(C)>0$, we can deduce out below <font color="DeepSkyBlue">properties</font>:  
>&#10112;$P(A\vert C)$+$P(A^{c}\vert C)$=$1$, holds for all conditions.  
>&#10113;if $A\cap C$=$0$, then $P(A\vert C)$=$0$.  
>&#10114;if $C\subset A$, then $A\cap C$=$C$, $P(A\vert C)$=$1$.  
>&#10115;if $A\subset C$, then $A\cap C$=$A$, $P(A\vert C)$=$\frac {P(A)}{P(C)}\ge P(A)$, since $P(C)\le 1$.  

### <font color="RoyalBlue">Example</font>: Illustration By Tossing A Fair Die
>Suppose you are tossing a fair die, the sample space $\Omega$=$\\{1,2,3,4,5,6\\}$.  We denote the event of numbers smaller than $3$ as $A$=$\\{1,2\\}$, and denote the event of even numbers as $B$=$\\{2,4,6\\}$.  
>&#10112;if we know the current rolled out number is even, what's the probability the number is smaller than $3$?  
>$P(A\vert B)$=$\frac {P(A\cap B)}{P(B)}$=$\frac {\frac {1}{6}}{\frac {1}{2}}$=$\frac {1}{3}$,  
>where $P(A\cap B)$=$P(\\{2\\})$=$\frac {1}{6}$.  
>&#10113;if we know the rolled out number is smaller than $3$, what's the probability the number is even?  
>$P(B\vert A)$=$\frac {P(B\cap A)}{P(A)}$=$\frac {\frac {1}{6}}{\frac {1}{3}}$=$\frac {1}{2}$.  

### <font color="RoyalBlue">Example</font>: Illustration By Fuel Residence Time
>Given a engine full of chemical fuel in its combustion chamber and just starts, we denote the event that the particle is left as <font color="OrangeRed">non-comleted chemical reaction state after t seconds</font> as $R_{t}$.  
>
>Suppose the probability of such chemical reaction is in [exponential distribution]({{ site.github.repo }}{{ site.baseurl }}/2018/01/24/intro-exp-dist/), the probability of $R_{t}$, $P(R_{t})$=$e^{-t}$.   
>
>Then, <font color="DeepSkyBlue">the probability of the particle stay over 4 seconds will stay over 5 seconds</font> would be to ask for <font color="DeepSkyBlue">$P(R_{5}\vert R_{4})$</font>.  
>&#10112;$R_{4}$=$e^{-4}$  
>&#10113;$R_{5}$=$e^{-5}$  
>&#10114;since <font color="DeepPink">$R_{5}\subset R{4}$</font>, we have <font color="DeepPink">$R_{5}\cap R_{4}$=$R_{5}$</font>.  
>Therefore, $P(R_{5}\vert R_{4})$=$\frac {P(R_{5}\cap R_{4})}{P(R_{4})}$=$\frac {P(R_{5})}{P(R_{4})}$=$e^{-1}$.  

### The <font color="Red">Probability Chaining Rule</font>
>The probability chaining rule has it that:  
>&#10112;$P(A\cap C)=P(A\vert C)\cdot P(C)$  
>&#10113;$P((A\cap B)\vert C)$=$P(A\vert (B\cap C))\cdot P(B\vert C)$  
>&#10114;$P(A\cap B\cap C)$=$P(A\vert (B\cap C))\cdot P(B\vert C)\cdot P(C)$  
>
><font color="Brown">proof::mjtsai1974</font>  
>&#10112;begin from the conditional probability:  
>$P(A\vert C)$=$\frac {P(A\cap C)}{P(C)}$  
>$\Leftrightarrow P(A\cap C)=P(A\vert C)\cdot P(C)$  
>&#10113;$P((A\cap B)\vert C)$  
>=$\frac {P((A\cap B)\cap C)}{P(C)}$  
>=$\frac {P(A\cap (B\cap C))}{P(C)}$  
>=$\frac {P(A\vert (B\cap C))\cdot P(B\cap C)}{P(C)}$  
>=$P(A\vert (B\cap C))\cdot P(B\vert C)$  
>&#10114;from above,  
>$\frac {P((A\cap B)\cap C)}{P(C)}$=$P(A\vert (B\cap C))\cdot P(B\vert C)$  
>$\Leftrightarrow P(A\cap B\cap C)$=$P(A\vert (B\cap C))\cdot P(B\vert C)\cdot P(C)$  
>
>Also known as <font color="DeepSkyBlue">the multiplication rule</font>.  
>Below expression illustrates <font color="Red">probability chaining rule</font> <font color="DeepSkyBlue">extension</font>:  
>$P(N_{1}\cap N_{2}\cap N_{3}\cap ...\cap N_{m})$  
>=$P(N_{1}\vert (N_{2}\cap N_{3}\cap ...\cap N_{m}))\cdot P(N_{2}\vert (N_{3}\cap ...\cap N_{m}))\cdot ...\cdot P(N_{m-1}\vert N_{m})\cdot P(N_{m})$  

### <font color="RoyalBlue">Example</font>: Illustration By Fuel Residence Time For <font color="DeepSkyBlue">Extension</font>
>If we are given the same condition to the engine containing a combustion chamber in it, we'd like to estimate <font color="OrangeRed">the probability of the particle stay over 1 seconds will stay over 10 seconds</font>.  
>
><font color="OrangeRed">Suppose the chemical particle still left at 10-th second is the final one molecular</font>, and the probability of such chemical reaction is in [exponential distribution]({{ site.github.repo }}{{ site.baseurl }}/2018/01/24/intro-exp-dist/), the probability of $R_{t}$, $P(R_{t})$=$e^{-t}$.
>
><font color="Brown">proof::mjtsai1974</font>  
>This is to ask for $P(R_{10}\vert R_{1})$=$\frac {P(R_{10}\cap R_{1})}{P(R_{1})}$.  
>&#10112;by the given assumption, the final particle is in $R_{10}$, it just passed through $R_{1}$,$R_{2}$,...,$R_{10}$.  
>Hence, $(R_{10}\cap R_{1})$=$(R_{10}\cap R_{9}\cap ... \cap R_{1})$  
>&#10113;by the <font color="OrangeRed">probability chaining rule</font>,  
>$P(R_{10}\cap R_{9}\cap ... \cap R_{1})$  
>=$P(R_{10}\vert (R_{9}\cap ... \cap R_{1}))$  
>$\;\;\;\;\cdot P(R_{9}\vert (R_{8}\cap ... \cap R_{1}))$  
>$\;\;\;\;\cdot P(R_{8}\vert (R_{7}\cap ... \cap R_{1}))$  
>$\;\;\;\;...$  
>$\;\;\;\;\cdot P(R_{3}\vert (R_{2}\cap R_{1}))$  
>$\;\;\;\;\cdot P(R_{2}\vert R_{1})$  
>$\;\;\;\;\cdot P(R_{1})$  
>&#10114;with each multiplication term equaling to $e^{-1}$,  
>$P(R_{10}\cap R_{9}\cap ... \cap R_{1})$=$e^{-10}$  
>then, $P(R_{10}\vert R_{1})$=$\frac {P(R_{10}\cap R_{1})}{P(R_{1})}$=$e^{-9}$.  

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