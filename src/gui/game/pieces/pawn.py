import possible_moves as moves

class Pawn:

    def __init__(self, team, current_location):
        self.team = team
        self.current_location = current_location
        self.first_move = True

    def possible_moves(self):
        # First one is only possible if first_move is True Last one is En Passant
        return {moves.PossibleMoves(0, 2), moves.PossibleMoves(0, 1), moves.PossibleMoves(1, 1)}
