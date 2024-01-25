import pygame
import random
import os
import pyautogui

pygame.init()
base = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(path):
    return os.path.join(base, path)

class pellets:

    pygame.init()

    def __init__ (self):

        self.score = 0
        self.ammo_add = 0
        self.ammo = 50
                
        #Fonts
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        #images
        self.image = pygame.image.load(sanitize_path('Images/ammoIconGrey.png'))
        self.SCALE_SIZE = (75, 75)
        self.image = pygame.transform.scale(self.image, self.SCALE_SIZE)


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
        score_rect.center = (WIDTH - 120, 180)
        window.blit(score_disp, score_rect)
        #print(self.score)

    def update_score(self):
        self.score += 1
        self.ammo_add += 1
        if self.ammo_add % 5 == 0:
            pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/new_bullet.wav"))
            self.add_ammo(1)
            self.ammo_add = 0
            

    def display_ammo(self, window, WIDTH):
        ammo_disp = self.font.render(str(self.ammo), True, self.WHITE) 
        ammo_rect = ammo_disp.get_rect()
        ammo_rect.center = (WIDTH - 70, 250)
        window.blit(ammo_disp, ammo_rect)
        window.blit(self.image, (WIDTH - 160, 210))
        #print(self.score)

    def get_ammo(self):
        return self.ammo

    def add_ammo(self, amount):
        self.ammo += amount

    def use_ammo(self, amount):
        self.ammo -= amount