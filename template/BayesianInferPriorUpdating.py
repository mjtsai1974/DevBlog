#!/usr/bin/python

'''
mjtsai1974@20180614,v1.0, a simple Bayesian inference experiment
'''

import numpy as np
from matplotlib import pyplot as plt

#Define the prior/hypothesis probability table
g_prior = [0.001, 0.999]

#Define the likelihood table
g_prob_likelihood = []

#Define indices to access in the prob_likelihood[[], []]
def_row_idx_malignant = 0
def_row_idx_benign = 1
def_col_idx_given_cancer = 0
def_col_idx_given_free = 1

#Define the function to update the given prior
def UpdatePrior(cancer_prob):
    g_prior[0] = cancer_prob
    g_prior[1] = 1 - g_prior[0]

    print('[UpdatePrior]P(Cancer)={0:5.3f}, P(Free)={1:5.3f}'.format(g_prior[0], g_prior[1]))

#Calculate the total probability of evidence
def CalculateTotalProbability(idx_evidence):
    '''
    http://puremonkey2010.blogspot.com/2016/09/python-lambda.html
    
        score = int(input('Int: '))  
        level = score // 10  
        {  
            10: lambda: print('Perfect'),  
            9 : lambda: print('A'),  
            8 : lambda: print('B'),  
            7 : lambda: print('C'),  
            6 : lambda: print('D')  
        }.get(level, lambda: print('E'))()  
    
    or
    
    Python switch-case equivalence:
    values = {
    value1: do_some_stuff1,
    value2: do_some_stuff2,
    ...
    valueN: do_some_stuffN,
    }
    values.get(var, do_default_stuff)()
	
	or still a dictionary
result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}[value](x)

	or still a dictionary
def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 is default if x not found
    '''
    total_prob = 0

    level = idx_evidence

    total_prob = {
        def_row_idx_malignant: lambda: g_prob_likelihood[def_row_idx_malignant][def_col_idx_given_cancer] * g_prior[def_col_idx_given_cancer] + g_prob_likelihood[def_row_idx_malignant][def_col_idx_given_free] * g_prior[def_col_idx_given_free],
        def_row_idx_benign: lambda: g_prob_likelihood[def_row_idx_benign][def_col_idx_given_cancer] * g_prior[def_col_idx_given_cancer] + g_prob_likelihood[def_row_idx_benign][def_col_idx_given_free] * g_prior[def_col_idx_given_free]
    }.get(level, lambda: -1)()

    return total_prob

#Do the Bayesian inference
def MakeBayesianInference(idx_run, hypothesis, evidence):
    idx_another = lambda hypothesis: 1 - hypothesis if hypothesis > 0  else 1 + hypothesis
    str_hypothesis = lambda hypothesis: 'Cancer' if hypothesis == 0 else 'Free'
    str_evidence = lambda evidence: 'Malignant' if evidence == 0 else 'Benign'

    print('[Bayesian]run {0:d}'.format(idx_run))
    print('[Bayesian]P(Cancer)::0={0:.5f}, P(Free)::0={1:.5f}'.format(g_prior[0], g_prior[1]))

    #Calculate the posterior - P(hypothesis|evidence)
    posterior = (g_prob_likelihood[evidence][hypothesis] * g_prior[hypothesis]) / CalculateTotalProbability(evidence)

    print('[Bayesian]P({0:s}|{1:s})={2:.8f}'.format(str_hypothesis(hypothesis), str_evidence(evidence), posterior))

    #Update the the prior/hypothesis probability table
    g_prior[hypothesis] = posterior
    g_prior[idx_another(hypothesis)] = 1 - posterior

    print('[Bayesian]P(Cancer)::1={0:.5f}, P(Free)::1={1:.5f}'.format(g_prior[0], g_prior[1]))
	
    return posterior

#The batch execution
def BatchExecution(q_idx, q_hypothesis, q_evidence, q_posterior):
    g_prior[0] = 0.001
    g_prior[1] = 0.999  #Restore the given prior/hypothesis table to the most initial value

    for i, h, e, p in zip(q_idx, q_hypothesis, q_evidence, q_posterior):
        #print('{0:d},{1:d},{2:d},{3:5.3f}'.format(i, h, e, p))  #for a debug purpose
        p = MakeBayesianInference(i, h, e)

if __name__ == '__main__':
    print('[main]P(Cancer)={0:5.3f}, P(Free)={1:5.3f}'.format(g_prior[0], g_prior[1]))

    #Define the likelihood table
    prob_malignant_given_cancer = 0.99
    prob_malignant_given_free = 0.01
    prob_benign_given_cancer = 0.01
    prob_benign_given_free = 0.99

    g_prob_likelihood = [[prob_malignant_given_cancer, prob_malignant_given_free], [prob_benign_given_cancer, prob_benign_given_free]]

    #Display the initial given
    print('[main]P(Malignant|Cancer)={0:5.3f}, P(Malignant|Free)={1:5.3f}'.format(g_prob_likelihood[def_row_idx_malignant][def_col_idx_given_cancer], g_prob_likelihood[def_row_idx_malignant][def_col_idx_given_free]))
    print('[main]P(Benign|Cancer)={0:5.3f}, P(Benign|Free)={1:5.3f}'.format(g_prob_likelihood[def_row_idx_benign][def_col_idx_given_cancer], g_prob_likelihood[def_row_idx_benign][def_col_idx_given_free]))

    total_prob = CalculateTotalProbability(def_row_idx_malignant)
    print('[main]P(Malignant)={0:5.3f}'.format(total_prob))

    total_prob = CalculateTotalProbability(def_row_idx_benign)
    print('[main]P(Benign)={0:5.3f}'.format(total_prob))

    #p = MakeBayesianInference(0, def_col_idx_given_cancer, def_row_idx_malignant)  #We want the posterior P(Cancer|Malignant), a simple distinct test

    #Define running queue of input parameters - configuration 1, all P(Cancer|Benign)
    q_idx = np.arange(0, 100, dtype=int)  #Queue of index
    q_hypothesis = np.zeros(100, dtype=int)  #Queue of hypothesis
    q_evidence = np.ones(100, dtype=int)  #Queue of evidence
    q_posterior = np.zeros(100, dtype=float)  #Queue of posterior result thus obtained

    #Execute the queued jobs
    print('Configuration 1: all P(Cancer|Benign)')

    BatchExecution(q_idx, q_hypothesis, q_evidence, q_posterior)

    #Define running queue of input parameters - configuration 2, all P(Cancer|Malignant)
    q_idx = np.arange(0, 100, dtype=int)  #Queue of index
    q_hypothesis = np.zeros(100, dtype=int)  #Queue of hypothesis
    q_evidence = np.zeros(100, dtype=int)  #Queue of evidence
    q_posterior = np.zeros(100, dtype=float)  #Queue of posterior result thus obtained

    #Execute the queued jobs
    print('Configuration 2: all P(Cancer|Malignant)')

    BatchExecution(q_idx, q_hypothesis, q_evidence, q_posterior)