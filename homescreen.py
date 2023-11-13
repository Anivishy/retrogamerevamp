
import pygame
import random

pygame.init()

WIDTH = 1536
HEIGHT = 1024

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen.fill((0, 0, 0))
pygame.display.set_caption("Homescreen")
openingFont = pygame.font.SysFont("monospace", 50)
start = True

size = 115
cols = (WIDTH // size) + 2
rows = (HEIGHT // size) + 2
table = [[0 for x in range(cols)] for y in range(rows)]

def grid(x, y):
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(move)

    for xShift, yShift in move:
        x2 = x + xShift
        y2 = y + yShift
        if -1 < x2 < cols and -1 < y2 < rows and not table [y2][x2]:
            table [y2][x2] = True

            pygame.draw.line(screen, (0, 0, 255), (x * size, y * size), (x2 * size, y2 * size), 3)
            pygame.display.flip()
            pygame.time.wait(30)
            grid(x2, y2)
        
def openingText(text, x, y):
    for i in range(len(text)):
        char = openingFont.render(text[i], True, (255, 255, 255), (0, 0, 0))
        screen.blit(char, (x, y))

        x += char.get_width()
        if i != len(text)-1:
            screen.blit(openingFont.render("|", True, (255, 255, 255)), (x, y))

        pygame.display.flip()

        if start:
            pygame.time.wait(115)

def CenterText(text):
    textWidth, textHeight = openingFont.size(text)
    return ((WIDTH - textWidth) / 2)

def CenterButtons(text, buttonX, buttonY, buttonWidth, buttonHeight):
    textWidth, textHeight = openingFont.size(text)
    startX = buttonX + (buttonWidth - textWidth) / 2
    startY = buttonY + (buttonHeight - textHeight) / 2
    return (startX, startY)

grid(0, 0)

openingText("Welcome!", CenterText("Welcome!"), (.15*HEIGHT))
pygame.time.wait(500)
instructions = "Click 'begin' to get started!"
openingText(instructions, CenterText(instructions), (.25*HEIGHT))

openingFont = pygame.font.SysFont("monospace", 40)

# begin button
beginButtonOutline = (300, 450, 400, 150)
beginButton = (310, 460, 380, 130)
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(beginButtonOutline), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(beginButton))
x, y = CenterButtons("Begin", 310, 460, 380, 130)
openingText("Begin", x, y)

# instructions button
instructionButtonOutline = (800, 450, 400, 150)
instructionButton = (810, 460, 380, 130)
pygame.draw.rect(screen, (30, 144, 255), pygame.Rect(instructionButtonOutline), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(instructionButton))
x, y = CenterButtons("Instructions", 810, 460, 380, 130)
openingText("Instructions", x, y)

# settings button
settingButtonOutline = (300, 700, 400, 150)
settingButton = (310, 710, 380, 130)
pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(settingButtonOutline), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(settingButton))
x, y = CenterButtons("Settings", 310, 710, 380, 130)
openingText("Settings", x, y)

# quit button
quitButtonOutline = (800, 700, 400, 150)
quitButton = (810, 710, 380, 130)
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(quitButtonOutline), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(quitButton))
x, y = CenterButtons("Quit", 810, 710, 380, 130)
openingText("Quit", x, y)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(quitButtonOutline):
                pygame.quit()
                quit()
    
    # instructions button clicked
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #         if pygame.Rect(instructionButtonOutline):
                # subprocess.run(instructions)

    # begin button clicked
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #         if pygame.Rect(beginButtonOutline):
    #             subprocess.run(mazegen)
                

    pygame.display.flip()

    # todo:  buttons (start game, instructions, settings, quit), create instructions
    # later: splashscreen? better background
    # Add comments
    