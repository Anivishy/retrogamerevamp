import pygame
import sys
import homescreen
import pyautogui

class createInstructions:
    def __init__(self, WIDTH, HEIGHT, FULLSCREEN):
        pygame.init()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        if (FULLSCREEN):
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
            self.fullscreen = True

        else:
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            self.fullscreen = False

        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("Instructions")

        self.exitButtonOutline = ((50/1536)*self.WIDTH, (70/1024)*self.HEIGHT, (50/1536)*self.WIDTH, (50/1024)*self.HEIGHT)

    def printText(self, text, y, title, start, screen, font):
        lines = self.breakLines(text, font)

        for l in lines:
            x = self.centerText(l, font)
            x2 = x

            for i in range(len(l)):
                color = (200, 200, 200)
                
                if title:
                    color = (255, 255, 255)
                
                char = font.render(l[i], True, color, (0, 0, 0))
                screen.blit(char, (x2, y))

                x2 += char.get_width()

                if i != len(l)-1:
                    screen.blit(font.render("|", True, (255, 255, 255)), (x2, y))

                pygame.display.flip()

                if title and start:
                    pygame.time.wait(20) #20

                elif start:
                    pygame.time.wait(5) #5

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
        titleFont = pygame.font.SysFont("monospace", int(50*self.WIDTH/1536))
        subtitleFont = pygame.font.SysFont("monospace", int(30*self.WIDTH/1536))
        bodyFont = pygame.font.SysFont("monospace", int(24*self.WIDTH/1536))

        self.printText("Instructions", (.05 * self.HEIGHT), True, True, self.screen, titleFont)

        controls = "Use your up, down, left, and right arrows for movement. In the main game, Press 'esc' to exit the game."

        introGoal = "You will first play the intro level, where you want to collect all pellets in the area without losing all your lives. You have 3 lives and lose one each time a ghost hits you."
        
        mainGoal = "In the main game, you must travel to the corner of each of the 4 zones, where you will find a boss. To beat them, shoot by left clicking (on keyboard) or with the right trigger (with a controller) until they lose their health. You gain 1 ammo to shoot for every 5 pellets you collect. You must beat all 4 bosses to win the game."
        mainGoal2 = "While in or travelling between zones, if you are hit by a ghost or take damage from a boss, you are slowed down and have a brief period of invincibility. You also lose a little bit of your health. If your health runs out, you lose the game. You will have a health shield of 50 that regenerates every 10 seconds to help you in the game."
        
        zones = "This game consists of an intro level, similar to standard Pacman, followed by 4 different Zones, each with a boss to beat."

        self.printText("Controls", (.15 * self.HEIGHT), True, True, self.screen, subtitleFont)
        self.printText(controls, (.2 * self.HEIGHT), False, True, self.screen, bodyFont)

        self.printText("Zones", (.3 * self.HEIGHT), True, True, self.screen, subtitleFont)
        self.printText(zones, (.35 * self.HEIGHT), False, True, self.screen, bodyFont)

        self.printText("Intro Level Goal", (.45 * self.HEIGHT), True, True, self.screen, subtitleFont)
        self.printText(introGoal, (.5 * self.HEIGHT), False, True, self.screen, bodyFont)

        self.printText("Main Game Goal", (.625 * self.HEIGHT), True, True, self.screen, subtitleFont)
        self.printText(mainGoal, (.675 * self.HEIGHT), False, True, self.screen, bodyFont)
        self.printText(mainGoal2, (0.825 * self.HEIGHT), False, True, self.screen, bodyFont)

        pygame.display.flip()

    def run(self):
        a, b, _, _ = self.exitButtonOutline
        char = pygame.font.SysFont("monospace", int(80*self.WIDTH/1536)).render("<", True, (255, 255, 255))
        self.exitButtonOutline = list(self.exitButtonOutline)
        self.exitButtonOutline[2] = char.get_rect().width
        self.exitButtonOutline[3] = char.get_rect().height
        self.exitButtonOutline = tuple(self.exitButtonOutline)
        
        self.screen.blit(char, (a, b))
        
        self.printInstructions()

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        c = homescreen.createHomescreen(self.WIDTH, self.HEIGHT, self.fullscreen)
                        c.run(False)

                elif event.type == pygame.VIDEORESIZE:
                    s = createInstructions(self.WIDTH, self.HEIGHT, self.fullscreen)
                    s.run()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(self.exitButtonOutline).collidepoint(pygame.mouse.get_pos()):
                        c = homescreen.createHomescreen(self.WIDTH, self.HEIGHT, self.fullscreen)
                        c.run(False)

if __name__ == "__main__":
    try:
        WIDTH, HEIGHT = pyautogui.size()
    except:
        WIDTH = 800
        HEIGHT = 600

    i = createInstructions(WIDTH, HEIGHT, True)
    i.run()

    # update tasks, improve visuals, add a 'back' button, fix text for 2nd screen setting

    # create a scrollbar if needed: https://copyprogramming.com/howto/pygame-scrolling-down-page#pygame-scrolling-down-page

    