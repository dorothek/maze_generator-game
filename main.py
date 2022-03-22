import bonus
import maze
import player
import pygame
import time
import random
import math

def is_collision(object1: bonus.Object, object2: bonus.Object):
    distance = math.sqrt(math.pow(object1.object_x - object2.object_x, 2) + (math.pow(object1.object_y - object2.object_y, 2)))
    if distance < 5:
        return True
    else:
        return False

#controls gameplay
def main():
    #TODO wyświetlić rules of the game
    #TODO wybór trybu gry
    #TODO jeśli single player to wybrać level

    print("Please, input the size of the maze: ")
    data = int(input())
    #maze generation
    labirynt = maze.Maze(data)
    labirynt.make_cartesian()
    labirynt.draw_maze(2 * labirynt.cell_size, 2 * labirynt.cell_size)

    #creating map of the gameboard
    labirynt.create_map()

    gamer=player.Human()
    gamer.object_x = 2 * labirynt.cell_size
    gamer.object_y = labirynt.cell_size
    labirynt.add_object(gamer)
    #add the end
    end = bonus.End()
    end.object_x=labirynt.all_web - labirynt.cell_size
    end.object_y=labirynt.all_web
    labirynt.add_object(end)
    #add cat
    cat=bonus.Cat()
    cat_add=False
    while not cat_add:
        x = random.randint(0, labirynt.all_web-cat.object_size)
        y = random.randint(0, labirynt.all_web-cat.object_size)
        cat_add=labirynt.move_object_to(cat, x, y)
    labirynt.add_object(cat)
    #calculates how many cheeses has to create in dependence of the maze size
    ser_num=int(data/2)
    for num in range(ser_num):
        ser=bonus.Cheese()
        ser_landed=False
        while not ser_landed:
            x = random.randint(0, labirynt.all_web-ser.object_size)
            y = random.randint(0, labirynt.all_web-ser.object_size)
            ser_landed=labirynt.move_object_to(ser, x, y)
        labirynt.add_object(ser)
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
        #moves
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
        #TODO sprawdzic czy zachaczył o ser, jak tak to go zjada + info o bonusie
        #TODO czy zderzenie z wrogiem jak tak to GAME OVER
        #TODO czy dotarł do końca jak tak to info o koncu gry i pytanie czy chce isc na dalszy poziom

main()
