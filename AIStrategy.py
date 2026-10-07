from abc import ABC, abstractmethod
from collections import deque
import random

class AIStrategy:
    @abstractmethod
    def choose_move(self, board):
        pass

class HoundsRandomAI(AIStrategy):
    def choose_move(self, board):
        # shallow copy hounds list
        hounds_copy = board.hounds.copy()

        # shuffle the hounds order
        random.shuffle(hounds_copy)

        # for each hound try to find a next valid move
        for hound in hounds_copy:
            next_moves = board.get_next_hound_moves(hound.get_position())
            if not next_moves:
                continue
            else:
                return hound, random.choice(next_moves)

        # if no next moves then return empty
        return ()      

class HoundsMinimaxAI(AIStrategy):
    def choose_move(self, board):
        pass

class FoxRandomAI(AIStrategy):
    def choose_move(self, board):
        next_moves = board.get_next_fox_moves()
        if not next_moves:
            return ()
        return board.fox, random.choice(next_moves)

# uses Breadth-First Search (BFS)
class FoxShortPathAI(AIStrategy):
    def choose_move(self, board):
        start = board.fox.get_position()
        queue = deque([start])
        visited = {start}

        # keep track of the first move for each square
        first_move = {}

        # track the shortest distance to goal state
        shortest_distance_neighbor = None
        shortest_distance = None

        while queue:
            current = queue.popleft()

            neighbors = board.get_next_fox_moves(current)
            random.shuffle(neighbors)

            for neighbor in neighbors:
                if neighbor in visited:
                    continue

                visited.add(neighbor)
                queue.append(neighbor)

                # if this is the first move then set first move to itself
                if current == start:
                    first_move[neighbor] = neighbor
                else:
                    # otherwise, inherit the first move of the current
                    first_move[neighbor] = first_move[current]

                # if this neighbor square is the goal state then return first move
                if neighbor == board.fox_goal_state:
                    return board.fox, first_move[neighbor]

                # if we didn't hit a goal state then track the distance
                neighbor_distance = (abs(neighbor[0] - board.fox_goal_state[0]) 
                                     + abs(neighbor[1] - board.fox_goal_state[1]))

                # if neighbor distance to goal state is new shortest distance then update
                if shortest_distance is None or neighbor_distance < shortest_distance:
                    shortest_distance = neighbor_distance
                    shortest_distance_neighbor = neighbor

        # if we get to this point then we did not reach our goal state as the fox,
        # therefore we need to return the shortest distance neighbor to goal state
        if shortest_distance_neighbor is not None:
            return board.fox, first_move[shortest_distance_neighbor]

        # if no available neighbors then return empty
        return ()

                
