import pygame
import random
import os
import pyautogui

class pellets:

    pygame.init()

    def __init__ (self):

        self.score = 0
                
        #Fonts
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        #Window Constants
        #self.WIDTH, self.HEIGHT = pyautogui.size()

        #Colors
        self.GREEN = (0, 255, 0)
        self.YELLOW = (224, 247, 20)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.COLOR = ()

    def display_score(self, window, WIDTH):
        score_disp = self.font.render("Score: " + str(self.score), True, self.WHITE) 
        score_rect = score_disp.get_rect()
        score_rect.center = (WIDTH - 120, 130)
        window.blit(score_disp, score_rect)
        #print(self.score)

    def update_score(self):
        self.score += 1

    def display_ammo(self, window, WIDTH):
        ammo_disp = self.font.render("Score: " + str(self.score), True, self.WHITE) 
        ammo_rect = ammo_disp.get_rect()
        ammo_rect.center = (WIDTH - 270, 130)
        window.blit(ammo_disp, ammo_rect)
        #print(self.score)

    def update_ammo(self):
        self.score += 1