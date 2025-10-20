from queue import PriorityQueue
from timeit import default_timer
from node import Node

import time_solve
import maze

import numpy
import pygame

def solve(draw , grid , start , end , counter_start , speed):
    count = 0
    node_path = {}
    queue = PriorityQueue()
    
    distance = {spot : float("inf") for row in grid for spot in row}
    distance[start] = 0
  
    queue_hash = {start}
    queue.put((distance[start] , count , start)) 

    nodes_open = 0
    nodes_close = 0

    draw_count = 0
    total_draw_time_algorithm = 0

    while not queue.empty():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        current = queue.get()[2]
        queue_hash.remove(current)
        nodes_close += 1

        if current == end:
            path_data = time_solve.reconstruct_path(node_path , end , draw , counter_start , speed , total_draw_time_algorithm)
            start.make_start()
            end.make_end()
            return {
                'time': path_data['time'],
                'nodes_opened': nodes_open,
                'nodes_closed': nodes_close,
                'path_length': path_data['path_length'],
                'path_found': True
            }
        
        for neighbor in current.neighbours:
            temp_distance = distance[current] + 1

            if temp_distance < distance[neighbor]:
                node_path[neighbor] = current
                distance[neighbor] = temp_distance

                if neighbor not in queue_hash:
                    count += 1
                    nodes_open += 1
                    draw_count += 1
                    queue.put((distance[neighbor] , count , neighbor))
                    queue_hash.add(neighbor)
                    neighbor.make_open_dijkstra()
                    
        if draw_count % speed == 0:
            draw_start = default_timer()
            draw()
            draw_end = default_timer()
            total_draw_time_algorithm += ( draw_end - draw_start)


        if current != start:
            current.make_close_dijkstra()

    return {
        'time': default_timer() - counter_start,
        'nodes_opened': nodes_open,
        'nodes_closed': nodes_close,
        'path_length': 0,
        'path_found': False   
    }
