from object import Object

class Board():

    def __init__(self):
        # create 2D grid of positions which can be occupied by walls
        self.grid = []
        for i in range(20):
            row = []
            for j in range(30):
                row.append(False)  # false indicates no wall
            self.grid.append(row)

