

class RewardModel(object):
    def __init__(self):
        self._reward_matrix = dict()

    def __str__(self):
        str = ''

        for k, v in self._reward_matrix.items():
            str += '{}:{}\n'.format(k, v)

        return str

    @property
    def reward_matrix(self):
        return self._reward_matrix

    """
    Configure the reward of o from state sj by action a
    """
    def ConfigureRewardMatrix(self, o, sj, a, val):
        self._reward_matrix['{},{},{}'.format(o.Name, sj.Name, a.Name)] = val
        self._reward_matrix[o, sj, a] = val

    def GetRwrardByActionStateObservation(self, o, sj, a):
        return self._reward_matrix.get('{},{},{}'.format(o.Name, sj.Name, a.Name))
        #return self._reward_matrix[o, sj, a]