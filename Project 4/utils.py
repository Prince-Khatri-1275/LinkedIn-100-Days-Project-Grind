# Jai Shri Ram
# Jai Balaji Maharaaj Ki

import pygame
from constants import *
from maze_generations import *

class Tile:
    def __init__(self, pos_idx, neighbors:list|set|tuple|None=None, *, restrictions:None|tuple|list|set=None):
        i, j = pos_idx
        self.rect = pygame.rect.Rect(j*TILE_WIDTH, i*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        if neighbors:
            self.neighbors = set(neighbors)
        else:
            self.neighbors = set()

        self.available_neighbors = AVAILABLE_NEIGHBORS.copy()

        # If there are any restrictions i.e. edge or corner cases then remove those from options
        if restrictions:
            self.available_neighbors.difference_update(set(restrictions))

    def update_neighbors(self, val):
        if val in AVAILABLE_NEIGHBORS:
            self.neighbors.add(val)
        
    def draw(self, win):
        walls = AVAILABLE_NEIGHBORS.difference(self.neighbors)
        for wall in walls:
            cords = self._get_wall_cords(wall)
            
            if cords[0] is None or cords[1] is None:
                continue
            
            pygame.draw.line(win, WALL_COLOR, cords[0], cords[1], WALL_WIDTH)

    # Helper Function to draw and match walls
    def _get_wall_cords(self, wall):
        match wall:
            case "left"  :  return self.rect.topleft , self.rect.bottomleft
            case "right" :  return self.rect.topright , self.rect.bottomright
            case "up"    :  return self.rect.topleft , self.rect.topright
            case "down"  :  return self.rect.bottomleft , self.rect.bottomright
            case _: return None, None


class Maze:
    def __init__(self, generation_mode="random"):
        self.tiles = generate_maze(generation_mode)
        
    def draw(self, win):
        for tile in self.tiles.values():
            tile.draw(win)

class Game:
    def __init__(self, name:str|None="My Game"):
        pygame.init()

        self.screen = pygame.display.set_mode(RES)
        self.maze_surf = pygame.surface.Surface(SURF_RES)

        if name:
            pygame.display.set_caption(name)

        self.running = True
        self.clock = pygame.time.Clock()

        self.maze = Maze(MAZE_GENERATION_MODE)

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def draw(self):
        self.screen.fill(BG_COLOR)

        self.maze_surf.fill(SURF_COLOR)

        self.maze.draw(self.maze_surf)

        pygame.draw.rect(self.maze_surf, SURF_BOUNDARY_COLOR, self.maze_surf.get_rect(), width=SURF_BOUNDARY_SIZE)

        self.screen.blit(self.maze_surf, SURF_POS)

    def run(self):
        while self.running:
            delta = self.clock.tick(FPS) # The delta will be useful when handling player movement
            self.eventHandler()
            
            self.draw()
            
            pygame.display.update()
        pygame.quit()


def generate_maze(mode) -> dict[tuple[int, int], Tile]:
    tiles = {(i, j): Tile((i, j)) for i in range(n_rows) for j in range(n_cols)}

    match mode.lower():
        case "random":
            return random_generation(tiles)
        case "dfs":
            return dfs_for_maze_generation(tiles)
        case _:
            return random_generation(tiles)
