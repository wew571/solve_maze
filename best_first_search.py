from queue import PriorityQueue
from node import Node

import numpy
import pygame
import time_solve

def heuristic(p1 , p2):
    x1 , y1 = p1
    x2 , y2 = p2
    return numpy.absolute(x1 - x2) + numpy.absolute(y1 - y2)

def solve(draw , grid , start , end , counter_start):
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

    while not queue.empty():
        current = queue.get()[2]
        queue_hash.remove(current)

        if  current == end:
            time_solve.reconstruct_path(node_path , end , draw , counter_start)
            start.make_start()
            end.make_end()
            return True
        
        for neibour in current.neighbours:

            temp_f_score = heuristic(neibour.get_pos() , end.get_pos())
            if temp_f_score < f_score[neibour]:
                node_path[neibour] = current
                f_score[neibour] = temp_f_score

                if neibour not in queue_hash and not neibour.is_wall() :
                    count += 1
                    queue.put((f_score[neibour] , count , neibour))
                    queue_hash.add(neibour)
                    neibour.make_open_bestfs()

        draw()
        if current != start:
            current.make_close_bestfs()

    return False

