import pygame
import random
import sys

sys.setrecursionlimit(20000)

def dfs_algorithm(draw , grid , start , end):
    rows = len(grid)
    cols = len(grid[0])

    for row in grid:
        for spot in row:
            if not spot.is_outer_wall() and spot != start and spot != end:
                spot.make_wall()
        

    def is_in_grid(row , col):
        return 0 <= row < rows and 0 <= col < cols
    
    draw_count = [0]
    def generation(rows , cols):
        if grid[rows][cols] != start and grid[rows][cols]:
            grid[rows][cols].reset()

        draw_count[0] += 1
        if draw_count[0] % 75 == 0:
            draw()


        directions = [(2,0), (-2,0), (0,2), (0,-2)]
        random.shuffle(directions)

        for row , col in directions:
            new_row = row + rows
            new_col = col + cols
            if is_in_grid(new_row , new_col) and grid[new_row][new_col].is_wall():
                mid_row = rows + row // 2
                mid_col = cols + col // 2
                grid[mid_row][mid_col].reset()
                generation(new_row , new_col)

    start_row, start_col = start.get_pos()
    generation(start_row, start_col)

    #remove wall if start blocks
    x_start , y_start = start.get_pos()
    start_directions = [ (1 , 0) , ( -1 , 0) , ( 0 , 1) , (0 , 1) ]#up down left right
    start_near_outer_wall = 0

    if grid[x_start+1][y_start].is_outer_wall():
        start_near_outer_wall += 1
    if grid[x_start-1][y_start].is_outer_wall():
        start_near_outer_wall += 1
    if grid[x_start][y_start+1].is_outer_wall():
        start_near_outer_wall += 1
    if grid[x_start][y_start-1].is_outer_wall():
        start_near_outer_wall += 1   

    if start_near_outer_wall >= 2:
        for row , col in start_directions:
            grid[x_start+row][y_start+col].reset()

    if (grid[x_start+1][y_start].is_wall() and 
        grid[x_start-1][y_start].is_wall() and 
        grid[x_start][y_start+1].is_wall() and 
        grid[x_start][y_start-1].is_wall()):

        random.shuffle(start_directions)
        row , col = start_directions[1]
        grid[x_start+row][y_start+col].reset()    

    #remove wall if end blocks
    x_end , y_end = end.get_pos()
    end_directions = [ (1 , 0) , (-1 , 0) , (0 , -1) , (0 , 1) ] #up down left right
    end_near_outer_wall = 0

    if grid[x_end+1][y_end].is_outer_wall():
        end_near_outer_wall += 1
    if grid[x_end-1][y_end].is_outer_wall():
        end_near_outer_wall += 1
    if grid[x_end][y_end+1].is_outer_wall():
        end_near_outer_wall += 1
    if grid[x_end][y_end-1].is_outer_wall():
        end_near_outer_wall += 1

    if end_near_outer_wall >= 2:
        for row , col in end_directions:
            grid[x_end+row][y_end+col].reset()

    if (grid[x_end+1][y_end].is_wall() and 
        grid[x_end-1][y_end].is_wall() and 
        grid[x_end][y_end+1].is_wall() and 
        grid[x_end][y_end-1].is_wall()):

        random.shuffle(end_directions)
        row , col = end_directions[1]
        grid[x_end+row][y_end+col].reset()
    

    start.make_start()
    end.make_end()
    return grid

