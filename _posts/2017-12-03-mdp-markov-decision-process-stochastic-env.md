---
layout: post
title: Markov Decision Process In Stochastic Environment
---

## Markov Decision Process In Stochastic Environment
<p class="message">
MDP is a prefered framework in <font color="#EB00EB">stochastic</font> environment and we believe it is full observable.  Due to the outcome of action execution is uncertain and random, action choice should not follow conventional planning, instead, an optimal <font color="#00ADAD">policy</font>.
</p>

### Self Design Stochastic Environment
>The most frequently used example is the information space build on the grid world.  This article would just align with world's grid world for MDP.  Alternative illustration of other example would be found in later article in this dev blog.  
>Let's begin by a design of 3 by 4 matrix of grid world, $M$.  Take $M_{1,4}=+100$, $M_{2,4}=-100$ to be the terminal states with their value specified.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-grid.png "grid world example")

>To make it into MDP, we <font color="#EB00EB">assume actions are somewhar stochastic</font>.  Suppose we start from a grid cell and would like to head for the direction we intends to, the deterministic agent will always succeed to move in the direction it plans, on conditions that the target cell on that direction must be available.  
>

<!-- Notes -->
<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#C20000">conclusion, finding</font> -->
<!-- <font color="green">conclusion, finding</font> -->
