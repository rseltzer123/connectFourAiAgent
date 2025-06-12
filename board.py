class Board:

    ROWS: int = 6
    COLUMNS: int = 7

    def __init__(self):
        self.reset()

    def reset(self):
        self.game_state = [
            ['' for _ in range(self.COLUMNS)] for _ in range(self.ROWS)
        ]

    def get_game_state(self):
        return self.game_state

    def get_cell(self, column: int, row: int) -> str:
        if 0 <= row < self.ROWS and 0 <= column < self.COLUMNS:
            return self.game_state[row][column]
        else:
            raise IndexError("Row or column out of bounds")

    def set_cell(self, column: int, row: int, value: str) -> None:
        if value not in ("red", "black", ""):
            raise ValueError("Value must be 'red', 'black', or ''")
        if 0 <= row < self.ROWS and 0 <= column < self.COLUMNS:
            self.game_state[row][column] = value
        else:
            raise IndexError("Row or column out of bounds")

    def get_next_row(self, column: int):
        if not 0 <= column < self.COLUMNS:
            return None
        for row in range(self.ROWS - 1, -1, -1):
            if self.game_state[row][column] == "":
                return row
        return None

    def drop_piece(self, column: int, player: str) -> bool:
        row = self.get_next_row(column)
        if row is None:
            return False
        self.set_cell(column, row, player)
        return True

    def is_full(self):
        for row in self.game_state:
            if "" in row:
                return False
        return True

    def is_winner(self, player):
        # horizontal
        for row in range(self.ROWS):
            for col in range(self.COLUMNS - 3):
                if all(self.game_state[row][col + i] == player for i in range(4)):
                    return True
        # vertical
        for col in range(self.COLUMNS):
            for row in range(self.ROWS - 3):
                if all(self.game_state[row + i][col] == player for i in range(4)):
                    return True
        # diagonal down-right
        for row in range(self.ROWS - 3):
            for col in range(self.COLUMNS - 3):
                if all(self.game_state[row + i][col + i] == player for i in range(4)):
                    return True
        # diagonal up-right
        for row in range(3, self.ROWS):
            for col in range(self.COLUMNS - 3):
                if all(self.game_state[row - i][col + i] == player for i in range(4)):
                    return True
        return False

    def check_win_direction(self, col, row, delta_col, delta_row, player):
        for i in range(4):
            c = col + i * delta_col
            r = row + i * delta_row
            if not (0 <= c < self.COLUMNS and 0 <= r < self.ROWS):
                return False
            if self.game_state[r][c] != player:
                return False
        return True

    def __str__(self):
        board_str = ""
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                cell = self.get_cell(col, row)
                cell = cell[0] if cell else ''
                board_str += f"{cell or '.'} "
            board_str += "\n"
        return board_str
