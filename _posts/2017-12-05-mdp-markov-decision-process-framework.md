---
layout: post
title: Markov Decision Process Framework
---

## Markov Decision Process Framework

<p class="message">
The MDP is quiet beautiful a framework, rather than using a single sequence of states and actions, as would be the case in the deterministic planning, now we make an entire field a so called <font color="#00ADAD">policy</font> that assigns an <font color="DeepSkyBlue">action</font> to every possible <font color="Red">state</font>.  And, we compute it using the technique of <font color="Green">value iteration</font>.
</p>

### Conclusion
>&#10112;MDP is <font color="#6100A8">full observable</font>, for each distinct state $S$, there exists actions $A$ associated with it.  
>&#10113;the execution of action in the <font color="#EB00EB">stochastic</font> environment might not go as well as you had expected, the outcome is random.  The state transition probability from state $S$ to $S'$ by action $A$ is $P(S'\left|S,A\right.)$.  
>&#10114;there exists immediate reward, $R(S)$ or cost for each state $S$.  
>&#10115;the objective is to find a policy $\pi:S\rightarrow A$ that can <font color="OrangeRed">maximize</font> the given expression:  
$$E\left[\sum_{t=0}^\infty\gamma^t\cdot R_t\left|S_0\right.\right]$$  
>&#10116;by <font color="Green">value iteration</font>, from Bellman inequality to the Bellman equality when the value function <font color="OrangeRed">converges</font>:  
$$V(S)\leftarrow R(S)+\underset A{max}\left[\gamma\cdot\sum_{S'}P(S'\left|S,A\right.)\cdot V(S')\right]$$  
$$V(S)=R(S)+\underset A{max}\left[\gamma\cdot\sum_{S'}P(S'\left|S,A\right.)\cdot V(S')\right]$$  
>&#10117;after the <font color="Green">value iteration</font> has been <font color="OrangeRed">converged</font>, we're able to define a <font color="#00ADAD">policy</font> by using the <font color="OrangeRed">argmax</font> to constraint the expected discounted future reward term in the value iteration expression:  
$$\pi(S)=\underset A{armax}\sum_{S'}P(S'\left|S,A\right.)\cdot V(S')$$
>The $A$ thus obtained is the <font color="DeepSkyBlue">optimal action</font> that maximizes the expected accumulated and discounted futured rewards of the state $S$.   

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Green">value iteration</font> -->
<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="DeepSkyBlue">optimal action</font> -->
<!-- <font color="red">value of a state</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->
<!-- <font color="#C20000">positive conclusion, finding</font> -->
<!-- <font color="green">negative conclusion, finding</font> -->
