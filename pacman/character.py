from abc import ABC

class Character(ABC):
    @property
    def x(self):
        pass

    @property
    def y(self):
        pass

    # This method gives a recipe to initialize a new instance of the class
    def __init__(self):
        pass

