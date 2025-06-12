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
        try:
            column = int(self.current_agent.take_turn(self.board.get_game_state()))
        except ValueError:
            print("Invalid input. Please enter a column number.")
            return False
        if not (0 <= column < self.board.COLUMNS):
            print("Invalid column. Try again.")
            return False
        if not self.board.drop_piece(column, self.current_agent.color):
            print("Column is full. Try again.")
            return False
        print(self.board)
        if self.board.is_winner(self.current_agent.color):
            print(f"{self.current_agent.color} wins!")
            self.is_over = True
        elif self.board.is_full():
            print("The game is a draw.")
            self.is_over = True
        else:
            self.switch_agents()
        return True

    def switch_agents(self):
        self.current_agent = self.agent2 if self.current_agent == self.agent1 else self.agent1
