import pygame as pg
from setting import *

class Object:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_wall()
    
    def draw(self):
        self.render_game_obj()
    
    def render_game_obj(self):
        list_obj = self.game.raycasting.obj_to_render
        for depth, image, pos in list_obj:
            self.screen.blit(image, pos)
        
    @staticmethod
    def get_Texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        try:
            texture = pg.image.load(path).convert_alpha()
            return pg.transform.scale(texture, res)
        except pg.error as e:
            print("Error loading texture:", e)
            return None
    
    def load_wall(self):
        return {
            1: self.get_Texture('Texture/2.png')
        }