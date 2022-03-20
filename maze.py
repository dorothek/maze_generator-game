import pygame
import time
import random
from itertools import product

print("Hello in 'THE MAZE GAME'! Please, input the size of the labirynth: ")
web_size=5 #TODO: zrobić input tak, żeby użytkownik sam wpisywał liczbe 2-11 +walidacja
#TODO albo pomysł z podziałem na levele 1-10, wtedy różne wielkości kratek

WHITE=(255,255,255)
GREEN=(0,204,102)
RED=(255,20,0)
BROWN=(165,42,42)

cell_size=30
grid_size=(web_size*2)+1
#margin which i left from the border in window
margin = cell_size
all_web = cell_size * grid_size

pygame.init()
pygame.display.set_caption("'THE MAZE GAME'")

screen = pygame.display.set_mode((all_web + 2*margin, all_web + 2*margin))
screen.fill(BROWN)

# pygame.draw.rect(screen, RED, (margin, margin, all_web, all_web))

cartesian=[]
visited=[]
stop=[]

#funcion for creating a web
def build_web():
    for i in range(1, grid_size):
        pygame.draw.line(screen, WHITE, ((i * cell_size) + margin, margin), ((i * cell_size) + margin, all_web + margin), 1)
        pygame.draw.line(screen, WHITE, (margin, (i * cell_size) + margin), (all_web + margin, (i * cell_size) + margin), 1)
        pygame.display.flip()

build_web()

#moves for the maze generator
def up(x,y):
    pygame.draw.rect(screen, GREEN, (x, y-2*cell_size, cell_size, cell_size*3))
    visited.append((x,y-2*cell_size))
    visited.append((x,y-cell_size))
    visited.append((x,y))
    pygame.display.flip()
def down(x,y):
    pygame.draw.rect(screen, GREEN, (x, y, cell_size,cell_size * 3))
    visited.append((x, y+2*cell_size))
    visited.append((x, y+cell_size))
    visited.append((x, y))
    pygame.display.flip()
def right(x,y):
    pygame.draw.rect(screen, GREEN, (x, y, cell_size * 3, cell_size))
    visited.append((x, y))
    visited.append((x+cell_size, y))
    visited.append((x+2*cell_size, y))
    pygame.display.flip()
def left(x,y):
    pygame.draw.rect(screen, GREEN, (x-2*cell_size, y, cell_size * 3, cell_size))
    visited.append((x-2*cell_size, y))
    visited.append((x-cell_size, y))
    visited.append((x, y))
    pygame.display.flip()

for i in range(grid_size):
    cartesian.append(i*cell_size+cell_size)

#generates map of the board and fill it with 0 (in that moment everything is the wall)
map=[[0 for x in range(grid_size+2)] for y in range(grid_size+2)]
for i in range(grid_size+2):
    for j in range(grid_size+2):
        map[i][j]=0

print(map)
#wszystkie współrzedne na planszy
board=list(product(cartesian,cartesian))
# print(board)

def draw_maze(x, y):
    stop.append((x, y))
    visited.append((x, y))
    while len(stop)>0:
        # time.sleep(0.1)
        dir = []
        #define possibilities of moves
        if (x, y - 2*cell_size) not in visited and (x, y - 2*cell_size) in board:
            dir.append("up")
        if (x, y + 2*cell_size) not in visited and (x, y + 2*cell_size) in board:
            dir.append("down")
        if (x-2*cell_size, y) not in visited and (x-2*cell_size, y) in board:
            dir.append("left")
        if (x+2*cell_size, y) not in visited and (x+2*cell_size, y) in board:
            dir.append("right")

        if len(dir)>0:
            draw=random.choice(dir)
            if draw=="up":
                up(x, y)
                # visited.append((x,y))
                y = y - 2*cell_size
                # visited.append((x, y))
                # visited.append((x,y-cell_size))
                stop.append((x, y))
            elif draw=="down":
                down(x, y)
                # visited.append((x, y))
                y = y + 2 * cell_size
                # visited.append((x, y))
                # visited.append((x, y + cell_size))
                stop.append((x, y))
            elif draw=="left":
                left(x, y)
                # visited.append((x, y))
                x = x - 2 * cell_size
                # visited.append((x, y))
                # visited.append((x-cell_size, y))
                stop.append((x, y))
            elif draw=="right":
                right(x, y)
                # visited.append((x, y))
                x = x + 2 * cell_size
                # visited.append((x, y))
                # visited.append((x + cell_size, y))
                stop.append((x, y))
        else:
            x,y=stop.pop()
    pygame.image.save(screen, 'maze.jpg')

def test_map(map):
    for i in range(grid_size + 2):
        map[i][i] = 1

def dig_corridor(map,visited):
    for position in visited:
        x,y=position
        pos_x = int(x/cell_size)
        pos_y = int(y/cell_size)
        print(x,y,pos_x,pos_y)
        map[pos_y][pos_x]=1

pygame.draw.rect(screen,GREEN,(2*cell_size,cell_size,cell_size,cell_size))
visited.append((2*cell_size,cell_size))
visited.append((all_web-cell_size,all_web))
pygame.draw.rect(screen,GREEN,(all_web-cell_size,all_web,cell_size,cell_size))
draw_maze(2*cell_size,2*cell_size)

dig_corridor(map,visited)
#test_map(map)
for line in map:
    print(line)