def prims_algorithm(draw, grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize all as walls
    for row in grid:
        for spot in row:
            if not spot.is_outer_wall() and spot != start and spot != end:
                spot.make_wall()
    
    # Start from a random cell
    start_x = random.randint(1, rows-2)
    start_y = random.randint(1, cols-2)
    grid[start_x][start_y].reset()
    
    frontiers = []
    # Add neighboring walls to frontiers
    for dx, dy in [(2,0), (-2,0), (0,2), (0,-2)]:
        nx, ny = start_x + dx, start_y + dy
        if 1 <= nx < rows-1 and 1 <= ny < cols-1:
            frontiers.append((nx, ny, start_x, start_y))

    draw_count = 0
    while frontiers:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        draw_count += 1
        if draw_count % 75 == 0:
            draw()
        
        # Pick random frontier
        idx = random.randint(0, len(frontiers)-1)
        fx, fy, px, py = frontiers.pop(idx)
        
        if grid[fx][fy].is_wall():
            # Carve passage
            grid[fx][fy].reset()
            # Carve passage between frontier and parent
            mid_x = (fx + px) // 2
            mid_y = (fy + py) // 2
            grid[mid_x][mid_y].reset()
            
            # Add new frontiers
            for dx, dy in [(2,0), (-2,0), (0,2), (0,-2)]:
                nx, ny = fx + dx, fy + dy
                if 1 <= nx < rows-1 and 1 <= ny < cols-1 and grid[nx][ny].is_wall():
                    frontiers.append((nx, ny, fx, fy))

    #remove wall if start blocks
    x_start , y_start = start.get_pos()
    start_directions = [ (1 , 0) , ( -1 , 0) , ( 0 , 1) , (0 , 1) ]#up down left right
    start_near_outer_wall = 0

    if grid[x_start+1][y_start].is_outer_wall():
        start_near_outer_wall += 1
    if grid[x_start-1][y_start].is_outer_wall():
        start_near_outer_wall += 1
    if grid[x_start][y_start+1].is_outer_wall():
        start_near_outer_wall += 1
    if grid[x_start][y_start-1].is_outer_wall():
        start_near_outer_wall += 1   

    if start_near_outer_wall >= 2:
        for row , col in start_directions:
            grid[x_start+row][y_start+col].reset()

    if (grid[x_start+1][y_start].is_wall() and 
        grid[x_start-1][y_start].is_wall() and 
        grid[x_start][y_start+1].is_wall() and 
        grid[x_start][y_start-1].is_wall()):

        random.shuffle(start_directions)
        row , col = start_directions[1]
        grid[x_start+row][y_start+col].reset()    

    #remove wall if end blocks
    x_end , y_end = end.get_pos()
    end_directions = [ (1 , 0) , (-1 , 0) , (0 , -1) , (0 , 1) ] #up down left right
    end_near_outer_wall = 0

    if grid[x_end+1][y_end].is_outer_wall():
        end_near_outer_wall += 1
    if grid[x_end-1][y_end].is_outer_wall():
        end_near_outer_wall += 1
    if grid[x_end][y_end+1].is_outer_wall():
        end_near_outer_wall += 1
    if grid[x_end][y_end-1].is_outer_wall():
        end_near_outer_wall += 1

    if end_near_outer_wall >= 2:
        for row , col in end_directions:
            grid[x_end+row][y_end+col].reset()

    if (grid[x_end+1][y_end].is_wall() and 
        grid[x_end-1][y_end].is_wall() and 
        grid[x_end][y_end+1].is_wall() and 
        grid[x_end][y_end-1].is_wall()):

        random.shuffle(end_directions)
        row , col = end_directions[1]
        grid[x_end+row][y_end+col].reset()
    

    start.make_start()
    end.make_end()
    return grid

def kruskals_algorithm(draw, grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize all as walls
    for row in grid:
        for spot in row:
            if not spot.is_outer_wall() and spot != start and spot != end:
                spot.make_wall()
    
    # Union-Find data structure
    parent = {}
    def find(cell):
        if parent[cell] != cell:
            parent[cell] = find(parent[cell])
        return parent[cell]
    
    def union(cell1, cell2):
        root1, root2 = find(cell1), find(cell2)
        if root1 != root2:
            parent[root2] = root1
            return True
        return False
    
    # Initialize cells and edges
    edges = []
    for i in range(1, rows-1, 2):
        for j in range(1, cols-1, 2):
            cell = (i, j)
            parent[cell] = cell
            grid[i][j].reset()
            
            # Add edges to neighbors
            if i + 2 < rows-1:
                edges.append(((i, j), (i+2, j), (i+1, j)))
            if j + 2 < cols-1:
                edges.append(((i, j), (i, j+2), (i, j+1)))
    
    random.shuffle(edges)
    
    # Process edges
    for draw_count , (cell1, cell2, wall) in enumerate(edges):
        if union(cell1, cell2):
            grid[wall[0]][wall[1]].reset()
            if draw_count % 75 == 0:
                draw()
                
    #remove wall if start blocks
    x_start , y_start = start.get_pos()
    start_directions = [ (1 , 0) , ( -1 , 0) , ( 0 , 1) , (0 , 1) ]#up down left right
    start_near_outer_wall = 0

    if grid[x_start+1][y_start].is_outer_wall():
        start_near_outer_wall += 1
    if grid[x_start-1][y_start].is_outer_wall():
        start_near_outer_wall += 1
    if grid[x_start][y_start+1].is_outer_wall():
        start_near_outer_wall += 1
    if grid[x_start][y_start-1].is_outer_wall():
        start_near_outer_wall += 1   

    if start_near_outer_wall >= 2:
        for row , col in start_directions:
            grid[x_start+row][y_start+col].reset()

    if (grid[x_start+1][y_start].is_wall() and 
        grid[x_start-1][y_start].is_wall() and 
        grid[x_start][y_start+1].is_wall() and 
        grid[x_start][y_start-1].is_wall()):

        random.shuffle(start_directions)
        row , col = start_directions[1]
        grid[x_start+row][y_start+col].reset()    

    #remove wall if end blocks
    x_end , y_end = end.get_pos()
    end_directions = [ (1 , 0) , (-1 , 0) , (0 , -1) , (0 , 1) ] #up down left right
    end_near_outer_wall = 0

    if grid[x_end+1][y_end].is_outer_wall():
        end_near_outer_wall += 1
    if grid[x_end-1][y_end].is_outer_wall():
        end_near_outer_wall += 1
    if grid[x_end][y_end+1].is_outer_wall():
        end_near_outer_wall += 1
    if grid[x_end][y_end-1].is_outer_wall():
        end_near_outer_wall += 1

    if end_near_outer_wall >= 2:
        for row , col in end_directions:
            grid[x_end+row][y_end+col].reset()

    if (grid[x_end+1][y_end].is_wall() and 
        grid[x_end-1][y_end].is_wall() and 
        grid[x_end][y_end+1].is_wall() and 
        grid[x_end][y_end-1].is_wall()):

        random.shuffle(end_directions)
        row , col = end_directions[1]
        grid[x_end+row][y_end+col].reset()
    
    start.make_start()
    end.make_end()
    return grid
