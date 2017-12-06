---
layout: post
title: Support Vector Machine Imperfect Separation And KKT Condition
---

## Imperfect Separation And KKT Condition

<p class="message">
How, if there exists some data points in the safeguard zone?  When we are studying the field of SVM, it is the condition never be abandoned.  This article will lead you break through the <font color="OrangeRed">noise</font> case and come out to the <font color="Red">KKT condition</font>.  
</p>

### Imperfect Separation With <font color="OrangeRed">Noise</font>
>There exists some condition that we don't strictly enfore that <font color="OrangeRed">no</font> data points in between $H_1$ and $H_2$.  We can extend SVM to allow some <font color="OrangeRed">noise</font>(data points) in between the safeguard zone.  Thus, we want to <font color="OrangeRed">penalize</font> the data points that cross the boundaries($H_1$,$H_2$).  
>In this way, by introducting $\xi\geq0$, non-negative, such that:  

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->

<!-- <font color="#C20000">positive conclusion, finding</font> -->
<!-- <font color="green">negative conclusion, finding</font> -->

<!-- <font color="Green">value iteration</font> -->
<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->
