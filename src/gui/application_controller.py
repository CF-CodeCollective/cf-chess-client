"""
Handles all logic in the program

@author John Harris
"""
import application_view as view
import application_model as model
import pieces.pawn as pawn


class ApplicationController:

    def __init__(self, application_view):
        self.application_view = application_view
        self.application_model = model.ApplicationModel

    def fill_board(self):
        # create pawns for white, same is applied for black pawns and then individually add in special pieces
        for i in range(8):
            self.application_model.add_piece(1, i, pawn.Pawn("WHITE", self.create_starting_notation(2, i)))

    def create_starting_notation(self, number, index):
        # will be refactored but takes the current row you
        letter_notation = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
        return letter_notation[index] + number
