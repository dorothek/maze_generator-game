#kontroluje cały przebieg gry
import maze
import player
import pygame
import time

# def is_collision(obj_x, obj_y, self_x, self_y):
#     distance = math.sqrt(math.pow(obj_x - self_x, 2) + (math.pow(obj_y - self_y, 2)))
#     if distance < 20:
#         return True
#     else:
#         return False

def main():
    #wyświetlić rules of the game
    #wybór trybu gry
    #jeśli single player to wybrać level

    print("Please, input the size of the maze: ")
    data = int(input())
    #maze generation
    labirynt = maze.Maze(data)
    labirynt.build_web()
    labirynt.make_cartesian()
    labirynt.draw_maze(2 * labirynt.cell_size, 2 * labirynt.cell_size)

    #creating map of the gameboard
    labirynt.create_map()

    gamer=player.Human()
    gamer.object_x = 2 * labirynt.cell_size
    gamer.object_y = labirynt.cell_size
    labirynt.add_object(gamer)
    labirynt.refresh_screen()
    #the main loop
    run = True
    while run:
        time.sleep(0.4)
        for event in pygame.event.get():
            step_size=5
            move_x = 0
            move_y = 0
            if event.type == pygame.QUIT:
                run = False
                ##########
        # right or left move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = step_size
                if event.key == pygame.K_LEFT:
                    move_x = -step_size
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        move_x = 0
        # up or down move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    move_y = step_size
                if event.key == pygame.K_UP:
                    move_y = -step_size
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    move_y = 0
            if move_x !=0 or move_y !=0:
                labirynt.move_object_to(gamer, gamer.object_x+move_x, gamer.object_y+move_y)
                labirynt.refresh_screen()

main()
