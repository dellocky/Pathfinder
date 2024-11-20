import pygame
from Tile import Tile
from Mouse import Mouse
import Generate_Board
from Set_Up import *

class Board:
    def __init__(self) -> None:
        
        self.tiles = []
        self.create_map()

    def create_map(self):
        
        x = 0
        y = 0
        color1 = (175, 175, 175)
        color2 = (145, 145 ,145)
        color_val = 1
        color = color1
        for tiles in range(HEIGHT):
            for tile in range(WIDTH):
                Current_Tile = Tile((color),x, y)
                self.tiles.append(Current_Tile)
                if color_val == 1:
                    color = color2
                    color_val = 2
                else: 
                    color = color1
                    color_val = 1
                x += 1
            if color_val == 1:
                color = color2
                color_val = 2
            else: 
                color = color1
                color_val = 1
            x = 0
            y += 1
        
        Generate_Board.generate_board(self.tiles, 25)
        self.mouse = Mouse(self.tiles)

    def run(self, event_list):
        for Tile in self.tiles:
            Tile.run()
        self.mouse.run(event_list)
        

            