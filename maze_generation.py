
import pygame
import random

def build(draw , grid , start , end):
    rows = len(grid)
    cols = len(grid[0])

    for row in grid:
        for spot in row:
            if not spot.is_outer_wall() and spot != start and spot != end:
                spot.make_wall()
        draw()

    def is_in_grid(row , col):
        return 0 <= row < rows and 0 <= col < cols
    
    def generation(rows , cols):
        grid[rows][cols].reset()
        if grid[rows][cols] != start and grid[rows][cols]:
            grid[rows][cols]

        draw()
        pygame.display.update()

        directions = [(2,0), (-2,0), (0,2), (0,-2)]
        random.shuffle(directions)

        for row , col in directions:
            new_row = row + rows
            new_col = col + cols
            if is_in_grid(new_row , new_col) and grid[new_row][new_col].is_wall():
                mid_row = rows + row // 2
                mid_col = cols + col // 2
                grid[mid_row][mid_col].reset()
                generation(new_row , new_col)

    start_row, start_col = start.get_pos()
    generation(start_row, start_col)

    x_end , y_end = end.get_pos()
    end_directions = [ (1 , 0) , (-1 , 0) , (0 , -1) , (0 , 1) ] #up down left right
    near_outer_wall = 0

    if grid[x_end+1][y_end].is_outer_wall():
        near_outer_wall += 1
    if grid[x_end-1][y_end].is_outer_wall():
        near_outer_wall += 1
    if grid[x_end][y_end+1].is_outer_wall():
        near_outer_wall += 1
    if grid[x_end][y_end-1].is_outer_wall():
        near_outer_wall += 1

    if near_outer_wall >= 2:
        for row , col in end_directions:
            grid[x_end+row][y_end+col].reset()


    if (grid[x_end+1][y_end].is_wall() and 
        grid[x_end-1][y_end].is_wall() and 
        grid[x_end][y_end+1].is_wall() and 
        grid[x_end][y_end-1].is_wall()):

        random.shuffle(end_directions)
        row , col = end_directions[1]
        grid[x_end+row][y_end+col].reset()
    

    start.make_start()
    end.make_end()
    return grid
