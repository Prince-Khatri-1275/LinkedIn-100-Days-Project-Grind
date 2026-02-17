FPS = 60
RES = WIDTH, HEIGHT = 800, 640

SURF_RES = surf_width, surf_height = 480, 480


# Just got it if this surf pos got negative than we can have a zoom in maze awesome isn't it
SURF_POS = (WIDTH - surf_width) // 2, (HEIGHT - surf_height) // 2

BG_COLOR = 0, 0, 0
SURF_COLOR = 24, 24, 24

SURF_BOUNDARY_COLOR = 224, 224, 224
SURF_BOUNDARY_SIZE = 2

n_rows, n_cols = 10, 12

TILE_WIDTH, TILE_HEIGHT = surf_width // n_cols, surf_height // n_rows

# Total options of a tile (maybe just maybe later on we make it 3D so just in case)
AVAILABLE_NEIGHBORS = set(
    ["up", "down", "left", "right"]
)


WALL_WIDTH = 2
WALL_COLOR = 255, 255, 255

MAZE_GENERATION_MODE = "random"
