import pygame
import maze
import grid
from timeit import default_timer

def reconstruct_path(node_path, current, draw, counter_start):
    pygame.display.set_caption("Maze Solver ( Constructing Path... )")
    path_count = 0

    while current in node_path:
        current = node_path[current]            
        current.make_path()
        path_count += 1
        draw()
    counter_end = default_timer()
    time_elapsed = counter_end - counter_start
    pygame.display.set_caption(f'Time Elapsed: {format(time_elapsed, ".2f")}s |Number Node Open :{len(node_path)+1}| Shortest Path: {path_count + 1} Cells')
    
    return time_elapsed    