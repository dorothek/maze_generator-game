import pygame

#virtual class of the object in game
class Object:
    print("class Object")
    def __init__(self):
        self.object_size=0
        self.object_x=0
        self.object_y=0
        self.img=None

#interface of the board
class Board():
    def move_object_to(self, object: Object, x, y)->bool:
        pass

#end of the game
class End(Object):
    def __init__(self):
        Object.__init__(self)
        self.img = pygame.image.load('end.png')
        self.object_size = 24

    def winner(self):
        print("Congratulations! You are the winner! :) ")

#bonus cheese
class Cheese(Object):
    def __init__(self):
        Object.__init__(self)
        self.img = pygame.image.load('cheese.png')
        self.object_size = 16

#enemy cat
class Cat(Object):
    def __init__(self):
        Object.__init__(self)
        self.img = pygame.image.load('cat.png')
        self.object_size = 24