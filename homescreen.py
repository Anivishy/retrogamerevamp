
import pygame

pygame.init()

try:
    import pyautogui
    WIDTH, HEIGHT = pyautogui.size()
except:
    WIDTH = 800
    HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen.fill((0, 0, 0))
pygame.display.set_caption("Homescreen")
openingFont = pygame.font.SysFont("monospace", 40)
start = True

def openingText(text, x, y):
    for i in range(len(text)):
        char = openingFont.render(text[i], True, (255, 255, 255), (0, 0, 0))
        screen.blit(char, (x, y))

        x += char.get_width()
        if i != len(text)-1:
            screen.blit(openingFont.render("|", True, (255, 255, 255)), (x, y))

        pygame.display.flip()

        if start:
            pygame.time.wait(150)

def CenterText(text):
    textWidth, textHeight = openingFont.size(text)
    return ((WIDTH - textWidth) / 2)

openingText("Welcome!", CenterText("Welcome!"), 150)
instructions = "Click 'begin' to get started!"
openingText(instructions, CenterText(instructions), 250)
start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()


    pygame.display.flip()

    # todo: all instructions, cursor, buttons (start game, instructions, settings, quit)
    # later: splashscreen? background