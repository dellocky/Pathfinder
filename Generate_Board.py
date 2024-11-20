from random import randint
from Set_Up import *

def generate_board(tiles, chance):
    
    for tile in (tiles):
        if randint(1, 100) < chance:
            tile.is_obstacle = True
            if tile.rgb[0] == 175:
                tile.rgb = (175, 0, 0)
            else:
                tile.rgb = (145, 0, 0)





