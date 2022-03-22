import maze
import pygame
import math

playerImg = pygame.image.load('rat.png')
playerX=2*maze.cell_size
playerY=maze.cell_size
player_size=24
move_x=0
move_y=0

schema = []

def player(x,y):
    maze.screen.blit(playerImg, (x,y))
    pygame.display.flip()

# def is_collision(obj_x, obj_y, self_x, self_y):
#     distance = math.sqrt(math.pow(obj_x - self_x, 2) + (math.pow(obj_y - self_y, 2)))
#     if distance < 20:
#         return True
#     else:
#         return False

def check_point(x,y):
    map_x=math.floor(x/board.cell_size)
    map_y=math.floor(y/board.cell_size)
    pom=board.map[map_y][map_x]
    if pom==1:
        return True
    else:
        return False

def is_corridor(x,y):
    if not check_point(x,y):
        return False
    if not check_point(x+player_size,y):
        return False
    if not check_point(x,y+player_size):
        return False
    if not check_point(x+player_size,y+player_size):
        return False
    return True

# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     #right or left move
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_RIGHT:
#                 move_x = 0.25
#             if event.key==pygame.K_LEFT:
#                 move_x = -0.25
#         if event.type==pygame.KEYUP:
#             if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
#                 move_x=0
#     #up or down move
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_DOWN:
#                 move_y = 0.25
#             if event.key==pygame.K_UP:
#                 move_y = -0.25
#         if event.type==pygame.KEYUP:
#             if event.key==pygame.K_DOWN or event.key==pygame.K_UP:
#                 move_y=0
# #chce zeby przelecialo przez cala plaszczyzne kartezjanska a jesli jest oznaczony kwadrat jako visited to pomalowalo go od nowa na zielono
#     # for i in len(maze.visited):
#     #     if (playerX,playerY)==maze.visited:
#     #         pygame.draw.rect(maze.screen, maze.GREEN, (playerX, playerY, maze.cell_size, maze.cell_size))
#     tempX = playerX+move_x
#     tempY = playerY+move_y
#     if is_corridor(tempX,tempY):
#         playerX += move_x
#         playerY += move_y
#         background = pygame.image.load('maze.jpg')
#         maze.screen.blit(background, (0, 0))
#         player(playerX, playerY)
#         pygame.display.flip()