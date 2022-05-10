import pygame

#virtual class of the object in game
class Object:
    def __init__(self):
        self.object_size=0
        self.object_x=0
        self.object_y=0
        self.img=None

    def give_xy(self):
        x=str(self.object_x)
        y=str(self.object_y)
        return x+" "+y

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

#bonus cheese
class Cheese(Object):
    def __init__(self):
        Object.__init__(self)
        self.img = pygame.image.load('cheese.png')
        self.object_size = 16

class Player(Object):
    def __init__(self):
        Object.__init__(self)

class Human(Player):
    def __init__(self):
        Player.__init__(self)
        self.img = pygame.image.load('rat.png')
        self.object_size = 24
        self.points=0