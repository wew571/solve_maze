from queue import PriorityQueue

import maze
import pygame
import time_solve

def heuristic(p1, p2):
    x1, y1 = p1 # spliting values from a tuple
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def algorithm(draw, grid, start, end, counter_start):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    node_path = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())
    open_set_hash = {start}
    while not open_set.empty():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            time_solve.reconstruct_path(node_path, end, draw, counter_start)
            end.make_end()
            start.make_start()
            return True
        
        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                node_path[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + heuristic(neighbour.get_pos(), end.get_pos())

                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open_astar()

        draw()
        if current != start:
            current.make_close_astar()

    pygame.display.set_caption("Maze Solver ( Unable To Find The Target Node ! )")
    return False
