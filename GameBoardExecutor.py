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
                # add each game execution to thread pool
                future = executor.submit(
                    self.run_game,
                    game_mode
                )

                futures.append(future)

            for future in as_completed(futures):
                winner = future.result()
                results.append(winner)
            
        return results

    def run_game(self, game_mode):
        game_results = GameBoard().run(game_mode)
        return game_results

            