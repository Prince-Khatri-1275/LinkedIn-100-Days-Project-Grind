import numpy as np
from constants import *

# Adding a decorator to keep neighbors in sync after generation
def sync_neighbors(func):
    def wrapper(*args, **kwargs):
        tiles = func(*args, **kwargs)
        return keep_in_sync(tiles)
    return wrapper

@sync_neighbors
def random_generation(tiles):
    for tile in tiles.values():
        k_neigh = np.random.randint(0, 5)
        
        # Choosing k neighbors randomly to the tile but this has a flaw as it is not keeping & maintaining the neighbors set book of neighbors
        chosen_neighbors = set(
                np.random.choice(
                    list(tile.available_neighbors), 
                    size=k_neigh
                )
            )
        for chosen_neighbor in chosen_neighbors:
            tile.update_neighbors(chosen_neighbor)
        
    return tiles

@sync_neighbors
def dfs_for_maze_generation(tiles):
    return tiles

def keep_in_sync(tiles):
    """
    This is a helper function to keep the neighbors of the tiles in sync with each other.
    For example if tile A has tile B as its neighbor then tile B should also have tile
    """
    for pos, tile in tiles.items():
        for neighbor in tile.neighbors:
            i, j = pos
            match neighbor:
                case "up":
                    if (i-1, j) in tiles:
                        tiles[(i-1, j)].update_neighbors("down")
                case "down":
                    if (i+1, j) in tiles:
                        tiles[(i+1, j)].update_neighbors("up")
                case "left":
                    if (i, j-1) in tiles:
                        tiles[(i, j-1)].update_neighbors("right")
                case "right":
                    if (i, j+1) in tiles:
                        tiles[(i, j+1)].update_neighbors("left")
    return tiles