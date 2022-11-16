import pygame
from pygame.locals import *
from mr_pacman import Pacman
from ghost import Ghost

pygame.init()

width = 640
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pacman")

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

    screen.fill((0, 0, 0))   # R,G,B = 0,0,0 is black
    for ghost in ghosts:
        pygame.draw.circle(surface=screen, color=(255, 255, 255), center=(ghost.x_pos, ghost.y_pos), radius=2)

    pygame.draw.circle(surface=screen, color=(255, 255, 0), center=(mr_pacman.x_pos, mr_pacman.y_pos), radius=2)
    pygame.display.update()

pygame.quit()