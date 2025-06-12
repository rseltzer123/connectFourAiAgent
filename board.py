class Board:

    # [['','','','','',''],['','','','','',''],['','','','','',''],['','','','','',''],['','','','','',''],['','','','','','']]

    game_state: list[list[str]] = []
    ROWS: int = 6
    COLUMNS: int = 7

    def __init__(self):
        self.game_state = [
            [['' for _ in range(self.ROWS)] for _ in range(self.COLUMNS)]]

    def reset(self):
        self.game_state = [
            [['' for _ in range(self.ROWS)] for _ in range(self.COLUMNS)]]

    def get_game_state(self):
        return self.game_state

    def get_cell(self, column, row):
        if 0 <= row < self.COLUMNS and 0 <= column < self.ROWS:
            return self.game_state[column][row]
        else:
            raise IndexError("Row or column out of bounds")

    def set_cell(self, column, row, value):
        if not isinstance(value, str) and (value != 'red' and value != 'black'):
            raise ValueError("Value must be 'red' or 'black'")
        if 0 <= row < self.COLUMNS and 0 <= column < self.ROWS:
            self.game_state[column][row] = value
        else:
            raise IndexError("Row or column out of bounds")

    def is_full(self):
        for col in self.game_state:
            if '' in col:
                return False
        return True

    def is_winner(self, player):
        # Check horizontal, vertical, and diagonal lines for a win
        for col in range(self.COLUMNS):
            for row in range(self.ROWS):
                if self.check_win_direction(col, row, 1, 0, player) or \
                   self.check_win_direction(col, row, 0, 1, player) or \
                   self.check_win_direction(col, row, 1, 1, player) or \
                   self.check_win_direction(col, row, 1, -1, player):
                    return True
        return False

    def check_win_direction(self, col, row, delta_col, delta_row, player):
        # Check for four in a row in a specific direction
        for i in range(4):
            if not (0 <= col + i * delta_col < self.COLUMNS and
                    0 <= row + i * delta_row < self.ROWS):
                return False
            if self.game_state[col + i * delta_col][row + i * delta_row] != player:
                return False
        return True

    def __str__(self):
        board_str = ""
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                cell = self.get_cell(col, row)
                board_str += f"{cell or '.'} "
            board_str += "\n"
        return board_str
