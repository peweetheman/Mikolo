import pygame
from pygame.locals import *
import pickle

height = 600
width = 600
num_rows = 30
num_cols = 30
rect_height = height/num_rows
rect_width = width/num_cols
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(True)

grid = []  # [[False, False, False], [], ...
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        row.append(False)  # false indicates no wall
    grid.append(row)

current_pos = -1, -1
running = True
while running:
    screen.fill(color=(0, 0, 0))  # R,G,B = 0,0,0 for black background
    for i in range(num_rows):
        for j in range(num_cols):
            isFilled = grid[i][j]
            if isFilled:
                pygame.draw.rect(surface=screen, color=(0, 0, 255), rect=(j/num_cols*width, i/num_rows*height, rect_width, rect_height))

    ## loop to check for mouse action and its position ##
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ## if mouse is pressed get position of cursor ##
            pos = pygame.mouse.get_pos()
            grid[int(pos[1] / rect_height)][int(pos[0] / rect_width)] = not grid[int(pos[1] / rect_height)][int(pos[0] / rect_width)]
    if pygame.mouse.get_pressed()[0]:
        try:
            pos = pygame.mouse.get_pos()
            nearest_row = int(pos[1] / rect_height)
            nearest_col = int(pos[0] / rect_width)
            if current_pos[0] != nearest_row or current_pos[1] != nearest_col:
                grid[nearest_row][nearest_col] = not grid[nearest_row][nearest_col]
            current_pos = nearest_row, nearest_col
        except:
            pass
    pygame.display.update()
pygame.quit()

file_name = input("Enter the map name: ")
with open('./maps/' + file_name, 'wb') as f:
    pickle.dump(grid, f)