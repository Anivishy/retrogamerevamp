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
        self.laser_projectile_left = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_left.png'))
        self.SCALE_SIZE = (75, 75)
        self.laser_projectile_left = pygame.transform.scale(self.laser_projectile_left, self.SCALE_SIZE)
        #-------------------------------------------------------------------------------------
        self.laser_projectile_up = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_up.png'))
        self.SCALE_SIZE = (75, 75)
        self.laser_projectile_up = pygame.transform.scale(self.laser_projectile_up, self.SCALE_SIZE)
        #-------------------------------------------------------------------------------------
        self.laser_projectile_down = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_down.png'))
        self.SCALE_SIZE = (75, 75)
        self.laser_projectile_down = pygame.transform.scale(self.laser_projectile_down, self.SCALE_SIZE)

        self.path = []


    def projectile_collision(self):
        return True

    def calculate_path(self, mouse_coords, playerx, playery):
        speed = 10
        y_rate = (mouse_coords[1] - playery)
        x_rate = (mouse_coords[0] - playerx)
        start_point = (playerx, playery)
        self.path.append(start_point)
        
