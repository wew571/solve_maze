from timeit import default_timer
from grid import make_grid
from grid import draw
from status import draw_info_window

import color
import maze_generation

import astar
import breath_first_search
import depth_first_search
import best_first_search
import dijkstra

import pygame

pygame.init()

def get_mouse_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    if x >= width:
        return None , None

    row = y // gap
    col = x // gap

    #ensure program doesn't crash when click in status window
    if row >= rows or col >= rows:
        return None, None

    return row, col


def main(win , width):
    ROWS = 125
    grid = make_grid(ROWS, width) #matrix 125 x 125 ~15625 nodes
    save_grid = grid

    Start = None
    End = None
    Run = True

    speed = 10

    stats = {
        'algorithm': 'None',
        'time': 0.0,
        'nodes_opened': 0,
        'nodes_closed': 0,
        'path_length': 0,
        'status': 'Ready',
        'speed' : speed
    }

    while Run:
        draw(win, grid, ROWS, width)
        draw_info_window(win, width, stats , speed)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Run = False

            if pygame.mouse.get_pressed()[0]: #[0] left mouse btn
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos, ROWS, width)

                if row is None or col is None:
                    continue

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

                if row is None or col is None:
                    continue

                spot = grid[row][col]
                spot.reset()
                if spot == Start:
                    Start = None
                if spot == End:
                    End = None    

            if e.type == pygame.KEYDOWN:
            
                if not Start and not End:
                    stats['status'] = "Set Start & End Nodes!"
                    pygame.display.set_caption("Maze Solver ( Set Start & End Nodes ! )")

                #refresh 
                if e.key == pygame.K_q: 
                    for row in grid:
                        for spot in row:
                            if (spot.is_astar_open() or 
                                spot.is_bfs_open() or 
                                spot.is_dfs_open() or 
                                spot.is_bestfs_open() or 
                                spot.is_dijkstra_open() or 
                                spot.is_astar_close() or 
                                spot.is_bfs_close() or 
                                spot.is_dfs_close() or 
                                spot.is_bestfs_close() or 
                                spot.is_dijkstra_close() or 
                                spot.is_path()) :

                                spot.reset()
                                stats = {
                                    'time': 0.0,
                                    'nodes_opened': 0,
                                    'nodes_closed': 0,
                                    'path_length': 0,
                                    'status': 'Grid Reset'
                                }

                if e.key == pygame.K_m:
                    if Start  and End:
                        grid = maze_generation.dfs_algorithm(lambda : draw(win , grid , ROWS , width) , grid , Start , End)
                        stats['algorithm'] = "DFS Alogorithm"
                        stats['status'] = "Maze Generated"

                if e.key == pygame.K_n:
                    if Start and End:
                        grid = maze_generation.prims_algorithm(lambda : draw(win , grid , ROWS , width) , grid , Start , End)
                        stats['algorithm'] = "Prims Algorithm"
                        stats['status'] = "Maze Generated"

                if e.key == pygame.K_b:
                    if Start and End:
                        grid = maze_generation.kruskals_algorithm(lambda : draw(win , grid , ROWS , width) , grid , Start , End)
                        stats['algorithm'] = "Kruskals Algorithm"
                        stats['status'] = "Maze Generated"

                if e.key == pygame.K_r and Start and End:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    stats['algorithm'] = "A* Search"
                    stats['status'] = "Searching..."

                    for row in grid:    
                        for spot in row:
                            spot.update_neighbours(grid)

                    res = astar.algorithm(lambda: draw(win, grid, ROWS, width), grid, Start, End, counter_start , speed)

                    if res:
                        stats['time'] = res['time']
                        stats['nodes_opened'] = res['nodes_opened']
                        stats['nodes_closed'] = res['nodes_closed'] 
                        stats['path_length'] = res['path_length']
                        stats['status'] = "Path Found!" if res['path_found'] else "No Path Found"

                if e.key == pygame.K_t and Start and End:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    stats['algorithm'] = "Breadth First Search"
                    stats['status'] = "Searching..."

                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)

                    res = breath_first_search.solve(lambda : draw(win , grid , ROWS , width) , grid , Start , End , counter_start , speed)
                    if res:
                        stats['time'] = res['time']
                        stats['nodes_opened'] = res['nodes_opened']
                        stats['nodes_closed'] = res['nodes_closed'] 
                        stats['path_length'] = res['path_length']
                        stats['status'] = "Path Found!" if res['path_found'] else "No Path Found"        

                if e.key == pygame.K_y and Start and End:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    stats['algorithm'] = "Depth First Search"
                    stats['status'] = "Searching..."

                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)

                    res = depth_first_search.solve(lambda : draw(win , grid , ROWS , width) , grid , Start , End , counter_start)
                    if res:
                        stats['time'] = res['time']
                        stats['nodes_opened'] = res['nodes_opened']
                        stats['nodes_closed'] = res['nodes_closed'] 
                        stats['path_length'] = res['path_length']
                        stats['status'] = "Path Found!" if res['path_found'] else "No Path Found"   

                if e.key == pygame.K_u and Start and End:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    stats['algorithm'] = "Best First Search"
                    stats['status'] = "Searching..."

                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)

                    res = best_first_search.solve(lambda : draw(win , grid , ROWS , width) , grid , Start , End , counter_start , speed)
                    if res:
                        stats['time'] = res['time']
                        stats['nodes_opened'] = res['nodes_opened']
                        stats['nodes_closed'] = res['nodes_closed'] 
                        stats['path_length'] = res['path_length']
                        stats['status'] = "Path Found!" if res['path_found'] else "No Path Found"

                if e.key == pygame.K_i and Start and End:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    stats['algorithm'] = "Dijkstra"
                    stats['status'] = "Searching..."

                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)

                    res = dijkstra.solve(lambda : draw(win , grid , ROWS , width) , grid , Start , End , counter_start)
                    if res:
                        stats['time'] = res['time']
                        stats['nodes_opened'] = res['nodes_opened']
                        stats['nodes_closed'] = res['nodes_closed'] 
                        stats['path_length'] = res['path_length']
                        stats['status'] = "Path Found!" if res['path_found'] else "No Path Found"

                if e.key == pygame.K_o:
                    counter_start = default_timer()
                    pygame.display.set_caption("Maze Solver ( Searching... )")
                    stats['algorithm'] = "????"
                    stats['status'] = "Searching..." 


                if e.key == pygame.K_e:
                    Start = None
                    End = None
                    pygame.display.set_caption("Maze Solver ")
                    stats = {
                        'time': 0.0,
                        'nodes_opened': 0,
                        'nodes_closed': 0,
                        'path_length': 0,
                        'status': 'Grid Reset'
                    }
                    grid = make_grid(ROWS, width) 

                if e.key == pygame.K_ESCAPE:
                    Run = False

    pygame.quit()

