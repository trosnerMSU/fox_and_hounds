from abc import ABC, abstractmethod

class AIStrategy:
    @abstractmethod
    def choose_move(self, fox, hounds, valid_positions):
        pass

class HoundsRandomAI(AIStrategy):
    def choose_move(self, fox, hounds, valid_positions):
        pass

class HoundsMinimaxAI(AIStrategy):
    def choose_move(self, fox, hounds, valid_positions):
        pass

class FoxRandomAI(AIStrategy):
    def choose_move(self, fox, hounds, valid_positions):
        pass

class FoxShortPathAI(AIStrategy):
    def choose_move(self, fox, hounds, valid_positions):
        pass