import pygame
import sys

class openSettings:
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
        pygame.display.set_caption("Settings")
        exitButtonOutline = ((100/1536)*self.WIDTH, (150/1024)*self.HEIGHT, (100/1536)*self.WIDTH, (150/1024)*self.HEIGHT)

    def printText(self):
        import homescreen
        h = homescreen
        titleFont = pygame.font.SysFont("monospace", 50)
        bodyFont = pygame.font.SysFont("monospace", 30)

        textWidth, textHeight = titleFont.size("Settings:")
        h.openingText("Settings:", h.centerText("Settings:"), (.15 * self.HEIGHT))

        pygame.display.flip()

# if __name__ == "__main__":
i = openSettings()
i.printText()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if pygame.Rect(i.exitButton).collidepoint(pygame.mouse.get_pos()):
        
    
    