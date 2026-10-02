from enum import Enum

class GameResults:
    def __init__(self):
        self.finished = False
        self.winner = GameWinnerType.NONE

    def declare_winner(self, winner):
        self.finished = True
        self.winner = winner

class GameWinnerType(Enum):
    NONE = 1
    FOX = 2
    HOUNDS = 3
