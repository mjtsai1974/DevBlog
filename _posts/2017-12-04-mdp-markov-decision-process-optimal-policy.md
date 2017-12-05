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

### <font color="Green">Value Iteration</font> Under <font color="#EB00EB">Stochastic</font> Environment Of The Grid World
>The idea behind is that in every state, we want to choose the action that maximize the value of the future.  This paragraph would lead you through the whole process still in example of the grid world.  
>
>The <font color="#EB00EB">stochastic environment</font> of grid world with the same setting and the action has the <font color="#EB00EB">stochastic outcomes</font>, where $80\%$ is the probability we can get our action of our command done, otherwise, we get left or right.  
>
>At this time, we are not forgetting the issue of <font color="#9300FF">costs</font>, we denote <font color="#9300FF">costs</font> as the award function over all possible states, below design might be an incentive to shorten the action sequence, the agent should complete as soon as possible, or the value function of each iterated state might be decreased:  
>$$R(S)=\left\{\begin{array}{c}+100,for\;M_{1,4}\\-100,for\;M_{2,4}\\-3,othewise\end{array}\right.$$
>
>Assume that the initial values are all $0$, except for $M_{1,4}=+100$, $M_{2,4}=-100$ and $\gamma=1$ for simplicity.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-04-mdp-markov-decision-process-optimal-policy-value-iterate-init.png "grid world init")

>[1]Let's try to calculate the value of $M_{1,3}$ after a <font color="OrangeRed">single backup</font>.  
>&#10112;$V(M_{1,3},E)=-3+0.8\cdot100+0.1\cdot0+0.1\cdot0=77$, for we choose east, the immediate reward of leaving $M_{1,3}$ is $-3$, and $80\%$ chance to arrive $M_{1,4}$ of reward $+100$, $10\%$ chance to bounce back to $M_{1,3}$ of reward $0$, $10\%$ chance to down to $M_{2,3}$ of reward $0$.  
>&#10113;$V(M_{1,3},W)=-3+0.8\cdot0+0.1\cdot0+0.1\cdot0=-3$, for we choose west, the immediate reward of leaving $M_{1,3}$ is $-3$, and $80\%$ chance to arrive $M_{1,2}$ of reward $0$, $10\%$ chance to bounce back to $M_{1,3}$ of reward $0$, $10\%$ chance to down to $M_{2,3}$ of reward $0$.  
>&#10114;$V(M_{1,3},N)=-3+0.8\cdot0+0.1\cdot0+0.1\cdot100=7$, for we choose north, the immediate reward of leaving $M_{1,3}$ is $-3$, and $80\%$ chance to bounce back to $M_{1,3}$ of reward $0$, $10\%$ chance to $M_{1,2}$ of reward $0$, $10\%$ chance to $M_{1,4}$ of reward $100$.  
>&#10114;$V(M_{1,3},S)=-3+0.8\cdot0+0.1\cdot0+0.1\cdot100=7$, for we choose north, the immediate reward of leaving $M_{1,3}$ is $-3$, and $80\%$ go to $M_{2,3}$ of reward $0$, $10\%$ chance to $M_{1,2}$ of reward $0$, $10\%$ chance to $M_{1,4}$ of reward $100$.  
>Trivially, we have $V(M_{1,3},E)=77$ the maximized value, and the east is the <font color="DeepSkyBlue">optimal action</font>.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-04-mdp-markov-decision-process-optimal-policy-value-iterate-backup-1.png "1 backup")

>[2]Suppose we are inheriting from above state, where $V(M_{1,3})=77$, what is the value of $M_{2,3}$ after still another <font color="OrangeRed">single backup</font>?  
>&#10112;$V(M_{2,3},E)=-3+0.8\cdot-100+0.1\cdot77+0.1\cdot0=-75.3$, for we choose east, the immediate reward of leaving $M_{2,3}$ is $-3$, and $80\%$ chance to arrive $M_{2,4}$ of reward $-100$, $10\%$ chance to $M_{1,3}$ of reward $77$, $10\%$ chance to down to $M_{3,3}$ of reward $0$.  
>&#10113;$V(M_{2,3},W)=-3+0.8\cdot0+0.1\cdot77+0.1\cdot0=4.7$, for we choose west, the immediate reward of leaving $M_{2,3}$ is $-3$, and $80\%$ chance to bounce back to $M_{2,3}$ of reward $0$, $10\%$ chance to $M_{1,3}$ of reward $77$, $10\%$ chance to down to $M_{3,3}$ of reward $0$.  
>&#10114;$V(M_{2,3},N)=-3+0.8\cdot77+0.1\cdot0+0.1\cdot-100=48.6$, for we choose north, the immediate reward of leaving $M_{2,3}$ is $-3$, and $80\%$ chance to arrive $M_{1,3}$ of reward $77$, $10\%$ chance to bounce back to $M_{2,3}$ of reward $0$, $10\%$ chance to down to $M_{2,4}$ of reward $-100$.  
>&#10115;$V(M_{2,3},S)=-3+0.8\cdot0+0.1\cdot0+0.1\cdot-100=-13$, for we choose south, the immediate reward of leaving $M_{2,3}$ is $-3$, and $80\%$ chance to arrive $M_{3,3}$ of reward $0$, $10\%$ chance to bounce back to $M_{2,3}$ of reward $0$, $10\%$ chance to down to $M_{2,4}$ of reward $-100$.  
>Trivially, we have $V(M_{2,3},N)=48.6$ the maximized value, and the north is the <font color="DeepSkyBlue">optimal action</font>.  Please be recalled that <font color="#C20000">hitting the wall is not the most optimal action any more, it is a major different from prior illustration!  That's because we have successfully backup a optimal value of $M_{1,3}=77$</font>.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-04-mdp-markov-decision-process-optimal-policy-value-iterate-backup-2.png "2 backups")

