#!\usr\bin\python
'''
mjtsai1974@20180603, v1.0, Simple plot
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

#Generate a randomized data set
#x = np.random.randn(500)

#Plot command::Begin
#plot(x, y), y v.s. x::Begin
#plt.plot(x) #Take the x dataset on the Y-axis, interconnect x[i]<->x[i+1]
#plt.plot(x, '.')  #Take the x dataset on the Y-axis, draw each x[i] as '.', for '.' is a symbol
#plt.plot(x, np.arange(len(x)))  #Take the x dataset on the X-axis, and np.arange(len(x))=[0..500] on the Y-axis
#plt.plot(np.arange(len(x)), x)  #Take the np.arange(len(x))=[0..500] as X-axis, and x dataset on the Y-axis, interconnect x[i]<->x[i+1]
#plot(x, y), y v.s. x::End

#scatter(x, y), y v.s. x::Begin
##plt.scatter(np.arange(len(x)),x)
#scatter(x, y), y v.s. x::End

#histogram::Begin
#plt.hist(x, bins=25)  #bin=25 specifies 25 bins in graph
#histogram::End

#Kernel density estimation::Begin
#sns.kdeplot(x)
#sns.kdeplot(x, bw=1.0)  #bw is the bandwitdh, the determination of the smoothness of the estimation
#Kernel density estimation::End

#Cumulative frequency::Begin
#plt.plot(stats.cumfreq(x, 40)[0]) #stats.cumfreq(x, 40)[0], x->data set, 40->number of bins, [0]->Zero-based index for input data(maybe)
#Cumulative frequency::End

#Errorbar::Begin
'''
index = np.arange(5)
y = index**2
ErrorBar = y/2

plt.errorbar(index, y, yerr=ErrorBar, fmt='o')
'''
#Errorbar::End

#Box plot::Begin
#plt.plot(x, sym='*')
#Box plot::End

#Violinplot::Begin
#to be conti...
#Violinplot::End

#Group bar charts::Begin
'''
x = np.random.rand(10, 4)

df = pd.DataFrame(x, columns=['x1', 'x2', 'x3', 'x4'])

df.plot(kind='bar')
'''
#Group bar charts::End

#Pie charts::Begin
'''
txtLabels = 'Cat', 'Dogs', 'Frogs', 'Others'
fractions = [45, 30, 15, 10]
offsets = (0, 0.05, 0, 0)
#plt.pie(fractions, explode=offsets, labels=txtLabels)  #Pie chart basic prototype
#plt.pie(fractions, explode=offsets, labels=txtLabels, autopct='%1.1f%%')  #Pie chart basic prototype + proportion%
#plt.pie(fractions, explode=offsets, labels=txtLabels, autopct='%1.1f%%', shadow=True)  #Pie chart basic prototype + proportion% + shadow
#plt.pie(fractions, explode=offsets, labels=txtLabels, autopct='%1.1f%%', shadow=True, startangle=90)  #Pie chart basic prototype + proportion% + shadow + start with 90 degree consisting of such parts if it is
plt.pie(fractions, explode=offsets, labels=txtLabels, autopct='%1.1f%%', shadow=True, startangle=90, colors=sns.color_palette('muted'))

plt.axis('equal')
'''
#Pie charts::End

#Scatter plot::Begin
df = pd.DataFrame(np.random.rand(50, 4), columns=['a','b','c','d'])
#df.plot(kind='scatter', x='a', y='b')  #scatter plot matrix of y v.s. x
df.plot(kind='scatter', x='a', y='b', s=df['c']*10)  #s=scale
#df.plot.line()
#df.plot.scatter(x='a', y='b')
#df.plot.hist()
#Scatter plot::End

#Plot command::End

plt.show()