from abc import ABC, abstractmethod


class Character(ABC):
    # This method gives a recipe to initialize a new instance of the class
    def __init__(self, x, y, speed):
        self.x_pos = x
        self.y_pos = y
        self.y_vel = 0
        self.x_vel = 0
        self.speed = speed

# character_instance = Character(2, 4)
# print(character_instance.x_val)
# print(character_instance.get_speed())