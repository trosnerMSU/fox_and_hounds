from enum import Enum
from AIStrategy import HoundsRandomAI, HoundsMinimaxAI, FoxRandomAI, FoxShortPathAI

class GameMode:
    def __init__(self, choice, iters):
        self.mode = GameModeType(choice)
        self.iters = iters
        if self.iters >= 1 and self.iters <= 3:
            self.display = True
        else:
            self.display = False
        
        if self.mode == GameModeType.RANDOM_RANDOM:
            print("Random fox vs Random hounds")
            self.fox_ai = FoxRandomAI()
            self.hounds_ai = HoundsRandomAI()
        elif self.mode == GameModeType.RANDOM_AI:
            print("Random fox vs Minimax hounds")
            self.fox_ai = FoxRandomAI()
            self.hounds_ai = HoundsMinimaxAI()
        elif self.mode == GameModeType.AI_RANDOM:
            print("Shortest path fox vs Random hounds")
            self.fox_ai = FoxShortPathAI()
            self.hounds_ai = HoundsRandomAI()
        elif self.mode == GameModeType.AI_AI:
            print("Shortest path fox vs Minimax hounds")
            self.fox_ai = FoxShortPathAI()
            self.hounds_ai = HoundsMinimaxAI()

class GameModeType(Enum):
    RANDOM_RANDOM = 1
    RANDOM_AI = 2
    AI_RANDOM = 3
    AI_AI = 4