---
layout: post
title: Markov Chain(Markov Process)
---

## Markov Chain
<p class="message">
It is the approximation or expression of stochastic environment.  Markov Chain also known by Markov Process.  Cautions must be made that it is not equivalent to the Markov Decision Process, because it has <font color="red">no</font> action control.
</p>

### A Glance At The Markov Chain
>The Markov Chain consists of finite number of discrete states, probabilistic transition between states, <font color="deeppink">maybe rewards</font> of each state, and the most important is Markov Chain has <font color="red">no</font> action control.  <font color="red">No</font> action to take, just from one state to another state.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-01-mdp-markov-chain-economic-states.png "markov chain economic states")

>The 3 ellipses in different colors are individual states, where the green color indicates the <font color="green">stable</font> state, the gray color stands for <font color="#545454">bubble</font> state, the red color means the <font color="red">recession</font> state.  The transition probability is along each curve with its direction by the arrow.
>You can see that <font color="deeppink">no any reward</font> found in above graph, since <font color="deeppink">the Markov Process don't always has the reward values associated with them</font>.  
>
>Still another example of Markov Process is exhibited below, in this example, we add <font color="deeppink">immediate reward</font> on each state, R=0 for state <font color="red">1</font>, R=10 for state <font color="green">2</font>, R=0 for state <font color="blue">3</font>:  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-01-mdp-markov-chain-states-with-rewards.png "markov chain states with rewards")

>Notes that:  
>&#10112;<font color="#DB0000">the probability on all the outgoing arcs of each state sum to one</font>!  
>&#10113;the Markov Process could be constructed <font color="deeppink">with or without the reward</font> in each state, it depends on <font color="blue">artificial design</font>.
>&#10114;<font color="red">no</font> action to take, just transite from one state to another state.  

### The Markov Chain Components And Features
>The primary components of the Markov Chain:  
>&#10112;states  
>&#10113;transition probabilities  
>&#10114;rewards  
>
>The major feature is that it has <font color="red">no</font> actions to take, <font color="red">no</font> decisions to make, just transits in between states.  

### The Markov Property
>In Markov Process, <font color="#00ADAD">next state is determined only by the current state</font>, which is <font color="#00ADAD">the Markov property</font>.  

### 
