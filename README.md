# Fox and Hounds '45

## Overview

This project implements a custom variant of checkers called **Fox and Hounds '45** in Python using a Jupyter Notebook.

The game consists of one Fox and four Hounds on a 6×6 board. The Fox attempts to reach the opposite side of the board while the Hounds attempt to trap the Fox so that it has no valid moves remaining.

The project includes both random and AI-based strategies for the Fox and Hounds and supports running multiple simulations to compare their performance.

## Game Rules

- The game is played on a 6×6 board.
- Only designated playable squares are used.
- The Fox begins in one corner of the board.
- Four Hounds begin on the opposite side.
- The Fox moves diagonally in any valid direction.
- The Hounds move diagonally according to their allowed movement rules.
- Pieces cannot move onto occupied squares.
- The Fox wins by reaching the target square on the opposite side of the board.
- The Hounds win if the Fox has no remaining valid moves.

## Project Structure

```text
fox_and_hounds/
│
├── GameBoard.py
├── GamePieces.py
├── GameResults.py
├── fox_and_hounds.ipynb
├── environment.yml
└── README.md
```

### GameBoard.py

Contains the main game state and game logic.

Responsibilities include:

- Initializing the board
- Tracking Fox and Hound positions
- Determining available board squares
- Generating valid Fox moves
- Generating valid Hound moves
- Moving pieces
- Checking win conditions
- Running the game loop
- Displaying the game board

### GamePieces.py

Contains the game-piece classes, including:

- `GamePiece`
- `Fox`
- `Hound`

Each piece stores its current row and column position.

### GameResults.py

Stores information about the result of a completed game.

This includes the winner and whether the game has finished.

### fox_and_hounds.ipynb

The primary Jupyter Notebook used to configure, run, display, and analyze game simulations.

## AI Strategies

The project supports multiple strategies for each side.

### Fox Random AI

The random Fox strategy:

1. Retrieves all valid moves from the `GameBoard`.
2. Randomly selects one of the available moves.
3. Returns the selected move to the board.

### Fox Shortest-Path AI

The Fox AI searches for a path toward the goal using a shortest-path search strategy.

The algorithm evaluates legal board positions and attempts to select the next move that gives the Fox the best path toward the destination while avoiding occupied squares.

### Hounds Random AI

The random Hounds strategy:

1. Randomizes the order of the Hounds.
2. Checks each Hound for available moves.
3. Selects a Hound that can move.
4. Randomly selects one of that Hound's valid positions.

If none of the Hounds have a legal move, the strategy returns an empty tuple.

### Hounds Minimax AI

The Hounds Minimax strategy evaluates possible future game states in order to choose moves that reduce the Fox's ability to reach the goal.

The Hounds attempt to maximize their chances of trapping the Fox while minimizing the Fox's ability to progress across the board.

## Game Modes

Different combinations of strategies can be tested, including:

- Random Fox vs. Random Hounds
- Random Fox vs. Minimax Hounds
- Shortest-Path Fox vs. Random Hounds
- Shortest-Path Fox vs. Minimax Hounds

These modes make it possible to compare AI performance against random baseline strategies.

## Running Multiple Simulations

Multiple games can be executed using `GameBoardExecutor`.

Each simulation receives its own `GameBoard` instance.

Example structure:

```python
executor = GameBoardExecutor()
results = executor.run(game_mode)
```

The executor uses Python's `ThreadPoolExecutor` to submit multiple independent games.

Completed games are collected using `as_completed()`.

Because each simulation receives a separate board, game state is not shared between simulations.

## Board Display

The game board is displayed using Matplotlib.

The board is rotated 45 degrees to produce the diamond-shaped appearance of a traditional checkers board.

The pieces are represented as:

- Red circle — Fox
- Blue circles — Hounds

When display mode is enabled, Jupyter output is cleared before drawing the next board state:

```python
clear_output(wait=True)
```

This allows the game to update the existing display instead of creating a new board image after every move.

A short `time.sleep()` delay can also be used between moves to make the simulation easier to observe.

## Environment Setup

This project uses Conda for dependency management.

Create the environment from the included YAML file:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate fox_and_hounds
```

If the environment already exists and the YAML file has changed:

```bash
conda env update -f environment.yml --prune
```

## Running JupyterLab

After activating the environment:

```bash
jupyter lab
```

Then open:

```text
fox_and_hounds.ipynb
```

If JupyterLab is not installed in the environment:

```bash
conda install jupyterlab
```

## Running the Project

1. Clone the repository.
2. Create the Conda environment.
3. Activate the environment.
4. Start JupyterLab.
5. Open `fox_and_hounds.ipynb`.
6. Select a game mode.
7. Configure the number of simulations.
8. Run the game or simulation cells.

Example:

```python
game_board = GameBoard()
results = game_board.run(game_mode)
```

For multiple simulations:

```python
executor = GameBoardExecutor()
results = executor.run(game_mode)
```

## Design Decisions

The project separates game rules from AI decision-making.

`GameBoard` is responsible for determining what moves are legal, while each AI strategy is responsible for deciding which legal move should be selected.

This prevents individual AI implementations from duplicating board rules.

For example:

```python
valid_moves = game_board.get_next_fox_moves()
```

The AI can use the returned positions to make its decision without modifying how legal moves are calculated.

The project also creates a new `GameBoard` for every simulation. This keeps game state independent when multiple games are executed concurrently.

## Future Improvements

Possible future improvements include:

- Improving the Fox pathfinding heuristic
- Increasing the depth of the Hounds Minimax search
- Adding Alpha-Beta pruning
- Tracking average game duration
- Tracking the average number of moves
- Comparing win percentages between AI strategies
- Improving simulation performance
- Adding additional board visualization options
- Supporting reproducible simulations using random seeds

## Technologies

- Python
- Jupyter Notebook
- Conda
- Matplotlib
- NumPy
- `concurrent.futures`
- Object-Oriented Programming
- Shortest-path search
- Minimax search

## Author

Developed for COSC 523 at UT Knoxville as an implementation and analysis of search, game-playing, and artificial intelligence algorithms.