from queue import PriorityQueue
from timeit import default_timer
from node import Node

import numpy
import pygame
import time_solve

def heuristic(p1 , p2):
    x1 , y1 = p1
    x2 , y2 = p2
    return numpy.absolute(x1 - x2) + numpy.absolute(y1 - y2)

def solve(draw , grid , start , end , counter_start , speed):
    count = 0
    queue = PriorityQueue()

    node_path = {}
    f_score = {spot : float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start.get_pos() , end.get_pos())
    #f_score = {}
    # for row in grid:
    #     for spot in row:
    #         f_score[spot] = float("inf")
    queue_hash = {start}
    queue.put(( f_score[start] , count , start))

    nodes_open = 0
    nodes_close = 0
    total_nodes = 0

    draw_count = 0 
    total_draw_time_algorithm = 0

    for row in grid:
        for spot in row:
            if not spot.is_wall() and not spot.is_outer_wall():
                total_nodes += 1

    while not queue.empty():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        current = queue.get()[2]
        queue_hash.remove(current)
        nodes_close += 1

        if  current == end:
            exploration_ratio = nodes_close / total_nodes * 100
            path_data = time_solve.reconstruct_path(node_path , end , draw , counter_start , speed , total_draw_time_algorithm)
            start.make_start()
            end.make_end()
            return {
                'time': path_data['time'],
                'nodes_opened' : nodes_open,
                'nodes_closed' : nodes_close,
                'exploration_ratio' : exploration_ratio,
                'path_length' : path_data['path_length'],
                'path_found' : True
            }
        
        for  neibour in current.neighbours:
            temp_f_score = heuristic(neibour.get_pos() , end.get_pos())
            if temp_f_score < f_score[neibour]:
                node_path[neibour] = current
                f_score[neibour] = temp_f_score

                if neibour not in queue_hash and not neibour.is_wall() :
                    count += 1
                    nodes_open += 1
                    draw_count += 1
                    queue.put((f_score[neibour] , count , neibour))
                    queue_hash.add(neibour)
                    neibour.make_open_bestfs()

        if draw_count % speed == 0:
            draw_start = default_timer()
            draw()
            draw_end = default_timer()
            total_draw_time_algorithm += (draw_end - draw_start)

        if current != start:
            current.make_close_bestfs()

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


