import pygame
import random
import os
import pyautogui
import time
import asyncio

base = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(path):
    return os.path.join(base, path)

from calculated_vars import *
class mouseTarget:

    def __init__ (self):
        self.target = pygame.image.load(sanitize_path('Images/crosshair.png')) 
        self.SCALE_SIZE = (75, 75)
        self.target = pygame.transform.scale(self.target, self.SCALE_SIZE)
        self.bx = WIDTH // 2
        self.by = HEIGHT // 2

    def update_target(self, window, mouse_pos, joystick):
        if joystick:

            # if (joystick and joystick.get_axis(2) <= -JOYSTICK_THRESHOLD):
            #     self.bx = max(0, self.bx - 1)
            # if (joystick and joystick.get_axis(2) >= JOYSTICK_THRESHOLD):
            #     self.bx = max(0, self.bx + 1)
            # if (joystick and joystick.get_axis(3) <= -JOYSTICK_THRESHOLD):
            #     self.by = max(0, self.by - 1)
            # if (joystick and joystick.get_axis(3) >= JOYSTICK_THRESHOLD):
            #     self.by = max(0, self.by + 1)
            
            if abs(joystick.get_axis(2)) > JOYSTICK_THRESHOLD / 5:
                self.bx = min(max(0, self.bx + (joystick.get_axis(2) * 20)), WIDTH)
            if abs(joystick.get_axis(3)) > JOYSTICK_THRESHOLD / 5:
                self.by = min(max(0, self.by + (joystick.get_axis(3) * 20)), HEIGHT)
            



            updated_mouse_pos = (self.bx - 40, self.by - 40)
            window.blit(self.target, updated_mouse_pos)
        else:
            mouse_pos = pygame.mouse.get_pos()
            updated_mouse_pos = (mouse_pos[0] - 40, mouse_pos[1] - 40)
            window.blit(self.target, updated_mouse_pos)

