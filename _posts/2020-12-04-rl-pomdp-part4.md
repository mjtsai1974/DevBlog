---
layout: post
title: Partial Observable Markov Decision Process - Part 4
---

## Prologue To Partial Observable Markov Decision Process - Part 4
<p class="message">
This post will explain why <font color="Red">PWLC</font> works and how it is aggregated in value iteration of <font color="Red">POMDP</font>(Partial Observable Markov Decision Process).  
</p>

### Recap <font color="Red">POMDP</font> Value Iteration
>* Basic idea in <font color="Red">POMDP</font> value iteration  
>&#10112;calculate value function vectors for each action with regard to observation thus made in horizon $1$.  
>&#10113;continue looking forward horizon $2$,$3$,...  
>&#10114;make such value iteration until convergence  
>
>* The <font color="Red">PWLC</font>(piecewise linear convex)  
>The value function of <font color="Red">POMDP</font> can be represented as <font color="MediumSpringGreen">max of linear segments - <font color="Red">PWLC</font></font>.  
>$\left(1\right)$convexity:  
>>state is known at the edges of belief space  
>$\left(2\right)$linear segments:  
>>&#10112;linear function in the format of belief $\times$ reward  
>>&#10113;segments in horizon 1 are linear  
>>&#10114;<font color="MediumSpringGreen">segments in horizon $n$ are linear combination of horizon $n-1$'s segments</font>  

### <font color="RoyalBlue">Why And How <font color="Red">PWLC</font> Works?</font>
>In this section, I am going to lead you to the reason to why <font color="Red">PWLC</font> takes effect, and guide you through the way it is aggregated to a <font color="DeepSkyBlue">convergence</font>.  
>

### Addendum
>&#10112;[Partial Observable Markov Decision Process, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4677668675/concepts/46822685970923)  
>&#10113;[POMDP Value Iteration Example, Tony, Brown University's Computer Science Department](http://cs.brown.edu/research/ai/pomdp/tutorial/pomdp-vi-example.html)  
>&#10114;[POMDP Tutorial, Stefan Kopp, Bielefeld University](https://www.techfak.uni-bielefeld.de/~skopp/Lehre/STdKI_SS10/POMDP_tutorial.pdf)  
>&#10115;[Partially Observable Markov Decision Process, Geoff Hollinger, 2007 fall](https://www.cs.cmu.edu/~ggordon/780-fall07/lectures/POMDP_lecture.pdf)    
>&#10116;[POMDPOs, Rowan McAllister and Alexandre Navarro, MLG Reading Group, 02 June 2016, Cambridge University](http://cbl.eng.cam.ac.uk/pub/Intranet/MLG/ReadingGroup/pomdp.pdf)  

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
<!-- \left|X\right| -->
<!-- \xrightarrow{r_t} -->
<!-- \left\|?\right\| => ||?|| -->
<!-- \left|?\right| => |?| -->
<!-- \left(?\right) => (?) -->
<!-- \lbrack BQ\rbrack => [BQ] -->
<!-- \subset -->
<!-- \subseteq -->
<!-- \widehat -->
<!-- \left\langle1,2,3\right\rangle => <1,2,3> -->
<!-- \because -->
<!-- \therefore -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus, mathematic expression</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha, quiz, example</font> -->
<!-- <font color="Green">new alpha</font> -->
<!-- <font color="Aqua">new alpha</font> -->
<!-- <font color="AquaMarine">new alpha</font> -->
<!-- <font color="MediumSpringGreen">new alpha</font> -->

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

<!-- <font color="Brown">Notes::mjtsai1974</font> -->

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!--
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Why at this moment, the Poisson and exponential probability come out with different result?</font>  
-->

<!-- http://www.html-color-names.com/ -->
<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->