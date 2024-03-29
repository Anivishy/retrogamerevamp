import pygame
import sys
import homescreen
import instructions
import pyautogui
import settings
import user_settings
import colors

class openSettings2:
    # initializing and setting page-specific constants and variables
    def __init__(self, WIDTH, HEIGHT, FULLSCREEN):
        pygame.init()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        # try:
        #     self.WIDTH, self.HEIGHT = pyautogui.size()
        # except:
        #     self.WIDTH, self.HEIGHT = 800, 600

        if (FULLSCREEN):
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
            self.fullscreen = True

        else:
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            self.fullscreen = False

        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("Smack-man")
        
        self.colorSetting = user_settings.CB_COLOR_OVERRIDE
        self.constantSeed = user_settings.CONSTANT_SEED

        self.exitButton = ((55/1536)*self.WIDTH, (75/1024)*self.HEIGHT, (40/1536)*self.WIDTH, (40/1024)*self.HEIGHT)
        self.returnButton = ((.7)*self.WIDTH, (.9)*self.HEIGHT, (.25)*self.WIDTH, (.06)*self.HEIGHT)

        self.C1 = ((.125)*self.WIDTH, (.25)*self.HEIGHT, (.15)*self.WIDTH, (.06)*self.HEIGHT)
        self.C2 = ((.325)*self.WIDTH, (.25)*self.HEIGHT, (.15)*self.WIDTH, (.06)*self.HEIGHT)
        self.C3 = ((.525)*self.WIDTH, (.25)*self.HEIGHT, (.15)*self.WIDTH, (.06)*self.HEIGHT)
        self.C4 = ((.725)*self.WIDTH, (.25)*self.HEIGHT, (.15)*self.WIDTH, (.06)*self.HEIGHT)

        self.constantSeedToggle = (.47*self.WIDTH, .4*self.HEIGHT, .06*self.WIDTH, .045* self.HEIGHT)
        
        self.start = False
        
        self.green, self.blue, self.red, self.gray = self.colorUpdate()
        
    # printing text for titles and buttons
    def text(self, i, h):
        
        # printing titles
        titleFont = pygame.font.SysFont("monospace", int(50*self.WIDTH/1536))
        subtitleFont = pygame.font.SysFont("monospace", int(30*self.WIDTH/1536))
        
        i.printText("Settings", (.1 * self.HEIGHT), True, self.start, self.screen, titleFont)
        i.printText("Color Options", (.2 * self.HEIGHT), False, self.start, self.screen, subtitleFont)
        i.printText("Constant Seed", (.35 * self.HEIGHT), False, self.start, self.screen, subtitleFont)

        buttonFont = pygame.font.SysFont("monospace", int(30*self.WIDTH/1536))

        # Color Settings Labels
        a, b, c, d = self.C1
        x, y = h.CenterButtons("None", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("None", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.C2
        x, y = h.CenterButtons("Protanopia", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("Protanopia", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.C3
        x, y = h.CenterButtons("Deuteranopia", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("Deuteranopia", True, (255, 255, 255)), (x, y))

        a, b, c, d = self.C4
        x, y = h.CenterButtons("Tritanopia", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("Tritanopia", True, (255, 255, 255)), (x, y))
        
        # previous page label 
        a, b, c, d = self.returnButton
        x, y = h.CenterButtons("Previous Settings \u2191", a, b, c, d, buttonFont)
        self.screen.blit(buttonFont.render("Previous Settings \u2191", True, (255, 255, 255)), (x, y))
        
        # constant seed toggle label
        if self.constantSeed:
            a, b, c, d = self.constantSeedToggle
            x, y = h.CenterButtons("on", a, b, c, d, buttonFont)
            self.screen.blit(buttonFont.render("on", True, (255, 255, 255)), (x, y))
            
        else:
            a, b, c, d = self.constantSeedToggle
            x, y = h.CenterButtons("off", a, b, c, d, buttonFont)
            self.screen.blit(buttonFont.render("off", True, (0, 0, 0)), (x, y))
        
    def setup(self):
        i = instructions.createInstructions(self.WIDTH, self.HEIGHT, self.fullscreen)
        h = homescreen.createHomescreen(self.WIDTH, self.HEIGHT, self.fullscreen)

        # printing exit button
        a, b, _, _ = self.exitButton
        char = pygame.font.SysFont("monospace", int(80*self.WIDTH/1536)).render("<", True, (255, 255, 255))
        self.exitButton = list(self.exitButton)
        self.exitButton[2] = char.get_rect().width
        self.exitButton[3] = char.get_rect().height
        self.exitButton = tuple(self.exitButton)

        self.screen.blit(char, (a, b))

        # printing color setting buttons
        s = settings.openSettings(self.WIDTH, self.HEIGHT, self.fullscreen)
        
        if (self.colorSetting == 0):
            pygame.draw.rect(self.screen, self.red, pygame.Rect(self.C1), 13)
        else:
            pygame.draw.rect(self.screen, self.red, pygame.Rect(self.C1), 5)
            
        if (self.colorSetting == 1):
            pygame.draw.rect(self.screen, self.blue, pygame.Rect(self.C2), 13)
        else:
            pygame.draw.rect(self.screen, self.blue, pygame.Rect(self.C2), 5)
        
        if (self.colorSetting == 2):
            pygame.draw.rect(self.screen, self.green, pygame.Rect(self.C3), 13)
        else:
            pygame.draw.rect(self.screen, self.green, pygame.Rect(self.C3), 5)
        
        if (self.colorSetting == 3):
            pygame.draw.rect(self.screen, self.gray, pygame.Rect(self.C4), 13)
        else:
            pygame.draw.rect(self.screen, self.gray, pygame.Rect(self.C4), 5)
        
        # printing previous settings button
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.returnButton), 5)
        
        # printing constant seed toggle (filled if true)
        if self.constantSeed:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.constantSeedToggle), 7)
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.constantSeedToggle))
            
        # calling function to print titles and labels
        self.text(i, h)

    # updates last two settings (color, constant seed) based on changes made in this page
    def update(self):
        user_settings.SETTINGS_JSON = {
                "WIDTH": user_settings.WIDTH,
                "HEIGHT": user_settings.HEIGHT,
                "FULLSCREEN": user_settings.FULLSCREEN,

                "SFX_VOLUME": user_settings.SFX_VOLUME,
                "MUSIC_VOLUME": user_settings.MUSIC_VOLUME,
                "FPS": user_settings.FPS,

                "JOYSTICK_THRESHOLD": user_settings.JOYSTICK_THRESHOLD,
                "BULLET_HELL_BOTTOM_RIGHT": user_settings.BULLET_HELL_BOTTOM_RIGHT,

                "CB_COLOR_OVERRIDE": self.colorSetting,

                "CONSTANT_SEED": self.constantSeed
            }
        user_settings.save_vars()
        user_settings.reload_vars()
        
    # updates rgb values for color scheme based on color option
    def colorUpdate(self):
        if self.colorSetting == 0:
            return ((30, 220, 50), (75, 150, 230), (240, 30, 40), (120, 50, 120))
        elif self.colorSetting == 1:
            return ((220, 108, 30), (75, 175, 230), (221, 240, 30), (159, 70, 202))
        elif self.colorSetting == 2:
            return ((255, 72, 72), (75, 22, 230), (190, 208, 13), (159, 70, 202))
        elif self.colorSetting == 3:
            return ((75, 230, 203), (0, 145, 255), (208, 167, 13), (173, 106, 255))

    # event handling loop
    def run(self):
        self.setup() # prints buttons, titles, labels
        
        while True:
            retearly = False
            for event in pygame.event.get():

                # handles exiting or resizing of page
                if event.type == pygame.QUIT:
                    import sys; sys.exit()

                elif event.type == pygame.VIDEORESIZE:
                    s = openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
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
                        
                    # return button pressed, go to settings
                    if pygame.Rect(self.returnButton).collidepoint(pygame.mouse.get_pos()):
                        self.update()
                        s = settings.openSettings(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # constant seed toggle
                    elif pygame.Rect(self.constantSeedToggle).collidepoint(pygame.mouse.get_pos()):
                        self.constantSeed = not self.constantSeed
                        self.update()
                        s = openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()
                        
                    # color option 0
                    elif pygame.Rect(self.C1).collidepoint(pygame.mouse.get_pos()):
                        self.colorSetting = 0
                        self.update()
                        s = openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # color option 1
                    elif pygame.Rect(self.C2).collidepoint(pygame.mouse.get_pos()):
                        self.colorSetting = 1
                        self.update()
                        s = openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # color option 2
                    elif pygame.Rect(self.C3).collidepoint(pygame.mouse.get_pos()):
                        self.colorSetting = 2
                        self.update()
                        s = openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # color option 3
                    elif pygame.Rect(self.C4).collidepoint(pygame.mouse.get_pos()):
                        self.colorSetting = 3
                        self.update()
                        s = openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()
                        
                pygame.display.update()
            if retearly: break
        user_settings.SETTINGS_JSON = {
            "WIDTH": user_settings.WIDTH,
            "HEIGHT": user_settings.HEIGHT,
            "FULLSCREEN": user_settings.FULLSCREEN,

            "SFX_VOLUME": user_settings.SFX_VOLUME,
            "MUSIC_VOLUME": user_settings.MUSIC_VOLUME,
            "FPS": user_settings.FPS,

            "JOYSTICK_THRESHOLD": user_settings.JOYSTICK_THRESHOLD,
            "BULLET_HELL_BOTTOM_RIGHT": user_settings.BULLET_HELL_BOTTOM_RIGHT,

            "CB_COLOR_OVERRIDE": self.colorSetting,

            "CONSTANT_SEED": self.constantSeed
        }
        user_settings.save_vars()
        user_settings.reload_vars()

# used to test page directly 
if __name__ == "__main__":
    try:
        WIDTH, HEIGHT = pyautogui.size()
    except:
        WIDTH = 800
        HEIGHT = 600

    s = openSettings2(WIDTH, HEIGHT, True)
    s.run()