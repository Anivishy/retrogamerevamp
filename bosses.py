import pygame

from user_settings import *
from calculated_vars import *

import colors

import math
import time

class BossTL: # top left
    def __init__(self, screen):
        self.screen = screen

        self.x = SQUARE_SIZE * 2
        self.y = SQUARE_SIZE * 2

        self.width = self.height = SQUARE_SIZE * 0.75
        self.speed = BOSS_SPEED
        self.projectiles = set()
        self.created_at = time.time()
        self.last_updated = time.time()


    def check_all_collisions(self):
        cp = set()
        for projectile in self.projectiles:
            pos = projectile[0]
            if pos[0] - PROJECTILE_RADIUS >= -WALL_WIDTH / 2 \
            and pos[0] + PROJECTILE_RADIUS <= BOSS_AREA * SQUARE_SIZE + WALL_WIDTH / 2 \
            and pos[1] - PROJECTILE_RADIUS >= -WALL_WIDTH  / 2 \
            and pos[1] + PROJECTILE_RADIUS <= BOSS_AREA * SQUARE_SIZE + WALL_WIDTH  / 2:
                cp.add(projectile)
        return cp

    def process_projectiles(self, frame):
        s = time.time()
        if frame == 0 or (FPS is None and s - self.last_updated > 1):
            self.last_updated = s
            self.projectiles.add(
                ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), 0, 1.5 * BOSS_SPEED)
            )
            self.projectiles.add(
                ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), 90, 1.5 * BOSS_SPEED)
            )
            self.projectiles.add(
                ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), 180, 1.5 * BOSS_SPEED)
            )
            self.projectiles.add(
                ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), -90, 1.5 * BOSS_SPEED)
            )
            
        c = set()
        for _ in range(len(self.projectiles)):
            projectile = list(self.projectiles.pop())
            pos = projectile[0]

            if FPS:
                dx = math.cos(math.radians(projectile[1])) * (SQUARE_SIZE * projectile[2] / FPS)
                dy = math.sin(math.radians(projectile[1])) * (SQUARE_SIZE * projectile[2] / FPS)
            else:
                dx = math.cos(math.radians(projectile[1])) * (projectile[2] * SQUARE_SIZE * UCFD.delay)
                dy = math.sin(math.radians(projectile[1])) * (projectile[2] * SQUARE_SIZE * UCFD.delay)
                
            pos = (pos[0] + dx, pos[1] + dy)
            projectile[0] = pos

            c.add(tuple(projectile))

        self.projectiles = c
        self.projectiles = self.check_all_collisions()
        
        for projectile in self.projectiles:
            pygame.draw.circle(self.screen, (0, 0, 0), projectile[0], PROJECTILE_RADIUS)
            pygame.draw.circle(self.screen, colors.FOREST, projectile[0], PROJECTILE_RADIUS, width=int(PROJECTILE_RADIUS // 3))

    def update(self, relx, rely, frame):
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

        
        
        self.process_projectiles(frame)
        self.draw()

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