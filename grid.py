from node import Node
import color
import pygame

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Node(i, j, gap, rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, color.Grid, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, color.Grid ,(i * gap, 0), (i * gap, width))
    pygame.draw.line(win , color.Grid , ( 1300 , 0) , ( 1300 , 1600) , 2)

def draw_grid_wall(rows, grid):
    for i in range(rows):
        for j in range(rows):
            if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                spot = grid[i][j]
                spot.make_outer_wall()

def draw(win, grid, rows, width):

    for row in grid:
        for spot in row:
            spot.draw(win)
    
    draw_grid(win, rows, width)
    draw_grid_wall(rows, grid)
    pygame.display.update()
