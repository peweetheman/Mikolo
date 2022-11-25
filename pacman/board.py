import os
from object import Object
import pickle

class Board():

    def __init__(self):
        # create 2D grid of positions which can be occupied by walls
        self.grid = []
        height = 30
        width = 30
        map_name = input("Enter a map name: ")
        with open('./maps/' + map_name, 'rb') as f:
            self.grid = pickle.load(f)
        # for i in range(height):
        #     row = []
        #     for j in range(width):
        #         row.append(False)  # false indicates no wall
        #     self.grid.append(row)
        # self.grid[1][1] = True
        # self.grid[2][2] = True

