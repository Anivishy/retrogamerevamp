import pygame
import heapq

from calculated_vars import *
from wall_generation import walls_around
import colors

import random

class Ghost:
    def __init__(self, screen, type_, x, y):
        self.screen = screen
        self.type = type_

        self.x = x
        self.y = y

        self.speed = 2.5 / SQUARE_SIZE

        self.path = []


        self.ctx = x
        self.cty = y

        self.lastx = None
        self.lasty = None

        self.color = [
            colors.FOREST,
            colors.LAVA,
            colors.ICE,
            colors.SHADOW
        ][type_ - 1]

        self.full_points = self.get_full_points()
        self.unavailable = set()
        for x in range(BOSS_AREA):
            for y in range(BOSS_AREA):
                self.unavailable.add((-MAP_RADIUS + x + real_round((WIDTH / 2) / SQUARE_SIZE), -MAP_RADIUS + y + real_round(HEIGHT / 2 / SQUARE_SIZE)))
                self.unavailable.add((MAP_RADIUS - BOSS_AREA + x + real_round((WIDTH / 2) / SQUARE_SIZE), MAP_RADIUS - BOSS_AREA + y + real_round(HEIGHT / 2 / SQUARE_SIZE)))
                self.unavailable.add((-MAP_RADIUS + x + real_round((WIDTH / 2) / SQUARE_SIZE), MAP_RADIUS - BOSS_AREA + y + real_round(HEIGHT / 2 / SQUARE_SIZE)))
                self.unavailable.add((MAP_RADIUS - BOSS_AREA + x + real_round((WIDTH / 2) / SQUARE_SIZE), -MAP_RADIUS + y + real_round(HEIGHT / 2 / SQUARE_SIZE)))

    def heuristic(self, x1, y1, x2, y2):
        return (abs(x1 - x2) + abs(y1 - y2))
    
    def get_full_points(self):
        s = set()
        if self.type == 1:
            dx = -(MAP_RADIUS)
            dy = -(MAP_RADIUS)
        elif self.type == 2:
            dx = 0
            dy = -MAP_RADIUS
        elif self.type == 3:
            dx = -MAP_RADIUS
            dy = 0
        elif self.type == 4:
            dx = 0
            dy = 0
        for x in range(MAP_RADIUS):
            for y in range(MAP_RADIUS):
                s.add((x + dx + real_round(WIDTH / 2 / SQUARE_SIZE), y + dy + real_round(HEIGHT / 2 / SQUARE_SIZE)))
        return s

    def get_available(self, bx, by):
        n = set()
        walls = walls_around(int(bx), int(by))
        if ((bx, by), (bx + 1, by)) not in walls:
            n.add((bx, by - 1))
        if ((bx + 1, by), (bx + 1, by + 1)) not in walls:
            n.add((bx + 1, by))
        if ((bx, by + 1), (bx + 1, by + 1)) not in walls:
            n.add((bx, by + 1))
        if ((bx, by), (bx, by + 1)) not in walls:
            n.add((bx - 1, by))
        return n.intersection(self.full_points) - self.unavailable

    def astar(self, px, py): # TODO: ASTAR DOES NOT WORK - USE RANDOM WALK
        self.tx = px
        self.ty = py
        heap = []
        prev_distances = {}
        fp = self.get_full_points()
        #print((px, py) not in fp)
        #print((int(px), int(py)))
        if (px, py) not in fp: return
        for point in fp:
            prev_distances[point] = None
            if point != (self.x, self.y):
                heapq.heappush(heap, (float("inf"), point))
            else:
                heapq.heappush(heap, (self.heuristic(point[0], point[1], px, py), point))
            
        prev_distances[(self.x // 1, self.y // 1)] = (0, None)

        while len(heap) > 0:
            weight, start = heapq.heappop(heap)
            if start == (px, py): break
            bx, by = start
            try:
                previous = prev_distances[start][0]
            except: continue
            for point in self.get_available(bx, by).intersection(fp):
                added_distance = previous + 1
                if prev_distances[point] is None or added_distance < prev_distances[point][0]:
                    prev_distances[point] = (added_distance, start)
                    heapq.heappush(heap, (added_distance + self.heuristic(point[0], point[1], px, py), point))
        
        points = []
        current = (px, py)
        while current is not None:
            points.insert(0, current)
            try:
                current = prev_distances[current][1]
            except:
                return
        self.ctx, self.cty = points[0]
        self.path = points[1:]

    def step(self):
        surrounding = list(self.get_available(self.x // 1, self.y // 1))
        
        if len(surrounding) == 1 and surrounding[0] == (self.lastx, self.lasty):
            self.lastx = self.ctx
            self.lasty = self.cty
            self.ctx, self.cty = surrounding[0]
        else:
            if (self.lastx, self.lasty) in surrounding:
                surrounding.remove((self.lastx, self.lasty))
            self.lastx = self.ctx
            self.lasty = self.cty
            try:
                #...
                self.ctx, self.cty = random.choice(surrounding)
            except: 
                raise

    def update(self, startx, starty):
        
        dy = (self.cty - self.y)
        dx = (self.ctx - self.x)

        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance != 0:
            if UNCAPPED_FPS:
                ratio = self.speed * SQUARE_SIZE * UCFD.delay / distance
            else:
                ratio = (self.speed * SQUARE_SIZE) / FPS / distance

            if abs(dx * ratio) > abs(dx):
                self.x += dx
            else:
                self.x += dx * ratio

            if abs(dy * ratio) > abs(dy):
                self.y += dy
            else:
                self.y += dy * ratio
        else:
            self.step()

        # pygame.draw.rect(
        #     self.screen, (235, 131, 52), pygame.Rect(
        #         self.tx * SQUARE_SIZE - startx * SQUARE_SIZE,
        #         self.ty * SQUARE_SIZE - starty * SQUARE_SIZE,
        #         25,25
        #     )
        # )

        pygame.draw.rect(
            self.screen, self.color, pygame.Rect(
                self.x * SQUARE_SIZE - startx * SQUARE_SIZE,
                self.y * SQUARE_SIZE - starty * SQUARE_SIZE,
                25,25
            )
        )

        pygame.draw.rect(
            self.screen, (255, 0, 0), pygame.Rect(
                self.x * SQUARE_SIZE - startx * SQUARE_SIZE,
                self.y * SQUARE_SIZE - starty * SQUARE_SIZE,
                10,10
            )
        )


        
    
