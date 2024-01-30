import pygame
import sys
import homescreen
import instructions
import pyautogui
import settings2

import user_settings

class openSettings:
    def __init__(self, WIDTH, HEIGHT, FULLSCREEN):
        pygame.init()

        self.WIDTH = user_settings.WIDTH # value to use in settings
        self.HEIGHT = user_settings.HEIGHT # value to use in settings
        self.currentFPS = user_settings.FPS  # FPS Value to use in game
        self.currentVolume = int(user_settings.SFX_VOLUME * 100) # Volume value to use in game
        self.currentjoystick = int(user_settings.JOYSTICK_THRESHOLD * 100) # Joystick Threshold value to use in game
        self.difficulty = user_settings.BULLET_HELL_BOTTOM_RIGHT # Botton Right, value to use in games

        self.defaultWidth = WIDTH
        self.defaultHeight = HEIGHT
        try:
            self.defaultWidth, self.defaultHeight = pyautogui.size()
        except:
            self.defaultWidth, self.defaultHeight = 800, 600

        if (FULLSCREEN):
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
            self.fullscreen = True

        else:
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
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

        self.start = False

        self.fullscreenToggle = (.47*self.WIDTH, .4*self.HEIGHT, .06*self.WIDTH, .045* self.HEIGHT)

        self.difficultyToggle = (.47*self.WIDTH, .875*self.HEIGHT, .06*self.WIDTH, .045* self.HEIGHT)

        self.volumeSliderOutline = ((.25)*self.WIDTH, (.525)*self.HEIGHT, (.6)*self.WIDTH, (.02)*self.HEIGHT)
        self.volumeSliderStart = .28*self.WIDTH + ((.57)*self.WIDTH * (self.currentVolume/100) - (.02)*self.WIDTH)
        self.volumeSlider = (self.volumeSliderStart, (.5275)*self.HEIGHT, (.01)*self.WIDTH, (.015)*self.HEIGHT)
        self.volLocation = ((self.volumeSliderOutline[0] - .1 * self.WIDTH), self.volumeSliderOutline[1])

        self.joystickSliderOutline = ((.25)*self.WIDTH, (.625)*self.HEIGHT, (.6)*self.WIDTH, (.02)*self.HEIGHT)
        self.joystickSliderStart = .28*self.WIDTH + ((.57)*self.WIDTH * (self.currentjoystick/100) - (.02)*self.WIDTH)
        self.joystickSlider = (self.joystickSliderStart, (.6275)*self.HEIGHT, (.01)*self.WIDTH, (.015)*self.HEIGHT)
        self.joystickLocation = ((self.joystickSliderOutline[0] - .1 * self.WIDTH), self.joystickSliderOutline[1])
        
        self.nextButton = ((.75)*self.WIDTH, (.9)*self.HEIGHT, (.2)*self.WIDTH, (.06)*self.HEIGHT)

    def text(self, i, h):
        i.printText("Settings", (.1 * self.HEIGHT), True, self.start, self.screen)
        i.printText("Screen Dimensions", (.2 * self.HEIGHT), False, self.start, self.screen)
        i.printText("Fullscreen", (.35 * self.HEIGHT), False, self.start, self.screen)
        i.printText("Volume", (.475 * self.HEIGHT), False, self.start, self.screen)
        i.printText("Joystick Threshold", (.575 * self.HEIGHT), False, self.start, self.screen)
        i.printText("FPS", (.675 * self.HEIGHT), False, self.start, self.screen)
        i.printText("Increase Final Level Difficulty?", (.825 * self.HEIGHT), False, self.start, self.screen)

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
        
        # next page label 
        a, b, c, d = self.nextButton
        x, y = h.CenterButtons("More Settings \u2193", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("More Settings \u2193", True, (255, 255, 255)), (x, y))

        pygame.display.flip()

    def setup(self):
        i = instructions.createInstructions(self.WIDTH, self.HEIGHT, self.fullscreen)
        h = homescreen.createHomescreen(self.WIDTH, self.HEIGHT, self.fullscreen)

        # printing exit button
        a, b, _, _ = self.exitButton
        self.screen.blit(pygame.font.SysFont("monospace", int(60*self.WIDTH/1536)).render("<", True, (255, 255, 255)), (a, b))

        # printing more settings button
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.nextButton), 5)

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
        self.screen.blit(pygame.font.SysFont("monospace", int(30*self.WIDTH/1536)).render(str((self.currentVolume)) + ' ', True, (255, 255, 255), (0, 0, 0)), self.volLocation)

        # printing joystick slider
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.joystickSliderOutline))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.joystickSlider))
        self.screen.blit(pygame.font.SysFont("monospace", int(30*self.WIDTH/1536)).render(str((self.currentjoystick)) + ' ', True, (255, 255, 255), (0, 0, 0)), self.joystickLocation)

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

    def update(self):
        user_settings.SETTINGS_JSON = {
                "WIDTH": int(self.WIDTH),
                "HEIGHT": int(self.HEIGHT),
                "FULLSCREEN": self.fullscreen,

                "SFX_VOLUME": int(self.currentVolume) / 100,
                "MUSIC_VOLUME": user_settings.MUSIC_VOLUME,
                "FPS": self.currentFPS,

                "JOYSTICK_THRESHOLD": int(self.currentjoystick) / 100,
                "BULLET_HELL_BOTTOM_RIGHT": self.difficulty,

                "CB_COLOR_OVERRIDE": user_settings.CB_COLOR_OVERRIDE,

                "CONSTANT_SEED": user_settings.CONSTANT_SEED
            }
        user_settings.save_vars()
        user_settings.reload_vars()

    def run(self):
        # adding buttons, titles, labels
        self.setup()

        # used to track if either slider is moved
        mouseDownVol = False
        mouseDownjoystick = False

        while True:
            retearly = False
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    import sys; sys.exit()

                elif event.type == pygame.VIDEORESIZE:
                    s = openSettings(self.WIDTH, self.HEIGHT, self.fullscreen)
                    s.run()

                elif event.type == pygame.VIDEOEXPOSE:
                    s = openSettings(self.WIDTH, self.HEIGHT, self.fullscreen)
                    s.run()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.update()
                        c = homescreen.createHomescreen(self.WIDTH, self.HEIGHT, self.fullscreen)
                        c.run(False)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # back button pressed, return to homescreen
                    if pygame.Rect(self.exitButton).collidepoint(pygame.mouse.get_pos()):
                        self.update()
                        c = homescreen.createHomescreen(self.WIDTH, self.HEIGHT, self.fullscreen)
                        c.run(False)
                        
                    # more settings button pressed, go to settings 2
                    if pygame.Rect(self.nextButton).collidepoint(pygame.mouse.get_pos()):
                        self.update()
                        s2 = settings2.openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s2.run()

                    # fullscreen
                    elif pygame.Rect(self.fullscreenToggle).collidepoint(pygame.mouse.get_pos()):
                        if self.fullscreen:
                            try:
                                w, h = pyautogui.size()
                            except:
                                w, h = 800, 600
                            height = self.defaultHeight - (.025*self.defaultHeight)
                            width = self.defaultWidth - (.025*self.defaultWidth)
                            s = openSettings(width, height, False)

                        else:
                            try:
                                w, h = pyautogui.size()
                            except:
                                w, h = 800, 600
                            s = openSettings(w, h, True)

                        self.fullscreen = not self.fullscreen
                        self.update()
                        s.run()

                    # change final level difficulty
                    elif pygame.Rect(self.difficultyToggle).collidepoint(pygame.mouse.get_pos()):
                        self.difficulty = not self.difficulty
                        self.update()

                    # square screen
                    elif pygame.Rect(self.SD1).collidepoint(pygame.mouse.get_pos()):
                        self.HEIGHT = self.defaultHeight - (.3*self.defaultHeight)
                        self.WIDTH = self.HEIGHT
                        self.update()
                        s = openSettings(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # vertical screen
                    elif pygame.Rect(self.SD2).collidepoint(pygame.mouse.get_pos()):
                        self.HEIGHT = self.defaultHeight - (.3*self.defaultHeight)
                        self.WIDTH = self.HEIGHT * (2/3)
                        self.update()
                        s = openSettings(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # landscape screen
                    elif pygame.Rect(self.SD3).collidepoint(pygame.mouse.get_pos()):
                        # self.HEIGHT = self.defaultHeight - (.1*self.defaultHeight)
                        # self.WIDTH = self.defaultWidth - (.1*self.defaultWidth)
                        self.HEIGHT = 900
                        self.WIDTH = 1600
                        self.update()
                        s = openSettings(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # fullscreen screen
                    elif pygame.Rect(self.SD4).collidepoint(pygame.mouse.get_pos()):
                        self.WIDTH, self.HEIGHT = self.defaultWidth, self.defaultHeight
                        self.update()
                        s = openSettings(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # set FPS to 20
                    elif pygame.Rect(self.FPS1).collidepoint(pygame.mouse.get_pos()):
                        self.currentFPS = 20

                    # set FPS to 60
                    elif pygame.Rect(self.FPS2).collidepoint(pygame.mouse.get_pos()):
                        self.currentFPS = 60

                    # set FPS to 90
                    elif pygame.Rect(self.FPS3).collidepoint(pygame.mouse.get_pos()):
                        self.currentFPS = 90

                    # set FPS to 120
                    elif pygame.Rect(self.FPS4).collidepoint(pygame.mouse.get_pos()):
                        self.currentFPS = 120

                    # set FPS to uncapped
                    elif pygame.Rect(self.FPS5).collidepoint(pygame.mouse.get_pos()):
                        self.currentFPS = None

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
                        self.screen.blit(pygame.font.SysFont("monospace", int(30*self.WIDTH/1536)).render(self.currentVolume + '  ', True, (255, 255, 255), (0, 0, 0)), self.volLocation)
                        
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

                        self.screen.blit(pygame.font.SysFont("monospace", int(30*self.WIDTH/1536)).render(self.currentjoystick + '  ', True, (255, 255, 255), (0, 0, 0)), joystickLocation)
                            
                pygame.display.update()
            if retearly: break
        user_settings.SETTINGS_JSON = {
            "WIDTH": int(self.WIDTH),
            "HEIGHT": int(self.HEIGHT),
            "FULLSCREEN": self.fullscreen,

            "SFX_VOLUME": int(self.currentVolume) / 100,
            "MUSIC_VOLUME": user_settings.MUSIC_VOLUME,
            "FPS": self.currentFPS,

            "JOYSTICK_THRESHOLD": int(self.currentjoystick) / 100,
            "BULLET_HELL_BOTTOM_RIGHT": self.difficulty,

            "CB_COLOR_OVERRIDE": user_settings.CB_COLOR_OVERRIDE,

            "CONSTANT_SEED": user_settings.CONSTANT_SEED
        }
        user_settings.save_vars()
        user_settings.reload_vars()

if __name__ == "__main__":
    try:
        WIDTH, HEIGHT = pyautogui.size()
    except:
        WIDTH = 800
        HEIGHT = 600

    s = openSettings(WIDTH, HEIGHT, user_settings.FULLSCREEN)
    s.run()
