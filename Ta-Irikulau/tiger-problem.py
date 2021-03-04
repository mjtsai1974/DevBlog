from framework.pomdp.basics.action import Action
from framework.pomdp.basics.state import State
from framework.pomdp.basics.observation import Observation
from framework.pomdp.basics.histree import HisTreeNode
from framework.pomdp.basics.histree import HisTree
from framework.pomdp.environment.world import Environment
from framework.pomdp.model.reward import RewardModel
from framework.pomdp.model.transition import TransitionModel
from framework.pomdp.model.observation import ObservationModel
from framework.pomdp.agent.proxy import Agent
from util.logger import Logger

if __name__ == '__main__':
    s1 = State('Tiger_Left')
    s2 = State('Tiger_Right')
    print('s1={} s2={}'.format(s1, s2))
    print(s1==s2)

    o1 = Observation('Tiger_Left')
    o2 = Observation('Tiger_Right')
    print('o1={} o2={}'.format(o1, o2))
    print(o1==o2)

    a1 = Action('Listen')
    a2 = Action('Open_Left')
    a3 = Action('Open_Right')

    #Reward matrix configure, given that the agent don't know what world state it is!!!
    model_r = RewardModel()
    model_r.ConfigureRewardMatrix(o1, s1, a1, -1)  #make observation(Tiger_Left), in state(Tiger_Left), by action(Listen), reward = -1
    model_r.ConfigureRewardMatrix(o2, s1, a1, -1)  #make observation(Tiger_Right), in state(Tiger_Left), by action(Listen), reward = -1
    model_r.ConfigureRewardMatrix(o1, s2, a1, -1)  #make observation(Tiger_Left), in state(Tiger_Right), by action(Listen), reward = -1
    model_r.ConfigureRewardMatrix(o2, s2, a1, -1)  #make observation(Tiger_Right), in state(Tiger_Right), by action(Listen), reward = -1
    model_r.ConfigureRewardMatrix(o1, s1, a2, -100)  #make observation(Tiger_Left), in state(Tiger_Left), by action(Open_Left), reward = -100
    model_r.ConfigureRewardMatrix(o2, s1, a2, 10)  #make observation(Tiger_Right), in state(Tiger_Left), by action(Open_Left), reward = 10
    model_r.ConfigureRewardMatrix(o1, s2, a2, -100)  #make observation(Tiger_Left), in state(Tiger_Right), by action(Open_Left), reward = -100
    model_r.ConfigureRewardMatrix(o2, s2, a2, 10)  #make observation(Tiger_Right), in state(Tiger_Right), by action(Open_Left), reward = 10
    model_r.ConfigureRewardMatrix(o1, s1, a3, 10)  #make observation(Tiger_Left), in state(Tiger_Left), by action(Open_Right), reward = 10
    model_r.ConfigureRewardMatrix(o2, s1, a3, -100)  #make observation(Tiger_Right), in state(Tiger_Left), by action(Open_Right), reward = -100
    model_r.ConfigureRewardMatrix(o1, s2, a3, 10)  #make observation(Tiger_Left), in state(Tiger_Right), by action(Open_Right), reward = 10
    model_r.ConfigureRewardMatrix(o2, s2, a3, -100)  #make observation(Tiger_Right), in state(Tiger_Right), by action(Open_Right), reward = -100

    #Transitive probability configure
    model_t = TransitionModel()
    model_t.ConfigureTransitiveMatrix(s1, s1, a1, 1.0)  #from state(Tiger_Left) to state(Tiger_Left) by action(Listen), p = 1.0
    model_t.ConfigureTransitiveMatrix(s1, s2, a1, 0.0)  #from state(Tiger_Left) to state(Tiger_Right) by action(Listen), p = 0.0
    model_t.ConfigureTransitiveMatrix(s2, s2, a1, 1.0)  #from state(Tiger_Right) to state(Tiger_Right) by action(Listen), p = 1.0
    model_t.ConfigureTransitiveMatrix(s2, s1, a1, 0.0)  #from state(Tiger_Right) to state(Tiger_Left) by action(Listen), p = 0.0
    model_t.ConfigureTransitiveMatrix(s1, s1, a2, 0.5)  #from state(Tiger_Left) to state(Tiger_Left) by action(Open_Left), p = 0.5
    model_t.ConfigureTransitiveMatrix(s1, s2, a2, 0.5)  #from state(Tiger_Left) to state(Tiger_Right) by action(Open_Left), p = 0.5
    model_t.ConfigureTransitiveMatrix(s2, s2, a2, 0.5)  #from state(Tiger_Right) to state(Tiger_Right) by action(Open_Left), p = 0.5
    model_t.ConfigureTransitiveMatrix(s2, s1, a2, 0.5)  #from state(Tiger_Right) to state(Tiger_Left) by action(Open_Left), p = 0.5
    model_t.ConfigureTransitiveMatrix(s1, s1, a3, 0.5)  #from state(Tiger_Left) to state(Tiger_Left) by action(Open_Right), p = 0.5
    model_t.ConfigureTransitiveMatrix(s1, s2, a3, 0.5)  #from state(Tiger_Left) to state(Tiger_Right) by action(Open_Right), p = 0.5
    model_t.ConfigureTransitiveMatrix(s2, s2, a3, 0.5)  #from state(Tiger_Right) to state(Tiger_Right) by action(Open_Right), p = 0.5
    model_t.ConfigureTransitiveMatrix(s2, s1, a3, 0.5)  #from state(Tiger_Right) to state(Tiger_Left) by action(Open_Right), p = 0.5
 
    #Observation probability configure
    model_o = ObservationModel()
    model_o.ConfigureObservationMatrix(o1, s1, a1, 0.85)  #make observation(Tiger_Left), in state(Tiger_Left), by action(Listen), p = 0.85
    model_o.ConfigureObservationMatrix(o2, s1, a1, 0.15)  #make observation(Tiger_Right), in state(Tiger_Left), by action(Listen), p = 0.15
    model_o.ConfigureObservationMatrix(o1, s2, a1, 0.15)  #make observation(Tiger_Left), in state(Tiger_Right), by action(Listen), p = 0.15
    model_o.ConfigureObservationMatrix(o2, s2, a1, 0.85)  #make observation(Tiger_Right), in state(Tiger_Right), by action(Listen), p = 0.85
    model_o.ConfigureObservationMatrix(o1, s1, a2, 0.5)  #make observation(Tiger_Left), in state(Tiger_Left), by action(Open_Left), p = 0.5
    model_o.ConfigureObservationMatrix(o2, s1, a2, 0.5)  #make observation(Tiger_Right), in state(Tiger_Left), by action(Open_Left), p = 0.5
    model_o.ConfigureObservationMatrix(o1, s2, a2, 0.5)  #make observation(Tiger_Left), in state(Tiger_Right), by action(Open_Left), p = 0.5
    model_o.ConfigureObservationMatrix(o2, s2, a2, 0.5)  #make observation(Tiger_Right), in state(Tiger_Right), by action(Open_Left), p = 0.5
    model_o.ConfigureObservationMatrix(o1, s1, a3, 0.5)  #make observation(Tiger_Left), in state(Tiger_Left), by action(Open_Right), p = 0.5
    model_o.ConfigureObservationMatrix(o2, s1, a3, 0.5)  #make observation(Tiger_Right), in state(Tiger_Left), by action(Open_Right), p = 0.5
    model_o.ConfigureObservationMatrix(o1, s2, a3, 0.5)  #make observation(Tiger_Left), in state(Tiger_Right), by action(Open_Right), p = 0.5
    model_o.ConfigureObservationMatrix(o2, s2, a3, 0.5)  #make observation(Tiger_Right), in state(Tiger_Right), by action(Open_Right), p = 0.5

    root_node = HisTreeNode(None, None, None, None, 0, 0) #root node in policy tree
    history_tree_record = HisTree() #a hash record to track the policy tree

    logger = Logger(name = 'Uknav')

    agent = Agent()

    env = Environment("Tiger-Problem", model_t, model_o, model_r, 5, agent, logger)
    env.Actions = [a1, a2, a3]
    env.States = [s1, s2]
    env.Observations = [o1, o2]
    env.Inflate(root_node, history_tree_record)

    print('Actions:{}'.format(env.Actions))
    print('States:{}'.format(env.States))
    print('Observations{}'.format(env.Observations))

    env.main()