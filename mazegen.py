# This is a temporary file used to test maze generation,
# as well as controls and camera movement for the game.

# Later, this will be used for maze generation functions
# (such as finding the walls at a specific point).




import pygame
import random

pygame.init()

# screen

WIDTH = 800
HEIGHT = 600

SQUARE_SIZE = 50
assert WIDTH % SQUARE_SIZE == 0
assert HEIGHT % SQUARE_SIZE == 0

FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

# clock
clock = pygame.time.Clock()

walls = set()

wall_creation_threshold = 0.2

startx = 0
starty = 0

def gen_walls(from_x, from_y):
    walls = set()
    for x in range(-2, WIDTH // SQUARE_SIZE + 3):
        for y in range(-2, HEIGHT // SQUARE_SIZE + 3):
            point = ((from_x + x), (from_y + y))
            rgen = random.Random((from_x + x) * SQUARE_SIZE + (from_y + y))
            threshold = rgen.randint(15, 35) / 100
            if rgen.random() < threshold:
                walls.add((point, (point[0] + 1, point[1])))
            if rgen.random() < threshold:
                walls.add((point, (point[0], point[1] + 1)))
            if rgen.random() < threshold:
                walls.add((point, (point[0] - 1, point[1])))
            if rgen.random() < threshold:
                walls.add((point, (point[0], point[1] - 1)))
    return walls

walls = gen_walls(0, 0)

frame_count = 0

last_walls = walls
lastx = 0
lasty = 0

while True:
    # events
    direction = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_RIGHT:
                direction = 2
            if event.key == pygame.K_UP:
                direction = 3
            if event.key == pygame.K_DOWN:
                direction = 4

    velocity = 5 # squares per second

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        startx -= velocity / FPS
    if keys[pygame.K_RIGHT]:
        startx += velocity / FPS
    if keys[pygame.K_UP]:
        starty -= velocity / FPS
    if keys[pygame.K_DOWN]:
        starty += velocity / FPS

    

    # update
    #window.fill((80, 121, 235))
    window.fill((0, 0, 0))

    if startx // 1 != lastx or starty // 1 != lasty:
        walls = gen_walls(startx // 1, starty // 1)
        lastx = startx // 1
        lasty = starty // 1
        last_walls = walls

    else:
        walls = last_walls

    
    for wall in walls:
        pygame.draw.line(window, (255, 255, 255), 
                        ((wall[0][0]-startx) * SQUARE_SIZE - (SQUARE_SIZE / 2), (wall[0][1]-starty) * SQUARE_SIZE - (SQUARE_SIZE / 2)),
                        ((wall[1][0]-startx) * SQUARE_SIZE - (SQUARE_SIZE / 2), (wall[1][1]-starty) * SQUARE_SIZE - (SQUARE_SIZE / 2)), 5)


    # draw player
    # yellow circle at center of screen
    pygame.draw.circle(window, (255, 255, 0), (WIDTH // 2, HEIGHT // 2), 16)


    pygame.display.update()
    frame_count = (frame_count + 1) % FPS
    clock.tick(FPS)
