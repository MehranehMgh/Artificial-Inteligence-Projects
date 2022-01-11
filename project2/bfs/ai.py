import random
from collections import deque
from copy import deepcopy


class Agent:
    def __init__(self, perceive_func=None, agent_id=None):
        self.perceive_func = perceive_func
        self.my_id = agent_id

        ######### EDITABLE SECTION #########

        self.predicted_actions = []

        ######### END OF EDITABLE SECTION #########

    def act(self):
        sensor_data = self.perceive_func(self)

        ######### EDITABLE SECTION #########

        if self.predicted_actions==[]: self.predicted_actions=self.bfs(sensor_data['Current_Env'])
        action=self.predicted_actions.pop()

        ######### END OF EDITABLE SECTION #########

        return action

    ######### VV EDITABLE SECTION VV #########
    def bfs(self, game):
        actions = ['left', 'right', 'up', 'down']
        q = deque()
        q.append([game, []])
        while len(q) > 0:
            node = q.popleft()
            if random.random() > 0.8:
                random.shuffle(actions)
            for action in actions:
                child_game = node[0].create_copy()
                if 'has died' not in child_game.take_action(action, self.my_id):
                    q.append([child_game, [action] + node[1]])
                if child_game.goal_test():
                    return [action] + node[1]