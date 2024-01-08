import pygame
import random
import os
import pyautogui
import time
import asyncio

base = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(path):
    return os.path.join(base, path)

class Sprite(pygame.sprite.Sprite): 
    def __init__(self, height, width, window): 
        super().__init__() 
  
        self.laser_projectile = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_right.png'))
        self.SCALE_SIZE = (75, 75)
        self.laser_projectile = pygame.transform.scale(self.laser_projectile, self.SCALE_SIZE)
  
        pygame.draw.rect(window, (255,255,255), pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.laser_projectile.get_rect() 

class player_lazer:

    def __init__(self):
        # self.laser_projectile_right = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_right.png'))
        # self.SCALE_SIZE = (75, 75)
        # self.laser_projectile_right = pygame.transform.scale(self.laser_projectile_right, self.SCALE_SIZE)
        #-------------------------------------------------------------------------------------
        # self.laser_projectile_left = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_left.png'))
        # self.SCALE_SIZE = (75, 75)
        # self.laser_projectile_left = pygame.transform.scale(self.laser_projectile_left, self.SCALE_SIZE)
        # #-------------------------------------------------------------------------------------
        # self.laser_projectile_up = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_up.png'))
        # self.SCALE_SIZE = (75, 75)
        # self.laser_projectile_up = pygame.transform.scale(self.laser_projectile_up, self.SCALE_SIZE)
        # #-------------------------------------------------------------------------------------
        # self.laser_projectile_down = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_down.png'))
        # self.SCALE_SIZE = (75, 75)
        # self.laser_projectile_down = pygame.transform.scale(self.laser_projectile_down, self.SCALE_SIZE)
        self.paths = []
        self.all_sprite_list = pygame.sprite.Group()


    def projectile_collision(self):
        return True

    def calculate_path(self, mouse_coords, playerx, playery):
        temp = []
        speed = 1
        cur = 0
        quadrant = self.calc_quadrant(mouse_coords, playerx, playery)
        y_rate = (mouse_coords[1] - playery)
        x_rate = (mouse_coords[0] - playerx)
        start_point = (playerx, playery)
        temp.append(start_point)
        while cur < speed:
            if quadrant == 1:
               playerx += x_rate
               playery += y_rate
               temp.append((playerx, playery)) 
            if quadrant == 2:
               playerx -= x_rate
               playery += y_rate
               temp.append((playerx, playery)) 
            if quadrant == 3:
               playerx -= x_rate
               playery -= y_rate
               temp.append((playerx, playery)) 
            if quadrant == 4:
               playerx += x_rate
               playery -= y_rate
               temp.append((playerx, playery)) 
            cur += 1
        self.paths.append(temp)

    def calc_quadrant(self, mouse_coords, playerx, playery): 
        if playery >= mouse_coords[1]:
            if playerx >= mouse_coords[0]:
                return 1
            else:
                return 2
        else:
           if playery >= mouse_coords[1]:
            if playerx >= mouse_coords[0]:
                return 4
            else:
                return 3  
            
    def draw_lazers(self, window):
        for i in self.paths:
            try:
                cur_coord = i.pop(0)
            except:
                break
            lazer = Sprite(20, 20, window)
            lazer.rect.x = cur_coord[0]
            lazer.rect.y = cur_coord[1]
            self.all_sprite_list.add(lazer)
            self.all_sprite_list.draw(window)

    def get_projectiles(self):
        return self.paths
        
