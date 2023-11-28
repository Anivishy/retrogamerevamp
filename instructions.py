import pygame
import sys

class createInstructions:
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
        pygame.display.set_caption("Instructions")

        self.exitButtonOutline = ((100/1536)*self.WIDTH, (150/1024)*self.HEIGHT, (100/1536)*self.WIDTH, (150/1024)*self.HEIGHT)
        self.start = True

    def printText(self, text, y, font):
        lines = self.breakLines(text, font)

        for l in lines:
            x = self.centerText(l, font)
            x2 = x

            for i in range(len(l)):
                char = font.render(l[i], True, (255, 255, 255), (0, 0, 0))
                self.screen.blit(char, (x2, y))

                x2 += char.get_width()

                if x2 > (self.WIDTH - (.1* self.WIDTH)):
                    y += char.get_height() + 15
                    x2 = x

                if i != len(l)-1:
                    self.screen.blit(font.render("|", True, (255, 255, 255)), (x2, y))

                pygame.display.flip()

                if self.start:
                    pygame.time.wait(0) #115

    def centerText(self, text, font):
        textWidth, textHeight = font.size(text)
        return (self.WIDTH - textWidth) / 2
        
    def breakLines(self, text, font):
        maxWidth = self.WIDTH - (.1*self.WIDTH)
        chars = len(text)
        lines = []
        lineText = ""
        i = 0
        extraWidth, h = font.size("|")
        
        while i < chars:
            if text[i] == " ":
                l = lineText + text[i]
                textWidth, textHeight = font.size(l)
                if textWidth > maxWidth:
                    lines.append(lineText)
                    lineText = text[i]
                else:
                    lineText += text[i]

            else:
                lineText += text[i]

            i += 1

        lines.append(lineText)
        return lines

    def printInstructions(self):
        titleFont = pygame.font.SysFont("monospace", 50)
        bodyFont = pygame.font.SysFont("monospace", 35)

        self.printText("Instructions:", (.1 * self.HEIGHT), titleFont)

        controls = "Use your up, down, left, and right arrows for movement. Press 'esc' to exit the game."

        goal = "Goal"

        powerPellets = "Power Pellets"

        mapGeneration = "Map Bounds"

        zones = "Zones"

        self.printText("Controls", (.2 * self.HEIGHT), titleFont)
        self.printText(controls, (.25 * self.HEIGHT), bodyFont)

        self.printText(goal, (.35 * self.HEIGHT), bodyFont)

        self.printText(powerPellets, (.5 * self.HEIGHT), bodyFont)

        self.printText(mapGeneration, (.65 * self.HEIGHT), bodyFont)

        self.printText(zones, (.8 * self.HEIGHT), bodyFont)

        pygame.display.flip()

        self.start = False

# if __name__ == "__main__":
i = createInstructions()
i.printInstructions()


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
        


# things to include in instructions:
    # - up, down, left, right arrows to navigate
    # - goal is to collect all pellets in the area (or collect _ number of points?)
    # different powerups - infinite ammo [add more later]
    # defeat all 4 of the bosses with weapons - shoot the bosses
    # once you pass the first level, different zones will be unlocked, each with special challenges (maybe add instructions at the corner of each page with a (?))

    # update tasks

    # create a scrollbar: https://copyprogramming.com/howto/pygame-scrolling-down-page#pygame-scrolling-down-page