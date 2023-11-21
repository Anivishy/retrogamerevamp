
import pygame
import random
import sys

class createHomescreen:
    def __init__(self):
        pygame.init()

        try:
            import pyautogui
            self.WIDTH, self.HEIGHT = pyautogui.size()
        except:
            self.WIDTH = 800
            self.HEIGHT = 600

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("Homescreen")
        self.openingFont = pygame.font.SysFont("monospace", 50)
        self.start = True

        self.size = 115
        self.cols = (self.WIDTH // self.size) + 2
        self.rows = (self.HEIGHT // self.size) + 2
        self.table = [[0 for x in range(self.cols)] for y in range(self.rows)]

        self.beginButtonOutline = ((300/1536)*self.WIDTH, (450/1024)*self.HEIGHT, (400/1536)*self.WIDTH, (150/1024)*self.HEIGHT)
        self.beginButton = ((310/1536)*self.WIDTH, (460/1024)*self.HEIGHT, (380/1536)*self.WIDTH, (130/1024)*self.HEIGHT)
        self.instructionButtonOutline = ((800/1536)*self.WIDTH, (450/1024)*self.HEIGHT, (400/1536)*self.WIDTH, (150/1024)*self.HEIGHT)
        self.instructionButton = ((810/1536)*self.WIDTH, (460/1024)*self.HEIGHT, (380/1536)*self.WIDTH, (130/1024)*self.HEIGHT)
        self.settingButtonOutline = ((300/1536)*self.WIDTH, (700/1024)*self.HEIGHT, (400/1536)*self.WIDTH, (150/1024)*self.HEIGHT)
        self.settingButton = ((310/1536)*self.WIDTH, (710/1024)*self.HEIGHT, (380/1536)*self.WIDTH, (130/1024)*self.HEIGHT)
        self.quitButtonOutline = ((800/1536)*self.WIDTH, (700/1024)*self.HEIGHT, (400/1536)*self.WIDTH, (150/1024)*self.HEIGHT)
        self.quitButton = ((810/1536)*self.WIDTH, (710/1024)*self.HEIGHT, (380/1536)*self.WIDTH, (130/1024)*self.HEIGHT)

    def grid(self, x, y):
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(move)

        for xShift, yShift in move:
            x2 = x + xShift
            y2 = y + yShift
            if -1 < x2 < self.cols and -1 < y2 < self.rows and not self.table [y2][x2]:
                self.table [y2][x2] = True

                pygame.draw.line(self.screen, (0, 0, 255), (x * self.size, y * self.size), (x2 * self.size, y2 * self.size), 3)
                pygame.display.flip()
                pygame.time.wait(18) #18
                self.grid(x2, y2)
            
    def openingText(self, text, x, y):
        for i in range(len(text)):
            char = self.openingFont.render(text[i], True, (255, 255, 255), (0, 0, 0))
            self.screen.blit(char, (x, y))

            x += char.get_width()
            if i != len(text)-1:
                self.screen.blit(self.openingFont.render("|", True, (255, 255, 255)), (x, y))

            pygame.display.flip()

            if self.start:
                pygame.time.wait(115) #115

    def CenterText(self, text):
        textWidth, textHeight = self.openingFont.size(text)
        return ((self.WIDTH - textWidth) / 2)

    def CenterButtons(self, text, buttonX, buttonY, buttonWidth, buttonHeight):
        textWidth, textHeight = self.openingFont.size(text)
        startX = buttonX + (buttonWidth - textWidth) / 2
        startY = buttonY + (buttonHeight - textHeight) / 2
        return (startX, startY)
    
    def run(self):
        self.grid(0, 0)

        # title
        self.openingText("Welcome!", self.CenterText("Welcome!"), (.15 * self.HEIGHT))
        pygame.time.wait(500)
        instructions = "Click 'begin' to get started!"
        self.openingText(instructions, self.CenterText(instructions), (.25 * self.HEIGHT))

        # begin button
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.beginButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.beginButton))
        a, b, c, d = self.beginButtonOutline
        x, y = self.CenterButtons("Begin", a, b, c, d)
        self.openingText("Begin", x, y)

        # instructions button
        pygame.draw.rect(self.screen, (30, 144, 255), pygame.Rect(self.instructionButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.instructionButton))
        a, b, c, d = self.instructionButtonOutline
        x, y = self.CenterButtons("Instructions", a, b, c, d)
        self.openingText("Instructions", x, y)

        # settings button
        pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(self.settingButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.settingButton))
        a, b, c, d = self.settingButtonOutline
        x, y = self.CenterButtons("Settings", a, b, c, d)
        self.openingText("Settings", x, y)

        # quit button
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.quitButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.quitButton))
        a, b, c, d = self.quitButtonOutline
        x, y = self.CenterButtons("Quit", a, b, c, d)
        self.openingText("Quit", x, y)

        self.start = False

if __name__ == "__main__":
    c = createHomescreen()
    c.run()

while True:
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
            if pygame.Rect(c.quitButtonOutline).collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            
            # begin button clicked
            elif pygame.Rect(c.beginButtonOutline).collidepoint(pygame.mouse.get_pos()):
                import introlevel
                g = introlevel.start_game()

            # instruction button clicked
            elif pygame.Rect(c.instructionButtonOutline).collidepoint(pygame.mouse.get_pos()):
                import instructions
                i = instructions.createInstructions()
     
    pygame.display.flip()

    # todo: buttons functionality, create instructions page, decide on and add settings
    # later: splashscreen? Add comments to code

    # things to include in instructions:
        # - up, down, left, right arrows to navigate
        # - goal is to collect all pellets in the area (or collect _ number of points?)
        # - if you eat a "power pellet", you can eat ghosts for points
        # once you pass the first level, different zones will be unlocked, each with special challenges (add instructions at the corner of each page with a (?))
