import pygame
import random
import os
import pyautogui
import time
import asyncio

base = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(path):
    return os.path.join(base, path)



class weapons:

    def __init__(self):
        #Fonts
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        #images
        self.image = pygame.image.load(sanitize_path('Images/ammoIconGrey.png'))
        self.SCALE_SIZE = (75, 75)
        self.image = pygame.transform.scale(self.image, self.SCALE_SIZE)
        #-------------------------------------------------------------------------------------
        self.laser_flash = pygame.image.load(sanitize_path('projectileimgaes/lazerblast.png'))
        self.SCALE_SIZE = (75, 75)
        self.laser_flash = pygame.transform.scale(self.laser_flash, self.SCALE_SIZE)
        #-------------------------------------------------------------------------------------
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

        #Window Constants
        #self.WIDTH, self.HEIGHT = pyautogui.size()       

        #Colors
        self.GREEN = (0, 255, 0)
        self.YELLOW = (224, 247, 20)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.COLOR = ()
        self.active_projectiles = []

    def check_projectile_collision(self, point, last_key):
        if (last_key == "up_arrow" or last_key == "down_arrow" or last_key == "w" or last_key == "s"):
            return True
        #     if (proj_x, proj_y):
        #         #if moving up and down last, potential coliding walls must be horizontal
        #         #check if x is between start and end values of the wall
        #         #chekc if y is equal to etiher start or end of the wall since they will be the same for a horizontal wall
        #         pass
        # else:
        #     if (proj_x, proj_y):
        #         #if moving up and down last, potential coliding walls must be vertical
        #         #check if x is between start and end values of the wall
        #         #chekc if y is equal to etiher start or end of the wall since they will be the same for a horizontal wall
        #         pass

    async def shoot(self, window, playerx, playery, weapon_name, last_key):
        start_point = (playerx - 30, playery - 30)
        window.blit(self.laser_flash, start_point)
        pygame.display.update()
        window.blit(self.laser_flash, (-150, 150))
        pygame.display.update()
        if weapon_name == "laser_gun":
            self.shoot_laser(window, start_point, last_key)

    #Implementation for more guns if added later
    
    # def shoot_laser(self, window, start_point, last_key):
    #     if last_key == "right":
    #         window.blit(self.laser_projectile_right, start_point)
    #         time.sleep(0.05)
    #         pygame.display.update()
    #         window.blit(self.laser_projectile_right, (-150, 150))
    #         pygame.display.update()
    #     if last_key == "left":
    #         window.blit(self.laser_projectile_left, start_point)
    #         pygame.display.update()
    #         window.blit(self.laser_projectile_left, (-150, 150))
    #         pygame.display.update()
    #     if last_key == "up":
    #         window.blit(self.laser_projectile_up, start_point)
    #         pygame.display.update()
    #         window.blit(self.laser_projectile_up, (-150, 150))
    #         pygame.display.update()
    #     if last_key == "down":
    #         window.blit(self.laser_projectile_down, start_point)
    #         pygame.display.update()
    #         window.blit(self.laser_projectile_down, (-150, 150))
    #         pygame.display.update()
    #     self.active_projectiles.append((start_point, last_key))

    # def track_laser(self, window):
    #     for i in self.active_projectiles:
    #         if self.check_projectile_collision(i[0], i[1]):
    #             if i[1] == "right":
    #                 start_point = (i[0][0] + 50, i[0][1])
    #                 self.active_projectiles.remove(i)
    #                 self.shoot_laser(window, start_point, i[1])
                
            

    # def get_projectiles(self):
    #     return self.active_projectiles

