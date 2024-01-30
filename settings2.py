import pygame
import sys
import homescreen
import instructions
import pyautogui
import settings
import user_settings
import colors

class openSettings2:
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
        pygame.display.set_caption("Settings2")
        
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
        
        self.red = colors.LAVA
        self.blue = colors.ICE
        self.green = colors.FOREST
        self.gray = colors.SHADOW
        
    def text(self, i, h):
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
        pygame.draw.rect(self.screen, self.red, pygame.Rect(self.C1), 7)
        pygame.draw.rect(self.screen, self.blue, pygame.Rect(self.C2), 7)
        pygame.draw.rect(self.screen, self.green, pygame.Rect(self.C3), 7)
        pygame.draw.rect(self.screen, self.gray, pygame.Rect(self.C4), 7)
        
        # printing previous settings button
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.returnButton), 5)
        
        # printing constant seed toggle (is filled in if true)
        if self.constantSeed:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.constantSeedToggle), 7)
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.constantSeedToggle))
            
        # calling function to print titles and labels
        self.text(i, h)

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

    def run(self):
        # buttons, titles, labels
        self.setup()
        
        while True:
            retearly = False
            for event in pygame.event.get():

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
                        s = s = openSettings2(self.WIDTH, self.WIDTH, self.fullscreen)
                        s.run()
                        
                    # color 0
                    elif pygame.Rect(self.C1).collidepoint(pygame.mouse.get_pos()):
                        self.colorSetting = 0
                        self.update()
                        s = openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # color 1
                    elif pygame.Rect(self.C2).collidepoint(pygame.mouse.get_pos()):
                        self.colorSetting = 1
                        self.update()
                        s = openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # color 2
                    elif pygame.Rect(self.C3).collidepoint(pygame.mouse.get_pos()):
                        self.colorSetting = 2
                        self.update()
                        s = openSettings2(self.WIDTH, self.HEIGHT, self.fullscreen)
                        s.run()

                    # color 3
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

if __name__ == "__main__":
    try:
        WIDTH, HEIGHT = pyautogui.size()
    except:
        WIDTH = 800
        HEIGHT = 600

    s = openSettings2(WIDTH, HEIGHT, user_settings.FULLSCREEN)
    s.run()