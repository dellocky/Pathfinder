import pygame, sys
from Set_Up import *
from Board import Board

class Game:
    def __init__(self):
        
        pygame.init()
        self.screen=pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))
        self.clock=pygame.time.Clock()

        self.board = Board()
        
    def run(self):
        while True:
            event_list =  pygame.event.get()
            self.screen.fill('black')
            self.board.run(event_list)
            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            
            #self.board.run(event_list)
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    
    pathfinder = Game()
    pathfinder.run()