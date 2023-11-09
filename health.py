import pygame
import random
import os
import pyautogui

class healthbar:

    #pygame.init()

    def __init__ (self):
        self.player_health = 80
        
        #Fonts
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        #Window Constants
        self.WIDTH, self.HEIGHT = pyautogui.size()

        #Health Constants
        #self.player_health = 100 #Health of the player, as a percent

        #Colors
        self.GREEN = (0, 255, 0)
        self.YELLOW = (224, 247, 20)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.COLOR = ()


    def gen_healthbar(self, window):
        if self.player_health <= 100 and self.player_health > 50:
            self.COLOR = self.GREEN
            pygame.draw.rect(window, self.GREEN, [self.WIDTH - 350, 10, 300 * (self.player_health/100), 50])
        elif self.player_health <= 50 and self.player_health > 25:
            self.COLOR = self.YELLOW
            pygame.draw.rect(window, self.YELLOW, [self.WIDTH - 350, 10, 300 * (self.player_health/100), 50])
        elif self.player_health <= 25 and self.player_health > 0:
            self.COLOR = self.RED
            pygame.draw.rect(window, self.RED, [self.WIDTH - 350, 10, 300 * (self.player_health/100), 50])
        pygame.draw.rect(window, self.COLOR, [self.WIDTH - 350, 10, 302, 52], 2)
        self.gen_health_percent(window)

    def gen_health_percent(self, window):
        health = self.font.render(str(self.player_health) + "%", True, self.COLOR) 
        healthRect = health.get_rect()
        healthRect.center = (self.WIDTH - 320, 90)
        window.blit(health, healthRect)

    def take_damage(self, dmg):
        self.player_health -= dmg

    def heal(self, recover):
        if self.player_health + recover > 100:
            self.player_health = 100
        else:
            self.player_health = self.player_health + recover