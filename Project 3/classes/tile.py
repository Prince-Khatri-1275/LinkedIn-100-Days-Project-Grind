import pygame
from constants import *
from functions import get_rect, get_color_from_tile_state

class Tile:
    def __init__(self, pos, state="wall", paths=None):
        self.cords = pos
        self.rect = get_rect(pos, "tile")
        self._color = get_color_from_tile_state(state)
        
        if paths:
            self.paths = paths
        else:
            self.paths = {
                "up":"n",
                "down":"n",
                "right":"n",
                "left":"n"
            }
    
    def draw(self, win):
        pygame.draw.rect(win, self._color, self.rect) # type:ignore for error of the cause of rect having None as potential val
    
    def update_paths(self, way, code):
        """
            Here way is the key to path takes values of
            up, down, right and left whereas,
            -------------------------------------------
            code takes values of 
                `y`: yes the path is available
                `n`: not available path
                `r`: restricted or out of bound in 
                    case if the tile is boundary tile
        """
        self.paths[way] = code