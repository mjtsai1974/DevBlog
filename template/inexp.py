#! \usr\bin\python
'''
mjtsai1974@20180601, v1.0, Simple calculation for income and expense
'''

import numpy as np
import matplotlib.pyplot as plt

def IncomeExpense(data):
    income_total = np.sum(data[data>0])
    expense_total = np.sum(data[data<0])

    return (income_total, expense_total) #works
    #return [income_total, expense_total] #works

if __name__ == '__main__':
    #data=[100, 25, -43, 18, -55, 37, -70]  #this is incorrect to be used for data[data > 0] to find out positive elements, must be numpy.array
    data=np.array([100, 25, -43, 18, -55, 37, -70])

    (gain, loss)=IncomeExpense(data) #works
    #[gain, loss]=IncomeExpense(data) #works

    print('Gained:{0:5.2f} Loss:{1:5.2f}'.format(gain, -loss))  #this works, new format
    #print('Gained:%5.2f Loss:%5.2f' %(gain, -loss)) #also holds, to be believed old format
