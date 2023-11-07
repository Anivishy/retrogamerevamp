import random
import pygame
import os
from heapq import *

class Renderer:
    def __init__(self, width, height, size):
        pygame.init()
        self._game_size = size
        self._width = width
        self._height = height
        self._screen = pygame.display.set_mode((self._width, self._height), pygame.RESIZABLE)
        self._clock = pygame.time.Clock()
        self._game_over = False
        self._objects = []
        self.walls = []
        self._points = []
        self._ghosts = []
        self._powerups = []
        self._open_mouth = pygame.USEREVENT
        self._pacman = None
        self._hungry_pacman = False
        self._hungry_event = pygame.USEREVENT + 1
        self.paused = False
    
    def tick(self, fps):
        pygame.time.set_timer(self._open_mouth, 400)

        while not self._game_over:
            for object in self._objects:
                if not self.paused:
                    object.tick()
                object.draw()
            
            pygame.display.update()
            self._clock.tick(fps)
            self._screen.fill((0, 0, 0))
            self._handle_events()
    
    def new_object(self, object):
        self._objects.append(object)
    
    def new_wall(self, object):
        self._objects.append(object)
        self.walls.append(object)
    
    def start_hungry_timer(self):
        pygame.time.set_timer(self._hungry_event, 10000)
    
    def start_hungry_pacman(self):
        self._hungry_pacman = True

        for ghost in self._ghosts:
            ghost.afraid = True
            ghost.get_random_path(ghost)

        self.start_hungry_timer()

    
    def new_point(self, object):
        self._points.append(object)
        self._objects.append(object)

    def new_pacman(self, pacman):
        self._objects.append(pacman)
        self._pacman = pacman
    
    def get_pacman_position(self):
        return self._pacman.get_position()
    
    def new_ghost(self, ghost):
        self._objects.append(ghost)
        self._ghosts.append(ghost)
    
    def new_powerup(self, object):
        self._objects.append(object)
        self._powerups.append(object)

    def screen_to_maze_coordinates(self, coordinates):
        return int(coordinates[0] / self._game_size), int(coordinates[1] / self._game_size)
    
    def maze_to_screen_coordinates(self, coordinates):
        return coordinates[0] * self._game_size, coordinates[1] * self._game_size

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game_over == True
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = not self.paused
        
            if event.type == self._open_mouth:
                if self._pacman is None:
                    break
                else:
                    self._pacman.open = not self._pacman.open
            
            if event.type == self._hungry_event:
                self._hungry_pacman = False

                for ghost in self._ghosts:
                    ghost.afraid = False
        
        key_pressed = pygame.key.get_pressed()
        
        if not self.paused:
            if key_pressed[pygame.K_UP]:
                self._pacman.change_direction(1)
            elif key_pressed[pygame.K_DOWN]:
                self._pacman.change_direction(2)
            elif key_pressed[pygame.K_LEFT]:
                self._pacman.change_direction(3)
            elif key_pressed[pygame.K_RIGHT]:
                self._pacman.change_direction(4)


class GameObject:
    def __init__(self, surface, x, y, size, color, is_circle, is_image, image = None):
        self._size = size
        self._renderer = surface
        self._surface = surface._screen
        self.x = x
        self.y = y
        self._color = color
        self._circle = is_circle
        self._is_image = is_image
        self._image = image
        self._shape = pygame.Rect(self.x, self.y, size, size)
    
    def draw(self):
        if self._is_image:
            rect = self._image.get_rect()
            rect.topleft = (self.x, self.y)
            self._surface.blit(self._image, rect)
        elif self._circle:
            pygame.draw.circle(self._surface, self._color, (self.x, self.y), self._size)
        else:
            pygame.draw.rect(self._surface, self._color, (self.x, self.y, self._size, self._size))
    
    def get_position(self):
        return (self.x , self.y)
    
    def set_position(self, x, y):
        self.x = x
        self.y = y
    
    def get_shape(self):
        return pygame.Rect(self.x , self.y, self._size, self._size)

    def tick(self):
        pass

