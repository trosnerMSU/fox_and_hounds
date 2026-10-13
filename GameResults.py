from enum import Enum

class GameResults:
    def __init__(self):
        self.finished = False
        self.winner = GameWinnerType.NONE
        self.turns = 0

    def declare_winner(self, winner, turns=None):
        self.finished = True
        self.winner = winner
        self.turns = turns

class GameWinnerType(Enum):
    NONE = 1
    FOX = 2
    HOUNDS = 3
    DRAW = 4
