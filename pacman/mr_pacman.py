from character import Character

class Pacman(Character):
    # This method gives a recipe to initialize a new instance of the class
    def __init__(self, x, y):
        super().__init__(x, y, x_vel=-0.0, y_vel=0.0, speed=10.0)

