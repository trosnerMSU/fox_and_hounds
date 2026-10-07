import matplotlib.pyplot as plt
from matplotlib import transforms
from matplotlib.patches import Polygon, Circle
from IPython.display import clear_output

import numpy as np
import time
from enum import Enum
from typing import List, Tuple

from GamePieces import GamePiece, Fox, Hound
from GameResults import GameResults, GameWinnerType

class GameBoard:
    def __init__(self):
        self.fox = Fox(0, 0)
        self.hounds = [
            Hound(5, 5),
            Hound(5, 3),
            Hound(4, 4),
            Hound(3, 5)
        ]
        self.game_squares = [
            (0, 0), (2, 0), (4, 0),
            (1, 1), (3, 1), (5, 1),
            (0, 2), (2, 2), (4, 2),
            (1, 3), (3, 3), (5, 3),
            (0, 4), (2, 4), (4, 4),
            (1, 5), (3, 5), (5, 5)
        ]
        self.fox_goal_state = (5, 5)

    def get_next_fox_moves(self, position=None):
        if position is None:
            position = self.fox.get_position()

        # get all fox neighbor squares
        new_positions = self.get_fox_neighbors(position)

        # only include valid new positions
        valid_next_positions = [
            valid_square for valid_square in self.get_available_squares()
            if valid_square in new_positions
        ]

        return valid_next_positions

    def get_fox_neighbors(self, position):
        return [
            (position[0] + 1, position[1] + 1),
            (position[0] + 1, position[1] - 1),
            (position[0] - 1, position[1] + 1),
            (position[0] - 1, position[1] - 1)
        ]

    def get_next_hound_moves(self, position):
        # get hound neighbors
        new_positions = self.get_hound_neighbors(position)

        # include valid positions
        valid_next_positions = [
            valid_square for valid_square in self.get_available_squares()
            if valid_square in new_positions
        ]

        return valid_next_positions

    def get_hound_neighbors(self, position):
        return [
            (position[0] - 1, position[1] - 1),
            (position[0] + 1, position[1] - 1),
            (position[0] - 1, position[1] + 1)
        ]


    def get_available_squares(self):
        # include hound positons
        occupied_positions = {
            (hound.row, hound.col) for hound in self.hounds
        }

        # include the fox position
        occupied_positions.add((self.fox.row, self.fox.col))

        # only grab the non-occupied squares
        available_squares = [
            square for square in self.game_squares
            if square not in occupied_positions
        ]

        return available_squares

    def run(self, mode):
        fox_ai = mode.fox_ai
        hounds_ai = mode.hounds_ai
        count = 0
        max_loops = 1000

        results = GameResults()
        while not results.finished:
            if count >= max_loops:
                raise ValueError("Max loop iterations exceeded")
            
            # fox goes first
            fox_move = fox_ai.choose_move(self)
            if fox_move:
                fox, pos = fox_move
                self.move_fox(pos)
                if (mode.display):
                    time.sleep(0.25)
                    self.display()

            # check for winner
            self.check_winner(results)

            # hounds go second
            hounds_move = hounds_ai.choose_move(self)
            if hounds_move:
                hound, pos = hounds_move
                self.move_hound(hound, pos)
                if (mode.display):
                    time.sleep(0.25)
                    self.display()

            # check for winner
            self.check_winner(results)

            # increment count
            count += 1

        # return with the game results
        return results

    def move_fox(self, new_pos):
        # validate that the new position is a valid next move
        next_possible_moves = self.get_next_fox_moves()
        if (new_pos in next_possible_moves):
            self.fox.set_position(new_pos[0], new_pos[1])
        else:
            raise ValueError("Failed to move fox")

    def move_hound(self, hound, new_pos):
        # validate that the new position is a valid next move
        next_possible_moves = self.get_next_hound_moves(hound.get_position())
        if (new_pos in next_possible_moves):
            self.hounds[self.hounds.index(hound)].set_position(new_pos[0], new_pos[1])
        else:
            raise ValueError("Failed to move hound")

    def check_winner(self, results):
        if self.check_fox_winner():
            results.declare_winner(GameWinnerType.FOX)
        elif self.check_hounds_winner():
            results.declare_winner(GameWinnerType.HOUNDS)

    def check_fox_winner(self):
        return self.fox.get_position() == self.fox_goal_state

    def check_hounds_winner(self):
        next_fox_moves = self.get_next_fox_moves()
        if not next_fox_moves:
            return True
        return False

    def display(self):
        clear_output(wait=True)
        board = np.indices((6, 6)).sum(axis=0) % 2
        fig, ax = plt.subplots()

        # draw game board
        image = ax.imshow(
            board, 
            cmap="gray",
            extent=(-0.5, 5.5, 5.5, -0.5),
            interpolation="nearest"
        )

        # rotate the board
        rotation = transforms.Affine2D().rotate_deg_around(
            2.5,
            2.5,
            45
        )

        image.set_transform(rotation + ax.transData)

        # draw fox
        fox_circle = Circle(
            (self.fox.col, self.fox.row),
            radius=0.3,
            facecolor="red",
            edgecolor="black",
            linewidth=2
        )
        fox_circle.set_transform(rotation + ax.transData)
        ax.add_patch(fox_circle)

        # draw hounds
        for hound in self.hounds:
            hound_circle = Circle(
                (hound.col, hound.row),
                radius=0.3,
                facecolor="blue",
                edgecolor="black",
                linewidth=2
            )
            hound_circle.set_transform(rotation + ax.transData)
            ax.add_patch(hound_circle)

        # give the rotated board enough room
        ax.set_xlim(-2, 7)
        ax.set_ylim(7, -2)
    
        ax.axis("off")

        # add border
        border_points = [
            (-0.5, -0.5),
            (5.5, -0.5),
            (5.5, 5.5),
            (-0.5, 5.5)
        ]
        
        border = Polygon(
            border_points,
            closed=True,
            fill=False,
            edgecolor="black",
            linewidth=3
        )
        
        border.set_transform(rotation + ax.transData)
        ax.add_patch(border)
    
        plt.show()