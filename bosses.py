import pygame

from user_settings import *
from calculated_vars import *

import colors

import math

class BossTL: # top left
    def __init__(self, screen):
        self.screen = screen

        self.x = SQUARE_SIZE * 2
        self.y = SQUARE_SIZE * 2

        self.width = self.height = SQUARE_SIZE * 0.75
        self.speed = BOSS_SPEED

    def process_projectiles(self):
        ... # TODO uhhhhhh idk what to do for this yet

    def update(self, relx, rely):
        dy = rely - (self.y + self.height // 2)
        dx = relx - (self.x + self.width // 2)
        
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance != 0:
            if UNCAPPED_FPS:
                ratio = self.speed * SQUARE_SIZE * UCFD.delay / distance
            else:
                ratio = (self.speed * SQUARE_SIZE) / FPS / distance
            self.x += dx * ratio
            self.y += dy * ratio

        
        self.draw()
        pygame.draw.line(self.screen, (255, 0, 0), (relx, rely), (self.x + self.width // 2, self.y + self.height // 2), 2)

    def draw(self):
        pygame.draw.rect(
            self.screen,
            colors.FOREST,
            pygame.Rect(
                self.x,
                self.y,
                self.width, self.height
            )
        )