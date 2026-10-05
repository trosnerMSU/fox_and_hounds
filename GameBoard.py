import matplotlib.pyplot as plt
from matplotlib import transforms
from matplotlib.patches import Polygon, Circle

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

    def get_timestamp(self):
        return time.perf_counter()

    def get_elapsed_time(self, start, end):
        return end - start

    def get_next_fox_moves(self):
        # get all possible new positions
        new_positions = [
            (self.fox.row + 1, self.fox.col + 1),
            (self.fox.row + 1, self.fox.col - 1),
            (self.fox.row - 1, self.fox.col + 1),
            (self.fox.row - 1, self.fox.col - 1)
        ]

        # only include valid new positions
        valid_next_positions = [
            valid_square for valid_square in self.get_available_squares()
            if valid_square in new_positions
        ]

        return valid_next_positions

    def get_next_hound_moves(self, hound):
        # first, grab hound index (confirms this hound exists)
        hound_index = self.hounds.index(hound)

        # get all possible new positions
        hound = self.hounds[hound_index]
        new_positions = [
            (hound.row - 1, hound.col - 1),
            (hound.row + 1, hound.col - 1),
            (hound.row - 1, hound.col + 1)
        ]

        # include valid positions
        valid_next_positions = [
            valid_square for valid_square in self.get_available_squares()
            if valid_square in new_positions
        ]

        return valid_next_positions


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

    def move_fox(self, new_pos):
        # validate that the new position is a valid next move
        next_possible_moves = self.get_next_fox_moves()
        if (new_pos in next_possible_moves):
            self.fox.set_position(new_pos[0], new_pos[1])
        else:
            raise ValueError("Failed to move fox")

    def move_hound(self, hound, new_pos):
        # validate that the new position is a valid next move
        next_possible_moves = self.get_next_hound_moves(hound)
        if (new_pos in next_possible_moves):
            self.hounds[self.hounds.index(hound)].set_position(new_pos[0], new_pos[1])
        else:
            raise ValueError("Failed to move hound")

    def run(self, mode):
        fox_ai = mode.fox_ai
        hounds_ai = mode.hounds_ai

        results = GameResults()
        while not results.finished:
            # fox goes first
            fox_move = fox_ai.choose_move(self)
            if fox_move:
                fox, pos = fox_move
                self.move_fox(pos)

            # hounds go second
            hounds_move = hounds_ai.choose_move(self)
            if hounds_move:
                hound, pos = hounds_move
                self.move_hound(hound, pos)

            # check for winner
            # self.check_winner(results)
            results.declare_winner(GameWinnerType.FOX)

        # return with the game results
        return results


    def display(self):
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