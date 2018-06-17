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

#Define proprocessor to print debug message
def_no_debug_msg = 0
def_print_debug_msg = 1

#Define preprocessor to if draw by subplot2grid
def_plot = 0
def_subplot2grid = 1
def_subplot2grid_all_in_one = 2

g_subplot2grid_cfg = [0, 0, 0]  #[1 for already subplot2grid, 0 not yet; row count; col count]
g_subplot2grid_loc = [0, 0]  #[row, col], loc info for the subplot

#Define running queue of input parameters - configuration 4, P(Cancer|Malignant)x10, P(Cancer|Benign)...
q_idx = np.arange(0, 100, dtype=int)  #Queue of index
q_hypothesis = []  #Queue of hypothesis
q_evidence = []  #Queue of evidence
q_posterior = []  #Queue of posterior result thus obtained
q_updated_hypothesis_0 = np.zeros(100, dtype=float) #Queue of the updated 0-th hypothesis in the whole process
q_updated_hypothesis_1 = np.zeros(100, dtype=float) #Queue of the updated 1st hypothesis in the whole process
q_updated_evidence_0 = np.zeros(100, dtype=float) #Queue of the updated 0-th evidence in the whole process
q_updated_evidence_1 = np.zeros(100, dtype=float) #Queue of the updated 1st evidence in the whole process

#Define the function to update the given prior
def UpdatePrior(cancer_prob):
    g_prior[0] = cancer_prob
    g_prior[1] = 1 - g_prior[0]

    #print('[UpdatePrior]P(Cancer)={0:5.3f}, P(Free)={1:5.3f}'.format(g_prior[0], g_prior[1]))

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
def MakeBayesianInference(idx_run, hypothesis, evidence, b_dbg_msg):
    idx_another = lambda hypothesis: 1 - hypothesis if hypothesis > 0  else 1 + hypothesis
    str_hypothesis = lambda hypothesis: 'Cancer' if hypothesis == 0 else 'Free'
    str_evidence = lambda evidence: 'Malignant' if evidence == 0 else 'Benign'

    if b_dbg_msg == 1:
        print('[Bayesian]run {0:d}'.format(idx_run))

    #Calculate the posterior - P(hypothesis|evidence)
    posterior = (g_prob_likelihood[evidence][hypothesis] * g_prior[hypothesis]) / CalculateTotalProbability(evidence)

    if b_dbg_msg == 1:
        print('[Bayesian]P({0:s}|{1:s})={2:.15f}'.format(str_hypothesis(hypothesis), str_evidence(evidence), posterior))

    #Update the the prior/hypothesis probability table
    g_prior[hypothesis] = posterior
    g_prior[idx_another(hypothesis)] = 1 - posterior

    if b_dbg_msg == 1:
        print('[Bayesian]P(Cancer)={0:.15f}, P(Free)={1:.15f}'.format(g_prior[0], g_prior[1]))
        print('[Bayesian]P({0:s})={1:.15f}, P({2:s})={3:.15f}'.format(str_evidence(def_row_idx_malignant), CalculateTotalProbability(def_row_idx_malignant), str_evidence(def_row_idx_benign), CalculateTotalProbability(def_row_idx_benign)))

    return [posterior, g_prior[hypothesis], g_prior[idx_another(hypothesis)], CalculateTotalProbability(def_row_idx_malignant), CalculateTotalProbability(def_row_idx_benign)]

