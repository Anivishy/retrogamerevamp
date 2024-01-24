import pygame
import random
import os

import math
import health
import pelletsandammo
#import weapons
import mousetargettracker
import new_shooting


import asyncio
import time

from bosses import *
from user_settings import *
from calculated_vars import *
import colors

pygame.init()
player_health = health.healthbar()
player_score = pelletsandammo.pellets()
#player_bullets = new_shooting.lazer_bullet()
#player_weapon = weapons.weapons()
start_time = time.time()
shield_regen_timer = time.time()
cur_health = player_health.get_health()
player_target = mousetargettracker.mouseTarget()
last_key = ""
regen_time = 10
current_bullets = []
#temp = 0 testing variable for shield regen

# try:
#     import pyautogui
#     WIDTH, HEIGHT = pyautogui.size()
# except:
#     WIDTH = 800
#     HEIGHT = 600



player_health = health.healthbar()



from wall_generation import *


print(f"Initializing: {WIDTH}x{HEIGHT}, square size: {SQUARE_SIZE}\nSeed: {seed}")

window = pygame.display.set_mode((WIDTH, HEIGHT), (pygame.FULLSCREEN if FULLSCREEN else 0) | pygame.GL_DOUBLEBUFFER)



pygame.display.set_caption("Maze Generator")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

clock = pygame.time.Clock()


walls = set()



defeated_bosses = set()






import time



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

player_protected = False
protected_timer = 0

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
if len(joysticks) > 0:
    joystick = joysticks[0]
else:
    joystick = None

import big_maze_ghosts as bmg
a_ghost = bmg.Ghost(window, 1, 0, 0)
# a_ghost.ty = int(playery // SQUARE_SIZE)
#a_ghost.astar(int((playerx + WIDTH // 2) // SQUARE_SIZE), int((playery + HEIGHT // 2) // SQUARE_SIZE))


targettime = time.time()

ghosts = []
for _ in range(12):
    #ghosts.append(bmg.Ghost(window, 1, -MAP_RADIUS + real_round((WIDTH / 2) / SQUARE_SIZE) - int(0.2 * MAP_RADIUS), -MAP_RADIUS + real_round((HEIGHT / 2) / SQUARE_SIZE) - int(0.2 * MAP_RADIUS)))
    
    ghosts.append(bmg.Ghost(window, 1, -int(0.4 * MAP_RADIUS) + round(WIDTH / 2 / SQUARE_SIZE), -int(0.4 * MAP_RADIUS) + round(HEIGHT / 2 / SQUARE_SIZE)))
    ghosts.append(bmg.Ghost(window, 2, int(0.4 * MAP_RADIUS) + round(WIDTH / 2 / SQUARE_SIZE), -int(0.4 * MAP_RADIUS) + round(HEIGHT / 2 / SQUARE_SIZE)))
    ghosts.append(bmg.Ghost(window, 3, -int(0.4 * MAP_RADIUS) + round(WIDTH / 2 / SQUARE_SIZE), int(0.4 * MAP_RADIUS) + round(HEIGHT / 2 / SQUARE_SIZE)))
    ghosts.append(bmg.Ghost(window, 4, int(0.4 * MAP_RADIUS) + round(WIDTH / 2 / SQUARE_SIZE), int(0.4 * MAP_RADIUS) + round(HEIGHT / 2 / SQUARE_SIZE)))
    
velocity = PLAYER_SPEED

