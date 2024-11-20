import pygame
import Pathfind
from Debug import debug

class Mouse:
    def __init__(self, tiles) -> None:

        pygame.init()
        self.display = pygame.display.get_surface()
        self.pos = pygame.mouse.get_pos()
        self.rect = pygame.Rect(self.pos, (5, 5))
        self.rect_hitbox = pygame.Rect((self.pos[0]+2, self.pos[1]+2), (1, 1))
        pygame.mouse.set_visible(False)
        self.tiles=tiles
        self.rgb = (0, 0, 255)
        self.click_state = 1
        self.event_list = None
        self.target = None



    def process(self):
        
        for event in self.event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click()

               
    def click(self):
        
        if self.click_state == 1:
            self.create_start()
        
        elif self.click_state == 2:
            self.path_find()


    def create_start(self):
        for tile in self.tiles:
            if tile.rect.colliderect(self.rect_hitbox) and tile.is_obstacle is False:
                tile.rgb = (0, 255, 0)
                self.start_tile = tile
                self.start_tile.is_searched = True
                self.click_state = 2
                
    def path_find(self):
        for tile in self.tiles:
            if tile.rect.colliderect(self.rect_hitbox) and tile.is_obstacle is False and tile.is_searched is False:
                self.target_tile = tile
                #print(f"Start Tile = {self.start_tile.coordinate}")
                #print(f"Target Tile = {self.target_tile.coordinate}")
                chain = [[self.start_tile.coordinate]]
                looping = True
                while looping:
                    for path in chain:
                        if self.target_tile.coordinate in path:
                            looping = False
                            final_path = path
                            break
                    print(chain)
                    chain = Pathfind.cascade(chain, self.tiles)
 
                
                for tile in self.tiles:
                    if tile.coordinate in final_path:
                        tile.rgb = (83, 5, 105)
                    
                self.start_tile.rgb = (0, 255, 0)
                self.target_tile.rgb = (0, 0, 255)
               
                    
        
                    

    def create_path(self, path):

        for coordinates in path:
            for tile in self.tiles:
                if tile.coordinate == coordinates:
                    tile.rgb = (128, 0, 128)

        

    def run(self, event_list):
          
        self.event_list = event_list
        self.pos = pygame.mouse.get_pos()
        self.rect = pygame.Rect(self.pos, (5, 5))
        self.rect_hitbox = pygame.Rect((self.pos[0]+2, self.pos[1]+2), (1, 1))
        self.process()
        pygame.draw.rect(self.display, self.rgb, self.rect)
        
        for tile in self.tiles:
            if tile.rect.colliderect(self.rect_hitbox):
                debug(tile.coordinate)
