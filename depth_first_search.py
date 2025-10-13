import time_solve
import maze
from node import Node

def solve(draw , grid , start , end , counter_start):
    stack = []
    stack.append(start)
    visit = {start}
    node_path = {}

    while stack:
        current = stack.pop()

        if current  == end:
            time_solve.reconstruct_path(node_path , end , draw , counter_start)
            end.make_end()
            start.make_start()
            return True
        
        for neightbor in current.neighbours:
            if neightbor not in visit :
                node_path[neightbor] = current
                visit.add(neightbor)
                stack.append(neightbor)
                neightbor.make_open_dfs() 

        draw()
        
        if current != start:
            current.make_close_dfs()    
    return False

    
