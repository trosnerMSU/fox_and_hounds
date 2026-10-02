import matplotlib.pyplot as plt
from matplotlib import transforms
from matplotlib.patches import Polygon, Circle

import numpy as np
import time
from enum import Enum
from typing import List, Tuple

from GamePieces import GamePiece, Fox, Hound

class GameBoard:
    def __init__(self):
        self.fox = Fox(0, 0)
        self.hounds = [
            Hound(5, 5),
            Hound(5, 3),
            Hound(4, 4),
            Hound(3, 5)
        ]

    def get_timestamp(self):
        return time.perf_counter()

    def get_elapsed_time(self, start, end):
        return end - start

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