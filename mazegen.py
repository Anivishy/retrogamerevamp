import pygame
import random
import os

import math
import health
import pelletsandammo
import weapons

import asyncio

from bosses import *
from user_settings import *
from calculated_vars import *
import colors

pygame.init()
player_health = health.healthbar()
player_score = pelletsandammo.pellets()
player_weapon = weapons.weapons()


# try:
#     import pyautogui
#     WIDTH, HEIGHT = pyautogui.size()
# except:
#     WIDTH = 800
#     HEIGHT = 600



player_health = health.healthbar()





print(f"Initializing: {WIDTH}x{HEIGHT}, square size: {SQUARE_SIZE}")

window = pygame.display.set_mode((WIDTH, HEIGHT), (pygame.FULLSCREEN if FULLSCREEN else 0) | pygame.GL_DOUBLEBUFFER)



pygame.display.set_caption("Maze Generator")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

clock = pygame.time.Clock()


walls = set()



defeated_bosses = set()






import time

boss_zones = set()
for x in range(BOSS_AREA):
    for y in range(BOSS_AREA):
        # top left
        boss_zones.add(((x - int(BORDER_X), y - int(BORDER_Y)), (x - int(BORDER_X), y + 1 - int(BORDER_Y))))
        boss_zones.add(((x - int(BORDER_X), y - int(BORDER_Y)), (x + 1 - int(BORDER_X), y - int(BORDER_Y))))

        # top right
        boss_zones.add(((x + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y - int(BORDER_Y)), (x + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y + 1 - int(BORDER_Y))))
        boss_zones.add(((x + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y - int(BORDER_Y)), (x + 1 + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y - int(BORDER_Y))))

        # bottom left
        boss_zones.add(((x - int(BORDER_X), y + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1), (x - int(BORDER_X), y + 1 + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1)))
        boss_zones.add(((x - int(BORDER_X), y + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1), (x + 1 - int(BORDER_X), y + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1)))

        # bottom right
        boss_zones.add(((x + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1), (x + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y + 1 + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1)))
        boss_zones.add(((x + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1), (x + 1 + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1)))

boss_walls = set()
for x in range(BOSS_AREA):
    boss_walls.add(((x - int(BORDER_X), -int(BORDER_Y) + BOSS_AREA), (x + 1 - int(BORDER_X), -int(BORDER_Y) + BOSS_AREA)))
    boss_walls.add(((x + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, -int(BORDER_Y) + BOSS_AREA), (x + 1 + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, -int(BORDER_Y) + BOSS_AREA)))
    boss_walls.add(((x - int(BORDER_X), int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1), (x + 1 - int(BORDER_X), int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1)))
    boss_walls.add(((x + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1), (x + 1 + int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1)))
