import pygame
import sys
from pygame.locals import *

class mainApp(self):
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244, 236, 203)) #Tupla de RGB para determianr el color de fondo de la pantalla
    
    
    def __on_close(self):
         pygame.quit()
         sys.exit()
    
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == quit:
                    self.__on_close()
                  
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    