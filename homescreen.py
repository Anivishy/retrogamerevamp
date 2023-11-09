
import pygame
import subprocess
# import mazegen
import instructions

pygame.init()

WIDTH = 1536
HEIGHT = 1024

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen.fill((0, 0, 0))
pygame.display.set_caption("Homescreen")
openingFont = pygame.font.SysFont("monospace", 50)
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
            pygame.time.wait(115)

def CenterText(text):
    textWidth, textHeight = openingFont.size(text)
    return ((WIDTH - textWidth) / 2)

def CenterButtons(text, buttonX, buttonY, buttonWidth, buttonHeight):
    textWidth, textHeight = openingFont.size(text)
    startX = buttonX + (buttonWidth - textWidth) / 2
    startY = buttonY + (buttonHeight - textHeight) / 2
    return (startX, startY)


openingText("Welcome!", CenterText("Welcome!"), (.15*HEIGHT))
pygame.time.wait(500)
instructions = "Click 'begin' to get started!"
openingText(instructions, CenterText(instructions), (.25*HEIGHT))

openingFont = pygame.font.SysFont("monospace", 40)

# begin button
beginButtonOutline = (300, 450, 400, 150)
beginButton = (305, 455, 390, 140)
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(beginButtonOutline), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(beginButton), 10)
x, y = CenterButtons("Begin", 305, 455, 390, 140)
openingText("Begin", x, y)

# instructions button
instructionButtonOutline = (800, 450, 400, 150)
instructionButton = (805, 455, 390, 140)
pygame.draw.rect(screen, (30, 144, 255), pygame.Rect(instructionButtonOutline), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(instructionButton), 10)
x, y = CenterButtons("Instructions", 805, 455, 390, 140)
openingText("Instructions", x, y)

# settings button
settingButtonOutline = (300, 700, 400, 150)
settingButton = (305, 705, 390, 140)
pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(settingButtonOutline), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(settingButton), 10)
x, y = CenterButtons("Settings", 305, 705, 390, 140)
openingText("Settings", x, y)

# quit button
quitButtonOutline = (800, 700, 400, 150)
quitButton = (805, 705, 390, 140)
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(quitButtonOutline), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(quitButton), 10)
x, y = CenterButtons("Quit", 805, 705, 390, 140)
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
    if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(instructionButtonOutline):
                subprocess.run(instructions)

    # begin button clicked
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #         if pygame.Rect(beginButtonOutline):
    #             subprocess.run(mazegen)
                

    pygame.display.flip()

    # todo:  buttons (start game, instructions, settings, quit), fix center button, create instructions FILE, create variable with constants
    # later: splashscreen? better background
    # Add comments
