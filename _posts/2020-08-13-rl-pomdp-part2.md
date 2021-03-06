---
layout: post
title: Partial Observable Markov Decision Process - Part 2
---

## Prologue To Partial Observable Markov Decision Process - Part 2
<p class="message">
This post will make a full illustration of belief update in <font color="Red">POMDP</font>(Partial Observable Markov Decision Process).  
</p>

### <font color="OrangeRed">The Real World Is Almost Partially Observable</font>
>* Regular MDP  
>When we are in the regular MDP, the agent observes the state of the environment, it can make full observation.  The chess grid and the 2 states examples exhibit the environment of the regular MDP.  
>&#10112;[Markov Decision Process In Stochastic Environment]({{ site.github.repo }}{{ site.baseurl }}/2017/12/03/mdp-markov-decision-process-stochastic-env/)  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-grid.png "Grid MDP")
>&#10113;[Markov Decision Process To Seek The Optimal Policy]({{ site.github.repo }}{{ site.baseurl }}/2017/12/04/mdp-markov-decision-process-optimal-policy/)  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-12-03-mdp-markov-decision-process-stochastic-env-2-states.png "2 states MDP")
>
>* <font color="Red">Partially Observable MDP</font>  
>If we are <font color="RosyBrown">in the partially observable environment, the agent can't observe the full world state, but the observation gives hint about true state</font>.  
>&#10112;the agent has no idea about the world state, what's behind the door, where am I.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-intuition.png "world state")
>&#10113;the agent don't know what state he is in if he didn't get reward after taking action.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-2-way-hallway.png "what state")
>
>* Types of partial observability  
>&#10112;the sensor(some component of the agent) might have measurement fail due to <font color="OrangeRed">noise</font>.  
>&#10113;multiple states might give the same observation, i.e., what's behind the door, what state the agent is in after taking action without reward.  

### <font color="OrangeRed">Policies Under POMDP?</font>
><font color="RoyalBlue">[Question]</font>  
>Should we use policy mapping state to action in POMDP?  
>
><font color="DeepSkyBlue">[Answer]</font>  
>Before we step any further, it strikes on our head that:  
>&#10112;the agent only gets some(partial) observations  
>&#10113;<font color="RosyBrown">no more Markovian signal(the state) directly available to the agent</font>  
>
>We should <font color="DeepPink">use all information obtained, the full history of observations</font>, by doing the <font color="Red">belief update</font>.  

