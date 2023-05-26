import pygame as pg
from setting import *

class Object:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_wall()
        
    def get_Texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture,res)
    
    def load_wall(self):
        return {
            1: self.get_Texture('Texture/wall.jpg')
        }