>We can <font color="OrangeRed">propagate</font> value <font color="OrangeRed">backwards</font> in <font color="OrangeRed">reverse order</font> of action, executing from $M_{1,4}=+100$, through this grid world and fill every every single state with a better value estimation.  If we do this, run the <font color="Green">value iteration</font> through <font color="OrangeRed">convergence</font>, then, we get the following <font color="Green">value function</font>:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-04-mdp-markov-decision-process-optimal-policy-value-iterate-converge.png "convergence")

>Below is the corresponding mapping of <font color="#00ADAD">optimal policy</font> containing an <font color="DeepSkyBlue">optimal action</font> to each distinct <font color="Red">state</font> that can <font color="OrangeRed">maximize</font> its <font color="Red">future value function</font>:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-04-mdp-markov-decision-process-optimal-policy-value-iterate-optimal-policy.png "optimal policy")

>After following up above iteration, you might be impressed with such backup process by propagating <font color="red">value function</font> in reverse order sequence of action executing from the goal state back to its previous state.  

### <font color="Green">Value Iteration</font> Under <font color="#EB00EB">Stochastic</font> Environment Of Two States World
>Next, I am going to illustrate in a more general case of <font color="#EB00EB">stochastic</font> environment containing only 2 states.  That's for the better understanding and ease of computation.  In this example, the goal state would be the estimated out target.  
>
>Suppose you are given below 2 states environment with each initialized with value function $0$, the red curve is the action you try to stay in the same state, that says you try to stop, while the blue curve is the action to move to another state:   

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-2-states.png "2 states")

>&#10112;the $S_1$ has both stop and move actions, the stop execution will have $50\%$ chance to stay, $50\%$ chance to move to $S_2$, the move action will have $100\%$ chance to reach $S_2$.  
>&#10113;the $S_2$ has both stop and move actions, the stop execution will have $100\%$ chance to stay, the move action will have $100\%$ chance to reach $S_1$.  
>&#10114;the immediate rewards are $R(S_1)=3$ and $R(S_2)=-1$.  
>Where the move action always succeeding in switching in between the 2 states, the stop action fully works only when it reaches the bad state, $R(S)=-1$.  Given $\gamma=0.5$ for a little tricky.  
>
>[1]Let's calculate the <font color="Red">value function</font> of $S_1$, beginning over here:  
>&#10112;$V(S_1,stop)=3+0.5\cdo(0.5\cdot0+0.5\cdot0)=3$, the stop action would come out with $50\%$ chance staying in the same place of reward $0$, $50\%$ chance to the $S_2$ of reward $0$.  
>&#10113;$V(S_1,move)=3+0.5\cdo(1.0\cdot0)=3$, the move action would come out with $100\%$ chance to the $S_2$ of reward $0$.  
>Trivially, $V(S_1)=3$, the optimal action of $S_1$ could not be tell at this moment, then, figure out the value function of $S_2$:  
>&#10114;$V(S_2,stop)=-1+0.5\cdo(1.0\cdot0)=-1$, the stop action would come out with $100\%$ chance to stay in $S_2$ of reward $0$.  
>&#10115;$V(S_2,move)=-1+0.5\cdo(1.0\cdot0)=-1$, the move action would come out with $100\%$ chance to the $S_1$ of reward $0$.  
>Trivially, $V(S_2)=-1$, the optimal action of $S_2$ could not be tell at this moment, either.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-2-states-value-iteration-1.png "2 states,1 backup")

>[2]The current optimal <font color="Red">value functions</font> are $V(S_1)=3$ and $V(S_2)=-1$, continue to do the <font color="Green">value iteration</font> again:  
>&#10112;$V(S_1,stop)=3+0.5\cdo(0.5\cdot3+0.5\cdot-1)=3.5$, the stop action would come out with $50\%$ chance staying in the same place of reward $3$, $50\%$ chance to the $S_2$ of reward $-1$.  
>&#10113;$V(S_1,move)=3+0.5\cdo(1.0\cdot-1)=2.5$, the move action would come out with $100\%$ chance to the $S_2$ of reward $-1$.  
>Trivially, $V(S_1)=3.5$, the optimal action of $S_1$ could be stop at this moment, then, figure out the value function of $S_2$:  
>&#10114;$V(S_2,stop)=-1+0.5\cdo(1.0\cdot-1)=-1.5$, the stop action would come out with $100\%$ chance to stay in $S_2$ of reward $-1$.  
>&#10115;$V(S_2,move)=-1+0.5\cdo(1.0\cdot3)=0.5$, the move action would come out with $100\%$ chance to the $S_1$ of reward $3$.  
>Trivially, $V(S_2)=0.5$, the optimal action of $S_2$ could be regarded as move at this moment.

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-2-states-value-iteration-2.png "2 states,2 backups")


<!-- ### <font color="Green">Value Iteration</font> Algorithm/Flow -->

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