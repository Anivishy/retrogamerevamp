from user_settings import *

SQUARE_SIZE = 100

p1 = SQUARE_SIZE
p2 = SQUARE_SIZE

while True:
    if WIDTH % p1 == 0 and HEIGHT % p1 == 0:
        SQUARE_SIZE = p1
        break
    if WIDTH % p2 == 0 and HEIGHT % p2 == 0:
        SQUARE_SIZE = p2
        break
    p1 += 1
    p2 -= 1

WALL_WIDTH = SQUARE_SIZE // 12


MAP_RADIUS = 25 # map consists of 4 adjacent MR*MR squares, blending adjacent edges together
BOSS_AREA = 5 # BA*BA square in the corners for bosses 

RADIUS = int(SQUARE_SIZE / 2) // 2
FIXED_X = FIXED_Y = False
BOUND = MAP_RADIUS * SQUARE_SIZE

PADX = PADY = False

GHOST_RESPAWN = 10.0 
PLAYER_PROTECT = 3.0

BORDER_X = (BOUND - WIDTH / 2 + WALL_WIDTH / 2) / SQUARE_SIZE
if int((BOUND - WIDTH / 2) / SQUARE_SIZE) == (BOUND - WIDTH / 2) / SQUARE_SIZE:
    BORDER_X += 0.5
    PADX = True
if BORDER_X < 0:
    FIXED_X = True

BORDER_Y = (BOUND - HEIGHT / 2 + WALL_WIDTH / 2) / SQUARE_SIZE
if int((BOUND - HEIGHT / 2) / SQUARE_SIZE) == (BOUND - HEIGHT / 2) / SQUARE_SIZE:
    BORDER_Y += 0.5
    PADY = True
if BORDER_Y < 0:
    FIXED_Y = True

UNCAPPED_FPS = (FPS is None)

global UNCAPPED_DELAY
UNCAPPED_DELAY = 0

class UCFDBase:
    def __init__(self):
        self.delay = 0

UCFD = UCFDBase() # uncapped frame delay - weird class hack

PLAYER_SPEED = 5
BOSS_SPEED = PLAYER_SPEED / 5
PROJECTILE_RADIUS = SQUARE_SIZE * 1.5/5 / 2


SAFE_RADIUS = 2

import math
def real_round(d):
    r = d % 1
    if r >= 0.5: return int(math.ceil(d))
    else: return int(math.floor(d))

REGEN_DELAY = 7.5