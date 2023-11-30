from user_settings import *

SQUARE_SIZE = 60
while True:
    try:
        if WIDTH % SQUARE_SIZE != 0: raise ValueError(f"{WIDTH} % {SQUARE_SIZE} = {WIDTH % SQUARE_SIZE}, not 0")
        if HEIGHT % SQUARE_SIZE != 0: raise ValueError(f"{HEIGHT} % {SQUARE_SIZE} = {HEIGHT % SQUARE_SIZE}, not 0")
    except:
        SQUARE_SIZE += 1
    else:
        break

WALL_WIDTH = SQUARE_SIZE // 12


MAP_RADIUS = 15 # map consists of 4 adjacent MR*MR squares, blending adjacent edges together
BOSS_AREA = 5 # BA*BA square in the corners for bosses 

RADIUS = int(SQUARE_SIZE / 2) // 2
FIXED_X = FIXED_Y = False
BOUND = MAP_RADIUS * SQUARE_SIZE

PADX = PADY = False

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
PROJECTILE_RADIUS = SQUARE_SIZE * 2/5 / 2