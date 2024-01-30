import pygame
import random
import os
import pyautogui

class bossbar:

    pygame.init()

    def __init__ (self):
        
        #Fonts
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        #Window Constants
        #self.WIDTH, self.HEIGHT = pyautogui.size()

        #Health Constants
        #boss_health = 100 #Health of the player, as a percent

        #Colors
        self.GREEN = (0, 255, 0)
        self.YELLOW = (224, 247, 20)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.BLUE = (63, 229, 235)
        self.COLOR = ()


    #Generation of the healthbar
    def gen_bossbar(self, window, WIDTH, boss_health):
        #Checks to change color based on the player's health, changing form green to yellow to red as they get clsoer to loosing all of their health
        if boss_health <= 100 and boss_health > 50:
            self.COLOR = self.GREEN
            pygame.draw.rect(window, self.GREEN, [(WIDTH/2) - 250, 10, 500 * (boss_health/100), 50])
        elif boss_health <= 50 and boss_health > 25:
            self.COLOR = self.YELLOW
            pygame.draw.rect(window, self.YELLOW, [(WIDTH/2) - 250, 10, 500 * (boss_health/100), 50])
        elif boss_health <= 25 and boss_health > 0:
            self.COLOR = self.RED
            pygame.draw.rect(window, self.RED, [(WIDTH/2) - 250, 10, 500 * (boss_health/100), 50])
        pygame.draw.rect(window, self.COLOR, [(WIDTH/2) - 250, 10, 502, 52], 2)
        self.gen_boss_percent(window, WIDTH, boss_health)

    def gen_boss_percent(self, window, WIDTH, boss_health):
        health = self.font.render(str(round(boss_health)), True, self.COLOR) 
        healthRect = health.get_rect()
        if boss_health == 100:
            healthRect.center = ((WIDTH/2) + 300, 40)
        else:
            healthRect.center = ((WIDTH/2) + 300 , 40)
        window.blit(health, healthRect)

    