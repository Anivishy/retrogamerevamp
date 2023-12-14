import pygame
import random
import os
import pyautogui
import time
import asyncio

base = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(path):
    return os.path.join(base, path)

class player_lazer:

    def __init__(self):
        self.laser_projectile_right = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_right.png'))
        self.SCALE_SIZE = (75, 75)
        self.laser_projectile_right = pygame.transform.scale(self.laser_projectile_right, self.SCALE_SIZE)
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


    def projectile_collision(self):
        return True

    def calculate_path(self, mouse_coords, playerx, playery):
        temp = []
        speed = 10
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
               temp.append(playerx, playery) 
            if quadrant == 2:
               pass 
            if quadrant == 3:
               pass 
            if quadrant == 4:
               pass 

    def calc_quadrant(self, mouse_coords, playerx, playery): #
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

    def get_projectiles(self):
        return self.paths
        
