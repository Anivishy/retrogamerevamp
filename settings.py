import pygame
import sys
import homescreen
import instructions
import pyautogui

class openSettings:
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
        pygame.display.set_caption("Settings")

        self.exitButton = ((55/1536)*self.WIDTH, (75/1024)*self.HEIGHT, (40/1536)*self.WIDTH, (40/1024)*self.HEIGHT)

        self.SD1 = ((.15)*self.WIDTH, (.25)*self.HEIGHT, (.125)*self.WIDTH, (.08)*self.HEIGHT)
        self.SD2 = ((.35)*self.WIDTH, (.25)*self.HEIGHT, (.125)*self.WIDTH, (.08)*self.HEIGHT)
        self.SD3 = ((.55)*self.WIDTH, (.25)*self.HEIGHT, (.125)*self.WIDTH, (.08)*self.HEIGHT)
        self.SD4 = ((.75)*self.WIDTH, (.25)*self.HEIGHT, (.125)*self.WIDTH, (.08)*self.HEIGHT)
        # make this centered!!

        self.start = True

        self.fullscreenToggle = (728, 700, 80, 50)
        self.input = (700, 900, 134, 75)
        

        self.input = ""

    def text(self):
        i = instructions.createInstructions(self.WIDTH, self.HEIGHT, self.fullscreen)

        i.printText("Settings", (.1 * self.HEIGHT), True)
        i.printText("Screen Dimensions", (.2 * self.HEIGHT), False)

        pygame.display.flip()

    def setup(self):
        self.text()

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.exitButton), 2)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.SD1), 3)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.SD2), 3)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.SD3), 3)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.SD4), 3)

        if self.fullscreen:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.fullscreenToggle))
        else:
            pygame.draw.rect(self.screen, (125, 125, 125), pygame.Rect(self.fullscreenToggle))

    def run(self):
        self.setup()

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
                    if pygame.Rect(self.exitButton).collidepoint(pygame.mouse.get_pos()):
                        c = homescreen.createHomescreen(self.WIDTH, self.HEIGHT, self.fullscreen)
                        c.run(False)
                   
                    elif pygame.Rect(self.fullscreenToggle).collidepoint(pygame.mouse.get_pos()):
                        pygame.display.toggle_fullscreen() # fix
                        self.fullscreen = not self.fullscreen

                    # square screen
                    elif pygame.Rect(self.SD1).collidepoint(pygame.mouse.get_pos()):
                        try:
                            _, h = pyautogui.size()
                        except:
                            h = 600
                        squareDimensions = h - (.1*h)
                        s = openSettings(squareDimensions, squareDimensions, False)
                        s.run()

                    # vertical
                    elif pygame.Rect(self.SD2).collidepoint(pygame.mouse.get_pos()):
                        try:
                            w, h = pyautogui.size()
                        except:
                            w, h = 800, 600
                        height = h - (.1*h)
                        width = height * (2/3)
                        s = openSettings(width, height, False)
                        s.run()

                    # landscape
                    elif pygame.Rect(self.SD3).collidepoint(pygame.mouse.get_pos()):
                        try:
                            w, h = pyautogui.size()
                        except:
                            w, h = 800, 600
                        height = h - (.1*h)
                        width = w - (.1*w)
                        s = openSettings(width, height, False)
                        s.run()

                    # fullscreen
                    elif pygame.Rect(self.SD4).collidepoint(pygame.mouse.get_pos()):
                        try:
                            w, h = pyautogui.size()
                        except:
                            w, h = 800, 600
                        s = openSettings(w, h, True)
                        s.run()

                pygame.display.flip()

if __name__ == "__main__":
    try:
        WIDTH, HEIGHT = pyautogui.size()
    except:
        WIDTH = 800
        HEIGHT = 600

    s = openSettings(WIDTH, HEIGHT, True)
    s.run()

# add image for back button/toggle, add sliders/input for settings, connect changes in settings to other pages
# scale text size