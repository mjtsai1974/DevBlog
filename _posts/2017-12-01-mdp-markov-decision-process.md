---
layout: post
title: Markov Decision Process By Intuition
---

## Markov Decision Process By Intuition
<p class="message">
It is the approximation or expression of optimal choice in stochastic environment.  Markov Decision Process is an extension of Markov Chain.  It <font color="green">takes action</font> control between state transition.
</p>

### From Markov Chain To Markov Decision Process
>Back to have a glance at the Markov Chain, the future state value might be stablized.  We wonder about the next state from current state, and would like to estimate it out.  The estimation involves one extra consideration of <font color="red">action choice</font>.  The regularized solution would be a <font color="green">policy for each state to take its optimal action to maximize its value over horizon of some magnitude</font>.  

### The Markov Decision Process Components And Features
>&#10112;a set of states, denote it as $S$.  
>&#10113;a set of actions associated with states, denoted as $A$.  
>&#10114;state transition probability, denote as $P(S_{t+1}\left|S_t\right.,a_t)$; where the Markov property claims:  
$$P(S_{t+1}\left|S_t\right.,a_t)=P(S_{t+1}\left|S_t\right.,S_{t-1},\dots,S_0,a_t,a_{t-1},\dots,a_0)$$  
>That is to say given the current state and action, the next state is <font color="red">independent</font> of the previous states and actions.  The current state estimates all that is relevant about the world to predict what the next state will be.  
>&#10115;<font color="deeppink">immediate reward</font> of each state, denoted as $R(S)$.  Some article pertaining to MDP would treat it as the <font color="deeppink">cost</font>, which would also be used in our future illustration.  
>
>The above four items are the major components in MDP.  And from now on, we would use MDP in this article, even more, the whole dev blog, to stand for the Markov Decision Process.  
>
>MDP takes action in decision making process with a hope that it can regularize a <font color="#00ADAD">policy</font> for each state to have an optimal choice of action to <font color="red">maximize</font> its expected state value estimated over herizon of magnitude of a long term, even infinity.    
>
>In advance to involve the <font color="#00ADAD">policy</font>, it would be better for us to distinguish in between conventional planning and MDP <font color="#00ADAD">policy</font>.  

### Conventional Plan v.s. MDP <font color="#00ADAD">Policy</font>
>&#10112;a plan is either an ordered list of actions or a partially ordered set of actions, executed <font color="red">without</font> reference to the state of the environment.  
>&#10113;for conditional planing, we treat it to act differently depending on the observation about the state of the world.  
>&#10114;in MDP, it is typically to compute a whole <font color="#00ADAD">policy</font> rather than a simple plan.  
>
>A <font color="#00ADAD">policy</font> is a mapping from states to actions, whatever state you happen to start from, a policy is the best to apply now.

### <font color="#EB00EB">Stochastic</font> v.s. Deterministic
>You still ponder why to replace conventional planning with MDP <font color="#00ADAD">policy</font>, in this paragraph, we will further investigate in the differences in between <font color="#EB00EB">stochastic</font> and deterministic.  
>Below shows you an image of the appropriate discipline with respect to the desired behavior under the environment condition.  For planning under uncertainty, we intend to refer to MDP or POMDP(PO means partial observable, would be discussed in another article), for learning, planning under under uncertainty, we will step into the reinforcement learning, still in another article.   

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-01-mdp-markov-decision-process-plan-under-uncertainty.png "planning under uncertainty")

>Next to make a unique identity of <font color="#EB00EB">stochastic</font> and determninistic.  
>&#10112;<font color="#EB00EB">stochastic</font> is an environment where the outcome of an action is somewhat random, that means, the execution result <font color="red">might not</font> go as well as you have expected.  
>&#10113;determninistic is an environment where the outcome of an action is predictable and always the same, that means the execution result would go as well as you have expected.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-01-mdp-markov-decision-process-stochastic-deterministic.png "stochastic v.s. deterministic")

>For the discipline of MDP, we are <font color="#6100A8">full observable</font> under <font color="#EB00EB">stochastic</font> environment.  Actually, full observable is impossible, we just believe that the design or hypothesis on the experimental environment is under the full control, but, anything out of the imagination would just errupt.  More precisely, we should treat almost every issue under <font color="#FFAC12">partial observable</font>, and it would be the domain of POMDP(Partial Observable Markov Decision Process), discussed in another article in my dev blog.  At this moment, focus on MDP only and hypnotize ourself that we have control everything.  
>
>At the end of this section, I would like to get you a clear expression of <font color="#EB00EB">stochastic</font> versus deterministic.  Given below diagram of three states, with each state has two actions. The left side reveals the deterministic environment, each action is taken from each state to its next state, and the execution result is the same as expected; whereas the right side exhibits the <font color="#EB00EB">stochastic</font> environment, the execution of action $A_1$ from state $S_1$ has been branched into two results by random with each has $0.5$ chance to reach next state $S_2$ and $S_3$ respectively.  This illustrates <font color="#C20000">the result of action execution in stochastic environment is random</font>.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-01-mdp-markov-decision-process-stochastic-deterministic-action-diff.png "stochastic v.s. deterministic")

<!-- Notes -->
<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#C20000">conclusion, finding</font> -->