#The batch execution
def BatchExecution(b_restore_prior, b_subplot2grid, str_plot, q_idx, q_hypothesis, q_evidence, q_posterior):
    if b_restore_prior > 0:  #Restore the given prior/hypothesis table to the most initial value
        g_prior[0] = 0.001
        g_prior[1] = 0.999

    #for i, h, e, p in zip(q_idx, q_hypothesis, q_evidence, q_posterior):
    for i in q_idx:
        #print('{0:d},{1:d},{2:d},{3:5.3f}'.format(i, h, e, p))  #for a debug purpose
        [q_posterior[i], q_updated_hypothesis_0[i], q_updated_hypothesis_1[i], q_updated_evidence_0[i], q_updated_evidence_1[i]] = MakeBayesianInference(i, q_hypothesis[i], q_evidence[i], def_no_debug_msg)

    if b_subplot2grid == def_plot:
        #Plot the distribution of the posterior given the evidence
        fig, ax = plt.subplots(figsize=(8, 5))
    
        plt.plot(q_idx, q_posterior, ls='-', c='green', label=r'posterior')
        plt.plot(q_idx, q_updated_evidence_0, ls='--', c='red', label=r'P(Malignant)')
        plt.plot(q_idx, q_updated_evidence_1, ls='--', c='deeppink', label=r'P(Benign)')
        plt.plot(q_idx, q_updated_hypothesis_0, ls=':', c='royalblue', label=r'P(Cancer)')
        plt.plot(q_idx, q_updated_hypothesis_1, ls=':', c='deepskyblue', label=r'P(Free)')
        plt.xlim(q_idx[0], q_idx[len(q_idx)-1])
        plt.ylim(-0.2, 1.2)
        plt.xlabel('i-th run')
        plt.ylabel('posterior')
        plt.title(str_plot)

        plt.legend()
        plt.show()
    elif b_subplot2grid == def_subplot2grid:
        #Plot by subplot2grid()
        fig = plt.figure()
        fig.subplots_adjust(hspace = 1, wspace = 0.4)

        #Plot posterior
        ax1 = plt.subplot2grid(shape = (3, 2), loc = (0, 0), colspan = 2)
        ax1.plot(q_idx, q_posterior, ls='-', c='green')
        ax1.set_title('posterior')

        #Plot P(Malignant)
        ax2 = plt.subplot2grid(shape = (3, 2), loc = (1, 0))
        ax2.plot(q_idx, q_updated_evidence_0, ls='-', c='red')
        ax2.set_title('P(Malignant)')

        #Plot P(Benign)
        ax3 = plt.subplot2grid(shape = (3, 2), loc = (1, 1))
        ax3.plot(q_idx, q_updated_evidence_1, ls='-', c='deeppink')
        ax3.set_title('P(Benign)')

        #Plot P(Cancer)
        ax4 = plt.subplot2grid(shape = (3, 2), loc = (2, 0))
        ax4.plot(q_idx, q_updated_hypothesis_0, ls='-', c='royalblue')
        ax4.set_title('P(Cancer)')

        #Plot P(Free)
        ax5 = plt.subplot2grid(shape = (3, 2), loc = (2, 1))
        ax5.plot(q_idx, q_updated_hypothesis_1, ls='-', c='deepskyblue')
        ax5.set_title('P(Free)')

        plt.xlim(q_idx[0], q_idx[len(q_idx)-1])
        plt.ylim(-0.2, 1.2)
        plt.title(str_plot)
        plt.legend()
        plt.show()
    elif b_subplot2grid == def_subplot2grid_all_in_one:
        #ALL in one plot by subplot2grid()
        if g_subplot2grid_cfg[0] == 0:
            fig = plt.figure()
            fig.subplots_adjust(hspace = 1, wspace = 0.4)
            #fig.tight_layout()  #No need in this sample, this is to have a tightly close subplots
            #fig.subplots_adjust(hspace=0)  #No need in this sample, this is to have a tightly close subplots

            ax = plt.subplot2grid(shape = (g_subplot2grid_cfg[1], g_subplot2grid_cfg[2]), loc = (g_subplot2grid_loc[0], g_subplot2grid_loc[1]))
            ax.plot(q_idx, q_posterior)
            ax.set_title(str_plot)

            g_subplot2grid_cfg[0] = 1
        elif g_subplot2grid_cfg[0] == 1:
            ax = plt.subplot2grid(shape = (g_subplot2grid_cfg[1], g_subplot2grid_cfg[2]), loc = (g_subplot2grid_loc[0], g_subplot2grid_loc[1]))
            ax.plot(q_idx, q_posterior)
            ax.set_title(str_plot)
        elif g_subplot2grid_cfg[0] == 2:
            ax = plt.subplot2grid(shape = (g_subplot2grid_cfg[1], g_subplot2grid_cfg[2]), loc = (g_subplot2grid_loc[0], g_subplot2grid_loc[1]))
            ax.plot(q_idx, q_posterior)
            ax.set_title(str_plot)

            plt.legend()
            plt.show()
        else:
            print('[BatchExecution]Incorrect subplot config!')
    else:
        print('[BatchExecution]Incorrect plot request!')

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
    print('[main]P(Malignant)={0:.12f}'.format(total_prob))

    total_prob = CalculateTotalProbability(def_row_idx_benign)
    print('[main]P(Benign)={0:.12f}'.format(total_prob))

    #p = MakeBayesianInference(0, def_col_idx_given_cancer, def_row_idx_malignant)  #We want the posterior P(Cancer|Malignant), a simple distinct test

    #Define running queue of input parameters - configuration 1, all P(Cancer|Benign)
    q_hypothesis = np.zeros(100, dtype=int)  #Queue of hypothesis
    q_evidence = np.ones(100, dtype=int)  #Queue of evidence
    q_posterior = np.zeros(100, dtype=float)  #Queue of posterior result thus obtained

    #Execute the queued jobs
    print('Configuration 1: all P(Cancer|Benign)')

    BatchExecution(1, def_subplot2grid, 'Configuration 1: all P(Cancer|Benign)', q_idx, q_hypothesis, q_evidence, q_posterior)

    #Define running queue of input parameters - configuration 2, all P(Cancer|Malignant)
    q_hypothesis = np.zeros(100, dtype=int)  #Queue of hypothesis
    q_evidence = np.zeros(100, dtype=int)  #Queue of evidence
    q_posterior = np.zeros(100, dtype=float)  #Queue of posterior result thus obtained

    #Execute the queued jobs
    print('Configuration 2: all P(Cancer|Malignant)')

    BatchExecution(1, def_subplot2grid, 'Configuration 2: all P(Cancer|Malignant)', q_idx, q_hypothesis, q_evidence, q_posterior)

    #Define running queue of input parameters - configuration 3, P(Cancer|Malignant)x1, P(Cancer|Benign)...
    q_hypothesis = np.zeros(100, dtype=int)  #Queue of hypothesis
    q_evidence = np.zeros(100, dtype=int)  #Queue of evidence
    q_posterior = np.zeros(100, dtype=float)  #Queue of posterior result thus obtained

    q_evidence[9:len(q_evidence)] = 1
	
    #Execute the queued jobs
    print('Configuration 3: P(Cancer|Malignant)x9, P(Cancer|Benign)...')

    BatchExecution(1, def_subplot2grid, 'Configuration 3: P(Cancer|Malignant)x9, P(Cancer|Benign)...', q_idx, q_hypothesis, q_evidence, q_posterior)

    #Define running queue of input parameters - configuration 4, P(Cancer|Malignant)x10, P(Cancer|Benign)...
    q_hypothesis = np.zeros(100, dtype=int)  #Queue of hypothesis
    q_evidence = np.zeros(100, dtype=int)  #Queue of evidence
    q_posterior = np.zeros(100, dtype=float)  #Queue of posterior result thus obtained

    q_evidence[10:len(q_evidence)] = 1
	
    #Execute the queued jobs
    print('Configuration 4: P(Cancer|Malignant)x10, P(Cancer|Benign)...')

    BatchExecution(1, def_subplot2grid, 'Configuration 4: P(Cancer|Malignant)x10, P(Cancer|Benign)...', q_idx, q_hypothesis, q_evidence, q_posterior)

    #Define running queue of input parameters - configuration 5, P(Cancer|Malignant)x50, P(Cancer|Benign)x50
    q_hypothesis = np.zeros(100, dtype=int)  #Queue of hypothesis
    q_evidence = np.zeros(100, dtype=int)  #Queue of evidence
    q_posterior = np.zeros(100, dtype=float)  #Queue of posterior result thus obtained

    q_evidence[49:len(q_evidence)] = 1

    #Execute the queued jobs
    print('Configuration 7: P(Cancer|Malignant)x50, P(Cancer|Benign)x50')

    BatchExecution(1, def_subplot2grid, 'Configuration 7: P(Cancer|Malignant)x50, P(Cancer|Benign)x50', q_idx, q_hypothesis, q_evidence, q_posterior)

    #Define running queue of input parameters - configuration 6, P(Cancer|Malignant), P(Cancer|Benign), P(Cancer|Malignant), P(Cancer|Benign)...
    q_hypothesis = np.zeros(100, dtype=int)  #Queue of hypothesis
    q_evidence = np.zeros(100, dtype=int)  #Queue of evidence
    q_posterior = np.zeros(100, dtype=float)  #Queue of posterior result thus obtained

    for i in q_idx:
        if i % 2 == 1:
            q_evidence[i] = 1

    #Execute the queued jobs
    print('Configuration 8: P(Cancer|Malignant), P(Cancer|Benign), P(Cancer|Malignant), P(Cancer|Benign)...')

    BatchExecution(1, def_subplot2grid, 'Configuration 8: P(Cancer|Malignant), P(Cancer|Benign), \nP(Cancer|Malignant), P(Cancer|Benign)...', q_idx, q_hypothesis, q_evidence, q_posterior)

    #Configuration {0:d}, P(Cancer|Malignant)x{1:d}, P(Cancer|Benign)...
    g_subplot2grid_cfg[0] = 0  #Reset to not yet initialized
    g_subplot2grid_cfg[1] = 4  #Row count of subplot
    g_subplot2grid_cfg[2] = 3  #Col count of subplot

    for i in np.arange(1, 13):
        q_evidence = np.zeros(100, dtype=int)
        q_posterior = np.zeros(100, dtype=float)

        q_evidence[i:len(q_evidence)] = 1

        #str_label = 'P(Cancer|Malignant)x{1:d}, P(Cancer|Benign)...'.format(i, i)
        str_label = 'P(C|T)x{1:d},P(C|F)..'.format(i, i)

        g_subplot2grid_loc[0] = int((i - 1) / g_subplot2grid_cfg[2])  #Row index of subplot
        g_subplot2grid_loc[1] = int((i - 1) % g_subplot2grid_cfg[2])  #Col index of subplot

        #Plot the whole subplot2grid
        if i == g_subplot2grid_cfg[1] * g_subplot2grid_cfg[2]:
            g_subplot2grid_cfg[0] = 2

        #Execute the queued jobs
        #print(str_label)

        BatchExecution(1, def_subplot2grid_all_in_one, str_label, q_idx, q_hypothesis, q_evidence, q_posterior)