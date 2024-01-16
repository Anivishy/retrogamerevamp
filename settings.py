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

        self.FPS1 = ((.1375)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)
        self.FPS2 = ((.2875)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)
        self.FPS3 = ((.4375)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)
        self.FPS4 = ((.5875)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)
        self.FPS5 = ((.7375)*self.WIDTH, (.725)*self.HEIGHT, (.125)*self.WIDTH, (.06)*self.HEIGHT)

        self.start = True

        self.fullscreenToggle = (.47*self.WIDTH, .4*self.HEIGHT, .06*self.WIDTH, .045* self.HEIGHT)

        self.difficultyToggle = (.47*self.WIDTH, .875*self.HEIGHT, .06*self.WIDTH, .045* self.HEIGHT)

        self.volumeSliderOutline = ((.25)*self.WIDTH, (.525)*self.HEIGHT, (.6)*self.WIDTH, (.02)*self.HEIGHT)
        self.volumeSliderStart = .26*self.WIDTH + (.6)*self.WIDTH - .03*self.WIDTH
        self.volumeSlider = (self.volumeSliderStart, (.5275)*self.HEIGHT, (.01)*self.WIDTH, (.015)*self.HEIGHT)
        self.volLocation = ((self.volumeSliderOutline[0] - .1 * self.WIDTH), self.volumeSliderOutline[1])

        self.currentVolume = 1.0 # value to use in game

        self.joystickSliderOutline = ((.25)*self.WIDTH, (.625)*self.HEIGHT, (.6)*self.WIDTH, (.02)*self.HEIGHT)
        self.joystickSliderStart = .26*self.WIDTH + (.3)*self.WIDTH - .03*self.WIDTH
        self.joystickSlider = (self.joystickSliderStart, (.6275)*self.HEIGHT, (.01)*self.WIDTH, (.015)*self.HEIGHT)
        self.joystickLocation = ((self.joystickSliderOutline[0] - .1 * self.WIDTH), self.joystickSliderOutline[1])

        self.currentjoystick = 0.5 # value to use in game

        self.difficulty = False

    def text(self, i, h):

        i.printText("Settings", (.1 * self.HEIGHT), True, False)
        i.printText("Screen Dimensions", (.2 * self.HEIGHT), False, False)
        i.printText("Fullscreen", (.35 * self.HEIGHT), False, False)
        i.printText("Volume", (.475 * self.HEIGHT), False, False)
        i.printText("Joystick Threshold", (.575 * self.HEIGHT), False, False)
        i.printText("FPS", (.675 * self.HEIGHT), False, False)
        i.printText("Increase Final Level Difficulty?", (.825 * self.HEIGHT), False, False)

        buttonFont = pygame.font.SysFont("monospace", int(30*self.WIDTH/1536))

        # Screen Dimension Labels
        a, b, c, d = self.SD1
        x, y = h.CenterButtons("Square", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("Square", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.SD2
        x, y = h.CenterButtons("Vertical", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("Vertical", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.SD3
        x, y = h.CenterButtons("Landscape", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("Landscape", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.SD4
        x, y = h.CenterButtons("Fullscreen", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("Fullscreen", True, (255, 255, 255)), (x, y))

        # FPS Labels
        a, b, c, d = self.FPS1
        x, y = h.CenterButtons("20", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("20", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.FPS2
        x, y = h.CenterButtons("60", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("60", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.FPS3
        x, y = h.CenterButtons("90", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("90", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.FPS4
        x, y = h.CenterButtons("120", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("120", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.FPS5
        x, y = h.CenterButtons("Uncapped", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("Uncapped", True, (255, 255, 255)), (x, y))

        pygame.display.flip()

    def setup(self):
        i = instructions.createInstructions(self.WIDTH, self.HEIGHT, self.fullscreen)
        h = homescreen.createHomescreen(self.WIDTH, self.HEIGHT, self.fullscreen)

        # printing exit button
        a, b, _, _ = self.exitButton
        self.screen.blit(pygame.font.SysFont("monospace", int(60*self.WIDTH/1536)).render("<", True, (255, 255, 255)), (a, b))

        # printing screen dimension buttons
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.SD1), 7)
        pygame.draw.rect(self.screen, (30, 144, 255), pygame.Rect(self.SD2), 7)
        pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(self.SD3), 7)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.SD4), 7)

        # printing fps buttons
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.FPS1), 7)
        pygame.draw.rect(self.screen, (30, 144, 255), pygame.Rect(self.FPS2), 7)
        pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(self.FPS3), 7)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.FPS4), 7)
        pygame.draw.rect(self.screen, (34, 139, 34), pygame.Rect(self.FPS5), 7)

        # printing volume slider + current value
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.volumeSliderOutline))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.volumeSlider))
        self.screen.blit(pygame.font.SysFont("monospace", int(30*self.WIDTH/1536)).render(str((self.currentVolume*100))[:3] + ' ', True, (255, 255, 255), (0, 0, 0)), self.volLocation)

        # printing joystick slider
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.joystickSliderOutline))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.joystickSlider))
        self.screen.blit(pygame.font.SysFont("monospace", int(30*self.WIDTH/1536)).render(str((self.currentjoystick*100))[:2] + ' ', True, (255, 255, 255), (0, 0, 0)), self.joystickLocation)

        # printing fullscreen toggle (is filled in if fullscreen)
        if self.fullscreen:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.fullscreenToggle), 7)
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.fullscreenToggle))

        # printing difficulty toggle (filled in for increased difficulty)
        if self.difficulty:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.difficultyToggle), 7)
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.difficultyToggle))

        # calling function to print titles and labels
        self.text(i, h)

    def run(self):
        # adding buttons, titles, labels
        self.setup()

        # used to track if either slider is moved
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
                    # back button pressed, return to homescreen
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

                    # change final level difficulty
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

                    # vertical screen
                    elif pygame.Rect(self.SD2).collidepoint(pygame.mouse.get_pos()):
                        try:
                            w, h = pyautogui.size()
                        except:
                            w, h = 800, 600
                        height = h - (.1*h)
                        width = height * (2/3)
                        s = openSettings(width, height, False)
                        s.run()

                    # landscape screen
                    elif pygame.Rect(self.SD3).collidepoint(pygame.mouse.get_pos()):
                        try:
                            w, h = pyautogui.size()
                        except:
                            w, h = 800, 600
                        height = h - (.1*h)
                        width = w - (.1*w)
                        s = openSettings(width, height, False)
                        s.run()

                    # fullscreen screen
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

                # if either slider was being moved, and now is not
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouseDownVol = False
                    mouseDownjoystick = False
            
                # if volume slider being moved
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

                        self.screen.blit(pygame.font.SysFont("monospace", int(30*self.WIDTH/1536)).render(self.currentVolume + ' ', True, (255, 255, 255), (0, 0, 0)), self.volLocation)
                        
                # if joystick slider being moved
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
