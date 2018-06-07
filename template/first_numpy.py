#! \usr\bin\python
'''
mjtsai1974@20180601, v1.0, Simple illustration
'''

import numpy as np
import matplotlib.pyplot as plt

#Generate time vales
t=np.arange(0, 10, 0.1)

#freq
freq=0.5

#Generate the sin output from time value & freq
y=np.sin(2*np.pi*freq*t)

#Graph the result
plt.plot(t,y)
plt.xlabel('time values')
plt.ylabel('sin values')
#plt.savefig(r'Sinewave.png', dpi=200)  #Save it as file
#plt.show() #No need this line could we even show it on iPython