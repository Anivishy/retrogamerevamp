
import pygame
import random

pygame.init()

try:
    import pyautogui
    WIDTH, HEIGHT = pyautogui.size()
except:
    WIDTH = 800
    HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen.fill((0,0,0))
pygame.display.set_caption("Homepage")
openingFont = pygame.font.SysFont("monospace", 40)
start = True

def openingText(text, pos):
    for i in range(len(text)):
        print = openingFont.render(text[:i+1], True, (255, 255, 255))
        screen.blit(print, pos)
        pygame.display.flip()
        if start:
            pygame.time.wait(200)

def CenterText(text):
    textWidth, textHeight = openingFont.size(text)
    return ((WIDTH - textWidth) / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    openingText("Welcome!", (CenterText("Welcome!"), 50))

    pygame.display.flip()

    # todo: cursor, buttons (start game, instructions, settings, quit)
    # later: splashscreen? better background