### Hints On <font color="Red">Belief Update</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Calculation</font>  
>POMDP is often given an initial belief:  
>&#10112;we are given an initial probability distribution over states in the departure point.  
>&#10113;we shhould keep track of how this initial probability distribution over states changes from initial point to the next step.  
>&#10114;by the already known prior belief $b$, the action taken $A$, the observation thus made $O$, to figure out the new next belief $b^{\'}$.  
>
>This process is called the <font color="Red">belief update</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Apply the Bayer's rule</font>  
>&#10112;begin from the <font color="Red">Bayes Theorem</font>:  
>$P(B\vert A)$=$\frac {P(A\vert B)\cdot P(B)}{P(A)}$  
>&#10113;substitute the relevant variables:  
>$P(S^{\'}\vert O)$=$\frac {P(O\vert S^{\'})\cdot P(S^{\'})}{P(O)}$  
>&#10114;<font color="DeepSkyBlue">add the action $A$ and prior belief $b$ in the given:</font>  
>$P(S^{\'}\vert O,A,b)$=$\frac {P(O\vert S^{\'},A,b)\cdot P(S^{\'}\vert A,b)}{P(O\vert A,b)}$  
>&#10115;expand $P(S^{\'}\vert A,b)$ and $P(O\vert A,b)$  
>$P(S^{\'}\vert O,A,b)$  
>=$\frac {P(O\vert S^{\'},A,b)\cdot P(S^{\'}\vert A,b)}{P(O\vert A,b)}$  
>=$\frac {P(O\vert S^{\'},A,b)\cdot \sum_{S}P(S^{\'}\vert A,S)\cdot b(S)}{\sum_{S^{\'\'}}P(O|S^{\'\'})\cdot\sum_{S}P(S^{\'\'}|A,S)\cdot b(S)}$  

### Full Illustration Of <font color="Red">Belief Update</font> In Tiger Problem
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The tiger problem</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-problem.png "tiger problem")
>* The given condition  
>&#10112;suppose you(the agent) are standing in front of 2 doors, there is a tiger behind one of the 2 doors, that is to say the <font color="OrangeRed">world states</font> are tiger is behind the left or right door.  
>&#10113;there are 3 actions, listen, open left door and open right door.  
>&#10114;listen is not free and might get inaccurate information.  
>&#10115;when you open the wrong door, you will get eaten by tiger, the reward is $-100$.  
>&#10116;if you open the right door, you will get $+10$ as the reward.  
>&#10117;you will get $-1$ after each listen.  
>
>* Transitive probability  
>&#10112;by listening, the tiger stays where it is.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-tran-listen.png "listen transitivity")
>&#10113;when you open the left door, the tiger has $50%$ to stay behind the left door, or $50%$ to stay behind the right door.
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-tran-open-left.png "open left transitivity")  
>&#10114;when you open the right door, the tiger has $50%$ to stay behind the right door, or $50%$ to stay behind the left door.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-tran-open-right.png "open right transitivity")
>
>* Observation and its probability  
>&#10112;when listening, if the world state is tiger left, by this given, we hear tiger left, such probability is <font color="OrangeRed">[a]</font>$P(HL\vert TL,listen,b)$=$0.85$, while we still have <font color="OrangeRed">[b]</font>$P(HR\vert TR,listen,b)$=$0.15$ for we hear tiger right, given that tiger is right(we think tiger is right) under the world state tiger left.  
>The probability <font color="OrangeRed">[c]</font>$P(HR\vert TR,listen,b)$=$0.85$ for we hear tiger right, given that the world state is tiger right, while there exists probability <font color="OrangeRed">[d]</font>$P(HL\vert TL,listen,b)$=$0.15$ for we hear tiger left, given that tiger is left under the world state tiger right.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-obs-listen.png "listen obs")
>&#10113;when opening the left door, below exhibits the observation probability given the world state is tiger left and right respectively.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-obs-open-left.png "open left obs")
>&#10114;when opening the right door, below exhibits the observation probability given the world state is tiger left and right respectively.    
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-obs-open-right.png "open right obs")
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">What decision should we make?</font>  
>Before we make a decision to open the correct door, we should have gathered sufficient information pertaining to the possible changes of probability distribution of tiger's location, that's to keep track of the belief history.  
>
><font color="#C20000">Reinforcement learning is to learn the model and planning.</font>  
>
>Suppose the model is of no question in this example of tiger problem, we need to maintain a list of all possibilities of the belief changes, such history is build by listening in each step.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="Brown">Belief update::mjtsai1974</font>  
>By listening in each step, we can gather information of tiger location, that's the belief, based on history of such belief, we can then have a plan, i.e, the action to take after HL$\rightarrow$HL, HL$\rightarrow$HR.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-b-upd.png "b upd")
>
>* Begin from initial point  
>We are given the tiger is at left and right with each probability $50%$ respectively, that's $b_{0}\lbrack 0.5\;0.5\rbrack$, the first $0.5$ is the probability for tiger at left side, the similarity for tiger at the right side.  
>
>* From init$\rightarrow$<font color="OrangeRed">HL</font>  
>Given that you are hearning tiger left, we'd like to calculate the belief at this moment.  
>&#10112;$b_{1}(TL)$  
>=$P(TL\vert HL,listen,b_{0})$  
>=$\frac {P(HL\vert TL,listen,b_{0})\cdot P(TL\vert listen,b_{0})}{P(HL\vert listen,b_{0})}$  
>=$\frac {P(HL\vert TL,listen,b_{0})\cdot\sum_{S}P(TL\vert listen,S)\cdot b_{0}(S)}{\sum_{S^{\'\'}}P(HL\vert listen,S^{\'\'})\cdot\sum_{S^{\'}}P(S^{\'\'}\vert listen,S^{\'})\cdot b_{0}(S^{\'})}$  
>=$\frac {0.85\cdot(1\cdot 0.5+0\cdot 0.5)}{0.85\cdot(1\cdot 0.5+0\cdot 0.5)+0.15\cdot(1\cdot 0.5+0\cdot 0.5)}$  
>=$0.85$  
>$\Rightarrow$We are now asking for belief state of tiger left, given that we are hearing left, thus the likeli should be the probability that we hear tiger left given that tiger is left, multiply by probability of tiger left, given from the prior belief state of tiger left(and by listen), divided by the total probability that we make the observation of hearing tiger left.  
>$\Rightarrow$The total probability of hearing tiger left is summing over all states($S^{\'\'}$), the probability of hearing tiger left given that the tiger state is $S^{\'\'}$, in turn multiply by summing over the state $S^{\'}$, the transitive probabilities from $S^{\'}$ to $S^{\'\'}$ by listening, finally multiply with the prior belief, the probability that the world state is $S^{\'}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-init-hl-b1tl.png "b-upd")
>&#10113;$b_{1}(TR)$  
>=$P(TR\vert HR,listen,b_{0})$  
>=$\frac {P(HR\vert TR,listen,b_{0})\cdot P(TR\vert listen,b_{0})}{P(HR\vert listen,b_{0})}$  
>=$\frac {P(HR\vert TR,listen,b_{0})\cdot\sum_{S}P(TR\vert listen,S)\cdot b_{0}(S)}{\sum_{S^{\'\'}}P(HR\vert listen,S^{\'\'})\cdot\sum_{S^{\'}}P(S^{\'\'}\vert listen,S^{\'})\cdot b_{0}(S^{\'})}$  
>=$\frac {0.15\cdot(0\cdot 0.5+1\cdot 0.5)}{0.15\cdot(0\cdot 0.5+1\cdot 0.5)+0.85\cdot(0\cdot 0.5+1\cdot 0.5)}$  
>=$0.15$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-init-hl-b1tr.png "b-upd")
>$\Rightarrow$we have belief updated from $b_{0}$ to $b_{1}\lbrack 0.85\;0.15\rbrack$ in this brach.  
>
>* From init$\rightarrow$<font color="OrangeRed">HR</font>  
>Given that you are hearning tiger right, we'd like to calculate the belief at this moment.  
>&#10112;$b_{1}(TL)$  
>=$P(TL\vert HL,listen,b_{0})$  
>=$\frac {0.15\cdot(1\cdot 0.5+0\cdot 0.5)}{0.15\cdot(1\cdot 0.5+0\cdot 0.5)+0.85\cdot(1\cdot 0.5+0\cdot 0.5)}$  
>=$0.15$  
>&#10113;$b_{1}(TR)$  
>=$P(TR\vert HR,listen,b_{0})$  
>=$\frac {0.85\cdot(0\cdot 0.5+1\cdot 0.5)}{0.85\cdot(0\cdot 0.5+1\cdot 0.5)+0.1\cdot(0\cdot 0.5+1\cdot 0.5)}$  
>=$0.85$  
>$\Rightarrow$we have belief updated from $b_{0}$ to $b_{1}\lbrack 0.15\;0.85\rbrack$ in this brach.  
>
>* From init$\rightarrow$HL$\rightarrow$<font color="OrangeRed">HL</font>  
>Suppose that you are hearning tiger left after hearing tiger left, we'd like to calculate the belief at this moment.  
>&#10112;$b_{2}(TL)$  
>=$P(TL\vert HL,listen,b_{1})$  
>=$\frac {0.85\cdot(1\cdot 0.85+0\cdot 0.15)}{0.85\cdot(1\cdot 0.85+0\cdot 0.15)+0.15\cdot(1\cdot 0.15+0\cdot 0.85)}$  
>=$0.967986$  
>$\approx 0.97$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-init-hl-b1tl-b2tl.png "b-upd")
>&#10113;$b_{2}(TR)$  
>=$P(TR\vert HR,listen,b_{1})$  
>=$\frac {0.15\cdot(0\cdot 0.85+1\cdot 0.15)}{0.15\cdot(0\cdot 0.85+1\cdot 0.15)+0.85\cdot(0\cdot 0.15+1\cdot 0.85)}$  
>=$0.03020$  
>$\approx 0.03$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-init-hl-b1tl-b2tr.png "b-upd")
>$\Rightarrow$we have belief updated from $b_{1}\lbrack 0.85\;0.15\rbrack$ to $b_{2}\lbrack 0.97\;0.03\rbrack$ in this brach.  
>
>* From init$\rightarrow$HL$\rightarrow$<font color="OrangeRed">HR</font>  
>Suppose that you are hearning tiger left after hearing tiger right, we'd like to calculate the belief at this moment.  
>&#10112;$b_{2}(TL)$  
>=$P(TL\vert HL,listen,b_{1})$  
>=$\frac {0.15\cdot(1\cdot 0.85+0\cdot 0.15)}{0.15\cdot(1\cdot 0.85+0\cdot 0.15)+0.85\cdot(1\cdot 0.15+0\cdot 0.85)}$  
>=$0.5$  
>&#10113;$b_{2}(TR)$  
>=$P(TR\vert HR,listen,b_{1})$  
>=$\frac {0.85\cdot(0\cdot 0.85+1\cdot 0.15)}{0.85\cdot(0\cdot 0.85+1\cdot 0.15)+0.15\cdot(0\cdot 0.15+1\cdot 0.85)}$  
>=$0.5$  
>$\Rightarrow$we have belief updated from $b_{1}\lbrack 0.85\;0.15\rbrack$ to $b_{2}\lbrack 0.5\;0.5\rbrack$ in this brach.  
><font color="Brown">Notes::mjtsai1974</font>  
>The likeli in the nominator is goint to use the belief distribution at the node which it is branching from as the prior.  
>
>* From init$\rightarrow$HR$\rightarrow$<font color="OrangeRed">HL</font>  
>Suppose that you are hearning tiger left after hearing tiger right, we'd like to calculate the belief at this moment.  
>&#10112;$b_{2}(TL)$  
>=$P(TL\vert HL,listen,b_{1})$  
>=$\frac {0.85\cdot(1\cdot 0.15+0\cdot 0.85)}{0.85\cdot(1\cdot 0.15+0\cdot 0.85)+0.15\cdot(1\cdot 0.85+0\cdot 0.15)}$  
>=$0.5$  
>&#10113;$b_{2}(TR)$  
>=$P(TR\vert HR,listen,b_{1})$  
>=$\frac {0.15\cdot(0\cdot 0.15+1\cdot 0.85)}{0.15\cdot(0\cdot 0.15+1\cdot 0.85)+0.85\cdot(0\cdot 0.85+1\cdot 0.15)}$  
>$0.5$  
>$\Rightarrow$we have belief updated from $b_{1}\lbrack 0.15\;0.85\rbrack$ to $b_{2}\lbrack 0.5\;0.5\rbrack$ in this brach.  
>
>* From init$\rightarrow$HR$\rightarrow$<font color="OrangeRed">HR</font>  
>Suppose that you are hearning tiger right after hearing tiger right, we'd like to calculate the belief at this moment.  
>&#10112;$b_{2}(TL)$  
>=$P(TL\vert HL,listen,b_{1})$  
>=$\frac {0.15\cdot(1\cdot 0.15+0\cdot 0.85)}{0.15\cdot(1\cdot 0.15+0\cdot 0.85)+0.85\cdot(1\cdot 0.85+0\cdot 0.15)}$  
>$\approx 0.03$  
>&#10113;$b_{2}(TR)$  
>=$P(TR\vert HR,listen,b_{1})$  
>=$\frac {0.85\cdot(0\cdot 0.15+1\cdot 0.85)}{0.85\cdot(0\cdot 0.15+1\cdot 0.85)+0.15\cdot(0\cdot 0.85+1\cdot 0.15)}$  
>=$\approx 0.97$  
>$\Rightarrow$we have belief updated from $b_{1}\lbrack 0.15\;0.85\rbrack$ to $b_{2}\lbrack 0.03\;0.97\rbrack$ in this brach.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Have a tea break before opening the door</font>  
>Making <font color="Red">belief update</font> over theses steps, we can do some plan on the belief histroy, <font color="RoyalBlue">if we make continuous 2 observations of hearing tiger left</font>, the belief would be the probability distribution over tiger left and tiger right, which is $b_{2}\lbrack 0.97\;0.03\rbrack$.  <font color="RoyalBlue">Should we open the right door??</font>  
>
>The ideal answer would be discusssed in my next article.  
>
><font color="DeepSkyBlue">[5]</font>
><font color="OrangeRed">Make extra one step</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-b-upd-2.png "b upd conti")
>* From init$\rightarrow$HL$\rightarrow$HL$\rightarrow$<font color="OrangeRed">HL</font>  
>Guess what, if we keep on following in this path, from init to hearning tiger left, next to hearing tiger left, next to hearing tiger left, we'd like to make the belief update at this moment.  
>&#10112;$b_{3}(TL)$  
>=$P(TL\vert HL,listen,b_{2})$  
>=$\frac {0.85\cdot\lbrack(1\cdot 0.97+0\cdot 0.03)+(1\cdot 0.5+0\cdot 0.5)\rbrack}{0.85\cdot\lbrack(1\cdot 0.97+0\cdot 0.03)+(1\cdot 0.5+0\cdot 0.5)\rbrack+0.15\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.03+0\cdot 0.97)\rbrack}$  
>$\approx 0.94$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-init-hl-hl-hl-b3tl.png "b-upd")
>&#10113;$b_{3}(TR)$  
>=$P(TR\vert HR,listen,b_{2})$  
>=$\frac {0.15\cdot\lbrack(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)\rbrack}{0.15\cdot\lbrack(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)\rbrack+0.85\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack}$  
>$\approx 0.06$  
>$\Rightarrow$we have belief updated from $b_{2}\lbrack 0.97\;0.03\rbrack$ to $b_{3}\lbrack 0.94\;0.06\rbrack$ in this brach.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-init-hl-hl-hl-b3tr.png "b-upd")
>
>* From init$\rightarrow$HL$\rightarrow$HL$\rightarrow$<font color="OrangeRed">HR</font>  
>Go from init to hearning tiger left, next to hearing tiger left, next to hearing tiger right, we'd like to make the belief update at this moment.  
>&#10112;$b_{3}(TL)$  
>=$P(TL\vert HL,listen,b_{2})$  
>=$\frac {0.15\cdot\lbrack(1\cdot 0.97+0\cdot 0.03)+(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.03+0\cdot 0.97)\rbrack}{0.15\cdot\lbrack(1\cdot 0.97+0\cdot 0.03)+(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.03+0\cdot 0.97)\rbrack+0.85\cdot(1\cdot 0.5+0\cdot 0.5)}$  
>=$0.3463$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-init-hl-hl-hr-b3tl.png "b-upd")
>&#10113;$b_{3}(TR)$  
>=$P(TR\vert HR,listen,b_{2})$  
>=$\frac {0.85\cdot\lbrack(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack}{0.85\cdot\lbrack(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack+0.15\cdot(0\cdot 0.5+1\cdot 0.5)}$  
>=$0.9444$  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-tiger-init-hl-hl-hr-b3tr.png "b-upd")
>$\Rightarrow$The $b_{3}(TL)$+$b_{3}(TR)$ not equal to $1$, we are encounter a big problem, guess what?  <font color="DeepPink">By normalization, we can get the correct answer.</font>  
>&#10114;$N(b_{3}(TL))$=$\frac {0.3463}{0.3463+0.9444}$=$0.268217$  
>&#10115;$N(b_{3}(TR))$=$\frac {0.9444}{0.3463+0.9444}$=$0.73169$  
>$\Rightarrow$we have belief updated from $b_{2}\lbrack 0.97\;0.03\rbrack$ to $b_{3}\lbrack 0.27\;0.73\rbrack$ in this brach.  
>
>* From init$\rightarrow$HL$\rightarrow$HR$\rightarrow$<font color="OrangeRed">HL</font>  
>Go from init to hearning tiger left, next to hearing tiger right, next to hearing tiger left, we'd like to make the belief update at this moment.  
>&#10112;$b_{3}(TL)$  
>=$P(TL\vert HL,listen,b_{2})$  
>=$\frac {0.85\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.97+0\cdot 0.03)+(1\cdot 0.5+0\cdot 0.5)\rbrack}{0.85\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.97+0\cdot 0.03)+(1\cdot 0.5+0\cdot 0.5)\rbrack+0.15\cdot(1\cdot 0.03+0\cdot 0.97)}$  
>$\approx 0.997$  
>&#10113;$b_{3}(TR)$  
>=$P(TR\vert HR,listen,b_{2})$  
>=$\frac {0.15\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)\rbrack}{0.15\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)\rbrack+0.85\cdot(0\cdot 0.03+1\cdot 0.97)}$  
>$\approx 0.158$  
>&#10114;$N(b_{3}(TL))$=$\frac {0.997}{0.997+0.158}$=$0.863$  
>&#10115;$N(b_{3}(TR))$=$\frac {0.158}{0.997+0.158}$=$0.137$  
>$\Rightarrow$we have belief updated from $b_{2}\lbrack 0.5\;0.5\rbrack$ to $b_{3}\lbrack 0.86\;0.14\rbrack$ in this brach.  
>
>* From init$\rightarrow$HL$\rightarrow$HR$\rightarrow$<font color="OrangeRed">HR</font>  
>Go from init to hearning tiger left, next to hearing tiger right, next to hearing tiger right, we'd like to make the belief update at this moment.  
>&#10112;$b_{3}(TL)$  
>=$P(TL\vert HL,listen,b_{2})$  
>=$\frac {0.15\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.03+0\cdot 0.97)\rbrack}{0.15\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.03+0\cdot 0.97)\rbrack+0.85\cdot\lbrack(1\cdot 0.97+0\cdot 0.03)+(1\cdot 0.5+0\cdot 0.5)\rbrack}$  
>=$0.0598194131$  
>$\approx 0.06$  
>&#10113;$b_{3}(TR)$  
>=$P(TR\vert HR,listen,b_{2})$  
>=$\frac {0.85\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack}{0.85\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack+0.15\cdot\lbrack(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)\rbrack}$  
>=$0.94$  
>$\Rightarrow$we have belief updated from $b_{2}\lbrack 0.5\;0.5\rbrack$ to $b_{3}\lbrack 0.06\;0.94\rbrack$ in this brach.  
>
>* From init$\rightarrow$HR$\rightarrow$HL$\rightarrow$<font color="OrangeRed">HL</font>  
>Go from init to hearning tiger right, next to hearing tiger left, next to hearing tiger left, we'd like to make the belief update at this moment.  
>&#10112;$b_{3}(TL)$  
>=$P(TL\vert HL,listen,b_{2})$  
>=$\frac {0.85\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.97+0\cdot 0.03)\rbrack}{0.85\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.97+0\cdot 0.03)\rbrack+0.15\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.03+0\cdot 0.97)\rbrack}$  
>$\approx 0.94$  
>&#10113;$b_{3}(TR)$  
>=$P(TR\vert HR,listen,b_{2})$  
>=$\frac {0.15\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.97+1\cdot 0.03)\rbrack}{0.15\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.97+1\cdot 0.03)\rbrack+0.85\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack}$  
>$\approx 0.06$  
>$\Rightarrow$we have belief updated from $b_{2}\lbrack 0.5\;0.5\rbrack$ to $b_{3}\lbrack 0.94\;0.06\rbrack$ in this brach.  
>
>* From init$\rightarrow$HR$\rightarrow$HL$\rightarrow$<font color="OrangeRed">HR</font>  
>&#10112;$b_{3}(TL)$  
>=$P(TL\vert HL,listen,b_{2})$  
>=$\frac {0.15\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.03+0\cdot 0.97)\rbrack}{0.15\cdot\lbrack(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.03+0\cdot 0.97)\rbrack+0.85\cdot\lbrack(1\cdot 0.97+0\cdot 0.03)+(1\cdot 0.5+0\cdot 0.5)\rbrack}$  
>$\approx 0.11$  
>&#10113;$b_{3}(TR)$  
>=$P(TR\vert HR,listen,b_{2})$  
>=$\frac {0.85\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack}{0.85\cdot\lbrack(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack+0.15\cdot(0\cdot 0.97+1\cdot 0.03)}$  
>$\approx 0.9913$  
>&#10114;$N(b_{3}(TL))$=$\frac {0.11}{0.11+0.9913}$=$0.099\approx 0.1$  
>&#10115;$N(b_{3}(TR))$=$\frac {0.9913}{0.11+0.9913}$=$0.9$  
>$\Rightarrow$we have belief updated from $b_{2}\lbrack 0.5\;0.5\rbrack$ to $b_{3}\lbrack 0.1\;0.9\rbrack$ in this brach.  
>
>* From init$\rightarrow$HR$\rightarrow$HR$\rightarrow$<font color="OrangeRed">HL</font>  
>&#10112;$b_{3}(TL)$  
>=$P(TL\vert HL,listen,b_{2})$  
>=$\frac {0.85\cdot\lbrack(1\cdot 0.03+0\cdot 0.97)+(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.97+0\cdot 0.03)\rbrack}{0.85\cdot\lbrack(1\cdot 0.03+0\cdot 0.97)+(1\cdot 0.5+0\cdot 0.5)+(1\cdot 0.97+0\cdot 0.03)\rbrack+0.15\cdot(1\cdot 0.5+0\cdot 0.5)}$  
>$\approx 0.9444$  
>&#10113;$b_{3}(TR)$  
>=$P(TR\vert HR,listen,b_{2})$  
>=$\frac {0.15\cdot\lbrack(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack}{0.15\cdot\lbrack(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)+(0\cdot 0.03+1\cdot 0.97)\rbrack+0.85\cdot(0\cdot 0.5+1\cdot 0.5)}$  
>$\approx 0.3461538$  
>&#10114;$N(b_{3}(TL))$=$\frac {0.9444}{0.94444+0.3461538}$=$0.7317\approx 0.73$  
>&#10115;$N(b_{3}(TR))$=$\frac {0.3461538}{0.94444+0.3461538}$=$0.268221\approx 0.27$  
>$\Rightarrow$we have belief updated from $b_{2}\lbrack 0.03\;0.97\rbrack$ to $b_{3}\lbrack 0.73\;0.27\rbrack$ in this brach.  
>
>* From init$\rightarrow$HR$\rightarrow$HR$\rightarrow$<font color="OrangeRed">HR</font>  
>&#10112;$b_{3}(TL)$  
>=$P(TL\vert HL,listen,b_{2})$  
>=$\frac {0.15\cdot\lbrack(1\cdot 0.03+0\cdot 0.97)+(1\cdot 0.5+0\cdot 0.5)\rbrack}{0.15\cdot\lbrack(1\cdot 0.03+0\cdot 0.97)+(1\cdot 0.5+0\cdot 0.5)\rbrack+0.85\cdot\lbrack(1\cdot 0.97+0\cdot 0.03)+(1\cdot 0.5+0\cdot 0.5)\rbrack}$  
>=$0.0598$  
>$\approx 0.06$  
>&#10113;$b_{3}(TR)$  
>=$P(TR\vert HR,listen,b_{2})$  
>=$\frac {0.85\cdot\lbrack(0\cdot 0.03+1\cdot 0.97)+(0\cdot 0.5+1\cdot 0.5)\rbrack}{0.85\cdot\lbrack(0\cdot 0.03+1\cdot 0.97)+(0\cdot 0.5+1\cdot 0.5)\rbrack+0.15\cdot\lbrack(0\cdot 0.97+1\cdot 0.03)+(0\cdot 0.5+1\cdot 0.5)\rbrack}$  
>=$0.9401$  
>$\approx 0.94$  
>$\Rightarrow$we have belief updated from $b_{2}\lbrack 0.03\;0.97\rbrack$ to $b_{3}\lbrack 0.06\;0.94\rbrack$ in this brach.  

### Belief Space
>Belief is a probability distribution over states.  
>&#10112;$\sum_{S}b(S)$=$1$  
>&#10113;for $n$ states, belief has $n-1$ degree of freedom  
>&#10114;belief lives in a $n-1$ dimensional simplex, i.e, a world of 2 states, $b(S_{0})$ is determined by the value of $b(S_{1})$, it has 1 degree of freedom.  i.e, a world of 3 states, $b(S_{i})$ is determined by the other 2 values, it has 2 degree of freedom.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-08-13-rl-pomdp-part2-b-space.png "b-space")

### Addendum
>&#10112;[Partial Observable Markov Decision Process, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4677668675/concepts/46822685970923)  
>&#10113;[Decsision Making in Intellingent Systems: POMDP, 14 April 2008, Frans Oliehoek](http://www.fransoliehoek.net/docs/pomdp-lect-b.pdf)  
>&#10114;[Intro to POMDPs, CompSci 590.2 Reinforcement Learning](http://db.cs.duke.edu/courses/fall17/cps296.2/POMDPs.pdf)  

<!-- Γ -->
<!-- \Omega -->
<!-- \cap intersection -->
<!-- \cup union -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- \vert_{0.5}^{\infty} -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- $E\lbrack X\rbrack$ -->
<!-- \overline{X_n} -->
<!-- \underset{Succss}P -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->
<!-- \lim_{t\rightarrow\infty} -->
<!-- \int_{0}^{a}\lambda\cdot e^{-\lambda\cdot t}\operatorname dt -->
<!-- \Leftrightarrow -->
<!-- \prod_{v\in V} -->
<!-- \subset -->
<!-- \subseteq -->
<!-- \varnothing -->
<!-- \perp -->
<!-- \overset\triangle= -->
<!-- \left|X\right| -->
<!-- \xrightarrow{r_t} -->
<!-- \left\|?\right\| => ||?||-->
<!-- \left|?\right| => |?|-->
<!-- \lbrack BQ\rbrack => [BQ] -->
<!-- \subset -->
<!-- \subseteq -->
<!-- \widehat -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus, mathematic expression</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha, quiz, example</font> -->
<!-- <font color="Green">new alpha</font> -->

<!-- <font color="#C20000">conclusion, finding</font> -->
<!-- <font color="DeepPink">positive conclusion, finding</font> -->
<!-- <font color="RosyBrown">negative conclusion, finding</font> -->

<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->

<!-- ### <font color="RoyalBlue">Example</font>: Illustration By Rainy And Sunny Days In One Week -->
<!-- <font color="RoyalBlue">[Question]</font> -->
<!-- <font color="DeepSkyBlue">[Answer]</font> -->

<!-- <font color="Brown">Notes::mjtsai1974</font> -->

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!--
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Why at this moment, the Poisson and exponential probability come out with different result?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->