import pygame as pg
import math
from setting import *

class Raycasting:
    def __init__(self, game):
        self.game = game
        self.raycasting_result = []
        self.obj_to_render = []
        self.texture = self.game.object_rendering.wall_texture
    
    def render_game_obj(self):
        self.obj_to_render = []
        for ray, value in enumerate(self.raycasting_result):
            depth, pro_height, texture, offset = value
            if pro_height < HEIGHT:
                wall_column = self.texture[texture].subsurface(
                    int(offset * (TEXTURE_SIZE - SCALE)), 0, SCALE, TEXTURE_SIZE
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, int(pro_height)))
                wall_pos = (ray * SCALE, HALF_HEIGHT - pro_height // 2)
            else:
                texture_height = TEXTURE_SIZE * HEIGHT / pro_height
                wall_column = self.texture[texture].subsurface(
                    int(offset * (TEXTURE_SIZE - SCALE)), HALF_TEXTURE - texture_height // 2, SCALE, texture_height
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT))
                wall_pos = (ray * SCALE, 0)
                
            self.game.screen.blit(wall_column, wall_pos)
    
    def raycasting(self):
        self.raycasting_result = []
        ox, oy = self.game.player.pos()
        xmap, ymap = self.game.player.map_pos()
        texture_ver, texture_hor = 1, 1
        
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUMBER_RAY):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            
            y_hor, dy = (ymap + 1, 1) if sin_a > 0 else (ymap - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            
            depth_delta = dy / sin_a
            dx = depth_delta * cos_a
            
            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.worldmap:
                    texture_hor = self.game.map.worldmap[tile_hor]
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += depth_delta
            
            x_vert, dx = (xmap + 1, 1) if cos_a > 0 else (xmap - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            
            depth_delta = dx / cos_a
            dy = depth_delta * sin_a
            
            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.worldmap:
                    texture_ver = self.game.map.worldmap[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += depth_delta
            
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_ver
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = x_hor if sin_a > 0 else (1 - x_hor)
            
            depth *= math.cos(self.game.player.angle - ray_angle)
            
            pro_height = SCREEN_PRO / (depth + 0.0001)
            
            self.raycasting_result.append((depth, pro_height, texture, offset))
            
            ray_angle += DELTA_ANGLE
    
    def update(self):
        self.raycasting()
        self.render_game_obj()
