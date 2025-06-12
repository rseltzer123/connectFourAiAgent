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

    def find_winner_coords(self, player):
        """Return list of coordinates comprising a winning sequence."""
        # horizontal
        for row in range(self.ROWS):
            for col in range(self.COLUMNS - 3):
                if all(self.game_state[row][col + i] == player for i in range(4)):
                    return [(col + i, row) for i in range(4)]
        # vertical
        for col in range(self.COLUMNS):
            for row in range(self.ROWS - 3):
                if all(self.game_state[row + i][col] == player for i in range(4)):
                    return [(col, row + i) for i in range(4)]
        # diagonal down-right
        for row in range(self.ROWS - 3):
            for col in range(self.COLUMNS - 3):
                if all(self.game_state[row + i][col + i] == player for i in range(4)):
                    return [(col + i, row + i) for i in range(4)]
        # diagonal up-right
        for row in range(3, self.ROWS):
            for col in range(self.COLUMNS - 3):
                if all(self.game_state[row - i][col + i] == player for i in range(4)):
                    return [(col + i, row - i) for i in range(4)]
        return []

    def is_winner(self, player):
        return bool(self.find_winner_coords(player))

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
        return self.render_board()

    def render_board(self, highlight=None):
        """Return a string representation of the board.

        If ``highlight`` is provided, cells whose ``(col, row)`` tuples are in
        the iterable will be printed in yellow text.
        """
        highlight_set = set(highlight or [])
        board_str = ""
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                cell = self.get_cell(col, row)
                char = cell[0] if cell else '.'
                if (col, row) in highlight_set and cell:
                    board_str += f"\x1b[33m{char}\x1b[0m "
                else:
                    board_str += f"{char} "
            board_str += "\n"
        return board_str
