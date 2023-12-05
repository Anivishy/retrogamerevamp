import pygame
import random
import os
import pyautogui
import time
import asyncio

base = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(path):
    return os.path.join(base, path)

class mouseTarget:

    def __init__ (self):
        self.target = pygame.image.load(sanitize_path('projectileimgaes/lazerblast.png')) #temp image
        self.SCALE_SIZE = (75, 75)
        self.target = pygame.transform.scale(self.target, self.SCALE_SIZE)

    def update_target(self, window, mouse_pos):
        mouse_pos = pygame.mouse.get_pos()
        updated_mouse_pos = (mouse_pos[0] - 40, mouse_pos[1] - 40)
        window.blit(self.target, updated_mouse_pos)
