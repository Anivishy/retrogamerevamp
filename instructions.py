import pygame
import sys
import homescreen

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

        self.exitButtonOutline = ((50/1536)*self.WIDTH, (70/1024)*self.HEIGHT, (50/1536)*self.WIDTH, (50/1024)*self.HEIGHT)
        self.exitButton = ((55/1536)*self.WIDTH, (75/1024)*self.HEIGHT, (40/1536)*self.WIDTH, (40/1024)*self.HEIGHT)
        self.start = True

    def printText(self, text, y, title):
        font = pygame.font.SysFont("monospace", 30)

        if title:
            font = pygame.font.SysFont("monospace", 50)

        lines = self.breakLines(text, font)

        for l in lines:
            x = self.centerText(l, font)
            x2 = x

            for i in range(len(l)):

                color = (200, 200, 200)
                if title:
                    color = (255, 255, 255)
                
                char = font.render(l[i], True, color, (0, 0, 0))
                self.screen.blit(char, (x2, y))

                x2 += char.get_width()

                if i != len(l)-1:
                    self.screen.blit(font.render("|", True, (255, 255, 255)), (x2, y))

                pygame.display.flip()

                if self.start:
                    pygame.time.wait(15) #15

            x2 = x
            textWidth, textHeight = font.size(text)
            y += textHeight
        
        self.start = False

    def centerText(self, text, font):
        textWidth, textHeight = font.size(text)
        return (self.WIDTH - textWidth) / 2
        
    def breakLines(self, text, font):
        maxWidth = self.WIDTH - (.2 * self.WIDTH)
        chars = len(text)
        lines = []
        lineText = ""
        i = 0
        word = ""
        
        while i < chars:
            if text[i] == " ":
                textWidth, textHeight = font.size(lineText)
                wordWidth, wordHeight = font.size(word)

                if (textWidth + wordWidth) > maxWidth:
                    lines.append(lineText)
                    lineText = word + " "
                    word = ""

                else:
                    word += " "
                    lineText += word
                    word = ""

            else:
                word += text[i]

            if i == chars - 1:
                lineText += word

            i += 1

        lines.append(lineText)
        return lines

    def printInstructions(self):
        titleFont = pygame.font.SysFont("monospace", 50)
        bodyFont = pygame.font.SysFont("monospace", 35)

        self.printText("Instructions", (.1 * self.HEIGHT), True)

        controls = "Use your up, down, left, and right arrows for movement. Press 'esc' to exit the game."

        goal = "In the intro level, collect all pellets in the area. Then, use your weapons to defeat each of the bosses."

        powerups = "In each of the zones, you can pick up special powerups, including _"

        zones = "This game consists of an intro level, similar to standard Pacman, followed by 4 different Zones, each with a boss to beat."

        self.printText("Controls", (.2 * self.HEIGHT), True)
        self.printText(controls, (.275 * self.HEIGHT), False)

        self.printText("Zones", (.4 * self.HEIGHT), True)
        self.printText(zones, (.475 * self.HEIGHT), False)

        self.printText("Goal", (.6 * self.HEIGHT), True)
        self.printText(goal, (.675 * self.HEIGHT), False)

        self.printText("Powerups", (.8 * self.HEIGHT), True)
        self.printText(powerups, (.875 * self.HEIGHT), False)


        pygame.display.flip()

        self.start = False

    def run(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.exitButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.exitButton))
        self.printInstructions()

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
                    if pygame.Rect(self.exitButtonOutline).collidepoint(pygame.mouse.get_pos()):
                        c = homescreen.createHomescreen()
                        c.run()

if __name__ == "__main__":
    i = createInstructions()
    i.run()

        
# things to include in instructions:
    # - up, down, left, right arrows to navigate
    # - goal is to collect all pellets in the area (or collect _ number of points?)
    # different powerups - infinite ammo [add more later]
    # defeat all 4 of the bosses with weapons - shoot the bosses
    # once you pass the first level, different zones will be unlocked, each with special challenges (maybe add instructions at the corner of each page with a (?))

    # update tasks, improve visuals, add a 'back' button

    # create a scrollbar if needed: https://copyprogramming.com/howto/pygame-scrolling-down-page#pygame-scrolling-down-page