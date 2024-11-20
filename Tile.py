import pygame
from Set_Up import *

class Tile:
    def __init__(self, rgb, x, y) -> None:
        
        self.display = pygame.display.get_surface()
        self.rgb = rgb
        self.x = x
        self.y = y
        self.coordinate = (x, y)
        self.rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.is_obstacle = False
        self.is_searched = False

    def run(self):

        pygame.draw.rect(self.display, self.rgb, self.rect)