---
layout: post
title: Markov Chain(Markov Process)
---

## Markov Chain
<p class="message">
It is the approximation or expression of stochastic environment.  Markov Chain also known by Markov Process.  Cautions must be made that it is not equivalent to the Markov Decision Process, because it has <font color="red">no</font> action control.
</p>

### What Is Markov Chain?
>It consists of finite number of discrete states, probabilistic transition between states, <font color="deeppink">maybe rewards</font> of each state, and the most important is Markov Chain has <font color="red">no</font> action control.  <font color="red">No</font> action to take, just from one state to another state.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-01-mdp-markov-chain-economic-states.png "Markov Chain Economic States")

>The 3 ellipses in different colors are individual states, where the green color indicates the <font color="green">stable</font> state, the gray color stands for <font color="#545454">bubble</font> state, the red color means the <font color="red">recession</font> state.  The transition probability is along each curve with its direction by the arrow.
>You can see that no any reward found in above graph, since <font color="deeppink">the Markov Process don't always has the reward values associated with them</font>. 
>Still another example of Markov Process is exhibited below:  

