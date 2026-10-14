# Fox and Hounds '45

## Overview

This project implements a 6×6 variant of **Fox and Hounds '45** in Python. One Fox attempts to reach the opposite corner of the board while four Hounds attempt to trap it.

The project compares random and AI-based strategies using repeated game simulations.

## Game Rules

- The Fox starts at `(0, 0)` and wins by reaching `(5, 5)`.
- The Fox can move diagonally in any valid direction.
- Hounds move diagonally according to their allowed movement rules.
- Pieces cannot move onto occupied squares.
- The Hounds win when the Fox has no valid moves.
- A game is declared a draw if the same board configuration occurs 100 times.

## AI Strategies

### Fox

- **Random AI** — selects a random legal move.
- **Shortest-Path AI** — uses Breadth-First Search (BFS) to search for the goal and chooses the first move along a shortest available path. If the goal cannot currently be reached, it moves toward the reachable position closest to the goal.

### Hounds

- **Random AI** — randomly selects a movable Hound and one of its legal moves.
- **Minimax AI** — performs a depth-limited Minimax search with the Hounds as the maximizing player and the Fox as the minimizing player. The current search depth is 4.

The Minimax heuristic rewards states where the Fox is farther from the goal and has fewer available moves:

```text
score = (fox_distance * 10) - (fox_moves * 2)
```

Terminal Hound wins receive `+1000`, while Fox wins receive `-1000`.

## Game Modes

The following strategy combinations are supported:

1. Random Fox vs. Random Hounds
2. Random Fox vs. Minimax Hounds
3. Shortest-Path Fox vs. Random Hounds
4. Shortest-Path Fox vs. Minimax Hounds

## Project Structure

```text
fox_and_hounds/
├── AIStrategy.py
├── GameBoard.py
├── GameBoardExecutor.py
├── GameMode.py
├── GamePieces.py
├── GameResults.py
├── fox_and_hounds.ipynb
├── environment.yml
└── README.md
```

`GameBoard` contains the game state, movement rules, win detection, draw detection, and Matplotlib board display. AI decision-making is separated into strategy classes in `AIStrategy.py`.

`GameBoardExecutor` uses `ThreadPoolExecutor` to run multiple independent simulations, with a separate `GameBoard` created for each game.

## Setup

Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate fox_and_hounds
```

Start JupyterLab:

```bash
jupyter lab
```

Then open `fox_and_hounds.ipynb`.

## Running Simulations

Create a `GameMode` with the desired mode and number of simulations, then run it through `GameBoardExecutor`.

```python
game_mode = GameMode(choice=4, iters=100)

executor = GameBoardExecutor()
results = executor.run(game_mode)
```

For small simulation counts, the board can be displayed using Matplotlib. Larger runs automatically disable visualization.

## Technologies

Python, Jupyter Notebook, Conda, Matplotlib, NumPy, BFS, Minimax, and `concurrent.futures`.

## Author

Developed for **COSC 523 at the University of Tennessee, Knoxville** as an implementation and analysis of search and game-playing algorithms.