calc_fps = 0
calc_time = 0
calc_counter = 0

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

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
                breakpoint()
            if event.key == pygame.K_q:
                a_ghost.step()
        elif event.type == pygame.JOYDEVICEADDED and not joystick:
            joystick = pygame.joystick.Joystick(event.device_index)
        elif event.type == pygame.JOYDEVICEREMOVED and joystick:
            joystick = None

        elif event.type == pygame.MOUSEBUTTONUP:
            # shooting place
            cur_time = time.time()
            if player_score.get_ammo() > 0 and (cur_time - start_time > 1):
                start_time = cur_time
                current_bullets.append(new_shooting.lazer_bullet(playerx - (startx * SQUARE_SIZE) - SQUARE_SIZE // 2, playery - (starty * SQUARE_SIZE) - SQUARE_SIZE // 2, mousex, mousey, HEIGHT, WIDTH))
                player_score.use_ammo(1)
    
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

    bullet_poscopy = {}
    for bullet in current_bullets:
        bullet_poscopy[bullet] = (bullet.x, bullet.y)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] or (joystick and joystick.get_axis(0) <= -JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[0] == -1):
        last_key = "left" 
        if not UNCAPPED_FPS:
            playerx -= velocity / FPS * SQUARE_SIZE
            # if BORDER_X * SQUARE_SIZE + WIDTH // 2 + SQUARE_SIZE // 2 > playerx > -BORDER_X * SQUARE_SIZE + WIDTH // 2 + SQUARE_SIZE // 2:
            #     for bullet in current_bullets:
            #         bullet.x += velocity / FPS * SQUARE_SIZE
            #         #bullet.x += velocity / FPS
        else:
            playerx -= velocity * (delay_to - last) * SQUARE_SIZE
            # if BORDER_X * SQUARE_SIZE + WIDTH // 2 + SQUARE_SIZE // 2 > playerx > -BORDER_X * SQUARE_SIZE + WIDTH // 2 + SQUARE_SIZE // 2:
            #     for bullet in current_bullets:
            #         bullet.x += velocity * (delay_to - last) * SQUARE_SIZE
                    
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] or (joystick and joystick.get_axis(0) >= JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[0] == 1):
        last_key = "right" 
        if not UNCAPPED_FPS:
            playerx += velocity / FPS * SQUARE_SIZE
            # if BORDER_X * SQUARE_SIZE + WIDTH // 2 + SQUARE_SIZE // 2 > playerx > -BORDER_X * SQUARE_SIZE + WIDTH // 2 + SQUARE_SIZE // 2:
            #     for bullet in current_bullets:
            #         bullet.x += velocity / FPS * SQUARE_SIZE
        else:
            playerx += velocity * (delay_to - last) * SQUARE_SIZE
            # if BORDER_X * SQUARE_SIZE + WIDTH // 2 + SQUARE_SIZE // 2 > playerx > -BORDER_X * SQUARE_SIZE + WIDTH // 2 + SQUARE_SIZE // 2:
            #     for bullet in current_bullets:
            #         bullet.x += velocity * (delay_to - last) * SQUARE_SIZE
    elif keys[pygame.K_UP] or keys[pygame.K_w] or (joystick and joystick.get_axis(1) <= -JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[1] == 1):
        last_key = "up" 
        if not UNCAPPED_FPS:
            playery -= velocity / FPS * SQUARE_SIZE
            # if BORDER_X * SQUARE_SIZE - WIDTH // 2 + SQUARE_SIZE // 2 > playerx > -BORDER_X * SQUARE_SIZE + WIDTH // 2 + SQUARE_SIZE // 2:        
            #     for bullet in current_bullets:
            #         bullet.y += velocity / FPS * SQUARE_SIZE
        else:
            playery -= velocity * (delay_to - last) * SQUARE_SIZE
            # for bullet in current_bullets:
            #     bullet.y += velocity * (delay_to - last) * SQUARE_SIZE
    elif keys[pygame.K_DOWN] or keys[pygame.K_s] or (joystick and joystick.get_axis(1) >= JOYSTICK_THRESHOLD) or (joystick and joystick.get_hat(0)[1] == -1):
        last_key = "down" 
        if not UNCAPPED_FPS:
            playery += velocity / FPS * SQUARE_SIZE
            # for bullet in current_bullets:
            #     bullet.x -= velocity / FPS * SQUARE_SIZE
        else:
            playery += velocity * (delay_to - last) * SQUARE_SIZE
            # for bullet in current_bullets:
            #     bullet.y -= velocity * (delay_to - last) * SQUARE_SIZE
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

    # if keys[pygame.K_RSHIFT]: wasd
    #     player_bullets.calculate_path(pygame.mouse.get_pos(), playerx, playery)

    # if keys [pygame.K_RSHIFT]:
    #     cur_time = time.time()
    #     if player_score.get_ammo() > 0 and (cur_time - start_time > 1):
    #         start_time = cur_time
    #         player_bullets.calculate_path(pygame.mouse.get_pos(), playerx - (startx * SQUARE_SIZE), playery - (starty * SQUARE_SIZE), WIDTH, HEIGHT)
    #         print(pygame.mouse.get_pos())
    #         player_score.use_ammo(1)

    # active_paths = player_bullets.get_projectiles()
    # if len(active_paths) > 0:
    #     #print("-------------------------------------------")
    #     player_bullets.draw_lazers(window, WIDTH, HEIGHT)
    #     for i in active_paths:
    #         if len(i) == 0:
    #             active_paths.remove(i)

    #current_bullets = []
    mousex, mousey = pygame.mouse.get_pos()
    if keys [pygame.K_RSHIFT]:
        # shooting place
        cur_time = time.time()
        if player_score.get_ammo() > 0 and (cur_time - start_time > 1):
            start_time = cur_time
            current_bullets.append(new_shooting.lazer_bullet(playerx - (startx * SQUARE_SIZE), playery - (starty * SQUARE_SIZE), mousex, mousey))
            player_score.use_ammo(1)

    #print(current_bullets)

    
            
    


    #Old shooting code, ignore for now, do not delete

    # if keys [pygame.K_RSHIFT]:
    #     cur_time = time.time()
    #     if player_score.get_ammo() > 0 and (cur_time - start_time > 1):
    #         start_time = cur_time
    #         asyncio.run(player_weapon.shoot(window, real_round(playerx - startx * SQUARE_SIZE - (SQUARE_SIZE // 2)), 
    #                             real_round(playery - starty * SQUARE_SIZE - (SQUARE_SIZE // 2)), "laser_gun", last_key))
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

    if ACTIVE_BOSS:
        if ACTIVE_BOSS.health <= 0:
            defeated_bosses.add(ACTIVE_BOSS.type_)

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

    player_rect = pygame.Rect(
        -startx * SQUARE_SIZE + playerx - SQUARE_SIZE // 2 - RADIUS, 
        -RADIUS - SQUARE_SIZE // 2 -starty * SQUARE_SIZE + playery, 
        RADIUS*2, RADIUS*2)

    do_damage = False
    if not player_protected:
        for ghost in ghosts:
            ghost_rect = pygame.Rect(
                ghost.x * SQUARE_SIZE - startx * SQUARE_SIZE - ghost.width // 2,
                ghost.y * SQUARE_SIZE - starty * SQUARE_SIZE - ghost.height // 2,
                ghost.width, ghost.height
            )
            if ghost_rect.colliderect(player_rect):
                do_damage = True
                player_protected = True
                break
    
    if not player_protected and ACTIVE_BOSS:
        for projectile in ACTIVE_BOSS.projectiles:
            pos = projectile[0]
            rect = pygame.Rect(
                pos[0] - ACTIVE_BOSS.cam_x - PROJECTILE_RADIUS // 2,
                pos[1] - ACTIVE_BOSS.cam_x - PROJECTILE_RADIUS // 2,
                PROJECTILE_RADIUS, PROJECTILE_RADIUS
            )
            if rect.colliderect(player_rect):
                ACTIVE_BOSS.projectiles.discard(projectile)
                do_damage = True
                player_protected = True
                break

    if do_damage:
        if player_health.player_shield > 0:
            player_health.player_shield -= 10
            if player_health.player_shield < 0:
                player_health.player_health -= abs(player_health.player_shield)
                player_health.player_shield = 0
        else:
            player_health.player_health -= 10 
        player_protected = True
        targettime = time.time()
        pygame.mixer.Sound.play(pygame.mixer.Sound("sfx/player_hurt.wav"))

    if player_protected:
        targettime = time.time()
        velocity = PLAYER_SPEED * 0.6
        if not UNCAPPED_FPS:
            protected_timer += 1
            if protected_timer >= FPS * PLAYER_PROTECT:
                player_protected = False
                protected_timer = 0
                velocity = PLAYER_SPEED
                targettime = time.time()
        else:
            protected_timer += UCFD.delay
            if protected_timer >= PLAYER_PROTECT:
                player_protected = False
                protected_timer = 0
                velocity = PLAYER_SPEED
                targettime = time.time()

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
            for bullet in current_bullets:
                bullet.x, bullet.y = bullet_poscopy[bullet]
            break

        cornerdistance = (cdx - width / 2) ** 2 + (cdy - height / 2) ** 2
        if cornerdistance < ((RADIUS-1) ** 2):
            playerx = copypx
            playery = copypy
            startx = copysx
            starty = copysy
            for bullet in current_bullets:
                bullet.x, bullet.y = bullet_poscopy[bullet]
            break 

    dsx = startx - copysx
    dsy = starty - copysy

    if dsx > 0:
        if FPS:
            for bullet in current_bullets:
                bullet.x -= velocity / FPS * SQUARE_SIZE
        else:
            for bullet in current_bullets:
                bullet.x -= velocity * (delay_to - last) * SQUARE_SIZE
    elif dsx < 0:
        if FPS:
            for bullet in current_bullets:
                bullet.x += velocity / FPS * SQUARE_SIZE
        else:
            for bullet in current_bullets:
                bullet.x += velocity * (delay_to - last) * SQUARE_SIZE
    if dsy > 0:
        if FPS:
            for bullet in current_bullets:
                bullet.y -= velocity / FPS * SQUARE_SIZE
        else:
            for bullet in current_bullets:
                bullet.y -= velocity * (delay_to - last) * SQUARE_SIZE
    elif dsy < 0:
        if FPS:
            for bullet in current_bullets:
                bullet.y += velocity / FPS * SQUARE_SIZE
        else:
            for bullet in current_bullets:
                bullet.y += velocity * (delay_to - last) * SQUARE_SIZE
    


    # draw calls - a LOT of them
    window.fill((0, 0, 0))

    

    

    if not player_protected:

        pygame.draw.circle(window, (255, 255, 0), (real_round(playerx - startx * SQUARE_SIZE - (SQUARE_SIZE // 2)), real_round(playery - starty * SQUARE_SIZE - (SQUARE_SIZE // 2))), RADIUS)
    else:
        pygame.draw.circle(window, (255, 127, 80), (real_round(playerx - startx * SQUARE_SIZE - (SQUARE_SIZE // 2)), real_round(playery - starty * SQUARE_SIZE - (SQUARE_SIZE // 2))), RADIUS)


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
                # tmp
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

    
    for ghost in ghosts:
        ghost.update(startx, starty)
    
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



    if (time.time() - targettime > 10):
        if FPS:
            player_health.regen(1/FPS * (50 / 5))
        else:
            player_health.regen(UCFD.delay * (50 / 5))
    player_health.gen_healthbar(window, WIDTH)
    player_health.gen_shieldbar(window, WIDTH)
    player_score.display_score(window, WIDTH)
    player_score.display_ammo(window, WIDTH)    
    player_target.update_target(window, (0,0))
    
    for bullet in current_bullets:
        bullet.shoot(window)
        leave = False
        for ghost in ghosts:
            ghost_rect = pygame.Rect(
                ghost.x * SQUARE_SIZE - startx * SQUARE_SIZE - ghost.width // 2,
                ghost.y * SQUARE_SIZE - starty * SQUARE_SIZE - ghost.height // 2,
                ghost.width, ghost.height
            )
            if pygame.Rect.collidepoint(ghost_rect, (bullet.x, bullet.y)):
                #ghosts.remove(ghost)
                ghost.health -= 50
                current_bullets.remove(bullet)
                leave = True
                break
        if leave: break
        if bullet.check_wall_col(window, startx, starty):
            current_bullets.remove(bullet)
            break
    pygame.display.update()
    
    if UNCAPPED_FPS:
        frame_count += 1
        if frame_count % 1000 == 0:
            #print(real_round(1/(time.time() - delay_to)))
            ...
        last = delay_to
        delay_to = time.time()
        UCFD.delay = delay_to - last
    else:
        frame_count = (frame_count + 1) % FPS
        clock.tick(FPS)
        if frame_count == 0:
            #print(real_round(clock.get_fps()))
            ...