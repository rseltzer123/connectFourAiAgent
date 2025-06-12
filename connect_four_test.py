import random
import pytest

from board import Board

ROWS = Board.ROWS
COLUMNS = Board.COLUMNS


def has_winner(state, player):
    # horizontal
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all(state[r][c + i] == player for i in range(4)):
                return True
    # vertical
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if all(state[r + i][c] == player for i in range(4)):
                return True
    # diagonal down-right
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all(state[r + i][c + i] == player for i in range(4)):
                return True
    # diagonal up-right
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all(state[r - i][c + i] == player for i in range(4)):
                return True
    return False


def generate_full_board(seed):
    random.seed(seed)
    board = []
    for _ in range(ROWS):
        row_vals = []
        for _ in range(COLUMNS):
            row_vals.append(random.choice(["red", "black"]))
        board.append(row_vals)
    return board


TEST_CASES = []
for case in range(100):
    state = generate_full_board(case)
    red_win = has_winner(state, "red")
    black_win = has_winner(state, "black")
    case_id = f"case_{case}_red_{int(red_win)}_black_{int(black_win)}"
    TEST_CASES.append(pytest.param(case, state, red_win, black_win, id=case_id))


def set_board_state(board: Board, state):
    for r in range(ROWS):
        for c in range(COLUMNS):
            board.set_cell(c, r, state[r][c])


@pytest.mark.parametrize("case_num,state,exp_red,exp_black", TEST_CASES)
def test_full_board_states(case_num, state, exp_red, exp_black):
    """Check winner detection on 100 filled boards."""
    board = Board()
    set_board_state(board, state)
    assert board.is_full(), f"Case {case_num} board should be full"
    assert board.is_winner("red") == exp_red
    assert board.is_winner("black") == exp_black
