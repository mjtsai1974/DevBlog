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
>
>It is just <font color="red">the expression of the expected sum of future possible discounted rewards</font>, where $0\leq\gamma\leq1$.  And why <font color="#D600D6">$\gamma$</font> is introduced(we already touch gamma in the article of [Markov Chain]({{ site.github.repo }}{{ site.baseurl }}/2017/12/01/mdp-markov-chain/))?  
>&#10112;if we add up all rewards out into infinity, then, sums might be infinite, but, this is not the ordinary case.  
>&#10113;by such design, a <font color="#D600D6">discount factor $\gamma$</font> could speed up the agent to get rewards sooner rather than later.  
>&#10114;the <font color="#D600D6">$\gamma$</font> decays the <font color="#9300FF">future rewards</font>; it is a kind of alternative to specify the <font color="#9300FF">costs(rewards)</font>.  
>
>So, we are ready to state <font color="Red">the actual objective of an MDP is to minimize not just the momentary cost(or maximize the momentary reward, in other words), but the sum of future rewards would be the optimized target</font>!!

### The Optimal Value Function
>Succeeding to the expression of the expected sum of future possible discounted rewards, to get the <font color="#00ADAD">optimal policy</font>, we need to further refine the <font color="red">state value function</font> so that it would be optimal for computation of <font color="#00ADAD">policy</font>:  
$$V^\pi(S)=\underset\pi E\left[\sum_{t=0}^\infty\gamma\cdot R^t\left|S_0\right.=S\right]$$  
>
>For each state $S$, <font color="red">the value function of the state is the expected sum of future discounted reward</font>, provided that <font color="#00ADAD">you execute the policy $\pi$</font>.  
>
>The way we are going to plan is that we are going to iterate and compute value function of each state, then, it will turn out for us to have a better <font color="#00ADAD">policy</font>.  This process is usually <font color="#D600D6">discounted by $\gamma$</font>, and we also add the <font color="#9300FF">reward</font> or the <font color="#9300FF">cost</font> of the starting state.  
>
>Because there are multiple actions associated with each distinct state, it's your choice to select the right action that will maximize over all possible actions, this is an equation called <font color="OrangeRed">backup</font>:  
$$V(S)\leftarrow R(S)+\underset A{max}\left[\gamma\cdot\sum_{S'}P(S'\left|S,A\right.)\cdot V(S')\right]$$
>
>The reason you see this left arrow in above expression is due to we are using a recursive algorithm to calculate the value function of each state.  By the introduction of <font color="#D600D6">discount factor gamma $\gamma$</font>, after iteration over some horizon, the Calculus just guarantees the convergence of the value function.  At that moment, we can just have below optimal value function:  
$$V(S)=R(S)+\underset A{max}\left[\gamma\cdot\sum_{S'}P(S'\left|S,A\right.)\cdot V(S')\right]$$  
>
>You can see that it is now the equal operator in the expression.  Just at this moment, we can know the optimal action from the optimal policy of each state with regards to its optimal value function.  When the equation holds true, we have what is called a <font color="Green">Bellman equality</font> or <font color="Green">Bellman equation</font>.  
>
>The <font color="Green">Bellman equation</font> contains 2 parts:  
>&#10112;$R(S)$, the reward(cost) in the state $S$.  
>&#10113;$\underset A{max}\left[\gamma\cdot\sum_{S'}P(S'\left|S,A\right.)\cdot V(S')\right]$, the maximum over all actions we could take in the state $S$, of the discounted expected optimal value of next state $S'$.  

### Value Iteration Under Stochastic Environment
>The idea behind is that in every state, we want to choose the action that maximize the value of the future.  This paragraph would lead you through the whole process still in example of the grid world.  
>
>The <font color="#EB00EB">stochastic environment</font> of grid world with the same setting and the action has the <font color="#EB00EB">stochastic outcomes</font>, where $80\%$ is the probability we can get our action of our command done, otherwise, we get left or right.  
>
>At this time, we are not forgetting the issue of <font color="#9300FF">costs</font>, we denote <font color="#9300FF">costs</font> as the award function over all possible states, below design might be an incentive to shorten the action sequence, the agent should complete as soon as possible, or the value function of each iterated state might be decreased:  
>$$R(S)=\left\{\begin{array}{c}+100,for\;M_{1,4}\\-100,for\;M_{2,4}\\-3,othewise\end{array}\right.$$
>
>Assume that the initial values are all $0$, except for $M_{1,4}=+100$, $M_{2,4}=-100$, let's try to calculate the value of $M_{3,3}$ after a <font color="OrangeRed">single backup</font>.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-04-mdp-markov-decision-process-optimal-policy-value-iterate-init.png "grid world init")

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