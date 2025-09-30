from agent import Agent
import random


class RandomAgent(Agent):
    def take_turn(self, game_state):
        return random.randint(1, 7)
