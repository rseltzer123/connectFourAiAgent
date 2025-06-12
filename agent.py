class Agent:
    def __init__(self, color, player_id):
        self.color = color
        self.player_id = player_id

    def take_turn(self, game_state) -> int:
        column = int(
            input(f"Player {self.player_id} ({self.color}), choose a column: "))
        return column
