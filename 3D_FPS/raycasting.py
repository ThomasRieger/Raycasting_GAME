import pygame as pg
import math
from setting import *

class Raycasting:
    def __init__(self,game):
        self.game = game
        
    def raycasting(self):
        ox, oy = self.game.player.pos()
        xmap, ymap = self.game.player.map_pos()
        
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
                tile_vert = int(x_vert),int(y_vert)
                if tile_vert in self.game.map.worldmap:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += depth_delta
            
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor
            
            depth *= math.cos(self.game.player.angle - ray_angle)
            
            #pg.draw.line(self.game.screen,'yellow', (100 * ox, 100 * oy),
            #             (100 * ox + 100 * depth * cos_a,100 * oy + 100 * depth * sin_a),2)
            
            pro_height = SCREEN_PRO / (depth + 0.0001)
            
            color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            pg.draw.rect(self.game.screen, color,(ray * SCALE, HALF_HEIGHT - pro_height // 2, SCALE,pro_height))
            
            ray_angle += DELTA_ANGLE
    
    def update(self):
        self.raycasting()