class MovingObject(GameObject):
    # 0 = None, 1 = Up, 2 = Down, 3 = Left, 4 = Right
    def __init__(self, surface, x, y, size, color, is_circle):
        super().__init__(surface, x, y, size, color, is_circle, False)
        self.directions = [360, 90, -90, 180, 0]
        self.direction = 0
        self.direction_buffer = 0
        self.previous_direction = 0
        self.location = []
    
    def change_direction(self, new_direction):
        self.direction = new_direction
        self.direction_buffer = new_direction

        if not self.check_move(new_direction)[0]:
            self.set_position(self.check_move(new_direction)[1][0], self.check_move(new_direction)[1][1])

    def next_location(self):
        if len(self.location) > 0:
            return self.location.pop(0)
        else:
            return None
     
    def can_move(self, new_position):
        object_perimeter = pygame.Rect(new_position[0], new_position[1], self._size, self._size)
        collides = False
        walls = self._renderer.walls

        for wall in walls:
            if object_perimeter.colliderect(wall.get_shape()):
                collides = True
                break
        return collides
    
    
    def check_move(self, direction):
        end_point = (0, 0)

        if direction == 0:
            return False, end_point
        elif direction == 1:
            end_point = (self.x, self.y - 1)
        elif direction == 2:
            end_point = (self.x, self.y + 1)
        elif direction == 3:
            end_point = (self.x - 1, self.y)
        elif direction == 4:
            end_point = (self.x + 1, self.y)
        
        return self.can_move(end_point), end_point

class Pacman(MovingObject):
    def __init__(self, surface, x, y, size):
        super().__init__(surface, x, y, size, None, False)
        self.last_position = (0, 0)
        self.open_mouth = pygame.image.load('Images/pacmanOpen.png').convert_alpha()
        self.closed_mouth = pygame.image.load('Images/pacmanClosed.png').convert_alpha()
        self.image = self.open_mouth
        self.open = True
    
    def tick(self):
        if self.x < 0:
            self.x = self._renderer._width
        
        if self.x > self._renderer._width:
            self.x = 0

        self.point_pickup()
        self.handle_ghosts()
    
    def draw(self):
        if self.open:
            self.image = self.open_mouth
        else:
            self.image = self.closed_mouth
        self.image = pygame.transform.rotate(self.image, self.directions[self.direction])
        rect = self.image.get_rect()
        rect.center = (self.x + 14, self.y + 14)
        self._surface.blit(self.image, rect)
    
    def point_pickup(self):
        collision_rect = pygame.Rect(self.x, self.y, self._size, self._size)
        points = self._renderer._points
        objects = self._renderer._objects
        points_reached = None
        for point in points:
            collision = collision_rect.colliderect(point.get_shape())
            if collision and point in objects:
                objects.remove(point)
                # Change score in future
                points_reached = point
        
        if points_reached:
            points.remove(points_reached)
        
        if len(self._renderer._points) == 0:
            #end game
            pass

        for powerup in self._renderer._powerups:
            collision = collision_rect.colliderect(powerup.get_shape())
            if collision and powerup in objects:
                objects.remove(powerup)
                self._renderer.start_hungry_pacman()
            
    
    def handle_ghosts(self):
        collision_rect = pygame.Rect(self.x, self.y, self._size, self._size)
        ghosts = self._renderer._ghosts
        objects = self._renderer._objects
        for ghost in ghosts:
            collision = collision_rect.colliderect(ghost.get_shape())
            if collision and ghost in objects and not ghost.fleeing:
                #ghost_position = ghost.get_position()
                ghost.fleeing = True
                #ghost.set_position((ghost_position[0] // 32 * 32), (ghost_position[1] // 32 * 32))
                ghost.back_to_spawn(ghost)
        
    
