import maze
import pygame
import bonus

class Player(bonus.Object):

    print("class Player")

class Human(Player):
    def __init__(self):
        self.img = pygame.image.load('rat.png')
        self.object_size = 24
        self.move_x = 0
        self.move_y = 0


    print("I am human player")

class Computer(Player):
    print("I am computer player")
#tu bedzie automatycznie rozwiazywał labirynt