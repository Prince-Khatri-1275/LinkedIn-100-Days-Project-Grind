import pygame
from constants import *
from classes.maze import Maze

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(RES)
        self.surf = pygame.Surface(SURF_RES)
        
        # self.player = Player() :-> To be continued ....
        self.maze = Maze()
        
        self.running = True
        self.clock = pygame.time.Clock()
        
    def draw(self):
        self.screen.fill(BG_COLOR)
        self.screen.blit(self.surf, SURF_POS_CORDS)
        
        self.surf.fill(SURF_COLOR)
        self.maze.draw(self.surf)
    
    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            
            self.eventHandler()
            self.draw()
            
            pygame.display.update()
        
        pygame.quit()