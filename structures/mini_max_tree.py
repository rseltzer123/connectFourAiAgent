import copy
from board import Board


def eval_function(game_state):
    return 0


class MiniMaxNode:

    parent = None

    def __init__(self, val: int, mode: str):
        self.val = val
        self.children = []
        self.mode = mode

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        if len(self.children) == 7:
            return Exception("Cant have more than 7 children!")
        child.set_parent(self)
        self.children.append(child)


def minimax(node: MiniMaxNode, depth: int, isMaximizingPlayer: bool, alpha: int, beta: int):

    if len(node.children) == 0:
        return eval_function(node.game_state)

    if isMaximizingPlayer:
        bestVal = -99999999999999999
        for child in node.children:
            value = minimax(node, depth+1, false, alpha, beta)
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal

    else:
        bestVal = +99999999999999999
        for child in node.children:
            value = minimax(node, depth+1, true, alpha, beta)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal


class MiniMaxTree:

    # at any level there are <= 7 possible choices for the current agent

    def __init__(self, game_state):
        self.root = MiniMaxNode(0, "max")
        self.game_state = copy.deepcopy(game_state)

        # go 5 levels deep around 16000 nodes
        game_state
