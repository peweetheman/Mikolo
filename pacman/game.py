import pygame
from pygame.locals import *
from mr_pacman import Pacman
from ghost import Ghost
from board import Board
import time

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PACMAN")

mr_pacman = Pacman(x=width/2, y=height/4)
num_ghosts = 4
ghosts = []  # [Ghost_instance_1, Ghost_instance_2, .... ]
for i in range(4):
    ghosts.append(Ghost(300 + i * 20, 168))

board = Board()
num_rows = len(board.grid)
num_cols = len(board.grid[0])
pygame.mouse.set_visible(True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ## if mouse is pressed get position of cursor ##
            print(pygame.mouse.get_pos())

    # When an object runs into a wall we need to change direction
    # check if characters wo uld run into wall. If so flip it's velocity
    for ghost in ghosts:
        #check if ghost will hit wall
        nearest_col = min(int( (ghost.x_pos + ghost.x_vel) / width * num_cols ), num_cols-1)
        nearest_row = min(int( (ghost.y_pos + ghost.y_vel) / height * num_rows ), num_rows-1)
        if board.grid[nearest_row][nearest_col] == True:
            # change to move towards mr pacman
            ghost.y_vel = - ghost.y_vel
            ghost.x_vel = - ghost.x_vel

    # UPDATE POSITIONS
    mr_pacman.x_pos = mr_pacman.x_pos + mr_pacman.x_vel
    mr_pacman.y_pos = mr_pacman.y_pos + mr_pacman.y_vel
    if mr_pacman.x_pos >= width:
        mr_pacman.x_vel = 0
    if mr_pacman.x_pos <= 0:
        mr_pacman.x_vel = 0

    for ghost in ghosts:
        ghost.x_pos = ghost.x_pos + ghost.x_vel
        ghost.y_pos = ghost.y_pos + ghost.y_vel
        # If it hits a left or right wall flip the x velocity. If it hits the top or bottom flip the y velocity.

    for ghost in ghosts:
        if ghost.x_pos >= width:
            ghost.x_vel = - ghost.x_vel
        if ghost.x_pos <= 0:
            ghost.x_vel = - ghost.x_vel
        if ghost.y_pos >= height:
            ghost.y_vel = - ghost.y_vel
        if ghost.y_pos <= 0:
            ghost.y_vel = - ghost.y_vel

    # DRAW ON SCREEN
    screen.fill(color=(0, 0, 0))   # R,G,B = 0,0,0 for black background
    for ghost in ghosts:
        pygame.draw.circle(surface=screen, color=(255, 255, 255), center=(ghost.x_pos, ghost.y_pos), radius=5)
    pygame.draw.circle(surface=screen, color=(255, 255, 0), center=(mr_pacman.x_pos, mr_pacman.y_pos), radius=5)

    # Draw board
    rect_height = height/num_rows
    rect_width = width/num_cols
    for i in range(num_rows):
        for j in range(num_cols):
            isFilled = board.grid[i][j]
            if isFilled:
                pygame.draw.rect(surface=screen, color=(0, 0, 255), rect=(j * rect_width, i * rect_height, rect_width, rect_height))

    pygame.display.update()

pygame.quit()