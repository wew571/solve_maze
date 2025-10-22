###########List Of Key############# 
# q : refresh open node 
# e : reset maze
# r : run A* algorithm
# t : run BFS algorithm
# y : run DFS algorithm
# u : run Best First Search algorithm
# i : run Dijkstra algorithm
# m , n , b : generation maze
# g : delete history , best results
# w : increase speed search
# s : decrease speed search
# esc : quit
# left button : make start point , finish point and make wall
# right button : remove start point , finish point and wall

import pygame
from maze import main

WIDTH = 1000
HEIGHT = 1000

info_width = 300
sub_width = 600

win = pygame.display.set_mode((WIDTH + info_width + sub_width , HEIGHT))
pygame.display.set_caption("Maze Solver ")


main(win , WIDTH)
