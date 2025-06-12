from board import Board
from agent import Agent


class Game:

    agent1: Agent
    agent2: Agent
    current_agent: Agent
    board: Board

    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2
        self.current_agent = agent1
        self.board = Board()
        self.is_over = False

    def do_turn(self):
        print(self.board)
        column = self.current_agent.take_turn(self.board.get_game_state())
        if not self.board.set_cell(column, self.board.get_next_row(column), self.current_agent.color):
            print("Invalid move. Try again.")
            return False
        if self.board.is_winner(self.current_agent.color):
            print(f"{self.current_agent.color} wins!")
            self.is_over = True
        elif self.board.is_full():
            print("The game is a draw.")
            self.is_over = True
        else:
            self.switch_agents()
        return True
