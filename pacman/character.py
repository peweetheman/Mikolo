from abc import ABC, abstractmethod


class Character(ABC):
    # This method gives a recipe to initialize a new instance of the class
    def __init__(self, x, y, x_vel=0, y_vel=0, speed=0):
        self.x_pos = x
        self.y_pos = y
        self.y_vel = y_vel         # current speed in the y direction
        self.x_vel = x_vel         # current speed in the x direction
        self.max_speed = speed # how fast it can move

# character_instance = Character(2, 4)
# print(character_instance.x_val)
# print(character_instance.get_speed())