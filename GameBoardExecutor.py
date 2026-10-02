from GameBoard import GameBoard
from GameResults import GameResults, GameWinnerType
from concurrent.futures import ThreadPoolExecutor, as_completed

class GameBoardExecutor:
    def __init__(self):
        pass

    def run(self, game_mode):
        results = []

        with ThreadPoolExecutor() as executor:
            futures = []
            for i in range(game_mode.iters):
                board = GameBoard()

                # add each game execution to thread pool
                future = executor.submit(
                    self.run_game,
                    board,
                    game_mode
                )

                futures.append(future)

            for future in as_completed(futures):
                winner = future.result()
                results.append(winner)
            
        return results

    def run_game(self, game_board, game_mode):
        fox_ai = game_mode.fox_ai
        hounds_ai = game_mode.hounds_ai
        print("Game is executing...")
        game_results = GameResults()
        game_results.declare_winner(GameWinnerType.FOX)
        return game_results

            