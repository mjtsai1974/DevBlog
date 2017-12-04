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
>But, <font color="#C20000">the action execution result might not go as well as you have expected in the stochastic environment</font>.  By our design of <font color="#EB00EB">stochastic</font> environment, we assume that:  
>&#10112;only $80\%$ chance for the <font color="#EB00EB">stochastic</font> agent to move in the direction it expects to.  
>&#10113;if there is a wall blocking, then, it would bouncce back to the prior starting point, the same cell,  with $80\%$ chance.  
>&#10114;there is a $10\%$ chance to the direction left or right perpendicular to the expected direction, that's say left or righ of $10\%$ chance respectively.  
>
>Above design is just to make the outcome random, that is <font color="#EB00EB">stochastic</font>.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-agent.png "stochastic agent")

>If the agent at $M_{3,3}$ would like to move to $M_{2,3}$, then, only $80\%$ chance to $M_{2,3}$, $10\%$ chance to $M_{3,2}$, $10\%$ chance to $M_{3,4}$.  
>
>If the agent at $M_{3,2}$ would like to move to $M_{2,2}$, then, $80\%$ chance to bounce back to $M_{3,2}$(since $M_{2,2}$ is a blocking wall), $10\%$ chance to $M_{3,1}$, $10\%$ chance to $M_{3,3}$.  
>
>Continue fo rthe illustration, if the agent at $M_{1,1}$ would like to move to north(its above), then, it will have totally $90\%$ chance to bounce back to $M_{1,1}$, wherein, $80\%$ chance bounce back from the north(above), $10\%$ chance bounce back from the left, and $10\%$ chance to $M_{1,2}$.  
>
>This is a <font color="#8400E6">stochastic state transition</font>,  so, if you planning a sequence of actions starting from $M_{3,1}$, to reach over the $+100$ at $M_{1,4}$, the final state, you might go N, N, E, E, E.  But, with our design, the stochastic agent might move east with $10%$ chance to $M_{3,2}$.  
>
>So, we wish to have a planning method that provides an answer no matter where we are, that's called a <font color="#00ADAD">policy</font>, where <font color="green">policy assigns actions to any state</font>, that is:  
>$Poicy\;\pi(S)\rightarrow A$, for each state, we have to regularize a <font color="#00ADAD">policy</font>, the planning problem now becomes finding the <font color="#00ADAD">optimal policy</font>.  

### Conventional Planning In Stochastic Environment Is Insufficient
>Suppose you are given the information space of the grid world, and would like to start from $M_{3,1}$ to reach the goal state at $M_{1,4}$.  By the conventional planning, we might create a tree diagram to construct to possible state transition, since we are now in the stochastic environment, the outcome of action execution to four directions, north, south, west, east is <font color="red">not deterministic</font>.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-plan-branching-factor.png "large branching factor")

>

<!-- Notes -->
<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#C20000">conclusion, finding</font> -->
<!-- <font color="green">conclusion, finding</font> -->