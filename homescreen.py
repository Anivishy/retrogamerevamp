
import pygame
import random
import sys
import instructions
import settings
import pyautogui
import settings2

class createHomescreen:
    # initializing and setting constant and variable values
    def __init__(self, WIDTH, HEIGHT, FULLSCREEN):
        pygame.init()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        if (FULLSCREEN):
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
            self.fullscreen = True

        else:
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
            self.fullscreen = False

        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("Homescreen")
        self.openingFont = pygame.font.SysFont("monospace", int(50*self.WIDTH/1536))

        self.size = 115
        self.cols = int(round((self.WIDTH // self.size) + 2))
        self.rows = int(round((self.HEIGHT // self.size) + 2))
        self.table = [[0 for x in range(self.cols)] for y in range(self.rows)]

        self.beginButtonOutline = ((300/1536)*self.WIDTH, (450/1024)*self.HEIGHT, (400/1536)*self.WIDTH, (150/1024)*self.HEIGHT)
        self.beginButton = ((310/1536)*self.WIDTH, (460/1024)*self.HEIGHT, (380/1536)*self.WIDTH, (130/1024)*self.HEIGHT)
        self.instructionButtonOutline = ((800/1536)*self.WIDTH, (450/1024)*self.HEIGHT, (400/1536)*self.WIDTH, (150/1024)*self.HEIGHT)
        self.instructionButton = ((810/1536)*self.WIDTH, (460/1024)*self.HEIGHT, (380/1536)*self.WIDTH, (130/1024)*self.HEIGHT)
        self.settingButtonOutline = ((300/1536)*self.WIDTH, (700/1024)*self.HEIGHT, (400/1536)*self.WIDTH, (150/1024)*self.HEIGHT)
        self.settingButton = ((310/1536)*self.WIDTH, (710/1024)*self.HEIGHT, (380/1536)*self.WIDTH, (130/1024)*self.HEIGHT)
        self.quitButtonOutline = ((800/1536)*self.WIDTH, (700/1024)*self.HEIGHT, (400/1536)*self.WIDTH, (150/1024)*self.HEIGHT)
        self.quitButton = ((810/1536)*self.WIDTH, (710/1024)*self.HEIGHT, (380/1536)*self.WIDTH, (130/1024)*self.HEIGHT)
        
        s2 = settings2.openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
        self.green, self.blue, self.red, self.gray = s2.colorUpdate()

    # generating maze background, moves 1 unit in a random direction until no spots are left
    # initial inspiration from https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
    def grid(self, x, y, start):
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(move)

        for xShift, yShift in move:
            x2 = x + xShift
            y2 = y + yShift
            if -1 < x2 < self.cols and -1 < y2 < self.rows and not self.table [y2][x2]:
                self.table [y2][x2] = True

                pygame.draw.line(self.screen, self.blue, (x * self.size, y * self.size), (x2 * self.size, y2 * self.size), 3)
                pygame.display.flip()
                if start:
                    pygame.time.wait(15) #15
                self.grid(x2, y2, start)
            
    # printing text character by character with a "|" in front, to create a typewriter effect
    # refered to this website when stuck: https://davy.ai/display-text-in-pygame-with-a-typewriter-effect/
    def openingText(self, text, x, y, start, font):
        for i in range(len(text)):
            char = font.render(text[i], True, (255, 255, 255), (0, 0, 0))
            self.screen.blit(char, (x, y))

            x += char.get_width()
            if i != len(text)-1:
                self.screen.blit(font.render("|", True, (255, 255, 255)), (x, y))

            pygame.display.flip()

            if start:
                pygame.time.wait(65) #65

    # returns width value at which text will be centered on the screen
    def CenterText(self, text):
        textWidth, textHeight = self.openingFont.size(text)
        return ((self.WIDTH - textWidth) / 2)

    # returns width and height value at which text will be centered within a previously declared button
    def CenterButtons(self, text, buttonX, buttonY, buttonWidth, buttonHeight, font):
        textWidth, textHeight = font.size(text)
        startX = buttonX + (buttonWidth - textWidth) / 2
        startY = buttonY + (buttonHeight - textHeight) / 2
        return (startX, startY)
    
    # printing text, buttons, and background maze to screen
    def setup(self, start):
        self.grid(0, 0, start)

        # title text
        self.openingText("Welcome!", self.CenterText("Welcome!"), (.15 * self.HEIGHT), start, self.openingFont)

        if start:
            pygame.time.wait(500)

        instructions = "Click 'begin' to get started!"
        self.openingText(instructions, self.CenterText(instructions), (.25 * self.HEIGHT), start, self.openingFont)

        # begin button
        pygame.draw.rect(self.screen, self.red, pygame.Rect(self.beginButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.beginButton))
        a, b, c, d = self.beginButtonOutline
        x, y = self.CenterButtons("Begin", a, b, c, d, self.openingFont)
        self.openingText("Begin", x, y, start, self.openingFont)

        # instructions button
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.instructionButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.instructionButton))
        a, b, c, d = self.instructionButtonOutline
        x, y = self.CenterButtons("Instructions", a, b, c, d, self.openingFont)
        self.openingText("Instructions", x, y, start, self.openingFont)

        # settings button
        pygame.draw.rect(self.screen, self.green, pygame.Rect(self.settingButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.settingButton))
        a, b, c, d = self.settingButtonOutline
        x, y = self.CenterButtons("Settings", a, b, c, d, self.openingFont)
        self.openingText("Settings", x, y, start, self.openingFont)

        # quit button
        pygame.draw.rect(self.screen, self.gray, pygame.Rect(self.quitButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.quitButton))
        a, b, c, d = self.quitButtonOutline
        x, y = self.CenterButtons("Quit", a, b, c, d, self.openingFont)
        self.openingText("Quit", x, y, start, self.openingFont)

    # event handling loop
    def run(self, start):
        self.setup(start) # prints all UI elements
        pygame.mouse.set_visible(True)
        out = False
        while True:
            # handles exiting of page
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # quit button clicked
                    if pygame.Rect(self.quitButtonOutline).collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                    
                    # begin button clicked
                    elif pygame.Rect(self.beginButtonOutline).collidepoint(pygame.mouse.get_pos()):
                        import introlevel 
                        introlevel.run()
                        # import mazegen
                        # mazegen.main()

                        out = True
                        break
                    # instruction button clicked
                    elif pygame.Rect(self.instructionButtonOutline).collidepoint(pygame.mouse.get_pos()):
                        i = instructions.createInstructions(self.WIDTH, self.HEIGHT, self.fullscreen)
                        i.run()

                    # settings button clicked
                    elif pygame.Rect(self.settingButtonOutline).collidepoint(pygame.mouse.get_pos()):
                        s = settings.openSettings(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()
            if out: break
            pygame.display.flip()

# user settings used to create correct colors, screen dimensions, etc, when first opening the game
import user_settings

if __name__ == "__main__":
    # try:
    #     WIDTH, HEIGHT = pyautogui.size()
    # except:
    #     WIDTH = 800
    #     HEIGHT = 600
    while True:
        WIDTH = user_settings.WIDTH
        HEIGHT = user_settings.HEIGHT

        c = createHomescreen(WIDTH, HEIGHT, user_settings.FULLSCREEN)
        c.run(True)