"""


@author John Harris
"""
import numpy as np


class ApplicationModel:
    WHITE = "WHITE"
    BLACK = "BLACK"
    in_check = False
    can_castle = False
    current_player_move = WHITE
    board = np.empty(8, 8, dtype=object)

    def __init__(self):
        print("this is the model")
        self.setup_board()

    def add_piece(self, row, col, piece):
        self.board[row][col] = piece
