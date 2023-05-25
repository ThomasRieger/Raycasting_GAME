import pygame as pg
_ = False
minimap = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,1,1,1,_,_,_,1,1,1,_,_,_,_,1],
    [1,_,1,_,_,_,_,_,1,_,_,_,_,_,_,1],
    [1,_,1,1,1,_,_,_,1,_,1,1,1,1,_,1],
    [1,_,_,_,1,_,_,_,1,_,1,_,_,_,_,1],
    [1,_,_,_,1,_,_,1,1,_,1,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.minimap = minimap
        self.worldmap = {}
        self.get_map()
        
    def get_map(self):
        for i ,row in enumerate(self.minimap):
            for j ,value in enumerate(row):
                if value:
                    self.worldmap[(j,i)] = value
                    
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100),2)
        for pos in self.worldmap]
            