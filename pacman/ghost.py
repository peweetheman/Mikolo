import random
from character import Character

class Ghost(Character):

    # This method gives a recipe to initialize a new instance of the class
    def __init__(self, x, y):
        super().__init__(x, y, x_vel=0.1, y_vel=0.1, speed=0)
        if random.random() > 0.5:  # with 50% chance
            self.x_vel = -self.x_vel
        if random.random() > 0.5:
            self.y_vel = -self.y_vel


# ghost_instance = Ghost(2, 2, 100)
# print(ghost_instance.get_speed())

