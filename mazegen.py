import pygame
import random
import os

import math
import health
import pelletsandammo
#import weapons
import mousetargettracker

import asyncio
import time

from bosses import *
from user_settings import *
from calculated_vars import *
import colors

pygame.init()
player_health = health.healthbar()
player_score = pelletsandammo.pellets()
#player_weapon = weapons.weapons()
start_time = time.time()
shield_regen_timer = time.time()
cur_health = player_health.get_health()
player_target = mousetargettracker.mouseTarget()
last_key = ""
regen_time = 10
#temp = 0 testing variable for shield regen

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

from wall_generation import *


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

import big_maze_ghosts as bmg
a_ghost = bmg.Ghost(window, 1)

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
            if event.key == pygame.K_SPACE:
                w = (walls_around(playerx // SQUARE_SIZE, playery // SQUARE_SIZE))
                print(walls.intersection(w))
                print(playerx // SQUARE_SIZE, playery // SQUARE_SIZE)
                bx, by = playerx // SQUARE_SIZE, playery // SQUARE_SIZE
                if ((bx, by), (bx + 1, by)) not in w:
                    print("up available")
                if ((bx + 1, by), (bx + 1, by + 1)) not in w:
                    print("right available")
                if ((bx, by + 1), (bx + 1, by + 1)) not in w:
                    print("down available")
                if ((bx, by), (bx, by + 1)) not in w:
                    print("left available")
                        #breakpoint()
            if event.key == pygame.K_q:
                a_ghost.step()
        elif event.type == pygame.JOYDEVICEADDED and not joystick:
            joystick = pygame.joystick.Joystick(event.device_index)
        elif event.type == pygame.JOYDEVICEREMOVED and joystick:
            joystick = None

    velocity = PLAYER_SPEED
    copysx = startx
    copysy = starty
    copypx = playerx
    copypy = playery

    #testing for shield regeneration
    # cur_health = 100
    # temp += 1
    # print("TEMP------------------------------------" + str(temp))
    # if temp > 1000:

    cur_health = player_health.get_health()


    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] or (joystick and joystick.get_axis(0) <= -JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[0] == -1):
        last_key = "left" 
        if not UNCAPPED_FPS:
            playerx -= velocity / FPS * SQUARE_SIZE
        else:
            playerx -= velocity * (delay_to - last) * SQUARE_SIZE
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] or (joystick and joystick.get_axis(0) >= JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[0] == 1):
        last_key = "right" 
        if not UNCAPPED_FPS:
            playerx += velocity / FPS * SQUARE_SIZE
        else:
            playerx += velocity * (delay_to - last) * SQUARE_SIZE
    elif keys[pygame.K_UP] or keys[pygame.K_w] or (joystick and joystick.get_axis(1) <= -JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[1] == 1):
        last_key = "up" 
        if not UNCAPPED_FPS:
            playery -= velocity / FPS * SQUARE_SIZE
        else:
            playery -= velocity * (delay_to - last) * SQUARE_SIZE
    elif keys[pygame.K_DOWN] or keys[pygame.K_s] or (joystick and joystick.get_axis(1) >= JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[1] == -1):
        last_key = "down" 
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
    #Old shooting code, ignore for now, do not delete

    # if keys [pygame.K_RSHIFT]:
    #     cur_time = time.time()
    #     if player_score.get_ammo() > 0 and (cur_time - start_time > 1):
    #         start_time = cur_time
    #         asyncio.run(player_weapon.shoot(window, round(playerx - startx * SQUARE_SIZE - (SQUARE_SIZE // 2)), 
    #                             round(playery - starty * SQUARE_SIZE - (SQUARE_SIZE // 2)), "laser_gun", last_key))
    #         player_score.use_ammo(1)

    # cur_proj = player_weapon.get_projectiles()
    # if len(cur_proj) > 0:
    #     for i in cur_proj:
    #         player_weapon.track_laser(window)


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
        walls = gen_walls(int(startx), int(starty)) - walls_to_remove
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
    if playerx - WIDTH // 2 > (BOUND - (BOSS_AREA * SQUARE_SIZE) + (SQUARE_SIZE // 2 if PADX else 0)) + SQUARE_SIZE and playery - HEIGHT // 2 < (-BOUND + (BOSS_AREA * SQUARE_SIZE) - (SQUARE_SIZE // 2 if PADY else 0)):
        if 2 not in defeated_bosses:
            if not wall_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_spawn.wav"))
                ba_overlap = boss_walls.intersection(walls)
                walls |= boss_walls
                wall_lock = True
                ACTIVE_BOSS = BossTR(window)
            last_walls = walls
    if playerx - WIDTH // 2 < (-BOUND + (BOSS_AREA * SQUARE_SIZE) - (SQUARE_SIZE // 2 if PADX else 0)) and playery - HEIGHT // 2 > (BOUND - (BOSS_AREA * SQUARE_SIZE) + (SQUARE_SIZE // 2 if PADY else 0)) + SQUARE_SIZE:
        if 3 not in defeated_bosses:
            if not wall_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_spawn.wav"))
                ba_overlap = boss_walls.intersection(walls)
                walls |= boss_walls
                wall_lock = True
                ACTIVE_BOSS = BossBL(window)
            last_walls = walls
    if playerx - WIDTH // 2 > (BOUND - (BOSS_AREA * SQUARE_SIZE) + (SQUARE_SIZE // 2 if PADX else 0)) + SQUARE_SIZE and playery - HEIGHT // 2 > (BOUND - (BOSS_AREA * SQUARE_SIZE) + (SQUARE_SIZE // 2 if PADY else 0)) + SQUARE_SIZE:
        if 4 not in defeated_bosses:
            if not wall_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_spawn.wav"))
                ba_overlap = boss_walls.intersection(walls)
                walls |= boss_walls
                wall_lock = True
                ACTIVE_BOSS = BossBR(window)
            last_walls = walls

    if playerx - WIDTH // 2 < (-BOUND + ((BOSS_AREA + 1) * SQUARE_SIZE)) and playery - HEIGHT // 2 < (-BOUND + ((BOSS_AREA + 1) * SQUARE_SIZE)):
        if 1 in defeated_bosses:
            ACTIVE_BOSS = None
            if 1 not in sound_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_defeat.wav"))
                sound_lock.add(1)
            walls = (walls - boss_walls) | ba_overlap
            last_walls = walls
            wall_lock = False
    if playerx - WIDTH // 2 > (BOUND - ((BOSS_AREA + 1) * SQUARE_SIZE)) + SQUARE_SIZE and playery - HEIGHT // 2 < (-BOUND + ((BOSS_AREA + 1) * SQUARE_SIZE)):
        if 2 in defeated_bosses:
            ACTIVE_BOSS = None
            if 2 not in sound_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_defeat.wav"))
                sound_lock.add(2)
            walls = (walls - boss_walls) | ba_overlap
            last_walls = walls
            wall_lock = False
    if playerx - WIDTH // 2 < (-BOUND + ((BOSS_AREA + 1) * SQUARE_SIZE)) and playery - HEIGHT // 2 > (BOUND - ((BOSS_AREA + 1) * SQUARE_SIZE)) + SQUARE_SIZE:
        if 3 in defeated_bosses:
            ACTIVE_BOSS = None
            if 3 not in sound_lock:
                pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/boss_defeat.wav"))
                sound_lock.add(3)
            walls = (walls - boss_walls) | ba_overlap
            last_walls = walls
            wall_lock = False
    if playerx - WIDTH // 2 > (BOUND - ((BOSS_AREA + 1) * SQUARE_SIZE)) + SQUARE_SIZE and playery - HEIGHT // 2 > (BOUND - ((BOSS_AREA + 1) * SQUARE_SIZE)) + SQUARE_SIZE:
        if 4 in defeated_bosses:
            ACTIVE_BOSS = None
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

    # draw calls - a LOT of them
    window.fill((0, 0, 0))

    pygame.draw.circle(window, (255, 255, 0), (round(playerx - startx * SQUARE_SIZE - (SQUARE_SIZE // 2)), round(playery - starty * SQUARE_SIZE - (SQUARE_SIZE // 2))), RADIUS)

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

    if ACTIVE_BOSS:        
        ACTIVE_BOSS.update_cam(
            startx + BORDER_X,
            startx - BORDER_X,
            starty + BORDER_Y,
            starty - BORDER_Y
        )
        ACTIVE_BOSS.update(playerx - (startx * SQUARE_SIZE) - SQUARE_SIZE // 2, playery - (starty * SQUARE_SIZE) - SQUARE_SIZE // 2, frame_count)

    
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

    # draw player
    # yellow circle at center of screen

    #health bar init and score init
    #shield regen 
    # print("SRT" + str(shield_regen_timer))
    # print("Regen time" + str(regen_time))
    # print("Difference" + str(shield_regen_timer - regen_time))
    if (cur_health == player_health.get_health()):
        regen_time = time.time()
    else:
        shield_regen_timer = time.time()
    if (-1 * (shield_regen_timer - regen_time) > 10):
        player_health.regen(1)
    player_health.gen_healthbar(window, WIDTH)
    player_health.gen_shieldbar(window, WIDTH)
    player_score.display_score(window, WIDTH)
    player_score.display_ammo(window, WIDTH)    
    player_target.update_target(window, (0,0))
    
    a_ghost.update(startx, starty)

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