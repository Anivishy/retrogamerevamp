
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
openingFont = pygame.font.SysFont("monospace", 60)
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
            pygame.time.wait(125)

def instructionsPage():
    x=x

def CenterText(text):
    textWidth, textHeight = openingFont.size(text)
    return ((WIDTH - textWidth) / 2)

openingText("Welcome!", CenterText("Welcome!"), 150)
pygame.time.wait(500)
instructions = "Click 'begin' to get started!"
openingText(instructions, CenterText(instructions), 250)

# begin button
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(300, 450, 400, 150), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(305, 455, 390, 140), 10)
openingText("Begin", 350, 500)

# instructions button
pygame.draw.rect(screen, (30, 144, 255), pygame.Rect(800, 450, 400, 150), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(805, 455, 390, 140), 10)
openingText("Instructions", 850, 500)

# settings button
pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(300, 700, 400, 150), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(305, 705, 390, 140), 10)
openingText("Settings", 350, 750)

# quit button
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(800, 700, 400, 150), 10)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(805, 705, 390, 140), 10)
openingText("Quit", 850, 750)

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
            if pygame.Rect(800, 700, 400, 150):
                pygame.quit()
                quit()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(800, 450, 400, 150):
                instructionsPage()

    pygame.display.flip()

    # todo:  buttons (start game, instructions, settings, quit), use WIDTH/HEIGHT instead of values, center button text, create instrictions popup
    # later: splashscreen? better background