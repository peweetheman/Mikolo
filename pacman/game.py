import pygame
from pygame.locals import *
from mr_pacman import Pacman
from ghost import Ghost
import time

pygame.init()

width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PACMAN")

mr_pacman = Pacman(x=width/2, y=height/4)
num_ghosts = 4
ghosts = []  # [Ghost_instance_1, Ghost_instance_2, .... ]
for i in range(4):
    ghosts.append(Ghost(width/2 + 20*i, height/2 + 20*i))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

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
    screen.fill(color=(0, 0, 0))   # R,G,B = 0,0,0 is black
    for ghost in ghosts:
        pygame.draw.circle(surface=screen, color=(255, 255, 255), center=(ghost.x_pos, ghost.y_pos), radius=5)

    pygame.draw.circle(surface=screen, color=(255, 255, 0), center=(mr_pacman.x_pos, mr_pacman.y_pos), radius=5)
    pygame.display.update()

pygame.quit()