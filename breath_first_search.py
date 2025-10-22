from queue import Queue
from timeit import default_timer
from node import Node

import time_solve
import pygame

#bfs
def solve(draw , grid , start , end , counter_start , speed):
    queue = Queue()
    queue.put(start)
    node_path = {}
    visit = {start}

    nodes_open = 0
    nodes_close = 0
    total_nodes = 0

    draw_count = 0
    total_draw_time_alogithm = 0

    for row in grid:
        for spot in row:
            if not spot.is_wall() and not spot.is_outer_wall():
                total_nodes += 1

    while not queue.empty():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                
        current = queue.get()
        nodes_close += 1
        
        if current == end:
            exploration_ratio = nodes_close / total_nodes * 100
            path_data = time_solve.reconstruct_path(node_path , end , draw , counter_start , speed , total_draw_time_alogithm)
            end.make_end()
            start.make_start()
            return {
                'time': path_data['time'],
                'nodes_opened' : nodes_open,
                'nodes_closed' : nodes_close,
                'exploration_ratio' : exploration_ratio,
                'path_length' : path_data['path_length'],
                'path_found' : True
            }
        
        for neightbor in current.neighbours:
            if neightbor not in visit :
                nodes_open += 1
                draw_count += 1
                node_path[neightbor] = current 
                visit.add(neightbor)
                queue.put(neightbor)
                neightbor.make_open_bfs()

        if draw_count % speed == 0:
            draw_start = default_timer()
            draw()
            draw_end = default_timer()
            total_draw_time_alogithm += (draw_end - draw_start)

        if current != start:
            current.make_close_bfs()

    exploration_ratio = nodes_close / total_nodes * 100
    pygame.display.set_caption("Maze Solver ( Unable To Find The Target Node ! )")

    return {
        'time': default_timer() - counter_start,
        'nodes_opened' : nodes_open,
        'nodes_closed' : nodes_close,
        'exploration_ratio' : exploration_ratio,
        'path_length' : 0,
        'path_found' : False
    }


        


