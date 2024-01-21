import pygame
import random
import os
import pyautogui
import time
import asyncio

base = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(path):
    return os.path.join(base, path)

class lazer(pygame.sprite.Sprite): 
    def __init__(self, window, x, y): 
        pygame.sprite.Sprite.__init__(self)  
        # laser_projectile = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_right.png'))
        # SCALE_SIZE = (75, 75)
        # laser_projectile = pygame.transform.scale(laser_projectile, SCALE_SIZE)
        # self.image = laser_projectile
        self.image = pygame.Surface((50,50))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # self.laser_projectile = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_right.png'))
        # self.SCALE_SIZE = (75, 75)
        # self.laser_projectile = pygame.transform.scale(self.laser_projectile, self.SCALE_SIZE)
        # pygame.draw.rect(window, (255,255,255), pygame.Rect(0, 0, width, height))   
        # self.rect = self.laser_projectile.get_rect() 

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
        self.projectiles = pygame.sprite.Group()



    def projectile_collision(self):
        return True

    def calculate_path(self, mouse_coords, playerx, playery, WIDTH, HEIGHT):
        temp = []
        speed = 100
        cur = 0
        x = 1
        y = 1
        quadrant = self.calc_quadrant(mouse_coords, playerx, playery)
        y_rate = (-1 * mouse_coords[1] + (HEIGHT/2)  - y)
        x_rate = (mouse_coords[0]  + (WIDTH/2)- x)
        slope = y_rate/x_rate
        print("RATE:" + str(x_rate), str(y_rate))
        start_point = (x, y)
        temp.append(start_point)
        while cur < speed:
            if quadrant == 1:
               x += 50
               y = x * slope
               temp.append((x, y)) 
            if quadrant == 2:
               x -= 50
               y = -1 * x * slope
               temp.append((x, y)) 
            if quadrant == 3:
               x -= 50
               y = x * slope
               temp.append((x, y)) 
            if quadrant == 4:
               x += 50
               y = -1 * x * slope
               temp.append((x, y)) 
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
            
    def draw_lazers(self, window, WIDTH, HEIGHT):
        for i in self.paths:
            try:
                cur_coord = i.pop(0)
            except:
                break
            print(cur_coord)
            cur_lazer = lazer(window, cur_coord[0] + (WIDTH/2), -1 * cur_coord[1] + (HEIGHT/2))
            self.projectiles.add(cur_lazer)
            self.projectiles.update()
        self.projectiles.draw(window)
        pygame.display.update()
        #self.projectiles.empty()
        #print(self.projectiles)
            # lazer = Sprite(20, 20, window)
            # lazer.rect.x = cur_coord[0]
            # lazer.rect.y = cur_coord[1]
            # #self.all_sprite_list.add(lazer)
            # self.all_sprite_list.draw(window)

    def get_projectiles(self):
        return self.paths
        
