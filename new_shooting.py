import pygame
import random
import os
import pyautogui
import time
import asyncio
import math

base = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(path):
    return os.path.join(base, path)

class lazer_gun():


    def __init__(self):
        self.paths = []
        #################
        # Replace the above with the image of the lazer gun
        

    def shoot_lazer(self, window, playerx, playery, mousex, mousey):
        angle = lazer_gun.calc_angle(playerx, playery, mousex, mousey)
        lazer_gun_copy = pygame.transform.rotate(lazer_gun.lazer_gun_image, angle)

        window.blit(lazer_gun_copy, playerx, playery)

    def calc_angle(self, playerx, playery, mousex, mousey):
        relx, rely = mousex - playerx, mousey - playery
        angle = (180 / math.pi) * -math.atan2(relx, rely)

        return angle
    
class lazer_bullet():
    def __init__ (self, x, y, mousex, mousey, height, width):
        self.x = x - (width / 14.91304347826087)
        self.y = y - (height / 11.25)
        # self.x = x - 115
        # self.y = y - 80
        self.mousex = mousex
        self.mousey = mousey
        self.speed = 10
        self.angle = math.atan2(y - mousey, x - mousex)
        self.angle_deg = self.angle * (180/math.pi)
        self.velx = math.cos(self.angle) * self.speed
        self.vely = math.sin(self.angle) * self.speed

    def shoot(self, window):
        self.x -= int(self.velx / 4)
        self.y -= int(self.vely / 4)
        self.lazer_gun_image = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_right.png'))
        SCALE_SIZE = (75, 75)
        self.lazer_gun_image = pygame.transform.scale(self.lazer_gun_image, SCALE_SIZE)

        deg = math.degrees(math.atan2(-self.vely, self.velx)) + 180

        self.lazer_gun_image = pygame.transform.rotate(self.lazer_gun_image, deg)
        self.lazer_gun_image_rect = self.lazer_gun_image.get_rect()
        self.lazer_gun_image_rect.center = (self.x, self.y)
        #print("Rotated image to angle: " + str(self.angle))
        #pygame.draw.circle(window, (255,255,255), (self.x, self.y), 5)
        window.blit(self.lazer_gun_image, self.lazer_gun_image_rect)
        #window.blit(self.lazer_gun_image_rect, (self.x, self.y))
        #print("NKLSDNFLKSDGN")

    def check_ghost_col(self):
        # for ghost in ghosts:
        #     if abs(self.x - ghost.x) == 10 and abs(self.y - ghost.y) == 10:
        #         return (True, ghosts)
        pass

    def check_wall_col(self):
        pass

    def check_boss_col(self):
        pass

        