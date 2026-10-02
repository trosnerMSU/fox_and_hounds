class GamePiece:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def introduction(self):
        print("GamePiece is initialized")

class Fox(GamePiece):
    def __init__(self, row, col):
        super().__init__(row, col)

    def introduction(self):
        print("Fox is initialized")

class Hound(GamePiece):
    def __init__(self, row, col):
        super().__init__(row, col)

    def introduction(self):
        print("Hound is initialized")