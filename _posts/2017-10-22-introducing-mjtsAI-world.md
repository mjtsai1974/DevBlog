---
layout: post
title: Introducing to mjt&#39;s AI world
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

[2][Stanford Machine Learning](https://www.coursera.org/learn/machine-learning)  

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
* Machine Learning Foundation
* Neural Network
* Support Vector Machine(SVM)
* Deep Learning
* Computer Graphics, 3D Rotation, Transformation and Quaternion

### Prerequisites

Whatever topic playing the consolidated fundamental basis implicitly be constructed as computer algorithm, but explicitly help the learning flow to converge the result would be in this section, includes 
the following:

* [Hoeffding Inequality v.s. Law of Large Number]({{ site.github.repo }}{{ site.baseurl }}/2017/10/24/prereq-hoeffding-vs-law-large-number/)
<!-- * <a href="{{ site.github.repo }}{{ site.baseurl }}/2017/10/24/prereq-hoeffding-vs-law-large-number/">Hoeffding Inequality v.s. Law of Large Number</a> --> <!-- this also works -->
* Lagrange Multiplier 
* QR Decomposition
* Cholesky Decomposition
* Spatial Value Decomposition(SVD)
* Introduction to Alpha Distribution
* Introduction to Gamma Distribution
* Introduction to F Distribution
* Introduction to Chi-Square Distribution
* Introduction to t Distribution
* The relation in between Normal, F, Chi-Square, t Distribution 
* Introduction to Exponential Distribution
* Introduction to Poisson Distribution
* Univariate Regression Model
* Multivariate Regression Model
* F-test, Chi-square test, t-test and still other power test evaluation
* (Log)Likelihood Ratio Test
* Still others...

> The related posts would be new added in the future, and supposed you are comfortable with calculus and linear algebra, and a little intuition about statistics is mandatory. 

### Machine Learning Foundation

After exploring in the prerequisites, you are supposed to come out with sufficient domain knowledge, next would be the following foundation in machine learning:

* Hoeffding Inequality v.s Law of Large Number
* Gradient Descendent
* Overfitting v.s. Regularization by means of Lagrangian 
* Binary Classification
* Principal Component Analysis(PCA by means of SVD)
* K-means Algorithm
* Collaborating Filtering Algorithm

> The related posts would be new added in the future, and supposed you are comfortable with posts in prerequisite section. 

### Neural Networks

Neural network is the software or hardware emulation in the topology resembling to the organization of human brain.  H/W usually aims at speeding up.  S/W implementation wouldn't 
be jargon-free.  It's quite difficult to realize the backward propagation, no even think to prove it in short.  Errors in N.N lectures could be found on the[Coursera](https://www.coursera.org/learn/machine-learning).
Even the professor ANG said to us that he couldn't figure it out the proof in the on-line video.  Thanks for god, the mathematicians since the old times has left one stupid and 
efficient method, guess what?  The mathematics induction, via which, we can easily show you the way backward propagation really means and the validity of its formula.

Hard to believe, it took me over 2 days to prove backward propagation.  Below is the major items:

* Basic topology
* Feed Forward Propagation
* Backward Propagation 

### Support Vector Machine(SVM)

Support vector machine targets in binary classification with a specific safe guard distance in between the two kinds.  Both neural network and support vector machine take major weights 
in my growth in machine learning foundation after CS221 on [Coursera](https://www.coursera.org/learn/machine-learning).  It took me almost 2 weeks to summary all the details from its 
theorem to the formula deduction, finally algorithm of the real thing.

* Support Vector machine Theorem
* What is KKT condition?
* Operation flow in SVM algorithm

### Deep Learning

Under construction...

### Computer Graphics, 3D Rotation, Transformation and Quaternion

Hard to believe, during my prerequisites study period, I involve myself in computer graphics and 3D topics, most impression might be the quaternion, it is the main kernel in modern 3D 
world.  Quaternion supports the rotation in accordance to any vector, not just be limited in system of fixed coordinate of reference.  If you can overcome quaternion, then, nothing could 
frustrate you in developing 3D related application. 

In this section, I am not show you only the prove of all the major topics, also illustrate by example to dump the Blender developed 3D obhject or animation to Android phone and show it
on phone just like what you see on PC screen.

under construction... 

### Programming Language

* Python
* R
* Octave(optional)

Thanks!