for y in range(BOSS_AREA):
    boss_walls.add(((-int(BORDER_X) + BOSS_AREA, y - int(BORDER_Y)), (-int(BORDER_X) + BOSS_AREA, y + 1 - int(BORDER_Y))))
    boss_walls.add(((int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y - int(BORDER_Y)), (int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y + 1 - int(BORDER_Y))))
    boss_walls.add(((-int(BORDER_X) + BOSS_AREA, y + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1), (-int(BORDER_X) + BOSS_AREA, y + 1 + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1)))
    boss_walls.add(((int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1), (int(BORDER_X) + (WIDTH // SQUARE_SIZE) - BOSS_AREA + 1, y + 1 + int(BORDER_Y) + (HEIGHT // SQUARE_SIZE) - BOSS_AREA + 1)))

def create_protected(from_x, from_y):
    protected = set()
    if abs(from_x) >= int(BORDER_X) - 1:
        if from_x < 0:
            for y in range(from_y - 1, from_y + (HEIGHT // SQUARE_SIZE) + 2):
                protected.add(
                    ((int(-BORDER_X), y), (int(-BORDER_X), y + 1))
                )
        else:
            for y in range(from_y - 1, from_y + (HEIGHT // SQUARE_SIZE) + 2):
                protected.add(
                    ((int(BORDER_X) + WIDTH // SQUARE_SIZE + 1, y), (int(BORDER_X) + WIDTH // SQUARE_SIZE + 1, y + 1))
                )

    if abs(from_y) >= int(BORDER_Y) - 2:
        if from_y < 0:
            for x in range(from_x - 1, from_x + (WIDTH // SQUARE_SIZE) + 2):
                protected.add(
                    ((x, int(-BORDER_Y)), (x + 1, int(-BORDER_Y)))
                )
        else:
            for x in range(from_x - 1, from_x + (WIDTH // SQUARE_SIZE) + 2):
                protected.add(
                    ((x, int(BORDER_Y) + HEIGHT // SQUARE_SIZE + 1), (x + 1, int(BORDER_Y) + HEIGHT // SQUARE_SIZE + 1))
                )
    return protected

def gen_walls(from_x, from_y):
    walls = set()
    protected = create_protected(from_x, from_y)

    for x in range(-3, WIDTH // SQUARE_SIZE + 3):
        for y in range(-3, HEIGHT // SQUARE_SIZE + 3):
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

    walls -= boss_zones
    walls |= protected
    for x in range(-3, WIDTH // SQUARE_SIZE + 3):
        for y in range(-3, HEIGHT // SQUARE_SIZE + 3):
            point = ((from_x + x), (from_y + y))
            rgen = random.Random((from_x + x) * SQUARE_SIZE + (from_y + y))
            # boilerplate extravaganza - you have been warned!
            x1 = point[0]
            y1 = point[1]
            x2 = point[0] + 1
            y2 = point[1] + 1

            top = ((x1, y1), (x2, y1)) # top
            left = ((x1, y1), (x1, y2)) # left
            right = ((x2, y1), (x2, y2)) # right
            bottom = ((x1, y2), (x2, y2)) # bottom


            go = True
            while go:
                go = False
                for possibility in [
                    {top, left, right},
                    {left, top, bottom},
                    {right, top, bottom},
                    {bottom, left, right}
                    ]:
                    if all(p in walls for p in possibility):
                            w = rgen.choice((list(possibility)))
                            if w not in protected:
                                walls.discard(w)
                                go = True
                                break
    return walls

def preload_walls(fromx, fromy, tox, toy, walls):
    direction = 0
    if fromx > tox:    
        direction = 1 # left
    elif fromx < tox:
        direction = 2 # right
    elif fromy > toy:
        direction = 3 # up
    elif fromy < toy:
        direction = 4 # down

    protected = create_protected(tox, toy)

    if fromx == tox:
        bxl = fromx - 3
        bxr = fromx + (WIDTH // SQUARE_SIZE) + 3
    if fromy == toy:
        byt = fromy - 3
        byb = fromy + (HEIGHT // SQUARE_SIZE) + 3
    
    if direction == 1:
        bxl = tox - 3
        bxr = tox + 1
    elif direction == 2:
        bxl = tox + WIDTH // SQUARE_SIZE - 1
        bxr = tox + WIDTH // SQUARE_SIZE + 3
    elif direction == 3:
        byt = toy - 3
        byb = toy + 1
    elif direction == 4:
        byt = toy + HEIGHT // SQUARE_SIZE - 1
        byb = toy + HEIGHT // SQUARE_SIZE + 3


    new_walls = set()
    if direction == 1:
        for wall in walls:
            if wall[0][0] != fromx + 3 + (WIDTH // SQUARE_SIZE) and wall[1][0] != fromx + 3 + (WIDTH // SQUARE_SIZE):
                new_walls.add(wall)
        for y in range(-3, HEIGHT // SQUARE_SIZE + 3):
            point = ((tox - 2), (toy + y))
            rgen = random.Random((tox - 2) * SQUARE_SIZE + (toy + y))
            threshold = rgen.randint(15, 35) / 100
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] + 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] + 1)])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] - 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] - 1)])))
    elif direction == 2:
        for wall in walls:
            if wall[0][0] != fromx - 3 and wall[1][0] != fromx - 3:
                new_walls.add(wall)
        for y in range(-3, HEIGHT // SQUARE_SIZE + 3):
            point = ((tox + WIDTH / SQUARE_SIZE + 2), (toy + y))
            rgen = random.Random((tox + WIDTH / SQUARE_SIZE + 2) * SQUARE_SIZE + (toy + y))
            threshold = rgen.randint(15, 35) / 100
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] + 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] + 1)])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] - 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] - 1)])))
    elif direction == 3:
        for wall in walls:
            if wall[0][1] != fromy + 3 + (HEIGHT // SQUARE_SIZE) and wall[1][1] != fromy + 3 + (HEIGHT // SQUARE_SIZE):
                new_walls.add(wall)
        for x in range(-3, WIDTH // SQUARE_SIZE + 3):
            point = ((tox + x), (toy - 2))
            rgen = random.Random((tox + x) * SQUARE_SIZE + (toy - 2))
            threshold = rgen.randint(15, 35) / 100
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] + 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] + 1)])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] - 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] - 1)])))
    elif direction == 4:
        for wall in walls:
            if wall[0][1] != fromy - 3 and wall[1][1] != fromy - 3:
                new_walls.add(wall)
        for x in range(-3, WIDTH // SQUARE_SIZE + 3):
            point = ((tox + x), (toy + HEIGHT / SQUARE_SIZE + 2))
            rgen = random.Random((tox + x) * SQUARE_SIZE + (toy + HEIGHT / 2 + 2))
            threshold = rgen.randint(15, 35) / 100
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] + 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] + 1)])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] - 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] - 1)])))

    new_walls -= boss_zones
    new_walls |= protected
    
    for x in range(int(bxl), int(bxr)):
        for y in range(int(byt), int(byb)):
            point = ((x), (y))
            rgen = random.Random((x) * SQUARE_SIZE + (y))
            # boilerplate extravaganza - you have been warned!
            x1 = point[0]
            y1 = point[1]
            x2 = point[0] + 1
            y2 = point[1] + 1

            top = ((x1, y1), (x2, y1)) # top
            left = ((x1, y1), (x1, y2)) # left
            right = ((x2, y1), (x2, y2)) # right
            bottom = ((x1, y2), (x2, y2)) # bottom


            go = True
            while go:
                go = False
                for possibility in [
                    {top, left, right},
                    {left, top, bottom},
                    {right, top, bottom},
                    {bottom, left, right}
                    ]:
                    if all(p in new_walls for p in possibility):
                            w = rgen.choice((list(possibility)))
                            if w not in protected:
                                new_walls.discard(w)
                                go = True
                                break

    return new_walls



