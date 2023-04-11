import possible_moves as moves


class Knight:

    def __init__(self, team, current_location):
        self.team = team
        self.current_location = current_location

    # returns a list of possible moves that can be applied to the list
    def possible_moves(self):
        # Our first example being that the knight can move up one square and 2 to the left
        return {moves.PossibleMoves(-1, 2), moves.PossibleMoves(1, 2), moves.PossibleMoves(1, -2),
                moves.PossibleMoves(-1, -2), moves.PossibleMoves(-2, -1), moves.PossibleMoves(-2, 1),
                moves.PossibleMoves(2, -1), moves.PossibleMoves(2, 1)}
