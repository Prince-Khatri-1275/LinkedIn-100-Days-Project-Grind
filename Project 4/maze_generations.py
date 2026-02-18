import numpy as np
from constants import *

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

def dfs_for_maze_generation(tiles):
    return tiles