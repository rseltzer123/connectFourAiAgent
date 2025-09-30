from agent import Agent
from structures.mini_max_tree import MiniMaxTree, MiniMaxNode


class MiniMaxAgent(Agent):

    mini_max_tree = None

    def take_turn(self, game_state):
        mini_max_tree = MiniMaxTree(game_state)
