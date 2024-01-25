import pygame
from calculated_vars import *
pygame.init()

class GameOver:
    def __init__(self, width, height, fullscreen, px, py):
        self.screen = pygame.display.set_mode((width, height), fullscreen if fullscreen else 0)
        clock = pygame.time.Clock()
        for _ in range(90):
            self.process_input()
            self.screen.fill((0, 0, 0))
            pygame.draw.circle(self.screen, (255, 255, 0), (px, py), RADIUS)
            pygame.display.update()
            clock.tick(60)

        for _ in range(2):
            pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/death1.wav"))
            for _ in range(30):
                self.process_input()
                self.screen.fill((0, 0, 0))
            #    pygame.draw.circle(self.screen, (255, 255, 0), (px, py), RADIUS)
                pygame.display.update()
                clock.tick(60)
            for _ in range(30):
                self.process_input()
                self.screen.fill((0, 0, 0))
                pygame.draw.circle(self.screen, (255, 255, 0), (px, py), RADIUS)
                pygame.display.update()
                clock.tick(60)

        pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/death2.wav"))
        for _ in range(120):
            self.process_input()
            self.screen.fill((0, 0, 0))
            #pygame.draw.circle(self.screen, (255, 255, 0), (px, py), RADIUS)
            pygame.display.update()
            clock.tick(60)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import sys; sys.exit()

GameOver(1600, 900, False, 1600/2, 900/2)
