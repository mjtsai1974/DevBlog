---
layout: page
title: Introduction
---

## Preface
Hello to the world, my name is Mjtsai, abbreviated from my Chinese name Meng-Jer Tsai.  Here is the dev-blog of my engineering knowledge gain.  When I am home after work, I kick-off another
session for investigation in the fields of interests, mostly, targeting in artificial intelligence, machine learning where statistic mathematics is the prerequisite, I think really it is.
I name this place mjt&#39;s AI world with a hope that one day I can become machine learning expert.

After several years of review in below academic discipline(with period), I think they are just the prerequisite:  

[1]Calculus(2010.01 ~ 2010.12)  
[2]Linear Algebra(2008.12 ~ 2009.12)  
[3]Probability & Statistics(2011.01.01 ~ 2011.06.17, 2017.01~2017.03)  
[4]Applied Linear Regression Model(2011.06.30 ~ 2011.12.13)  
[5]Matrix Algebra(2011.12.16 ~ 2013.02.27, 2015.05.30 ~ 2016.12.31, 2017.03 ~ 2017.07)  
[6]Computer graphics, 3D transformation, rotation, quaternion(2013.07.04 ~ 2013.07.31, 2013.08.01 ~ 2013.09.18)  

During the period of time, I also do the research with [6] to dump 3D objects and animation build by Blender onto Android phone, and it works.  I can show you why and how in my dev-blog, believe
it or not, I am a part-time Blender art and can do some simple 3D design both in objects and animation. 

