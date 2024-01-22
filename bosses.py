import pygame

from user_settings import *
from calculated_vars import *

import colors

import math
import time

import os
base = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(path):
    return os.path.join(base, path)

images = {}
for color in ["forest", "lava", "ice", "shadow", "dead"]:
    mapped = {}
    for direction in ["up", "down", "left", "right"]:
        mapped[direction] = pygame.transform.scale(pygame.image.load(sanitize_path("Images/procedural-ghosts/" + color + "-" + direction + ".png")), (int(SQUARE_SIZE * 0.75), int(SQUARE_SIZE * 0.75)))
    images[color] = mapped

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

        self.cam_x = 0
        self.cam_y = 0

        self.health = 100
        self.type_ = 1

        self.direction = 0


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
            pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_shoot.wav"))
            
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
            pygame.draw.circle(self.screen, (0, 0, 0), (projectile[0][0] - self.cam_x, projectile[0][1] - self.cam_y), PROJECTILE_RADIUS)
            pygame.draw.circle(self.screen, colors.FOREST, (projectile[0][0] - self.cam_x, projectile[0][1] - self.cam_y), PROJECTILE_RADIUS, width=int(PROJECTILE_RADIUS // 3))

    def update_cam(self, left, right, top, bottom):
        self.cam_x = left * SQUARE_SIZE
        self.cam_y = top * SQUARE_SIZE

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

            if dx == 0:
                if dy < 0:
                    self.direction = 4
                else:
                    self.direction = 2
            else:
                discrim = abs(math.atan(dy/dx))
                #print(discrim, dy)
                if discrim > (math.pi / 4):
                    if dy < 0:
                        self.direction = 4
                    else:
                        self.direction = 2
                else:
                    if dx < 0:
                        self.direction = 3
                    else:
                        self.direction = 1

        
        
        self.process_projectiles(frame)
        self.draw()

    def draw(self):
        direction = ["right", "down", "left", "up"][self.direction - 1]
        img = images["forest"][direction]
        self.screen.blit(
            img,
            pygame.Rect(
                self.x,
                self.y,
                self.width, self.height
            )
        )

class BossTR: # top right
    def __init__(self, screen):
        self.screen = screen

        self.x = WIDTH - SQUARE_SIZE * 2
        self.y = SQUARE_SIZE * 2

        self.width = self.height = SQUARE_SIZE * 0.75
        self.speed = BOSS_SPEED
        self.projectiles = set()
        self.created_at = time.time()
        self.last_updated = time.time()

        self.cam_x = 0
        self.cam_y = 0

        self.health = 100
        self.type_ = 2

        self.direction = 0
    
    def update_cam(self, left, right, top, bottom):
        self.cam_x = right * SQUARE_SIZE
        self.cam_y = top * SQUARE_SIZE


    def check_all_collisions(self):
        cp = set()
        for projectile in self.projectiles:
            pos = projectile[0]
            if pos[0] + PROJECTILE_RADIUS <= WIDTH + WALL_WIDTH / 2 \
            and pos[0] - PROJECTILE_RADIUS >= WIDTH - (BOSS_AREA * SQUARE_SIZE + WALL_WIDTH / 2) \
            and pos[1] - PROJECTILE_RADIUS >= -WALL_WIDTH / 2 \
            and pos[1] + PROJECTILE_RADIUS <= BOSS_AREA * SQUARE_SIZE + WALL_WIDTH / 2:
                cp.add(projectile)
        return cp

    def process_projectiles(self, frame):
        s = time.time()
        if frame == 0 or (FPS is None and s - self.last_updated > 1):
            self.last_updated = s
            self.projectiles.add(
                ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), 45, 1.5 * BOSS_SPEED)
            )
            self.projectiles.add(
                ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), 135, 1.5 * BOSS_SPEED)
            )
            self.projectiles.add(
                ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), -135, 1.5 * BOSS_SPEED)
            )
            self.projectiles.add(
                ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), -45, 1.5 * BOSS_SPEED)
            )
            pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_shoot.wav"))
            
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
            pygame.draw.circle(self.screen, (0, 0, 0), (projectile[0][0] - self.cam_x, projectile[0][1] - self.cam_y), PROJECTILE_RADIUS)
            pygame.draw.circle(self.screen, colors.LAVA, (projectile[0][0] - self.cam_x, projectile[0][1] - self.cam_y), PROJECTILE_RADIUS, width=int(PROJECTILE_RADIUS // 3))

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

            if dx == 0:
                if dy < 0:
                    self.direction = 4
                else:
                    self.direction = 2
            else:
                discrim = abs(math.atan(dy/dx))
                #print(discrim, dy)
                if discrim > (math.pi / 4):
                    if dy < 0:
                        self.direction = 4
                    else:
                        self.direction = 2
                else:
                    if dx < 0:
                        self.direction = 3
                    else:
                        self.direction = 1
        
        self.process_projectiles(frame)
        self.draw()

    def draw(self):
        direction = ["right", "down", "left", "up"][self.direction - 1]
        img = images["lava"][direction]
        self.screen.blit(
            img,
            pygame.Rect(
                self.x,
                self.y,
                self.width, self.height
            )
        )

class BossBL: # bottom left
    def __init__(self, screen):
        self.screen = screen

        self.x = SQUARE_SIZE * 2
        self.y = HEIGHT - SQUARE_SIZE * 2

        self.width = self.height = SQUARE_SIZE * 0.75
        self.speed = BOSS_SPEED
        self.projectiles = set()
        self.created_at = time.time()
        self.last_updated = time.time()

        self.marker = 0

        self.health = 100
        self.type_ = 3
        self.direction = 0

    def update_cam(self, left, right, top, bottom):
        self.cam_x = left * SQUARE_SIZE
        self.cam_y = bottom * SQUARE_SIZE

    def check_all_collisions(self):
        cp = set()
        for projectile in self.projectiles:
            pos = projectile[0]
            if pos[0] - PROJECTILE_RADIUS >= -WALL_WIDTH / 2 \
            and pos[0] + PROJECTILE_RADIUS <= BOSS_AREA * SQUARE_SIZE + WALL_WIDTH / 2 \
            and pos[1] + PROJECTILE_RADIUS <= HEIGHT - (WALL_WIDTH / 2) \
            and pos[1] - PROJECTILE_RADIUS >= HEIGHT - (BOSS_AREA * SQUARE_SIZE + WALL_WIDTH / 2):
                cp.add(projectile)
        return cp

    def process_projectiles(self, frame):
        s = time.time()
        
        if (FPS is None and s - self.last_updated > .5) or (FPS and frame % (FPS / 2) == 0):
            self.marker = (self.marker + 1) % 2
            self.last_updated = s
            if self.marker == 1:
                self.projectiles.add(
                    ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), 45, 1.5 * BOSS_SPEED)
                )
                self.projectiles.add(
                    ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), 135, 1.5 * BOSS_SPEED)
                )
                self.projectiles.add(
                    ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), -135, 1.5 * BOSS_SPEED)
                )
                self.projectiles.add(
                    ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), -45, 1.5 * BOSS_SPEED)
                )
            else:
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
            pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_shoot.wav"))

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
            pygame.draw.circle(self.screen, (0, 0, 0), (projectile[0][0] - self.cam_x, projectile[0][1] - self.cam_y), PROJECTILE_RADIUS)
            pygame.draw.circle(self.screen, colors.ICE, (projectile[0][0] - self.cam_x, projectile[0][1] - self.cam_y), PROJECTILE_RADIUS, width=int(PROJECTILE_RADIUS // 3))

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
            if dx == 0:
                if dy < 0:
                    self.direction = 4
                else:
                    self.direction = 2
            else:
                discrim = abs(math.atan(dy/dx))
                #print(discrim, dy)
                if discrim > (math.pi / 4):
                    if dy < 0:
                        self.direction = 4
                    else:
                        self.direction = 2
                else:
                    if dx < 0:
                        self.direction = 3
                    else:
                        self.direction = 1
        
        
        self.process_projectiles(frame)
        self.draw()

    def draw(self):
        direction = ["right", "down", "left", "up"][self.direction - 1]
        img = images["ice"][direction]
        self.screen.blit(
            img,
            pygame.Rect(
                self.x,
                self.y,
                self.width, self.height
            )
        )

class BossBR: # bottom right
    def __init__(self, screen):
        self.screen = screen
        self.type_ = 4 

        self.x = WIDTH - SQUARE_SIZE * 2
        self.y = HEIGHT - SQUARE_SIZE * 2

        self.width = self.height = SQUARE_SIZE * 0.75
        self.speed = BOSS_SPEED
        self.projectiles = []
        self.created_at = time.time()
        self.last_updated = time.time()

        self.marker = 0
        self.spiral = 8

        self.health = 100
        self.direction = 0

        if BULLET_HELL_BOTTOM_RIGHT:
            self.spiral = FPS
            if not FPS:
                self.spiral = 1 / UCFD.delay



    def check_all_collisions(self):
        cp = []
        for projectile in self.projectiles:
            pos = projectile[0]
            if pos[0] + PROJECTILE_RADIUS <= WIDTH - (WALL_WIDTH / 2) \
            and pos[0] - PROJECTILE_RADIUS >= WIDTH - (BOSS_AREA * SQUARE_SIZE + WALL_WIDTH / 2) \
            and pos[1] + PROJECTILE_RADIUS <= HEIGHT - (WALL_WIDTH / 2) \
            and pos[1] - PROJECTILE_RADIUS >= HEIGHT - (BOSS_AREA * SQUARE_SIZE + WALL_WIDTH / 2):
                cp.append(projectile)
        return cp

    def process_projectiles(self, frame):
        s = time.time()
        
        if (FPS is None and s - self.last_updated > 1/self.spiral) or (FPS and frame % (FPS // self.spiral) == 0):
            self.marker = (self.marker + 1) % self.spiral
            self.last_updated = s
            
            a = self.marker * (360 / self.spiral)
            self.projectiles.append(
                ((self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), a, 1.5 * BOSS_SPEED)
            )
            pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_shoot.wav"))
        c = []
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

            c.append(tuple(projectile))

        self.projectiles = c
        self.projectiles = self.check_all_collisions()
        
        for projectile in self.projectiles:
            pygame.draw.circle(self.screen, (0, 0, 0), (projectile[0][0] - self.cam_x, projectile[0][1] - self.cam_y), PROJECTILE_RADIUS)
            pygame.draw.circle(self.screen, colors.SHADOW, (projectile[0][0] - self.cam_x, projectile[0][1] - self.cam_y), PROJECTILE_RADIUS, width=int(PROJECTILE_RADIUS // 3))
    
    def update_cam(self, left, right, top, bottom):
        self.cam_x = right * SQUARE_SIZE
        self.cam_y = bottom * SQUARE_SIZE

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
            if dx == 0:
                if dy < 0:
                    self.direction = 4
                else:
                    self.direction = 2
            else:
                discrim = abs(math.atan(dy/dx))
                #print(discrim, dy)
                if discrim > (math.pi / 4):
                    if dy < 0:
                        self.direction = 4
                    else:
                        self.direction = 2
                else:
                    if dx < 0:
                        self.direction = 3
                    else:
                        self.direction = 1
        
        
        self.process_projectiles(frame)
        self.draw()

    def draw(self):
        direction = ["right", "down", "left", "up"][self.direction - 1]
        img = images["shadow"][direction]
        self.screen.blit(
            img,
            pygame.Rect(
                self.x,
                self.y,
                self.width, self.height
            )
        )