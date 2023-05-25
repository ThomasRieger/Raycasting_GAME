import pygame as pg
import sys
from setting import *
from map import *
from player import *
from raycasting import *

class Game:
    
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = Raycasting(self)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        
    def draw(self):
        self.screen.fill([0,0,0])
        #self.map.draw()
        #self.player.draw()
        
    
    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
                
    def run(self):
        try:
            while True:
                self.check_event()
                self.update()
                self.draw()
        except Exception as e:
            print("An error occurred:", e)
            pg.quit()
            sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()