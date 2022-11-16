from character import Character

class Ghost(Character):

    # This method gives a recipe to initialize a new instance of the class
    def __init__(self, x, y):
        super().__init__(x, y, 8)

# ghost_instance = Ghost(2, 2, 100)
# print(ghost_instance.get_speed())

