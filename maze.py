import pygame
import time
import random
import bonus
import math
from itertools import product

WHITE=(255,255,255)
GREEN=(0,170,0)
RED=(255,0,0)

class Maze(bonus.Board):
    def __init__(self, data: int):
        self.cell_size = self.margin = 30
        self.grid_size = 5
        self.cartesian = []
        self.visited = []
        self.stop = []
        self.board = []
        self.path = []
        self.solution = []
        self.web_size = data
        self.grid_size = (self.web_size * 2) + 1
        self.all_web = self.cell_size * self.grid_size
        pygame.init()
        pygame.display.set_caption("'THE MAZE GAME'")
        self.screen = pygame.display.set_mode((self.all_web + 2 * self.margin, self.all_web + 2 * self.margin))
        # self.screen.fill(WHITE)
        self.object_list = []
        self.map = [[]]
        self.background=pygame.image.load('moss.jpg')


    def add_object(self, object: bonus.Object):
        self.object_list.append(object)

    def remove_object(self, object: bonus.Object):
        self.object_list.remove(object)

    def load_background(self):
        self.background = pygame.image.load('maze.jpg')

    def refresh_screen(self):
        self.screen.blit(self.background, (0, 0))
        for obj in self.object_list:
            self.screen.blit(obj.img, (obj.object_x, obj.object_y))
            pygame.display.flip()

    def move_object_to(self, object: bonus.Object, x, y)->bool:
        if self.is_corridor(x, y, object):
            object.object_x=x
            object.object_y=y
            return True
        else:
            return False
        pass

    def is_corridor(self, x, y, object: bonus.Object):
        if not self.check_point(x, y):
            return False
        if not self.check_point(x + object.object_size, y):
            return False
        if not self.check_point(x, y + object.object_size):
            return False
        if not self.check_point(x + object.object_size, y + object.object_size):
            return False
        return True

    def check_point(self, x, y):
        map_x = math.floor(x / self.cell_size)
        map_y = math.floor(y / self.cell_size)
        pom = self.map[map_y][map_x]
        if pom == 1:
            return True
        else:
            return False

    # maze solving
    def czy_koniec(self, x, y):
        print("Checking: ",x," ",y)
        if (self.all_web - 2 * self.cell_size) == x and (self.all_web - self.cell_size) == y:
            return True
        else:
            return False

    def draw_solution(self, x,y):
        self.path.append((x,y))
        pygame.draw.circle(self.screen, WHITE, (x+15,y+15), 7)
        pygame.display.flip()
        if self.czy_koniec(x,y) == True:
            self.solution.append((x,y))
            return True
        direct = []

        # define possibilities of moves for solution
        if self.check_point(x, y-self.cell_size) and (x, y-self.cell_size) not in self.path:
            direct.append((x,y-self.cell_size))
        if self.check_point(x, y+self.cell_size) and (x, y+self.cell_size) not in self.path:
            direct.append((x, y+self.cell_size))
        if self.check_point(x-self.cell_size, y) and (x-self.cell_size, y) not in self.path:
            direct.append((x-self.cell_size, y))
        if self.check_point(x+self.cell_size, y) and (x+self.cell_size, y) not in self.path:
            direct.append((x+self.cell_size, y))
        for i,j in direct:
            if self.draw_solution(i, j)==True:
                self.solution.append((i,j))
                pygame.draw.rect(self.screen, RED, (i, j, self.cell_size, self.cell_size))
                pygame.display.flip()
                return True
        return False

    #funcion for creating a web
    def build_web(self):
        # self.screen.blit(self.background, (0, 0))
        for i in range(1, self.grid_size):
            pygame.draw.line(self.screen, WHITE, ((i * self.cell_size) + self.margin, self.margin), ((i * self.cell_size) + self.margin, self.all_web + self.margin), 1)
            pygame.draw.line(self.screen, WHITE, (self.margin, (i * self.cell_size) + self.margin), (self.all_web + self.margin, (i * self.cell_size) + self.margin), 1)
            pygame.display.flip()

    #moves for the maze generator
    def up(self, x, y):
        pygame.draw.rect(self.screen, GREEN, (x, y-2*self.cell_size, self.cell_size, self.cell_size*3))
        self.visited.append((x,y-2*self.cell_size))
        self.visited.append((x,y-self.cell_size))
        self.visited.append((x,y))
        pygame.display.flip()

    def down(self, x, y):
        pygame.draw.rect(self.screen, GREEN, (x, y, self.cell_size, self.cell_size * 3))
        self.visited.append((x, y+2*self.cell_size))
        self.visited.append((x, y+self.cell_size))
        self.visited.append((x, y))
        pygame.display.flip()

    def right(self, x, y):
        pygame.draw.rect(self.screen, GREEN, (x, y, self.cell_size * 3, self.cell_size))
        self.visited.append((x, y))
        self.visited.append((x+self.cell_size, y))
        self.visited.append((x+2*self.cell_size, y))
        pygame.display.flip()

    def left(self,x,y):
        pygame.draw.rect(self.screen, GREEN, (x-2*self.cell_size, y, self.cell_size * 3, self.cell_size))
        self.visited.append((x-2*self.cell_size, y))
        self.visited.append((x-self.cell_size, y))
        self.visited.append((x, y))
        pygame.display.flip()

    #creates cartesian board
    def make_cartesian(self):
        for i in range(self.grid_size):
            self.cartesian.append(i*self.cell_size+self.cell_size)
            self.board = list(product(self.cartesian, self.cartesian))

    #generates map of the board where the maze is already cerated
    def create_map(self):
        self.map = [[0 for x in range(self.grid_size + 2)] for y in range(self.grid_size + 2)]
        for i in range(self.grid_size + 2):
            for j in range(self.grid_size + 2):
                self.map[i][j] = 0
        for position in self.visited:
            x, y = position
            pos_x = int(x/self.cell_size)
            pos_y = int(y/self.cell_size)
            print(x, y, pos_x, pos_y)
            self.map[pos_y][pos_x] = 1
        for line in self.map:
            print(line)

    #the most important function which genarates the maze
    def draw_maze(self,x, y):
        self.screen.blit(self.background, (0, 0))
        self.stop.append((x, y))
        self.visited.append((x, y))
        while len(self.stop)>0:
            time.sleep(0.05)
            dir = []
            #define possibilities of moves
            if (x, y - 2*self.cell_size) not in self.visited and (x, y - 2*self.cell_size) in self.board:
                dir.append("up")
            if (x, y + 2*self.cell_size) not in self.visited and (x, y + 2*self.cell_size) in self.board:
                dir.append("down")
            if (x-2*self.cell_size, y) not in self.visited and (x-2*self.cell_size, y) in self.board:
                dir.append("left")
            if (x+2*self.cell_size, y) not in self.visited and (x+2*self.cell_size, y) in self.board:
                dir.append("right")
            #choose move
            if len(dir)>0:
                draw = random.choice(dir)
                if draw == "up":
                    self.up(x, y)
                    y = y - 2*self.cell_size
                    self.stop.append((x, y))
                elif draw == "down":
                    self.down(x, y)
                    y = y + 2 * self.cell_size
                    self.stop.append((x, y))
                elif draw == "left":
                    self.left(x, y)
                    x = x - 2 * self.cell_size
                    self.stop.append((x, y))
                elif draw == "right":
                    self.right(x, y)
                    x = x + 2 * self.cell_size
                    self.stop.append((x, y))
            else:
                x, y = self.stop.pop()
        pygame.draw.rect(self.screen, GREEN, (2 * self.cell_size, self.cell_size, self.cell_size, self.cell_size))
        self.visited.append((2 * self.cell_size, self.cell_size))
        self.visited.append((self.all_web - self.cell_size, self.all_web))
        pygame.draw.rect(self.screen, GREEN, (self.all_web - self.cell_size, self.all_web, self.cell_size, self.cell_size))
        pygame.image.save(self.screen, 'maze.jpg')