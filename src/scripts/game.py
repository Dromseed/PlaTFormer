from colors import SKY_BLUE
from settings import WIN_X, WIN_Y
import pygame as py
import sys

class Game:
    def __init__(self):
        py.init()
        self.window = py.display.set_mode((WIN_X, WIN_Y))
        py.display.set_caption("PlaTFormer")

    def run(self):
        running = 1
        while running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = 0
            
            self.window.fill(SKY_BLUE)
            py.display.flip()
        
        py.quit()
        sys.exit()