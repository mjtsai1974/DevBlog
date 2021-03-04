

class Environment(object):
    def __init__(self, name, T, O, R, horizon_length, agent, logger):
        self._name = name
        self._actions = None
        self._states = None
        self._observations = None
        self._transition_model = T
        self._observation_model = O
        self._reward_model = R
        self._belief = None
        self._belief_history = None
        self._horizon_length = horizon_length
        self._agent = agent
        self._logger = logger

    """
    All the actions in this environment, in the type of list
    """
    @property
    def Actions(self):
        return self._actions

    @Actions.setter
    def Actions(self, value):
        self._actions = value

    @Actions.deleter
    def Actions(self):
        del self._actions

    """
    All the states in this environment, in the type of list
    """
    @property
    def States(self):
        return self._states

    @States.setter
    def States(self, value):
        self._states = value

    @States.deleter
    def States(self):
        del self._states

    """
    All the observations in this environment, in the type of list
    """
    @property
    def Observations(self):
        return self._observations

    @Observations.setter
    def Observations(self, value):
        self._observations = value

    @Observations.deleter
    def Observations(self):
        del self._observations

    """
    Initialize the environment, they are:
    1. Initial belief
    2. Empty/reset the whole belief history
    3. Configure the agent with mandatory models, they are T, O, R, horizon_length
    4. Initialize the root node of the histree with the initial belief and connect it to the histree
    """
    def Inflate(self, root_node, histree):
        self._logger.Info('World initialization...')
        self._logger.Info('Actions = {}\nStates = {}\nObservations = {}'.format(self._actions, self._states, self._observations))
        self._logger.Debug('Reward matrix\n{}'.format(self._reward_model))
        self._logger.Debug('Transitive matrix\n{}'.format(self._transition_model))
        self._logger.Debug('Observation matrix\n{}'.format(self._observation_model))

        num_states = len(self._states)
        self._belief = [(1 / num_states) for _ in range(num_states)]  #In the beginning, the initial belief is uniform distribution manner

        self._agent.Configure(
            self._transition_model,
            self._observation_model,
            self._reward_model,
            self._horizon_length)
    
        root_node.Belief = self._belief
        histree.AddNodeInHistory(root_node.Layer, root_node)
    
        self._agent.Inflate(root_node, histree, self._logger)

    """
    The main body of this environment where major tasks go over here.
    """
    def main(self):
        #Do the monotinic action simulation
        self._agent.Simulation(self._actions, self._states, self._observations)