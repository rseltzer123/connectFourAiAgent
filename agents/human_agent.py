from agent import Agent


class HumanAgent(Agent):
    def take_turn(self, game_state) -> str:
        return input(f"Player {self.player_id} ({self.color}), choose a column: ")
