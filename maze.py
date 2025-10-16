from timeit import default_timer
from grid import make_grid
from grid import draw

import color
import astar
import breath_first_search
import depth_first_search
import best_first_search

import pygame
import random

pygame.init()

def get_mouse_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    if x >= width:
        return None , None

    row = y // gap
    col = x // gap

    if row >= rows or col >= rows:
        return None, None

    return row, col

def main(win, width):
    ROWS = 35
    grid = make_grid(ROWS, width)
    save_grid = grid

    Start = None
    End = None
    Run = True

    while Run:
        draw(win, grid, ROWS, width)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Run = False

            if pygame.mouse.get_pressed()[0]: #[0] left mouse btn
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not Start and spot != End:
                    Start = spot
                    Start.make_start()

                elif not End and spot != Start:
                    End = spot
                    End.make_end()

                elif spot != Start and spot != End:
                    spot.make_wall()                

            if pygame.mouse.get_pressed()[2]: #[2] Right mouse btn
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == Start:
                    Start = None
                if spot == End:
                    End = None    

            if e.type == pygame.KEYDOWN:
            
                if not Start and not End:
                    pygame.display.set_caption("Maze Solver ( Set Start & End Nodes ! )")

                #refresh 
                if e.key == pygame.K_q: 
                    for row in grid:
                        for spot in row:
                            if spot.is_astar_open() or spot.is_bfs_open() or spot.is_dfs_open() or spot.is_bestfs_open() or spot.is_astar_close() or spot.is_bfs_close() or spot.is_dfs_close() or spot.is_bestfs_close() or spot.is_path() :
                                spot.reset()

                if e.key == pygame.K_r and Start and End:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)

                    astar.algorithm(lambda: draw(win, grid, ROWS, width), grid, Start, End, counter_start)

                if e.key == pygame.K_t and Start and End:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    breath_first_search.solve(lambda : draw(win , grid , ROWS , width) , grid , Start , End , counter_start)

                if e.key == pygame.K_y and Start and End:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    depth_first_search.solve(lambda : draw(win , grid , ROWS , width) , grid , Start , End , counter_start)

                if e.key == pygame.K_u and Start and End:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    best_first_search.solve(lambda : draw(win , grid , ROWS , width) , grid , Start , End , counter_start)

                if e.key == pygame.K_e:
                    Start = None
                    End = None
                    pygame.display.set_caption("Maze Solver ( Using A* Algorithm )")
                    grid = make_grid(ROWS, width) 

    pygame.quit()



