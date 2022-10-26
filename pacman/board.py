from object import Object
from ghost import Ghost

init_ghost_speed = 2

class Board():

    def __init__(self):
        self.objects = [[]]
        for i in range(5):
            Ghost( ,init_ghost_speed)