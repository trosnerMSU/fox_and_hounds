from abc import ABC, abstractmethod
import random

class AIStrategy:
    @abstractmethod
    def choose_move(self, board):
        pass

class HoundsRandomAI(AIStrategy):
    def choose_move(self, board):
        # shallow copy hounds list
        hounds_copy = board.hounds.copy()

        # shuffle the hounds order
        random.shuffle(hounds_copy)

        # for each hound try to find a next valid move
        for hound in hounds_copy:
            next_moves = board.get_next_hound_moves(hound)
            if not next_moves:
                continue
            else:
                return hound, random.choice(next_moves)

        # if no next moves then return empty
        return ()      

class HoundsMinimaxAI(AIStrategy):
    def choose_move(self, board):
        pass

class FoxRandomAI(AIStrategy):
    def choose_move(self, board):
        next_moves = board.get_next_fox_moves()
        if not next_moves:
            return ()
        return board.fox, random.choice(next_moves)

class FoxShortPathAI(AIStrategy):
    def choose_move(self, board):
        pass