#!/usr/bin/python

'''
mjtsai1974@20180615,v1.0, a simple plt.subplot2grid application
'''

import numpy as np
from matplotlib import pyplot as plt

#Code section::https://morvanzhou.github.io/tutorials/data-manipulation/plt/4-2-subplot2/
plt.figure()

ax1 = plt.subplot2grid(shape=(3, 3), loc=(0, 0), colspan=3)
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title::(0, 0)')

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax2.set_title('ax2_title::(1, 0)')

ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax3.set_title('ax1_title::(1, 2)')

ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 1.6])
ax4.set_title('ax1_title::(2, 0)')

ax5 = plt.subplot2grid((3, 3), (2, 1))
ax5.set_title('ax1_title::(2, 1)')

#ax6 = plt.subplot2grid((3, 3), (2, 2))
#ax6.set_title('ax1_title::(2, 2)')

plt.show()