playerx = WIDTH // 2 + SQUARE_SIZE // 2
playery = HEIGHT // 2 + SQUARE_SIZE // 2

lpx = playerx
lpy = playery

startx = (playerx - (WIDTH // 2) - (SQUARE_SIZE // 2)) / SQUARE_SIZE
starty = (playery - (HEIGHT // 2) - (SQUARE_SIZE // 2)) / SQUARE_SIZE

cx = startx
cy = starty

lastx = startx
lasty = starty

delay_to = time.time()
last = delay_to - (1/60)

SAFE_RADIUS = 2

walls_to_remove = set()
x_off = int((WIDTH / SQUARE_SIZE) / 2)
y_off = int((HEIGHT / SQUARE_SIZE) / 2)
for x in range(-SAFE_RADIUS, SAFE_RADIUS+1):
    for y in range(-SAFE_RADIUS, SAFE_RADIUS+1):
        walls_to_remove.add(((x + x_off, y + y_off), (x + x_off, y + y_off + 1)))
        walls_to_remove.add(((x + x_off, y + y_off), (x + x_off + 1, y + y_off)))

        
#walls_to_remove = set()
walls = gen_walls(0, 0) - walls_to_remove

frame_count = 0

last_walls = walls
intersected = set()

ACTIVE_BOSS = None

ba_overlap = set()
wall_lock = False
sound_lock = set()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
if len(joysticks) > 0:
    joystick = joysticks[0]
else:
    joystick = None

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
        elif event.type == pygame.JOYDEVICEADDED and not joystick:
            joystick = pygame.joystick.Joystick(event.device_index)
        elif event.type == pygame.JOYDEVICEREMOVED and joystick:
            joystick = None

    velocity = PLAYER_SPEED
    copysx = startx
    copysy = starty
    copypx = playerx
    copypy = playery

    

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] or (joystick and joystick.get_axis(0) <= -JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[0] == -1): 
        if not UNCAPPED_FPS:
            playerx -= velocity / FPS * SQUARE_SIZE
        else:
            playerx -= velocity * (delay_to - last) * SQUARE_SIZE
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] or (joystick and joystick.get_axis(0) >= JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[0] == 1):
        if not UNCAPPED_FPS:
            playerx += velocity / FPS * SQUARE_SIZE
        else:
            playerx += velocity * (delay_to - last) * SQUARE_SIZE
    elif keys[pygame.K_UP] or keys[pygame.K_w] or (joystick and joystick.get_axis(1) <= -JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[1] == 1):
        if not UNCAPPED_FPS:
            playery -= velocity / FPS * SQUARE_SIZE
        else:
            playery -= velocity * (delay_to - last) * SQUARE_SIZE
    elif keys[pygame.K_DOWN] or keys[pygame.K_s] or (joystick and joystick.get_axis(1) >= JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[1] == -1):
        if not UNCAPPED_FPS:
            playery += velocity / FPS * SQUARE_SIZE
        else:
            playery += velocity * (delay_to - last) * SQUARE_SIZE
    elif keys[pygame.K_1]:
        defeated_bosses.add(1)
    elif keys[pygame.K_2]:
        defeated_bosses.add(2)
    elif keys[pygame.K_3]:
        defeated_bosses.add(3)
    elif keys[pygame.K_4]:
        defeated_bosses.add(4)


    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
    if keys[pygame.K_SPACE]:
        breakpoint()

    if keys [pygame.K_RSHIFT]:
        if player_score.get_ammo() > 0:
            player_weapon.shoot(window, round(playerx - startx * SQUARE_SIZE - (SQUARE_SIZE // 2)), round(playery - starty * SQUARE_SIZE - (SQUARE_SIZE // 2)), "laser_gun")
            player_score.use_ammo(1)


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

    # for some reason, there is 1 pixel of extra space at the top and the left
    # so the camera will try to go towards that, but this shifts the camera bound over by 1 pixel
    if not FIXED_X:
        startx = min(max(startx, -BORDER_X + (1/SQUARE_SIZE)), BORDER_X)
    else:
        startx = cx
       
    if not FIXED_Y:
        starty = min(max(starty, -BORDER_Y + (1/SQUARE_SIZE)), BORDER_Y)
    else:
        starty = cy


    if int(startx) != lastx or int(starty) != lasty:
        #walls = gen_walls(int(startx), int(starty)) - walls_to_remove
        walls = preload_walls(lastx, lasty, int(startx), int(starty), walls)
        lastx = int(startx)
        lasty = int(starty)

        last_walls = walls

    else:
        walls = last_walls
    
    walls -= walls_to_remove
    
    if playerx - WIDTH // 2 < (-BOUND + (BOSS_AREA * SQUARE_SIZE) - (SQUARE_SIZE // 2 if PADX else 0)) and playery - HEIGHT // 2 < (-BOUND + (BOSS_AREA * SQUARE_SIZE) - (SQUARE_SIZE // 2 if PADY else 0)):
        if 1 not in defeated_bosses:
            if not wall_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_spawn.wav"))
                ba_overlap = boss_walls.intersection(walls)
                walls |= boss_walls
                wall_lock = True
                ACTIVE_BOSS = BossTL(window)
            last_walls = walls
        else:
            if 1 not in sound_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_defeat.wav"))
                sound_lock.add(1)
            walls = (walls - boss_walls) | ba_overlap
            last_walls = walls
            wall_lock = False
    if playerx - WIDTH // 2 > (BOUND - (BOSS_AREA * SQUARE_SIZE) + (SQUARE_SIZE // 2 if PADX else 0)) + SQUARE_SIZE and playery - HEIGHT // 2 < (-BOUND + (BOSS_AREA * SQUARE_SIZE) - (SQUARE_SIZE // 2 if PADY else 0)):
        if 2 not in defeated_bosses:
            if not wall_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_spawn.wav"))
                ba_overlap = boss_walls.intersection(walls)
                walls |= boss_walls
                wall_lock = True
            last_walls = walls
        else:
            if 2 not in sound_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_defeat.wav"))
                sound_lock.add(2)
            walls = (walls - boss_walls) | ba_overlap
            last_walls = walls
            wall_lock = False
    if playerx - WIDTH // 2 < (-BOUND + (BOSS_AREA * SQUARE_SIZE) - (SQUARE_SIZE // 2 if PADX else 0)) and playery - HEIGHT // 2 > (BOUND - (BOSS_AREA * SQUARE_SIZE) + (SQUARE_SIZE // 2 if PADY else 0)) + SQUARE_SIZE:
        if 3 not in defeated_bosses:
            if not wall_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_spawn.wav"))
                ba_overlap = boss_walls.intersection(walls)
                walls |= boss_walls
                wall_lock = True
            last_walls = walls
        else:
            if 3 not in sound_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_defeat.wav"))
                sound_lock.add(3)
            walls = (walls - boss_walls) | ba_overlap
            last_walls = walls
            wall_lock = False
    if playerx - WIDTH // 2 > (BOUND - (BOSS_AREA * SQUARE_SIZE) + (SQUARE_SIZE // 2 if PADX else 0)) + SQUARE_SIZE and playery - HEIGHT // 2 > (BOUND - (BOSS_AREA * SQUARE_SIZE) + (SQUARE_SIZE // 2 if PADY else 0)) + SQUARE_SIZE:
        if 4 not in defeated_bosses:
            if not wall_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_spawn.wav"))
                ba_overlap = boss_walls.intersection(walls)
                walls |= boss_walls
                wall_lock = True
            last_walls = walls
        else:
            if 4 not in sound_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_defeat.wav"))
                sound_lock.add(4)
            walls = (walls - boss_walls) | ba_overlap
            last_walls = walls
            wall_lock = False

    walls_to_check = set()
    for x in range(0, 2):
        for y in range(0, 2):
            walls_to_check |= set(w for w in walls if (playerx // SQUARE_SIZE + x, playery // SQUARE_SIZE + y) in w)

    walls_to_check = walls_to_check.intersection(walls)

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

    window.fill((0, 0, 0))

    pygame.draw.circle(window, (255, 255, 0), (round(playerx - startx * SQUARE_SIZE - (SQUARE_SIZE // 2)), round(playery - starty * SQUARE_SIZE - (SQUARE_SIZE // 2))), RADIUS)
    for wall in walls:
        wall_color = colors.DEFAULT_BLUE
        if wall[0][0] > (WIDTH // 2 // SQUARE_SIZE) and wall[0][1] > (HEIGHT // 2 // SQUARE_SIZE):
            wall_color = colors.SHADOW
        elif wall[0][0] < (WIDTH // 2 // SQUARE_SIZE) and wall[0][1] > (HEIGHT // 2 // SQUARE_SIZE):
            wall_color = colors.ICE
        elif wall[0][0] > (WIDTH // 2 // SQUARE_SIZE) and wall[0][1] < (HEIGHT // 2 // SQUARE_SIZE):
            wall_color = colors.LAVA
        elif wall[0][0] < (WIDTH // 2 // SQUARE_SIZE) and wall[0][1] < (HEIGHT // 2 // SQUARE_SIZE):
            wall_color = colors.FOREST
        else:
            wall_color = colors.GREY
        
        if wall[0][0] == WIDTH // 2 // SQUARE_SIZE or wall[1][0] == WIDTH // 2 // SQUARE_SIZE + 1:
            wall_color = colors.GREY
        if wall[0][1] == HEIGHT // 2 // SQUARE_SIZE or wall[1][1] == HEIGHT // 2 // SQUARE_SIZE + 1:
            wall_color = colors.GREY


        pygame.draw.line(window, wall_color, 
                        ((wall[0][0]-startx) * SQUARE_SIZE - (SQUARE_SIZE // 2), (wall[0][1]-starty) * SQUARE_SIZE - (SQUARE_SIZE // 2)),
                        ((wall[1][0]-startx) * SQUARE_SIZE - (SQUARE_SIZE // 2), (wall[1][1]-starty) * SQUARE_SIZE - (SQUARE_SIZE // 2)), WALL_WIDTH)

    if ACTIVE_BOSS:
        
        ACTIVE_BOSS.update(playerx - (startx * SQUARE_SIZE) - SQUARE_SIZE // 2, playery - (starty * SQUARE_SIZE) - SQUARE_SIZE // 2)


    player_rect = pygame.Rect(
        -startx * SQUARE_SIZE + playerx - SQUARE_SIZE // 2 - RADIUS, 
        -RADIUS - SQUARE_SIZE // 2 -starty * SQUARE_SIZE + playery, 
        RADIUS*2, RADIUS*2)
    
    conx = min(max(playerx, -BORDER_X * SQUARE_SIZE + WIDTH // 2), BORDER_X * SQUARE_SIZE + WIDTH // 2) // SQUARE_SIZE
    cony = min(max(playery, -BORDER_Y * SQUARE_SIZE + HEIGHT // 2), BORDER_Y * SQUARE_SIZE + HEIGHT // 2) // SQUARE_SIZE
    
    for x in range(-WIDTH // SQUARE_SIZE // 2 - 2, WIDTH // SQUARE_SIZE // 2 + 3):
        for y in range(-HEIGHT // SQUARE_SIZE // 2 - 3, HEIGHT // SQUARE_SIZE // 2 + 3):
            square_length = SQUARE_SIZE / 8
            rgen = random.Random((conx + x) * SQUARE_SIZE + (cony + y))
            if rgen.random() < 0.5:
                rect = pygame.Rect(
                        (conx + x) * SQUARE_SIZE - (square_length // 2) - startx * SQUARE_SIZE,
                        (cony + y) * SQUARE_SIZE - (square_length // 2) - starty * SQUARE_SIZE,
                        square_length,
                        square_length
                    )

                indicator = (conx + x, cony + y)
                if rect.colliderect(player_rect):
                    # at this point,
                    # the game detects the player picked up a pellet
                    if indicator not in intersected:
                        player_score.update_score()
                        pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/pellet.wav"))
                        intersected.add(indicator)
                if indicator not in intersected:            
                    pygame.draw.rect(window, (170, 170, 0), rect)

    # draw player
    # yellow circle at center of screen

    #health bar init and score init
    player_health.gen_healthbar(window, WIDTH)
    player_score.display_score(window, WIDTH)
    player_score.display_ammo(window, WIDTH)
    
    pygame.display.update()
    
    if UNCAPPED_FPS:
        frame_count += 1
        if frame_count % 1000 == 0:
            #print(round(1/(time.time() - delay_to)))
            ...
        last = delay_to
        delay_to = time.time()
        UCFD.delay = delay_to - last
    else:
        frame_count = (frame_count + 1) % FPS
        clock.tick(FPS)
        if frame_count == 0:
            #print(round(clock.get_fps()))
            ...