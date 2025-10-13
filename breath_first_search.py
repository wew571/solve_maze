from queue import Queue
from node import Node
import time_solve
import grid
import maze

#bfs
def solve(draw , grid , start , end , counter_start):
    queue = Queue()
    queue.put(start)
    node_path = {}
    visit = {start}

    while not queue.empty():
        current = queue.get()
        
        if current == end:
            time_solve.reconstruct_path(node_path , end , draw , counter_start )
            end.make_end()
            start.make_start()
            return True
        
        for neightbor in current.neighbours:
            if neightbor not in visit :
                node_path[neightbor] = current 
                visit.add(neightbor)
                queue.put(neightbor)
                neightbor.make_open_bfs()
        
        draw()

        if current != start:
            current.make_close_bfs()

    return False


        