Before the moment I completed almost all above from [1] to [6], I just had myself involved in machine learning, by Stanford professor ANG CS221 on-line course in 2011.10.  Due to heavy duty on my daily 
job and some burden from my family, actually, I am a father of two, I left %40 of CS221 uncompleted.  At the meanwhile I think I realize some major topics in [1] to [6], usually, I made some review and
adjust in my handwritings.  It is almost the time, I resume the same course and found it a different world nowadays.  CS221 is now on [Coursera](https://www.coursera.org/learn/machine-learning).  The 
existing machine learning has become a rather evolutionary version, the deep learning.

For the time being(2017.10.24), I have completed below on-line courses and would like to further advance to deep learning:  
[1][NTU H.T.Lin's Machine Learning Foundation](https://zh-tw.coursera.org/learn/ntumlone-mathematicalfoundations)  
[2][Stanford CS221 Machine Learning of Coursera](https://www.coursera.org/learn/machine-learning)  

At the moment 2018.04.13, I have just completed the on-line course, it took me almost 6 months:  
[3][Reinforcement Learning By Georgia Tech(CS8803)](https://www.udacity.com/course/reinforcement-learning--ud600)  

Review of the major topics would be quiet complicated, you might ponder to classify it as statistics or computer science NP-hard algorithm.  Statisticians tend more to regress on already known sampling 
data, by means of mean squared error with F-test, t-test, Chi-square test to evaluate the fitness of the regression model in their hypothesis, even more, they are using likelihood ratio test to judge the 
power of each coefficient in the model.  Inevitably, Gaussian-Newton method just provides a better base point to be started in some statistic algorithm/flow to make approximation to some unknown target 
point, to be believed it just existed.

There exists a major difference in algorithm in between machine learning and statistic mathematics.  By machine learning experts' algorithm design, they intend to construct the cost function expressed in 
terms of squared error or even logistic regression much similar to traditional statistics, penalized with a regularization factor by means of lagrange multiplier, with one thing exception that most often
the coefficients in the cost function are random initialized to values closed to zero.  Finally, the target/future value might remain unknown for prediction is rather identical for both statistics and 
machine learning.

> After nurtured from above two courses, I would like to kidding myself whether I am now over fitting or still under fitting in the early stage of modern artificial intelligence.  Should I be regularized?
> How and where my direction should be head for?  Or maybe it is just a NP-hard task.

## How this dev-blog is organized?

The context of this bog just like current artificial intelligence, comes without any warranty and would be subject to change any time in the future.  It would be categorized into below major parts:

* Prerequisites
* Probability Bounds
* Machine Learning Foundation
* Bayesian Statistics And Machine Learning
* Neural Network
* Support Vector Machine(SVM) 
* Deep Learning
* Markov Decision Process(MDP)
* Partial Observable Markov Decision Process(POMDP)
* Reinforcement Learning
* Computer Graphics, 3D Rotation, Transformation and Quaternion
* Programming Language
* Implementation

### Prerequisites

Whatever topic playing the consolidated fundamental basis implicitly be constructed as computer algorithm, but explicitly help the learning flow to converge the result would be in this section, includes 
the following:

* [Hoeffding Inequality versus Chebyshev's Inequality]({{ site.github.repo }}{{ site.baseurl }}/2017/10/24/prereq-hoeffding-vs-law-large-number/)
<!-- * <a href="{{ site.github.repo }}{{ site.baseurl }}/2017/10/24/prereq-hoeffding-vs-law-large-number/">Hoeffding Inequality v.s. Law of Large Number</a> --> <!-- this also works -->
* [Lagrange Multiplier]({{ site.github.repo }}{{ site.baseurl }}/2017/10/27/prereq-lagrange-multiplier/)
* [QR Decomposition]({{ site.github.repo }}{{ site.baseurl }}/2017/10/31/prereq-qr-decomposition/)
* Cholesky Decomposition
* Spatial Value Decomposition(SVD)
* [Series Convergence]({{ site.github.repo }}{{ site.baseurl }}/2018/01/26/series-cnvg/)
* [Jacobian and Integral]({{ site.github.repo }}{{ site.baseurl }}/2017/11/16/prereq-jacobian-integral/)
* [Introduction To The Moment Generating Function]({{ site.github.repo }}{{ site.baseurl }}/2017/12/28/intro-mgf/)
* [Introduction To The Gamma Distribution]({{ site.github.repo }}{{ site.baseurl }}/2017/12/29/intro-gamma-dist/)
* [Introduction To The Beta Distribution]({{ site.github.repo }}{{ site.baseurl }}/2018/01/16/intro-beta-dist/)
* [Introduction To The Chi-Square Distribution]({{ site.github.repo }}{{ site.baseurl }}/2018/01/03/intro-chi-square-dist/)
* [Introduction To The F Distribution]({{ site.github.repo }}{{ site.baseurl }}/2018/01/05/intro-f-dist/)
* [Introduction To The t Distribution]({{ site.github.repo }}{{ site.baseurl }}/2018/01/15/intro-t-dist/)
* [Introduction To The Exponential Distribution]({{ site.github.repo }}{{ site.baseurl }}/2018/01/24/intro-exp-dist/)
* [Introduction To The Poisson Distribution]({{ site.github.repo }}{{ site.baseurl }}/2018/04/22/intro-poisson-dist/)
* [Introduction To The Poisson Process Inter-arrival Times]({{ site.github.repo }}{{ site.baseurl }}/2018/04/23/intro-poisson-dist-interarrival/)
* [Exponential versus Poisson Distribution::mjtsai1974]({{ site.github.repo }}{{ site.baseurl }}/2018/04/25/exponential-vs-poisson/)
* [The relation in between The Normal, F, Chi-Square, t, Exponential, Poisson Distributions]({{ site.github.repo }}{{ site.baseurl }}/2018/05/03/dist-relationship/)
* [Introduction To The Probability]({{ site.github.repo }}{{ site.baseurl }}/2018/05/25/intro-prob/)
* [Introduction To The Conditional Probability]({{ site.github.repo }}{{ site.baseurl }}/2018/05/25/intro-cond-prob/)
* [Event Independence versus Conditional Probability]({{ site.github.repo }}{{ site.baseurl }}/2018/05/26/evt-indep-vs-cond-prob/)
* [The Law Of Large Numbers]({{ site.github.repo }}{{ site.baseurl }}/2018/05/11/law-large-number/)
* [The Central Limit Theorem]({{ site.github.repo }}{{ site.baseurl }}/2018/05/12/central-limit-theorem/)
* [Unbiased Estimator And Random Sample]({{ site.github.repo }}{{ site.baseurl }}/2018/05/14/unbiased-estimator-random-sample/)
* Univariate Regression Model
* Multivariate Regression Model
* Degree Of Freedom(dof)
* F-test, Chi-square test, t-test and still other power test evaluation
* (Log)Likelihood Ratio Test
* Still others...

> The related posts would be new added in the future, and supposed you are comfortable with calculus and linear algebra, and a little intuition about statistics is mandatory. 

### Probability Bounds

Scientific experiments nowadays are all under sophisticated evaluation with rigorous probabilistic boundary check, thus come out with statistical guarantee on its result.  This section would guide you through 
a series of probability bounds, they all facilitate your study in learning theorem:  

* [Markov Inequality]({{ site.github.repo }}{{ site.baseurl }}/2018/02/27/prob-bound-markov-inequality/)
* [Chebyshev's Inequality]({{ site.github.repo }}{{ site.baseurl }}/2018/02/28/prob-bound-chebyshev-inequality/)
* [Chernoff Bounds]({{ site.github.repo }}{{ site.baseurl }}/2018/03/01/prob-bound-chernoff-bound/)
* [Chernoff Bounds For Normal Distribution]({{ site.github.repo }}{{ site.baseurl }}/2018/03/01/prob-bound-chernoff-bound-N/)
* [Chernoff Bounds For Rademacher Random Variable]({{ site.github.repo }}{{ site.baseurl }}/2018/03/01/prob-bound-chernoff-bound-rademacher/)
* [Jensen's Inequality]({{ site.github.repo }}{{ site.baseurl }}/2018/03/02/prob-bound-jensen-inequality/)
* [Symmetrization]({{ site.github.repo }}{{ site.baseurl }}/2018/03/05/prob-bound-symmetrization/)
* [Hoeffding Bounds]({{ site.github.repo }}{{ site.baseurl }}/2018/03/08/prob-bound-hoeffding-bound/)
* [Chernoff Bounds For Bernoulli Random Variable]({{ site.baseurl }}/2019/12/09/prob-bound-chernoff-bound-bernoulli/)
* [Chernoff Bounds For Arbitrary Random Variable]({{ site.baseurl }}/2019/12/23/prob-bound-chernoff-bound-arbitrary/)
* [Addendum]({{ site.github.repo }}{{ site.baseurl }}/2018/03/08/prob-bound-addendum/)

> The related posts would be new added in the future, the context in this section is subject to change at any time.  

### Machine Learning Foundation

After exploring in the prerequisites, you are supposed to come out with sufficient domain knowledge, next would be the following foundation in machine learning:

* Hoeffding Inequality v.s Law of Large Number
* [Gradient Descendent]({{ site.github.repo }}{{ site.baseurl }}/2017/11/07/ml-foundation-gradient-descendent/)
* [Overfitting v.s. Regularization by means of Lagrangian]({{ site.github.repo }}{{ site.baseurl }}/2017/11/11/ml-foundation-overfitting-vs-regularization/)
* [Binary and Multiple Classification]({{ site.github.repo }}{{ site.baseurl }}/2017/11/13/ml-foundation-binary-multiple-classification/)
* Principal Component Analysis(PCA by means of SVD)
* K-means Algorithm
* Collaborating Filtering Algorithm

> The related posts would be new added in the future, and supposed you are comfortable with posts in prerequisite section. 

### Bayesian Statistics And Machine Learning 

* [Introduction To The Bayes Theorem]({{ site.github.repo }}{{ site.baseurl }}/2018/05/23/bayesian-ml-intro/)
* [The Bayes Theorem Significance]({{ site.github.repo }}{{ site.baseurl }}/2018/05/28/bayesian-ml-significance/)
* [Bayes From Theorem To Practice]({{ site.github.repo }}{{ site.baseurl }}/2018/06/06/bayesian-ml-beyes-to-practice/)
* [The Bayesian Thinking]({{ site.github.repo }}{{ site.baseurl }}/2018/06/11/bayesian-ml-bayesian-think/)
* [The Bayesian Inference Exploitation]({{ site.github.repo }}{{ site.baseurl }}/2018/06/17/bayesian-ml-bayesian-inf-exploit/)
* [Introduction To The Bayesian Network]({{ site.github.repo }}{{ site.baseurl }}/2018/07/08/bayesian-ml-net-intro/)
* [The Bayesian Network Profound Meaning]({{ site.github.repo }}{{ site.baseurl }}/2018/07/11/bayesian-ml-net-profound/)
* [Variable Elimination In Bayesian Network]({{ site.github.repo }}{{ site.baseurl }}/2018/07/15/bayesian-ml-net-var-elim/)
* [Variable Elimination Order And Moral Graph]({{ site.github.repo }}{{ site.baseurl }}/2018/07/29/bayesian-ml-net-var-elim-order-moral/)
* [Propagation In The Bayesian Network]({{ site.github.repo }}{{ site.baseurl }}/2018/08/26/bayesian-ml-progagation/)
* [The Bayesian Network Propagation And Clique Tree]({{ site.github.repo }}{{ site.baseurl }}/2018/09/25/bayesian-ml-progagation-cliuque-tree/)
* [The Clique Tree Construction]({{ site.github.repo }}{{ site.baseurl }}/2018/10/14/bayesian-ml-clique-tree-construction/)
* [The Calibrated Clique Tree]({{ site.github.repo }}{{ site.baseurl }}/2018/11/12/bayesian-ml-clique-tree-calibrated/)

> The related posts would be new added in the future, and supposed you are comfortable with posts in prerequisite section. 

### Neural Networks

Neural network is the software or hardware emulation in the topology resembling to the organization of human brain.  H/W usually aims at speeding up.  S/W implementation wouldn't 
be jargon-free.  It's quite difficult to realize the backward propagation, no even think to prove it in short.  Errors in N.N lectures could be found on the [Coursera](https://www.coursera.org/learn/machine-learning).
Even the professor ANG said to us that he couldn't figure it out the proof in the on-line video.  Thanks for god, the mathematicians since the old times has left one stupid and 
efficient method, guess what?  The mathematics induction, via which, we can easily show you the way backward propagation really means and the validity of its formula.

Hard to believe, it took me over 2 days to prove backward propagation.  I will begin by model represent, then show you the way how neural network could learn and under trained by forward propagation,  followed by backward 
propagation to reduce the error cost during each distinct training in a gradient descendent alike fashion and end up with my complete proof in it.  

Below is the major items:

* [Basic Topology]({{ site.github.repo }}{{ site.baseurl }}/2017/11/19/nn-basic-topology/)
* [Feedforward Propagation]({{ site.github.repo }}{{ site.baseurl }}/2017/11/19/nn-feed-forward-propagation/)
* [Backward Propagation]({{ site.github.repo }}{{ site.baseurl }}/2017/11/20/nn-backward-propagation/)

### Sequential Minimum Optimization(SMO) To Support Vector Machine(SVM)

Support vector machine targets in binary classification with a specific safe guard distance in between the two kinds.  Both neural network and support vector machine take major weights 
in my growth in machine learning foundation after CS221 on [Coursera](https://www.coursera.org/learn/machine-learning).  It took me almost 2 weeks to summary all the details from its 
theorem to the formula deduction, finally algorithm of the real thing.

* [Prologue To Support Vector Machine]({{ site.github.repo }}{{ site.baseurl }}/2017/11/25/smo-to-svm-prologue/)
* [Initial Idea In Support Vector Machine]({{ site.github.repo }}{{ site.baseurl }}/2017/11/27/smo-to-svm-initial-idea/)
* [Imperfect Separation and The KKT condition]({{ site.github.repo }}{{ site.baseurl }}/2017/12/06/smo-to-svm-imperfect-separation-kkt/)
* [Inside Sequential Minimum Optimization]({{ site.github.repo }}{{ site.baseurl }}/2017/12/07/smo-to-svm-inside/)
* [SMO Framework And Algorithm]({{ site.github.repo }}{{ site.baseurl }}/2017/12/13/smo-to-svm-framework-algorithm/)
* [Addendum]({{ site.github.repo }}{{ site.baseurl }}/2017/12/15/smo-to-svm-addendum/)

### Deep Learning

Under construction...

### Markov Decision Process(MDP)

What's the average count of decisions you have make within every single day?  When you eat three meals a day, do you always take breakfast first, and then lunch, finally the dinner?  Do you behave in such a regular manner?  
How, if you sit up without last dinner, oversleep until noon, and you have 3 dishes on the table, what would you take?  Let me guess still the breakfast, it should be the first meal in daily life.  But, it is now almost noon,
the lunch is much newer and fresher, it should be the most optimal choice.  Then, you just wonder the less fresh breakfast might be wasted if you take lunch first, if so, you might further think last night dinner should be taken.
But, cautions must be made that it might just have deteriorated!  This information space of 3 meals a day is a little random and something exception is out of your imagination, like the food quality deterioration.

Or, when you drive to the office, does it guarantee that the shortest path get you the most efficient approach?  If you just obey the shortest path rule, and it really shorten your cost to the office, it really works, then, thank god.
Usually, you will encounter a traffic jam due to most drivers follow mobile guiding by GPS.  Even more, the car accident occurs every day.  It is stochastic in the living environment of world, you are safe to across the road upon
the green light is on, exception might not be the car breaking the red line, but the stony meteorite from the outer space strike you on your head!

That's why we need the Markov Decision process, it provides an algorithm approximating to some proportion of the stochasticity of the world.

* [Markov Chain(Markov Process)]({{ site.github.repo }}{{ site.baseurl }}/2017/12/01/mdp-markov-chain/)
* [Markov Decision Process By Intuition]({{ site.github.repo }}{{ site.baseurl }}/2017/12/01/mdp-markov-decision-process/)
* [Markov Decision Process In Stochastic Environment]({{ site.github.repo }}{{ site.baseurl }}/2017/12/03/mdp-markov-decision-process-stochastic-env/)
* [Markov Decision Process To Seek The Optimal Policy]({{ site.github.repo }}{{ site.baseurl }}/2017/12/04/mdp-markov-decision-process-optimal-policy/)
* [Value Iteration Algorithm Detail]({{ site.github.repo }}{{ site.baseurl }}/2017/12/05/mdp-value-iteration-algorithm-detail/)
* [Markov Decision Process Framework]({{ site.github.repo }}{{ site.baseurl }}/2017/12/05/mdp-markov-decision-process-framework/)
* [Addendum]({{ site.github.repo }}{{ site.baseurl }}/2017/12/06/mdp-addendum/)

### Reinforcement Learning

* [Temporal Difference Learning - Part 1]({{ site.github.repo }}{{ site.baseurl }}/2018/12/23/rl-temp-diff-learn-part1/)
* [Temporal Difference Learning - Part 2]({{ site.github.repo }}{{ site.baseurl }}/2019/01/22/rl-temp-diff-learn-part2/)
* [Temporal Difference In Q Form]({{ site.github.repo }}{{ site.baseurl }}/2019/02/19/rl-temp-diff-q/)
* [Bellman Operator Makes Convergence]({{ site.github.repo }}{{ site.baseurl }}/2019/03/05/rl-bellman-conv/)
* [Bellman Operator And Convergence Properties]({{ site.github.repo }}{{ site.baseurl }}/2019/03/17/rl-bellman-conv-thm-prop/)
* [More On Value Iteration]({{ site.github.repo }}{{ site.baseurl }}/2019/04/21/rl-more-on-val-i/)
* [Linear Programming In Value Iteration]({{ site.github.repo }}{{ site.baseurl }}/2019/05/10/rl-linear-prog-val-i/)
* [Policy Iteration]({{ site.github.repo }}{{ site.baseurl }}/2019/05/29/rl-policy-i/)
* [Meshing The Rewards - Part 1]({{ site.github.repo }}{{ site.baseurl }}/2019/06/29/rl-mesh-reward-part1/)
* [Meshing The Rewards - Part 2]({{ site.github.repo }}{{ site.baseurl }}/2019/07/07/rl-mesh-reward-part2/)
* [Explore versus Exploit - Part 1]({{ site.github.repo }}{{ site.baseurl }}/2019/08/11/rl-explore-exploit-part1/)
* [Explore versus Exploit - Part 2]({{ site.github.repo }}{{ site.baseurl }}/2019/09/04/rl-explore-exploit-part2/)
* [Exploit Evaluation By Hoeffding Bounds]({{ site.github.repo }}{{ site.baseurl }}/2019/10/09/rl-exploit-evaluate-by-hoeffding/)
* [Model-Based RL Algorithm RMAX - Part 1]({{ site.github.repo }}{{ site.baseurl }}/2020/02/08/rl-rmax-part1/)
* [Model-Based RL Algorithm RMAX - Part 2]({{ site.github.repo }}{{ site.baseurl }}/2020/02/23/rl-rmax-part2/)
* [Model-Based RL Algorithm RMAX - Part 3]({{ site.github.repo }}{{ site.baseurl }}/2020/02/28/rl-rmax-part3/)
* [Model-Based RL Algorithm RMAX - Part 4]({{ site.github.repo }}{{ site.baseurl }}/2020/03/26/rl-rmax-part4/)
* [POMDP - Part 1]({{ site.github.repo }}{{ site.baseurl }}/2020/07/21/rl-pomdp-part1/)
* [POMDP - Part 2]({{ site.github.repo }}{{ site.baseurl }}/2020/08/13/rl-pomdp-part2/)
* [POMDP - Part 3]({{ site.github.repo }}{{ site.baseurl }}/2020/10/10/rl-pomdp-part3/)
* Q Learning Algorithm
* Policy Iteration v.s. Value Iteration

> The related posts would be new added in the future, and supposed you are comfortable with posts in prerequisite section. 

### Computer Graphics, 3D Rotation, Transformation and Quaternion

Hard to believe, during my prerequisites study period, I involve myself in computer graphics and 3D topics, most impression might be the quaternion, it is the main kernel in modern 3D 
world.  Quaternion supports the rotation in accordance to any vector, not just be limited in system of fixed coordinate of reference.  If you can overcome quaternion, then, nothing could 
frustrate you in developing 3D related application. 

In this section, I am not show you only the prove of all the major topics, also illustrate by example to dump the Blender developed 3D object or animation to Android phone and show it
on phone just like what you see on PC screen.

under construction... 

### Programming Language

* Python
* R
* Octave(optional)

### Implementation

under construction... 

Thanks!
