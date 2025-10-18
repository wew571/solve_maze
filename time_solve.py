import pygame

from timeit import default_timer

def reconstruct_path(node_path, current, draw, counter_start , speed , total_draw_time_algorithm ):
    pygame.display.set_caption("Maze Solver ( Constructing Path... )")
    path_count = 0

    total_draw_time_reconstruct = 0
    draw_count_reconstruct = 0

    while current in node_path:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        current = node_path[current]            
        current.make_path()
        path_count += 1
        draw_count_reconstruct += 1
        if draw_count_reconstruct % speed == 0:
            draw_start = default_timer()
            draw()
            draw_end = default_timer()
            total_draw_time_reconstruct += (draw_end - draw_start)

    total_actual_time = default_timer() - counter_start
    total_draw_time = total_draw_time_algorithm + total_draw_time_reconstruct

    computation_time = (total_actual_time - total_draw_time)
    nomalized_draw_time = total_draw_time * speed

    time_elapsed = computation_time + nomalized_draw_time
        
    pygame.display.set_caption(f'Time Elapsed: {format(time_elapsed, ".2f")}s |Number Node Open :{len(node_path)+1}| Shortest Path: {path_count + 1} Cells')
    
    return {
        'time': time_elapsed,
        'path_length': path_count + 1,  # include end node
        'nodes_opened': len(node_path) + 1  
    }  


  
