from constants import *
from functions import *
from classes.tile import Tile

class Maze:
    def __init__(self):
        self.maze_data = generate_maze(mode="random")
        self.tiles_set = self.get_tiles_set()

    def get_tiles_set(self):
        tiles = set()

        for i in range(N_ROWS):
            for j in range(N_COLS):
                state = self.maze_data[i, j]

                new_tile = Tile(
                    (i, j), state=state
                )

                tiles.add(new_tile)

        return tiles
    
    def draw(self, win):
        w, h = win.get_size()
        
        for tile in self.tiles_set:
            tile.draw(win)
        
        # Hence the boundaries must be drawn after the drawing of the maze
        pygame.draw.lines(win, WALL_BOUNDARY, True, [(0, h-1), (w-1, h-1), (w-1, 0), (0, 0)])