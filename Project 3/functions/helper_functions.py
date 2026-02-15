import pygame
import numpy as np
from constants import *
from functions import maze_generations

def get_rect(cords, category):
    if category == "tile":
        i, j = cords
        
        rect = pygame.rect.Rect(j*TILE_WIDTH, i*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        
        return rect
    
    
def get_color_from_tile_state(tile_state):
    match tile_state:
        case "wall": return WALL_COLOR
        case _: return SURF_COLOR

def generate_maze(mode="random"):
    match mode:
        case "random": return maze_generations.random()
        case _: return maze_generations.random()
