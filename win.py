import pygame
from calculated_vars import *
pygame.init()

class Win:
    def __init__(self, screen, px, py):
        self.screen = screen
        clock = pygame.time.Clock()
        for _ in range(150):
            self.process_input()
            clock.tick(60)

        pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/win.wav"))
        
        pygame.draw.circle(self.screen, (0, 255, 0), (px, py), RADIUS+2)
        
        pygame.display.update()
        for _ in range(115):
            self.process_input()
            clock.tick(60)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import sys; sys.exit()

