from node import Node
from timeit import default_timer

import time_solve
import maze

import pygame

def solve(draw , grid , start , end , counter_start , speed):
    stack = []
    stack.append(start)
    visit = {start}
    node_path = {}

    nodes_open = 0
    nodes_close = 0

    draw_count = 0
    total_draw_time_algorithm = 0

    while stack:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()
        nodes_close += 1

        if current  == end:
            path_data = time_solve.reconstruct_path(node_path , end , draw , counter_start , speed , total_draw_time_algorithm)
            end.make_end()
            start.make_start()
            return {
                'time': path_data['time'],
                'nodes_opened': nodes_open,
                'nodes_closed': nodes_close,
                'path_length': path_data['path_length'],
                'path_found': True
            }
        
        for neightbor in current.neighbours:
            if neightbor not in visit :
                nodes_open += 1
                draw_count += 1
                node_path[neightbor] = current
                visit.add(neightbor)
                stack.append(neightbor)
                neightbor.make_open_dfs()
                 
        if draw_count % speed == 0:
            time_start = default_timer()
            draw()
            time_end = default_timer()
            total_draw_time_algorithm += ( time_end - time_start)
        
        if current != start:
            current.make_close_dfs()    

    return {
        'time': default_timer() - counter_start,
        'nodes_opened': nodes_open,
        'nodes_closed': nodes_close,
        'path_length': 0,
        'path_found': False        
    }

    
