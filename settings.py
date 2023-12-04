import pygame
import sys
import homescreen

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

        self.exitButtonOutline = ((50/1536)*self.WIDTH, (70/1024)*self.HEIGHT, (50/1536)*self.WIDTH, (50/1024)*self.HEIGHT)
        self.exitButton = ((55/1536)*self.WIDTH, (75/1024)*self.HEIGHT, (40/1536)*self.WIDTH, (40/1024)*self.HEIGHT)
        self.start = True

    def printText(self, text, y, title): # delete when done
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
        return lines # delete when done

    def text(self):
        titleFont = pygame.font.SysFont("monospace", 50)
        bodyFont = pygame.font.SysFont("monospace", 35)

        self.printText("Settings", (.1 * self.HEIGHT), True)

        pygame.display.flip()

    def run(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.exitButtonOutline), 10)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.exitButton))
        self.text()

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
                        c.run(False)

                pygame.display.flip()


if __name__ == "__main__":
    s = openSettings()
    s.run()


    