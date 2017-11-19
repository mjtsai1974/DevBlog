---
layout: post
title: Neural Network Basic Topology
---

## Neural Network Basic Topology
<p class="message">
Neural network aims at non-linear hypothesis, binary and multiple classification.  In the early 1990, it is believed that it achieves some training hypothesis and come out with results at certain convincible level. 
Due to the fact that it was not scaled very well to large problem at theat moment, it has been placed in the storage and it was almost the time I was a freshman in th euniversity.  Due to H/W calculation and processing
capability has a major improvement in the past two decads, in conjunction with big data science evolution due to open source environment, neural network has been re-inspected, even more, the deep learning has been build
on top of its model representation.  Although his founder Geoff Hilton suspects and claims that backward propagation might not be the most optimal approximation to the way human brain thinking, which is just like 
the case that jet engines could make human fly but human couldn't fly like a bird.  With full understanding of its model, the way it supports training and recognition would be quiet an add-in in future involve in deep learning.
</p>

### Model Representation By Intuition
>Begin by a very basic realization that human receives external data from eyes, mouth, tongue, skin, then transfer to our brain, wherein, it is manipulated and classified to some other layers or groups of the neurons, which then take their turns to make further processing, maybe neuron transform in a recursive manner.  The neural network is constructed with a hope to approximate the way our brain manipulating, training input and learning.  

![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2017-11-19-nn-basic-topology-model.png "model representation")
 
>The model representation graph exhibits that there exists an input layer to receive the external data, an output layer to generate the outcome value, some hidden layes(in this example, layer 2, 3) in between the input and the output layer.  One step further, the model design transfer the output layer outcome to the final preocessing function, usually, by means of the logistic regression to generalize the real identification result.  
>In this paragraph, $a_i^{(j)}$ is to denote the i-th activation function at layer j, wherein, it takes input from layer j-1 and make advanced processing at its layer, output it, in turns becoming the input data to next layer j+1.  We can have the model more generalized in another graph.  

