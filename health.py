import pygame
import random
import os
import pyautogui

class healthbar:

    pygame.init()

    def __init__ (self):
        #Value of player's starting health
        self.player_health = 100 
        #Shield init value, starts at 0 until regeneration begins
        self.player_shield = 0 
        
        #Fonts
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        #Window Constants
        #self.WIDTH, self.HEIGHT = pyautogui.size()

        #Health Constants
        #self.player_health = 100 #Health of the player, as a percent

        #Colors
        self.GREEN = (0, 255, 0)
        self.YELLOW = (224, 247, 20)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.BLUE = (63, 229, 235)
        self.COLOR = ()


    #Generation of the healthbar
    def gen_healthbar(self, window, WIDTH):
        #Checks to change color based on the player's health, changing form green to yellow to red as they get clsoer to loosing all of their health
        if self.player_health <= 100 and self.player_health > 50:
            self.COLOR = self.GREEN
            pygame.draw.rect(window, self.GREEN, [WIDTH - 350, 10, 300 * (self.player_health/100), 50])
        elif self.player_health <= 50 and self.player_health > 25:
            self.COLOR = self.YELLOW
            pygame.draw.rect(window, self.YELLOW, [WIDTH - 350, 10, 300 * (self.player_health/100), 50])
        elif self.player_health <= 25 and self.player_health > 0:
            self.COLOR = self.RED
            pygame.draw.rect(window, self.RED, [WIDTH - 350, 10, 300 * (self.player_health/100), 50])
        pygame.draw.rect(window, self.COLOR, [WIDTH - 350, 10, 302, 52], 2)
        self.gen_health_percent(window, WIDTH)

    def gen_health_percent(self, window, WIDTH):
        health = self.font.render(str(round(self.player_health)) + " |", True, self.COLOR) 
        healthRect = health.get_rect()
        if self.player_health == 100:
            healthRect.center = (WIDTH - 150, 140)
        else:
            healthRect.center = (WIDTH - 140, 140)
        window.blit(health, healthRect)

    def gen_shieldbar(self, window, WIDTH):
        pygame.draw.rect(window, self.BLUE, [WIDTH - 350, 60, 302, 52], 2)
        pygame.draw.rect(window, self.BLUE, [WIDTH - 350, 60, 300 * (self.player_shield/50), 50])
        self.gen_shieldbar_percent(window, WIDTH)

    def gen_shieldbar_percent(self, window, WIDTH):
        health = self.font.render("| " + str(round(self.player_shield)), True, self.BLUE) 
        healthRect = health.get_rect()
        if self.player_health == 100:
            healthRect.center = (WIDTH - 80, 140)
        else:
            healthRect.center = (WIDTH - 70, 140)
        window.blit(health, healthRect)

    def take_damage(self, dmg):
        if self.player_shield > dmg:
            self.player_shield -= dmg
        elif self.player_shield > 0 and self.player_shield < dmg:
            dmg -= self.player_shield
            self.player_shield = 0
            self.player_health -= dmg
        else:            
            self.player_health -= dmg

    def heal(self, recover):
        if self.player_health < 100:
            if self.player_health + recover > 100:
                self.player_health = 100
            else:
                self.player_health = self.player_health + recover
        else:
            if self.player_shield == 50:
                pass
            elif self.player_shield + recover > 50:
                self.player_shield = 50
            else:
                self.player_shield = self.player_shield + recover
    
    def regen(self, recover):
            if self.player_shield == 50:
                pass
            elif self.player_shield + recover > 50:
                self.player_shield = 50
            else:
                self.player_shield = self.player_shield + recover
    
    def get_health(self):
        return self.player_health
    
    