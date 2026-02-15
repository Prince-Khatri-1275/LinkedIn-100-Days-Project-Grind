import numpy as np
from constants import *

def random():
    return np.random.choice(POSSIBLE_TILE_STATES, TILES_SHAPE)

def dfs():
    ...