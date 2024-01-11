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

        self.SD1 = ((.125)*self.WIDTH, (.25)*self.HEIGHT, (.15)*self.WIDTH, (.06)*self.HEIGHT)
        self.SD2 = ((.325)*self.WIDTH, (.25)*self.HEIGHT, (.15)*self.WIDTH, (.06)*self.HEIGHT)
        self.SD3 = ((.525)*self.WIDTH, (.25)*self.HEIGHT, (.15)*self.WIDTH, (.06)*self.HEIGHT)
        self.SD4 = ((.725)*self.WIDTH, (.25)*self.HEIGHT, (.15)*self.WIDTH, (.06)*self.HEIGHT)

        self.FPS1 = ((.15)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)
        self.FPS2 = ((.3)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)
        self.FPS3 = ((.45)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)
        self.FPS4 = ((.6)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)
        self.FPS5 = ((.75)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)
        # ^ delete .125 from all widths to center

        self.start = True

        self.fullscreenToggle = (.47*self.WIDTH, .4*self.HEIGHT, .06*self.WIDTH, .045* self.HEIGHT)

        self.difficultyToggle = (.47*self.WIDTH, .875*self.HEIGHT, .06*self.WIDTH, .045* self.HEIGHT)

        self.volumeSliderOutline = ((.25)*self.WIDTH, (.525)*self.HEIGHT, (.6)*self.WIDTH, (.02)*self.HEIGHT)
        self.volumeSlider = ((.26)*self.WIDTH, (.5275)*self.HEIGHT, (.01)*self.WIDTH, (.015)*self.HEIGHT)
        self.currentVolume = 1.0
        self.printVol = str(self.currentVolume * 100)

        self.joystickSliderOutline = ((.25)*self.WIDTH, (.625)*self.HEIGHT, (.6)*self.WIDTH, (.02)*self.HEIGHT)
        self.joystickSlider = ((.26)*self.WIDTH, (.6275)*self.HEIGHT, (.01)*self.WIDTH, (.015)*self.HEIGHT)
        self.currentjoystick = 0.5

        self.difficulty = False

    def text(self):
        i = instructions.createInstructions(self.WIDTH, self.HEIGHT, self.fullscreen)
        h = homescreen.createHomescreen(self.WIDTH, self.HEIGHT, self.fullscreen)

        i.printText("Settings", (.1 * self.HEIGHT), True)
        i.printText("Screen Dimensions", (.2 * self.HEIGHT), False)
        i.printText("Fullscreen", (.35 * self.HEIGHT), False)
        i.printText("Volume", (.475 * self.HEIGHT), False)
        i.printText("Joystick Threshold", (.575 * self.HEIGHT), False)
        i.printText("FPS", (.675 * self.HEIGHT), False)
        i.printText("Final Level Difficulty", (.825 * self.HEIGHT), False)

        buttonFont = pygame.font.SysFont("monospace", int(30*self.WIDTH/1536))

        # Screen Dimension Labels
        a, b, c, d = self.SD1
        x, y = h.CenterButtons("Square", a, b, c, d, buttonFont)
        h.openingText("Square", x, y, False, buttonFont)

        a, b, c, d = self.SD2
        x, y = h.CenterButtons("Vertical", a, b, c, d, buttonFont)
        h.openingText("Vertical", x, y, False, buttonFont)

        a, b, c, d = self.SD3
        x, y = h.CenterButtons("Landscape", a, b, c, d, buttonFont)
        h.openingText("Landscape", x, y, False, buttonFont)

        a, b, c, d = self.SD4
        x, y = h.CenterButtons("Fullscreen", a, b, c, d, buttonFont)
        h.openingText("Fullscreen", x, y, False, buttonFont)

        # FPS Labels
        a, b, c, d = self.FPS1
        x, y = h.CenterButtons("20", a, b, c, d, buttonFont)
        h.openingText("20", x, y, False, buttonFont)

        a, b, c, d = self.FPS2
        x, y = h.CenterButtons("60", a, b, c, d, buttonFont)
        h.openingText("60", x, y, False, buttonFont)

        a, b, c, d = self.FPS3
        x, y = h.CenterButtons("90", a, b, c, d, buttonFont)
        h.openingText("90", x, y, False, buttonFont)

        a, b, c, d = self.FPS4
        x, y = h.CenterButtons("120", a, b, c, d, buttonFont)
        h.openingText("120", x, y, False, buttonFont)

        a, b, c, d = self.FPS5
        x, y = h.CenterButtons("Uncapped", a, b, c, d, buttonFont)
        h.openingText("Uncapped", x, y, False, buttonFont)

        pygame.display.flip()

    def setup(self):
        self.text()

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.exitButton), 2)

        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.SD1), 3)
        pygame.draw.rect(self.screen, (30, 144, 255), pygame.Rect(self.SD2), 3)
        pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(self.SD3), 3)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.SD4), 3)

        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.FPS1), 3)
        pygame.draw.rect(self.screen, (30, 144, 255), pygame.Rect(self.FPS2), 3)
        pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(self.FPS3), 3)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.FPS4), 3)
        pygame.draw.rect(self.screen, (34, 139, 34), pygame.Rect(self.FPS5), 3)

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.volumeSliderOutline))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.volumeSlider))

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.joystickSliderOutline))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.joystickSlider))
        
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.difficultyToggle))

        if self.fullscreen:
            # self.screen.blit(pygame.image.load('toggle.png'), pygame.Rect(self.fullscreenToggle))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.fullscreenToggle))
        else:
            pygame.draw.rect(self.screen, (125, 125, 125), pygame.Rect(self.fullscreenToggle))

    def run(self):
        self.setup()
        mouseDownVol = False
        mouseDownjoystick = False

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

                    # fullscreen
                    elif pygame.Rect(self.fullscreenToggle).collidepoint(pygame.mouse.get_pos()):
                        if self.fullscreen:
                            try:
                                w, h = pyautogui.size()
                            except:
                                w, h = 800, 600
                            height = h - (.025*h)
                            width = w - (.025*w)
                            s = openSettings(width, height, False)

                        else:
                            try:
                                w, h = pyautogui.size()
                            except:
                                w, h = 800, 600
                            s = openSettings(w, h, True)

                        self.fullscreen = not self.fullscreen
                        s.run()

                    # change difficulty
                    elif pygame.Rect(self.fullscreenToggle).collidepoint(pygame.mouse.get_pos()):
                        self.difficulty = not self.difficulty

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

                    # set FPS to 20
                    elif pygame.Rect(self.FPS1).collidepoint(pygame.mouse.get_pos()):
                        newFPS = 20

                    # set FPS to 60
                    elif pygame.Rect(self.FPS2).collidepoint(pygame.mouse.get_pos()):
                        newFPS = 60

                    # set FPS to 90
                    elif pygame.Rect(self.FPS3).collidepoint(pygame.mouse.get_pos()):
                        newFPS = 90

                    # set FPS to 120
                    elif pygame.Rect(self.FPS4).collidepoint(pygame.mouse.get_pos()):
                        newFPS = 120

                    # set FPS to uncapped
                    elif pygame.Rect(self.FPS5).collidepoint(pygame.mouse.get_pos()):
                        newFPS = None

                    # volume slider moved
                    elif pygame.Rect(self.volumeSliderOutline).collidepoint(pygame.mouse.get_pos()):
                        a, b, c, d = self.volumeSlider
                        currentX = pygame.mouse.get_pos()
                        mouseDownVol = True

                    # joystick slider moved
                    elif pygame.Rect(self.joystickSliderOutline).collidepoint(pygame.mouse.get_pos()):
                        a, b, c, d = self.joystickSlider
                        currentX = pygame.mouse.get_pos()
                        mouseDownjoystick = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    mouseDownVol = False
                    mouseDownjoystick = False
            
                if mouseDownVol:
                    if pygame.mouse.get_pos != currentX:
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.volumeSlider))
                        a, _ = pygame.mouse.get_pos()

                        min = self.volumeSliderOutline[0] + .01*self.WIDTH
                        max = self.volumeSliderOutline[0] + self.volumeSliderOutline[2] - .01*self.WIDTH - self.volumeSlider[2]

                        _, b, c, d = self.volumeSlider

                        if a < min:
                            a = min

                        elif a > max:
                            a = max

                        self.volumeSlider = (a, b, c, d)
                        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.volumeSlider))

                        self.currentVolume = ((a - min) / (max-min)) * 100
                        
                        self.currentVolume = str(round(self.currentVolume))

                        x, _, _, _ = self.volumeSliderOutline
                        _, volY, _, _ = self.volumeSlider
                        volX = x - .1 * self.WIDTH
                        volLocation = (volX, volY)

                        self.screen.blit(pygame.font.SysFont("monospace", int(30*self.WIDTH/1536)).render(self.currentVolume + ' ', True, (255, 255, 255), (0, 0, 0)), volLocation)
                            
                if mouseDownjoystick:
                    if pygame.mouse.get_pos != currentX:
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.joystickSlider))
                        a, _ = pygame.mouse.get_pos()

                        min = self.joystickSliderOutline[0] + .01*self.WIDTH
                        max = self.joystickSliderOutline[0] + self.joystickSliderOutline[2] - .01*self.WIDTH - self.joystickSlider[2]

                        _, b, c, d = self.joystickSlider

                        if a < min:
                            a = min
                        

                        elif a > max:
                            a = max

                        self.joystickSlider = (a, b, c, d)
                        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.joystickSlider))

                        self.currentjoystick = (((a - min) / (max-min)) * 100)
                        
                        self.currentjoystick = str(round(self.currentjoystick))

                        x, _, _, _ = self.joystickSliderOutline
                        _, joystickY, _, _ = self.joystickSlider
                        joystickX = x - .1 * self.WIDTH
                        joystickLocation = (joystickX, joystickY)

                        self.screen.blit(pygame.font.SysFont("monospace", int(30*self.WIDTH/1536)).render(self.currentjoystick + ' ', True, (255, 255, 255), (0, 0, 0)), joystickLocation)
                            

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