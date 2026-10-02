class GamePiece:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col

    def set_position(self, row, col):
        self.row = row
        self.col = col

class Fox(GamePiece):
    def __init__(self, row, col):
        super().__init__(row, col)

class Hound(GamePiece):
    def __init__(self, row, col):
        super().__init__(row, col)