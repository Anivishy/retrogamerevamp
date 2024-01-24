from calculated_vars import *
from user_settings import *
import random

import time
if CONSTANT_SEED:
    seed = 1706076342
else:
    seed = int(time.time())

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

walls_to_remove = set()
x_off = int((WIDTH / SQUARE_SIZE) / 2)
y_off = int((HEIGHT / SQUARE_SIZE) / 2)
for x in range(-SAFE_RADIUS, SAFE_RADIUS+1):
    for y in range(-SAFE_RADIUS, SAFE_RADIUS+1):
        walls_to_remove.add(((x + x_off, y + y_off), (x + x_off, y + y_off + 1)))
        walls_to_remove.add(((x + x_off, y + y_off), (x + x_off + 1, y + y_off)))


def create_protected(from_x, from_y):
    protected = set()
    if abs(from_x) >= int(BORDER_X) - 1:
        if from_x < 0:
            for y in range(int(from_y - 1), int(from_y + (HEIGHT // SQUARE_SIZE) + 2)):
                protected.add(
                    ((int(-BORDER_X), y), (int(-BORDER_X), y + 1))
                )
        else:
            for y in range(int(from_y - 1), int(from_y + int(HEIGHT // SQUARE_SIZE) + 2)):
                protected.add(
                    ((int(BORDER_X) + WIDTH // SQUARE_SIZE + 1, y), (int(BORDER_X) + WIDTH // SQUARE_SIZE + 1, y + 1))
                )

    if abs(from_y) >= int(BORDER_Y) - 2:
        if from_y < 0:
            for x in range(int(from_x - 1), int(from_x + int(WIDTH // SQUARE_SIZE) + 2)):
                protected.add(
                    ((x, int(-BORDER_Y)), (x + 1, int(-BORDER_Y)))
                )
        else:
            for x in range(int(from_x - 1), int(from_x + int(WIDTH // SQUARE_SIZE) + 2)):
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
            rgen = random.Random(seed + (from_x + x) * SQUARE_SIZE + (from_y + y))
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
            rgen = random.Random(seed + (from_x + x) * SQUARE_SIZE + (from_y + y))
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

def walls_around(point_x, point_y):
    walls = set()
    protected = create_protected(point_x, point_y)

    scan = 2

    for x in range(-scan, scan + 1):
        for y in range(-scan, scan + 1):
            point = ((point_x + x), (point_y + y))
            rgen = random.Random(seed + (point_x + x) * SQUARE_SIZE + (point_y + y))
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
    for x in range(-scan, scan + 2):
        for y in range(-scan, scan + 2):
            point = ((point_x + x), (point_y + y))
            rgen = random.Random(seed + (point_x + x) * SQUARE_SIZE + (point_y + y))
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
    return walls - walls_to_remove

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
    else:
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

    p = set()
    new_walls = set()
    if direction == 1:
        for wall in walls:
            if wall[0][0] != fromx + 3 + (WIDTH // SQUARE_SIZE) and wall[1][0] != fromx + 3 + (WIDTH // SQUARE_SIZE):
                new_walls.add(wall)
        for y in range(-3, HEIGHT // SQUARE_SIZE + 3):
            point = ((tox - 2), (toy + y))
            p.add(point)
            rgen = random.Random(seed + (tox - 2) * SQUARE_SIZE + (toy + y))
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
            p.add(point)
            rgen = random.Random(seed + (tox + WIDTH / SQUARE_SIZE + 2) * SQUARE_SIZE + (toy + y))
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
            p.add(point)
            rgen = random.Random(seed + (tox + x) * SQUARE_SIZE + (toy - 2))
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
            p.add(point)
            rgen = random.Random(seed + (tox + x) * SQUARE_SIZE + (toy + HEIGHT / 2 + 2))
            threshold = rgen.randint(15, 35) / 100
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] + 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] + 1)])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0] - 1, point[1])])))
            if rgen.random() < threshold:
                new_walls.add(tuple(sorted([point, (point[0], point[1] - 1)])))
    print(new_walls)
    new_walls -= boss_zones
    new_walls |= protected
    
    for x in range(int(bxl) - 1, int(bxr) + 1):
        for y in range(int(byt) - 1, int(byb) + 1):
            #print(x, y)
            point = ((x), (y))
            rgen = random.Random(seed + (x) * SQUARE_SIZE + (y))
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

