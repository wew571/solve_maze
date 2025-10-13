###########List Of Key############# 
# q : refresh open node 
# e : reset maze
# r : run A* algorithm
# t : run BFS algorithm
# y : run DFS algorithm
# u : run Best First Search algorithm
# left button : make start point , finish point and make wall
# right button : remove start point , finish point and wall

import pygame
from maze import main

WIDTH = 736
HEIGHT = 736

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver ")

main(win, WIDTH)