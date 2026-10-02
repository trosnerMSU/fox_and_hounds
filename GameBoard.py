from enum import Enum
from typing import List, Tuple
from GamePieces import GamePiece, Fox, Hound

import time

class GameBoard:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        self.start_time = time.perf_counter()

    def stop_timer(self):
        self.end_time = time.perf_counter()

    def get_elapsed_time(self):
        return self.end_time - self.start_time