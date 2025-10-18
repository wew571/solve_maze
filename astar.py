from queue import PriorityQueue
from timeit import default_timer

import maze
import pygame
import time_solve


def heuristic(p1, p2):
    x1, y1 = p1 # spliting values from a tuple
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def algorithm(draw, grid, start, end, counter_start , speed):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    node_path = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())

    nodes_open = 0
    nodes_close = 0

    draw_count = 0
    total_draw_time_algorithm = 0
    
    open_set_hash = {start}
    while not open_set.empty():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)
        nodes_close += 1

        if current == end:
            path_data = time_solve.reconstruct_path(node_path, end, draw, counter_start , speed , total_draw_time_algorithm)
            end.make_end()
            start.make_start()
            return {
                'time': path_data['time'],
                'nodes_opened': nodes_open,
                'nodes_closed': nodes_close,
                'path_length': path_data['path_length'],
                'path_found': True
            }

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                node_path[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + heuristic(neighbour.get_pos(), end.get_pos())
                
                if neighbour not in open_set_hash:
                    count += 1
                    nodes_open += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open_astar()

        draw_count += 1
        if draw_count % speed == 0:
            draw_start = default_timer()
            draw()
            draw_end = default_timer()
            total_draw_time_algorithm += ( draw_end - draw_start)

        if current != start:
            current.make_close_astar()

    pygame.display.set_caption("Maze Solver ( Unable To Find The Target Node ! )")

    return {
        'time': default_timer() - counter_start,
        'nodes_opened': nodes_open,
        'nodes_closed': nodes_close,
        'path_length': 0,
        'path_found': False
    }
