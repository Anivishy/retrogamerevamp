# This is a temporary file used to test maze generation,
# as well as controls and camera movement for the game.

# Later, this will be used for maze generation functions
# (such as finding the walls at a specific point).

# working title: PAC-ROOMS


# setup pygame project
import pygame
import random
import os
import pyautogui

os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pygame.init()

WIDTH, HEIGHT = pyautogui.size()

FULLSCREEN = True

# WIDTH = 1920
# HEIGHT = 1200

# screen
WALL_WIDTH = 5

SQUARE_SIZE = 96
while True:
    try:
        if WIDTH % SQUARE_SIZE != 0: raise ValueError(f"{WIDTH} % {SQUARE_SIZE} = {WIDTH % SQUARE_SIZE}, not 0")
        if HEIGHT % SQUARE_SIZE != 0: raise ValueError(f"{HEIGHT} % {SQUARE_SIZE} = {HEIGHT % SQUARE_SIZE}, not 0")
    except:
        SQUARE_SIZE += 1
    else:
        break

print(f"Initializing: {WIDTH}x{HEIGHT}, square size: {SQUARE_SIZE}")

window = pygame.display.set_mode((WIDTH, HEIGHT), (pygame.FULLSCREEN if FULLSCREEN else 0))
print(window.get_size())

FPS = 60

pygame.display.set_caption("Maze Generator")

# clock
clock = pygame.time.Clock()

walls = set()


MAP_RADIUS = 10
RADIUS = int(SQUARE_SIZE / 2) / 2
FIXED_X = FIXED_Y = False

BOUND = MAP_RADIUS * SQUARE_SIZE + SQUARE_SIZE // 2

