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
        

        #Window Constants
        #self.WIDTH, self.HEIGHT = pyautogui.size()

        #Colors
        self.GREEN = (0, 255, 0)
        self.YELLOW = (224, 247, 20)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.COLOR = ()

    def check_projectile_collision(self, walls, proj_x, proj_y, last_key):
        if (last_key == "up_arrow" or last_key == "down_arrow" or last_key == "w" or last_key == "s"):
            if (proj_x, proj_y):
                #if moving up and down last, potential coliding walls must be horizontal
                #check if x is between start and end values of the wall
                #chekc if y is equal to etiher start or end of the wall since they will be the same for a horizontal wall
                pass
        else:
            if (proj_x, proj_y):
                #if moving up and down last, potential coliding walls must be vertical
                #check if x is between start and end values of the wall
                #chekc if y is equal to etiher start or end of the wall since they will be the same for a horizontal wall
                pass

    async def shoot(self, window, playerx, playery, weapon_name):
        start_point = (playerx, playery)
        window.blit(self.laser_flash, start_point)
        pygame.display.update()
        window.blit(self.laser_flash, (-150, 150))
        pygame.display.update()
        # if weapon_name == "laser_gun":
        #     self.shoot_laser(window, start_point)

    #Implementation for more guns if added later
    
    # def shoot_laser(self, window, start_point):
    #     print("in shoot laser------------------------------")
    #     window.blit(self.laser_flash, start_point)
    #     pygame.display.update()
    #     time.sleep(1)
    #     self.laser_flash.fill((0,0,0,0))
    #     pygame.display.update()

