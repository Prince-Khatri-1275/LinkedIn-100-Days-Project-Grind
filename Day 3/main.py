import pygame
import numpy as np

from mazes import maze2 as maze, get_maze_dims

pygame.init()

RES = FULL_WIDTH, FULL_HEIGHT = 800, 640
MARGIN_WIDTH, MARGIN_HEIGHT = 100, 80

WIDTH, HEIGHT = FULL_WIDTH - 2*MARGIN_WIDTH, FULL_HEIGHT-2*MARGIN_HEIGHT

screen = pygame.display.set_mode(RES) # As it requires a tuple

BG_COLOR = "#03033A"
WALL_COLOR = "#530303"
PATH_COLOR = "#7AC28D"
BOUNDARY_COLOR = "#20000E"

TILE_WIDTH, TILE_HEIGHT = get_maze_dims(WIDTH, HEIGHT, maze)

def draw_boundaries(win, maze_dims):
    for i in range(maze_dims[0]+1):
        pygame.draw.line(win, BOUNDARY_COLOR, (MARGIN_WIDTH, i*TILE_HEIGHT+MARGIN_HEIGHT), (WIDTH+MARGIN_WIDTH, i*TILE_HEIGHT+MARGIN_HEIGHT))

    for j in range(maze_dims[1]+1):
        pygame.draw.line(
            win,
            BOUNDARY_COLOR,
            (j*TILE_WIDTH+MARGIN_WIDTH, MARGIN_HEIGHT), (j*TILE_WIDTH+MARGIN_WIDTH, MARGIN_HEIGHT+HEIGHT),
        )

def draw_maze(maze_data, win):
    m, n = len(maze_data), len(maze_data[0])
    for i in range(m):
        for j in range(n):
            tile_rect = pygame.Rect(j*TILE_WIDTH+MARGIN_WIDTH, i*TILE_HEIGHT+MARGIN_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
            if maze_data[i][j]:
                pygame.draw.rect(win, WALL_COLOR, tile_rect)
            else:
                pygame.draw.rect(win, PATH_COLOR, tile_rect)
        
    draw_boundaries(win, (m, n))


def draw(win):
    win.fill(BG_COLOR)
    draw_maze(maze_data=maze, win=win)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        
        draw(win=screen)
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
