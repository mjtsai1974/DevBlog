---
layout: post
title: Markov Decision Process To Seek The Optimal Policy
---

## Markov Decision Process To Seek The Optimal Policy

<p class="message">
We could treat MDP as the way the world works, then, <font color="#00ADAD">policy</font> would be the way the agent works.  If you take an MDP with a <font color="#00ADAD">policy</font> containing all of the actions are chosen and it would now just become a Markov Chain without action to be taken.  
Nevertheless, <font color="#C20000">a policy aims at mapping each distinct state to an optimal action maximizing the value of the state over the horizon of some magnitude or even infinity</font>.  Given a policy, it's easy to evaluate the expected value from each possible starting state by executing it. 
</p>

### The Rewards(Costs)
>If we are using the same grid world example, for the time being, we are really ignoring the issue of <font color="#9300FF">costs</font>, or some articles prefer to use the term <font color="#9300FF">rewards</font>.  The two are the same meaning in MDP.  In the real world, the moving to other location costs, like fuel, power consumption, time spends, these might be the unwanted burden, but inevitable.  
>
>Then, what is reward we are speaking of?  For example, you will get 1000\$ upon winning the championship in the swimming competition, that's the reward.  Still another example, if you are struggle to the river, by making one movement nearby to the riverside, just by leaving current far distance position, your spiritual would be encouraged, such encouragement would be the reward.  
>
>In MDP, usually, by design, when you would like to step into another state, upon leaving current state, you would be rewarded with a quantitative value.  For <font color="C20000">the cost, it is explicitly a negative reward per state</font>.  As to <font color="C20000">the reward, it might be a positive value</font>.  

### Policy Over Infinite Horizon
>The <font color="OrangeRed">criteria</font> for finding a good policy is to find <font color="#C20000">the policy that for each state, the expected reward of executing that policy is maximized, starting from that state</font>.  For <font color="OrangeRed">each state</font>, find the <font color="OrangeRed">single action</font> that <font color="OrangeRed">maximizes</font> the <font color="OrangeRed">expected rewards</font>.  
>
>In many cases, it is not very clear <font color="OrangeRed">how long</font> the process is going to run, it is often popular to move toward optimality with a <font color="#D600D6">discount factor gamma $\gamma$</font>.  The objective is to find a policy $\pi:S\rightarrow A$ that can <font color="OrangeRed">maximize</font> the given expression:  
$$E\left[\sum_{t=0}^\infty\gamma^t\cdot R_t\left|S_0\right.\right]$$  
>It is just <font color="red">the expression of the expected sum of future possible discounted rewards</font>, where $0\leq\gamma\leq1$.  And why <font color="#D600D6">$\gamma$</font> is introduced(we already touch gamma in the article of [Markov Chain]({{ site.github.repo }}{{ site.baseurl }}/2017/12/01/mdp-markov-chain/))?  
>&#10112;if we add up all rewards out into infinity, then, sums might be infinite, but, this is not the ordinary case.  
>&#10113;by such design, a <font color="#D600D6">discount factor $\gamma$</font> could speed up the agent to get rewards sooner rather than later.  
>&#10114;the <font color="#D600D6">$\gamma$</font> decays the <font color="#9300FF">future rewards</font>; it is a kind of alternative to specify the <font color="#9300FF">costs(rewards)</font>.  
>
>So, we are ready to state <font color="Red">the actual objective of an MDP is to minimize not just the momentary cost(or maximize the momentary reward, in other words), but the sum of future rewards would be the optimized target</font>!!

### The Optimal Value Function
>Succeeding to the expression of the expected sum of future possible discounted rewards, to get the optimal policy, we need to further refine the state value function so that it would be optimal for computation:  


<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
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