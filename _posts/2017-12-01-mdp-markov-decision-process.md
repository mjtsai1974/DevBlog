---
layout: post
title: Markov Decision Process
---

## Markov Decision Process
<p class="message">
It is the approximation or expression of optimal choice in stochastic environment.  Markov Decision Process is an extension of Markov Chain.  It <font color="red">takes action</font> control between state transition.
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
>The above four items are the major components in MDP.  And from now on, we would use MDP in this article, even more, the whole dev blog, to stand for the Markov Decision Process.  
>MDP takes action in decision making process with a hope that it can regularize a policy for each state to have an optimal choice of action to maximize its expected state value estimated over herizon of magnitude of a long term, even infinity.    
>In advance to involve the policy, it would be better for us to distinguish in between conventional planning and MDP policy.  

### Conventional Plan v.s. MDP Policy
>