class Ghost(MovingObject):
    def __init__(self, surface, x, y, size, controller, color):
        super().__init__(surface, x, y, size, None, False)
        self.controller = controller
        self.color = color
        self.state = 0
        self.fleeing_image_states = [pygame.image.load(f"Images/eyesUp.png").convert(),
                                     pygame.image.load(f"Images/eyesDown.png").convert(),
                                     pygame.image.load(f"Images/eyesLeft.png").convert(),
                                     pygame.image.load(f"Images/eyesRight.png").convert(),
                                     pygame.image.load(f"Images/scaredGhost.png").convert()]

        self.regular_image_states = [pygame.image.load(f"Images/{color}Up.png").convert(),
                             pygame.image.load(f"Images/{color}Down.png").convert(),
                             pygame.image.load(f"Images/{color}Left.png").convert(),
                             pygame.image.load(f"Images/{color}Right.png").convert(),
                             pygame.image.load(f"Images/scaredGhost.png").convert()]
        self.target = None
        self.afraid = False
        self.fleeing = False
        self.fleeing_first = True

    
    def target_reached(self):
        if (self.x, self.y) == self.target:
            if self.fleeing and not self.fleeing_first:
                self.fleeing_first = True

            if self.distance_to_pacman() < 6 and not self.fleeing and not self.afraid:
                self.get_path_to_pacman(self)
            #else:
                #if self.afraid and not self.fleeing:
                    #self.get_random_path(self)
            self.target = self.next_location()
        self.direction = self.get_next_direction()
    
    def distance_to_pacman(self):
        pacman_location = self._renderer.get_pacman_position()
        ghost_position = self.get_position()
        return (((pacman_location[0] // 32) - (ghost_position[0] // 32)) ** 2 + ((pacman_location[1] // 32) - (ghost_position[1] // 32)) ** 2) ** 0.5

    def new_path(self, new_path):
        self.location = []
        for direction in new_path:
            self.location.append(direction)
        self.target = self.next_location()
    
    def new_fleeing_path(self, new_path):
        current_target = self.target if self.target else None
        self.location = []
        
        if current_target:
            self.location.append(current_target)
            self.fleeing_first = False

        for direction in new_path:
            self.location.append(direction)
        self.target = self.next_location()
    
    def get_next_direction(self):
        if self.target is None and not self.fleeing:
            if self.distance_to_pacman() <= 6:
                self.get_path_to_pacman(self)
            else:
                self.get_random_path(self)
            return 0
        elif self.target is None and self.fleeing:
            self.fleeing = False
            self.get_random_path(self)
            return 0

        dx = self.target[0] - self.x
        dy = self.target[1] - self.y
        #print(f"{dy} {dx} {self.target} ({self.x}, {self.y})")

        if dx == 0:
            if dy < 0:
                return 1
            else:
                return 2
        if dy == 0:
            if dx < 0:
                return 3
            else:
                return 4
        
        self.get_random_path(self)
        return 0
    
    def get_path_to_pacman(self, ghost):
        pacman_position = self._renderer.screen_to_maze_coordinates(ghost._renderer.get_pacman_position())
        ghost_position = self._renderer.screen_to_maze_coordinates(ghost.get_position())
        path = self.controller.find_path((ghost_position[1], ghost_position[0]), (pacman_position[1], pacman_position[0]))
        translated_path = [self._renderer.maze_to_screen_coordinates(point) for point in path]
        ghost.new_path(translated_path)
    
    def get_random_path(self, ghost):
        ghost_position = self._renderer.screen_to_maze_coordinates(ghost.get_position())
        path = self.controller.random_path((ghost_position[1], ghost_position[0]))
        translated_path = [self._renderer.maze_to_screen_coordinates(point) for point in path]
        ghost.new_path(translated_path)
        
    def auto_move(self, direction, speed):
        if direction == 1:
            self.set_position(self.x, self.y - speed)
            self.state = 0
        elif direction == 2:
            self.set_position(self.x, self.y + speed)
            self.state = 1
        elif direction == 3:
            self.set_position(self.x - speed, self.y)
            self.state = 2
        elif direction == 4:
            self.set_position(self.x + speed, self.y)
            self.state = 3
        
        if self.afraid and not self.fleeing:
            self.state = 4

    def back_to_spawn(self, ghost):
        ghost_position = self._renderer.screen_to_maze_coordinates(ghost.target if ghost.target else (ghost.x, ghost.y))
        path = self.controller.find_path((ghost_position[1], ghost_position[0]), (9, 9))
        translated_path = [self._renderer.maze_to_screen_coordinates(point) for point in path]
        ghost.new_fleeing_path(translated_path)
        self.fleeing = True

    
    def tick(self):
        #print(self.location[-1] if self.location else None)
        self.target_reached()

        if not self.fleeing_first:
            if int(self.x) == self.x and int(self.y) == self.y:
                self.fleeing_first = True

        if self.fleeing and self.fleeing_first:
            speed = 1
        else:
            speed = 0.5
        self.auto_move(self.direction, speed)

    def draw(self):
        if self.fleeing:
            image = self.fleeing_image_states[self.state]
        else:
            image = self.regular_image_states[self.state]

        rect = image.get_rect()
        rect.center = (self.x + 16, self.y + 16)
        self._surface.blit(image, rect)
    

class Wall(GameObject):
    def __init__(self, surface, x, y, size, image):
        super().__init__(surface, x * size, y * size, size, None, False, True, image)

class Point(GameObject):
    def __init__(self, surface, x, y):
        super().__init__(surface, x, y, 4, (255, 255, 0), True, False)

class Powerup(GameObject):
    def __init__(self, surface, x, y):
        super().__init__(surface, x, y, 8, (255, 255, 255), True, False)

class Controller:
    def __init__(self):
        self.maze = []
        self.point_spaces = []
        self.powerup_spaces = []
        self.valid_spaces = []
        self.ghost_locations = []

# Fix walls with 1 side
        self.ascii_maze = [
            "hbbbbbbbbmbbbbbbbbi",
            "a        a        a",
            "aOec ebc f ebc ecOa",
            "a                 a",
            "a ec g ebmbc g ec a",
            "a    a   a   a    a",
            "kbbi nbc f ebo hbbj",
            "pppa a       a appp",
            "bbbj f hb bi f kbbb",
            "       a  Ga       ",
            "bbbi g kbbbj g hbbb",
            "pppa a       a appp",
            "hbbj f ebmbc f kbbi",
            "a        a  G     a",
            "a ei ebc f ebc hc a",
            "aO a           a Oa",
            "nc f g ebmbc g f eo",
            "a    a   a   a    a",
            "a ebblbc f eblbbc a",
            "a     G       G   a",
            "kbbbbbbbbbbbbbbbbbj",
        ]

        self.size = (0, 0)
        self.convert_maze()
    
    def random_path(self, start):
        end = random.choice(self.valid_spaces)
        return self.find_path(start, (end[1], end[0]))

    def find_path(self, start, end):

        def heuristic(a, b):
            return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

        adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        closed_set = set()
        parents = {}
        g_score = {start : 0}
        f_score = {start : heuristic(start, end)}
        priority_queue = []

        heappush(priority_queue, (f_score[start], start))

        while priority_queue:
            node = heappop(priority_queue)[1]

            if node == end:
                path = []
                while node in parents:
                    path.append((node[1], node[0]))
                    node = parents[node]
                return path[::-1]
            
            closed_set.add(node)
            for x, y in adjacent:
                neighbor = node[0] + x, node[1] + y
                score = g_score[node] + heuristic(node, neighbor)
                if 0 <= neighbor[0] < len(self.maze):
                    if 0 <= neighbor[1] < len(self.maze[0]):
                        if self.maze[neighbor[0]][neighbor[1]] != 1:
                            continue
                    else:
                        continue
                else:
                    continue
                if neighbor in closed_set and score >= g_score.get(neighbor, 0):
                    continue
                if score < g_score.get(neighbor, 0) or neighbor not in [x[1] for x in priority_queue]:
                    parents[neighbor] = node
                    g_score[neighbor] = score
                    f_score[neighbor] = score + heuristic(neighbor, end)
                    heappush(priority_queue, (f_score[neighbor], neighbor))
        return []

        


    def convert_maze(self):
        for x, row in enumerate(self.ascii_maze):
            self.size = (len(row), x + 1)
            current_row = []
            for y, column in enumerate(row):
                if column == 'G':
                    self.ghost_locations.append((y, x))
                if column == 'O':
                    self.powerup_spaces.append((y, x))

                if column == 'P':
                    pass
                elif column != ' ':
                    current_row.append(column)
                else:
                    current_row.append(1)
                    self.point_spaces.append((y, x))
                    self.valid_spaces.append((y, x))
                    if column == 'O':
                        self.powerup_spaces.append((y, x))
            self.maze.append(current_row)
    
class Game:

    def start_game(self):
        SIZE = 32
        new_game = Controller()
        game_size = new_game.size
        new_renderer = Renderer(game_size[0] * SIZE, game_size[1] * SIZE, SIZE)

        wall_images = [pygame.image.load('Images/wall1.png').convert(), 
                   pygame.image.load('Images/wall2.png').convert(),
                   pygame.image.load('Images/wall3.png').convert(), 
                   pygame.image.load('Images/wall4.png').convert(),
                   pygame.image.load('Images/wall5.png').convert(), 
                   pygame.image.load('Images/wall6.png').convert(),
                   pygame.image.load('Images/wall7.png').convert(), 
                   pygame.image.load('Images/wall8.png').convert(),
                   pygame.image.load('Images/wall9.png').convert(), 
                   pygame.image.load('Images/wall10.png').convert(),
                   pygame.image.load('Images/wall11.png').convert(), 
                   pygame.image.load('Images/wall12.png').convert(),
                   pygame.image.load("Images/wall13.png").convert(),
                   pygame.image.load("Images/wall14.png").convert(),
                   pygame.image.load('Images/wall15.png').convert(),
                   pygame.image.load('Images/wall16.png').convert()]

        for x, row in enumerate(new_game.maze):
            for y, column in enumerate(row):
                if column != 1 and column != 'G' and column != 'O':
                    print(column)
                    new_renderer.new_wall(Wall(new_renderer, y, x, SIZE, wall_images[ord(column) - 97]))

        ghost_colors = ['pink', 'orange', 'blue', 'red']
    
        for location in new_game.point_spaces:
            coordinates = new_renderer.maze_to_screen_coordinates(location)
            point = Point(new_renderer, coordinates[0] + SIZE // 2, coordinates[1] + SIZE // 2)
            new_renderer.new_point(point)
    
        for location in new_game.powerup_spaces:
            coordinates = new_renderer.maze_to_screen_coordinates(location)
            point = Powerup(new_renderer, coordinates[0] + SIZE // 2, coordinates[1] + SIZE // 2)
            new_renderer.new_powerup(point)

        for x, spawn in enumerate(new_game.ghost_locations):
            coordinates = new_renderer.maze_to_screen_coordinates(spawn)
            ghost = Ghost(new_renderer, coordinates[0], coordinates[1], SIZE, new_game, ghost_colors[x])
            new_renderer.new_ghost(ghost)

        pacman = Pacman(new_renderer, SIZE, SIZE, SIZE - 2)
        new_renderer.new_pacman(pacman)
        new_renderer.tick(60)

new_game = Game()
new_game.start_game()
            
        
    
