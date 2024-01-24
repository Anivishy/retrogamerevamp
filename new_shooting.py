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

import wall_generation
from calculated_vars import *

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
        self.x = x 
        self.y = y 

        self.sx = self.x
        self.sy = self.y
        # self.x = x - 115
        # self.y = y - 80
        self.mousex = mousex
        self.mousey = mousey
        self.speed = 25
        self.angle = math.atan2(y - mousey, x - mousex)
        self.angle_deg = self.angle * (180/math.pi)


        deg = (math.atan2(-y + mousey, -x + mousex)) + (math.pi)

        distance = ((y - mousey) ** 2 + (x - mousex) ** 2) ** 0.5
        self.velx = self.speed * ((x - mousex) / distance)
        self.vely = self.speed * ((y - mousey) / distance)




        # self.velx = math.cos(deg) * self.speed
        # self.vely = math.sin(deg) * self.speed

        self.lazer_gun_image = pygame.image.load(sanitize_path('projectileimgaes/lazerprojectile_right_cropped.png'))
        SCALE_SIZE = (75, 75)
        self.lazer_gun_image = pygame.transform.scale(self.lazer_gun_image, SCALE_SIZE)

        deg = math.degrees(math.atan2(-self.vely, self.velx)) + 180

        self.lazer_gun_image = pygame.transform.rotate(self.lazer_gun_image, deg)

    def shoot(self, window):
        self.x -= (self.velx / 4)
        self.y -= (self.vely / 4)
        
        
        self.lazer_gun_image_rect = self.lazer_gun_image.get_rect()
        self.lazer_gun_image_rect.center = (self.x, self.y)
        #print("Rotated image to angle: " + str(self.angle))
        #pygame.draw.circle(window, (255,255,255), (self.x, self.y), 5)
        # pygame.draw.rect(window, (0, 0, 255), pygame.Rect(
        #     self.sx, self.sy,
        #     5,
        #     5
        # ))
        # pygame.draw.rect(window, (255, 0, 0), pygame.Rect(
        #     self.mousex, self.mousey,
        #     5,
        #     5
        # ))
        #pygame.draw.line(window, (0, 255, 0), (self.sx, self.sy), (self.mousex, self.mousey))
        window.blit(self.lazer_gun_image, self.lazer_gun_image_rect)
        
        #pygame.draw.circle(window, (0, 0, 255), (self.x, self.y), 5)
        #window.blit(self.lazer_gun_image_rect, (self.x, self.y))
        #print("NKLSDNFLKSDGN")

    def check_ghost_col(self):
        # for ghost in ghosts:
        #     if abs(self.x - ghost.x) == 10 and abs(self.y - ghost.y) == 10:
        #         return (True, ghosts)
        pass

    def check_wall_col(self, window, playerx, playery):
        t = self.lazer_gun_image_rect
        #print(self.velx, self.vely)
        #print(self.x - playerx * SQUARE_SIZE, self.y - playery * SQUARE_SIZE)
        rect = pygame.Rect(
            t.x, t.y,
            t.width, t.height
        )
        #print(rect.x // SQUARE_SIZE, rect.y // SQUARE_SIZE)
        for wall in wall_generation.walls_around((rect.x) // SQUARE_SIZE + 1 + int(playerx), (rect.y) // SQUARE_SIZE + 1 + int(playery)):
            p1, p2 = wall
            p1 = list(p1)
            p2 = list(p2)
            

            if p1[1] == p2[1]:
                r = pygame.Rect((p1[0] * SQUARE_SIZE - playerx * SQUARE_SIZE - SQUARE_SIZE // 2), (p1[1] * SQUARE_SIZE - playery * SQUARE_SIZE) - WALL_WIDTH // 2 - SQUARE_SIZE // 2, SQUARE_SIZE, WALL_WIDTH)
            else:
                r = pygame.Rect((p1[0] * SQUARE_SIZE - playerx * SQUARE_SIZE - SQUARE_SIZE // 2) - WALL_WIDTH // 2, (p1[1] * SQUARE_SIZE - playery * SQUARE_SIZE) - SQUARE_SIZE // 2, WALL_WIDTH, SQUARE_SIZE)

            if pygame.Rect.collidepoint(r, (self.x, self.y)):
                return True

    def check_boss_col(self):
        pass

        