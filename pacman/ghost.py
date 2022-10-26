from character import Character

class Ghost(Character):
    @property
    def x(self):
        return self.x_pos

    @property
    def y(self):
        return self.y_pos

    # This method gives a recipe to initialize a new instance of the class
    def __init__(self, x, y, speed):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.speed = speed