BORDER_X = (BOUND - WIDTH // 2) / SQUARE_SIZE
if BORDER_X < 0:
    FIXED_X = True
BORDER_Y = (BOUND - HEIGHT // 2) / SQUARE_SIZE
if BORDER_Y < 0:
    FIXED_Y = True



import time


def gen_walls(from_x, from_y):
    walls = set()
    for x in range(-2, WIDTH // SQUARE_SIZE + 3):
        for y in range(-2, HEIGHT // SQUARE_SIZE + 3):
            point = ((from_x + x), (from_y + y))
            rgen = random.Random((from_x + x) * SQUARE_SIZE + (from_y + y))
            threshold = rgen.randint(15, 35) / 100
            if rgen.random() < threshold:
                walls.add(tuple(sorted([point, (point[0] + 1, point[1])])))
            if rgen.random() < threshold:
                walls.add(tuple(sorted([point, (point[0], point[1] + 1)])))
            if rgen.random() < threshold:
                walls.add(tuple(sorted([point, (point[0] - 1, point[1])])))
            if rgen.random() < threshold:
                walls.add(tuple(sorted([point, (point[0], point[1] - 1)])))

    for x in range(-2, WIDTH // SQUARE_SIZE + 3):
        for y in range(-2, HEIGHT // SQUARE_SIZE + 3):
            point = ((from_x + x), (from_y + y))
            rgen = random.Random((from_x + x) * SQUARE_SIZE + (from_y + y))


    return walls

walls = gen_walls(0, 0)

frame_count = 0

last_walls = walls



playerx = WIDTH // 2 + SQUARE_SIZE // 2
playery = HEIGHT // 2 + SQUARE_SIZE // 2

startx = (playerx - (WIDTH // 2) - (SQUARE_SIZE // 2)) / SQUARE_SIZE
starty = (playery - (HEIGHT // 2) - (SQUARE_SIZE // 2)) / SQUARE_SIZE

cx = startx
cy = starty

lastx = startx
lasty = starty

delay_to = time.time()

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

    copysx = startx
    copysy = starty
    copypx = playerx
    copypy = playery


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: 
        playerx -= velocity / FPS * SQUARE_SIZE
    elif keys[pygame.K_RIGHT]:
        playerx += velocity / FPS * SQUARE_SIZE
    elif keys[pygame.K_UP]:
        playery -= velocity / FPS * SQUARE_SIZE
    elif keys[pygame.K_DOWN]:
        playery += velocity / FPS * SQUARE_SIZE

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()


    startx = (playerx - (WIDTH // 2) - (SQUARE_SIZE // 2)) / SQUARE_SIZE
    starty = (playery - (HEIGHT // 2) - (SQUARE_SIZE // 2)) / SQUARE_SIZE
    

    # print(playerx - (startx * SQUARE_SIZE))
    
    # collision detection
    # find walls surrounding player
    # check if player is touching any of them
    # if so, move player back to previous position
    walls_to_check = set({
        ((playerx // SQUARE_SIZE, playery // SQUARE_SIZE), (playerx // SQUARE_SIZE + 1, playery // SQUARE_SIZE)),
        ((playerx // SQUARE_SIZE, playery // SQUARE_SIZE), (playerx // SQUARE_SIZE, playery // SQUARE_SIZE + 1)),
        ((playerx // SQUARE_SIZE + 1, playery // SQUARE_SIZE), (playerx // SQUARE_SIZE + 1, playery // SQUARE_SIZE + 1)),
        ((playerx // SQUARE_SIZE, playery // SQUARE_SIZE + 1), (playerx // SQUARE_SIZE + 1, playery // SQUARE_SIZE + 1))
    })

    if not FIXED_X:
        startx = min(max(startx, -BORDER_X), BORDER_X)
    else:
        startx = cx
       
    if not FIXED_Y:
        starty = min(max(starty, -BORDER_Y), BORDER_Y)
    else:
        starty = cy


    if int(startx) != lastx or int(starty) != lasty:
        walls = gen_walls(int(startx), int(starty))
        lastx = int(startx)
        lasty = int(starty)
        last_walls = walls

    else:
        walls = last_walls
    
    walls_to_check = set()
    for x in range(0, 2):
        for y in range(0, 2):
            walls_to_check |= set(w for w in walls if (playerx // SQUARE_SIZE + x, playery // SQUARE_SIZE + y) in w)

    walls_to_check = walls_to_check.intersection(walls)
    #print(walls_to_check)


    # thank you eJames https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection
    for wall in walls_to_check:
        if wall[0][0] == wall[1][0]:
            # top edge
            topleft = (wall[0][0] * SQUARE_SIZE - WALL_WIDTH / 2, wall[0][1] * SQUARE_SIZE)
            width = WALL_WIDTH
            height = SQUARE_SIZE
            rectx = (topleft[0] + width / 2, topleft[1] + height / 2)
        else:
            # left edge
            topleft = (wall[0][0] * SQUARE_SIZE, wall[0][1] * SQUARE_SIZE - WALL_WIDTH / 2)
            width = SQUARE_SIZE
            height = WALL_WIDTH
            rectx = (topleft[0] + width / 2, topleft[1] + height / 2)
        cdx = abs(playerx - rectx[0])
        cdy = abs(playery - rectx[1])
        if (cdx > (width / 2 + RADIUS)) or (cdy > (height / 2 + RADIUS)):
            continue
        if (cdx <= (width / 2)) or (cdy <= (height / 2)):
            playerx = copypx
            playery = copypy
            startx = copysx
            starty = copysy
            break

        cornerdistance = (cdx - width / 2) ** 2 + (cdy - height / 2) ** 2
        if cornerdistance < ((RADIUS-1) ** 2):
            playerx = copypx
            playery = copypy
            startx = copysx
            starty = copysy
            break 

    # if not (-SQUARE_SIZE * MAP_RADIUS <= playerx) or not (playerx <= SQUARE_SIZE * MAP_RADIUS):
    #     print(playerx, -SQUARE_SIZE * MAP_RADIUS)
    #     playerx = copypx
    #     playery = copypy
    #     startx = copysx
    #     starty = copysy
 

    # update
    #window.fill((80, 121, 235))
    window.fill((0, 0, 0))

    pygame.draw.circle(window, (255, 255, 0), (round(playerx - startx * SQUARE_SIZE - (SQUARE_SIZE // 2)), round(playery - starty * SQUARE_SIZE - (SQUARE_SIZE // 2))), RADIUS)
    for wall in walls:
        pygame.draw.line(window, (33, 33, 222), 
                        ((wall[0][0]-startx) * SQUARE_SIZE - (SQUARE_SIZE // 2), (wall[0][1]-starty) * SQUARE_SIZE - (SQUARE_SIZE // 2)),
                        ((wall[1][0]-startx) * SQUARE_SIZE - (SQUARE_SIZE // 2), (wall[1][1]-starty) * SQUARE_SIZE - (SQUARE_SIZE // 2)), WALL_WIDTH)

    if not FIXED_X:
        pygame.draw.line(window, (0, 255, 0),
            ((-startx * SQUARE_SIZE + WIDTH//2 - BORDER_X*SQUARE_SIZE), 0),
            ((-startx * SQUARE_SIZE + WIDTH//2 - BORDER_X*SQUARE_SIZE), HEIGHT),
            3
        )

        pygame.draw.line(window, (0, 255, 0),
            ((-startx * SQUARE_SIZE + WIDTH//2 + BORDER_X*SQUARE_SIZE), 0),
            ((-startx * SQUARE_SIZE + WIDTH//2 + BORDER_X*SQUARE_SIZE), HEIGHT),
            3
        )

    if not FIXED_Y:
        pygame.draw.line(window, (255, 165, 0),
                        (0, (-starty * SQUARE_SIZE + HEIGHT//2 - BORDER_Y*SQUARE_SIZE)),
                        (WIDTH, (-starty * SQUARE_SIZE + HEIGHT//2 - BORDER_Y*SQUARE_SIZE)),
                        3
                        )
        pygame.draw.line(window, (255, 165, 0),
                        (0, (-starty * SQUARE_SIZE + HEIGHT//2 + BORDER_Y*SQUARE_SIZE)),
                        (WIDTH, (-starty * SQUARE_SIZE + HEIGHT//2 + BORDER_Y*SQUARE_SIZE)),
                        3
                        )

    pygame.draw.line(window, (33, 33, 222),
        ((-startx * SQUARE_SIZE + WIDTH//2 - BOUND), 0),
        ((-startx * SQUARE_SIZE + WIDTH//2 - BOUND), HEIGHT),
        WALL_WIDTH
    )

    pygame.draw.line(window, (33, 33, 222),
        ((-startx * SQUARE_SIZE + WIDTH//2 + BOUND), 0),
        ((-startx * SQUARE_SIZE + WIDTH//2 + BOUND), HEIGHT),
        WALL_WIDTH
    )

    pygame.draw.line(window, (33, 33, 222),
                     (0, (-starty * SQUARE_SIZE + HEIGHT//2 - BOUND)),
                     (WIDTH, (-starty * SQUARE_SIZE + HEIGHT//2 - BOUND)),
                     WALL_WIDTH
                     )
    pygame.draw.line(window, (33, 33, 222),
                     (0, (-starty * SQUARE_SIZE + HEIGHT//2 + BOUND)),
                     (WIDTH, (-starty * SQUARE_SIZE + HEIGHT//2 + BOUND)),
                     WALL_WIDTH
                     )

    

    # draw player
    # yellow circle at center of screen

    pygame.display.update()
    frame_count = (frame_count + 1) % FPS
    clock.tick(FPS)
    if frame_count == 0:
        print(round(clock.get_fps()))