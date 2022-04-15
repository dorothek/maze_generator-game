import pygame
import bonus

class Player(bonus.Object):
    def __init__(self):
        bonus.Object.__init__(self)

    print("class Player")

class Human(Player):
    def __init__(self):
        Player.__init__(self)
        self.img = pygame.image.load('rat.png')
        self.object_size = 24
        self.points=0

class Computer(Player):
    print("I am computer player")
#TODO tu bedzie automatycznie rozwiazywał labirynt