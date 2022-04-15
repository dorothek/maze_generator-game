import bonus
import maze
import player
import pygame
import time
import random
import math
import keyboard
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


def is_collision(object1: bonus.Object, object2: bonus.Object):
    distance = math.sqrt(math.pow(object1.object_x - object2.object_x, 2) +
                         (math.pow(object1.object_y - object2.object_y, 2)))
    if distance < 10:
        return True
    else:
        return False

def retry():
    messagebox.askretrycancel('retry', 'Failed! want to try again?')

def again():
    if messagebox.askretrycancel('again', 'You won! Do you want to play again?')==False:
        quit()

# controls gameplay
def start_game():
    if messagebox.askyesno('Yes|No', 'Hello! Do you want to start "the maze game"?')==True:
        messagebox.showinfo("Say Hello", "Welcome to the maze game!")
    else:
        messagebox.showinfo("Say Goodbay", "Ok, see you next time")
        quit()

def esc_game():
    if messagebox.askyesno('Yes|No', 'Hello! Do you want to continue?')==False:
        messagebox.showinfo("See you", "Ok, see you next time")
        quit()

def show_rules():
    messagebox.showinfo("Rules", "You are a mouse in the the maze. The aim of the game is to go out of the maze,"
                                 " as fast as it is possible for you. You also can get extra-bonus points if you grab"
                                 " the cheese. If you want to end the game before you reach the exit, just press escape key."
                                 " Good luck!")

def choose_mode():
    if messagebox.askyesno('Yes|No', 'Do you want to play alone?') == True:
        if messagebox.askyesno('Yes|No', 'Are you human?') == True:
            messagebox.showinfo("Start human", "Human player mode has started")
        else:
            messagebox.showinfo("Start AI", "AI player mode has started")
    else:
        messagebox.showinfo("Start human vs AI", "Double player mode has started")


def main():
    ws = Tk()
    ws.title('Maze Game')
    ws.withdraw()
    start_game()
    # show_rules()
    answer1 = simpledialog.askinteger("Input", "Input the size of the maze? (between 3 and 11)", parent=ws,
                                      minvalue=3, maxvalue=11)
    data = int(answer1)
    choose_mode()
    show_rules()
    # maze generation
    labirynt = maze.Maze(data)
    labirynt.make_cartesian()
    labirynt.draw_maze(2 * labirynt.cell_size, 2 * labirynt.cell_size)

    # creating map of the gameboard
    labirynt.create_map()
    labirynt.load_background()
    gamer = player.Human()
    gamer.object_x = 2 * labirynt.cell_size
    gamer.object_y = labirynt.cell_size
    labirynt.add_object(gamer)
    # add the end
    end = bonus.End()
    end.object_x = labirynt.all_web - labirynt.cell_size
    end.object_y = labirynt.all_web
    labirynt.add_object(end)
    # calculates how many cheeses has to create in dependence of the maze size
    ser_num = int(data/2)
    cheeses=[]
    for num in range(ser_num):
        ser = bonus.Cheese()
        ser_landed = False
        while not ser_landed:
            x = random.randint(0, labirynt.all_web-ser.object_size)
            y = random.randint(0, labirynt.all_web-ser.object_size)
            ser_landed = labirynt.move_object_to(ser, x, y)
            labirynt.add_object(ser)
            cheeses.append(ser)
    labirynt.refresh_screen()

    # the main loop
    run = True
    while run:
        time.sleep(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        step_size = 2
        move_x = 0
        move_y = 0


        is_down_pressed = keyboard.is_pressed("down")
        is_up_pressed = keyboard.is_pressed("up")
        is_left_pressed = keyboard.is_pressed("left")
        is_right_pressed = keyboard.is_pressed("right")

        if(keyboard.is_pressed("esc")):
            esc_game()
        # moves
        if is_right_pressed:
            move_x = step_size
        elif is_left_pressed:
            move_x = -step_size

        # up or down move
        elif is_down_pressed:
            move_y = step_size
        elif is_up_pressed:
            move_y = -step_size

        if move_x != 0 or move_y != 0:
            labirynt.move_object_to(
                gamer, gamer.object_x+move_x, gamer.object_y+move_y)
            for ser in cheeses:
                if is_collision(ser, gamer)==True:
                    cheeses.remove(ser)
                    labirynt.remove_object(ser)
            labirynt.refresh_screen()
            if is_collision(end, gamer)==True:
                del labirynt
                again()
                return
while True:
    main()
