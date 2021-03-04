

class ObservationModel(object):
    def __init__(self):
        self._observation_matrix = dict()

    def __str__(self):
        str = ''

        for k, v in self._observation_matrix.items():
            str += '{}:{}\n'.format(k, v)

        return str

    @property
    def observation_matrix(self):
        return self._observation_matrix

    """
    Configure the observation probability of o from state sj by action a with probability p
    """
    def ConfigureObservationMatrix(self, o, sj, a, p):
        self._observation_matrix['{},{},{}'.format(o.Name, sj.Name, a.Name)] = p
        #self._observation_matrix[o, sj, a] = p

    def Probability(self, o, sj, a):
        return self._observation_matrix.get('{},{},{}'.format(o.Name, sj.Name, a.Name))
        #return self._observation_matrix[o, sj, a]