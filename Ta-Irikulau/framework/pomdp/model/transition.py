

class TransitionModel(object):
    def __init__(self):
        self._transition_matrix = dict()

    def __str__(self):
        str = ''

        for k, v in self._transition_matrix.items():
            str += '{}:{}\n'.format(k, v)

        return str

    @property
    def transition_matrix(self):
        return self._transition_matrix

    """
    Configure the transitive probability from state si to sj by action a with probability p
    """
    def ConfigureTransitiveMatrix(self, si, sj, a, p):
        self._transition_matrix['{},{},{}'.format(si.Name, sj.Name, a.Name)] = p
        #self._transition_matrix[si, sj, a] = p

    def Probability(self, si, sj, a):
        return self._transition_matrix.get('{},{},{}'.format(si.Name, sj.Name, a.Name))
        #return self._transition_matrix[si, sj, a]