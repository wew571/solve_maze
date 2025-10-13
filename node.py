import color
import pygame

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = color.Back_Ground
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def reset(self):
        self.color = color.Back_Ground

    def make_close(self):
        self.color = color.Path_Close

    def make_close_astar(self):
        self.color = color.Path_Close_Astar
    
    def make_close_bfs(self):
        self.color = color.Path_Close_BFS

    def make_close_dfs(self):
        self.color = color.Path_Close_DFS

    def make_close_bestfs(self):
        self.color = color.Path_Close_BestFS

    def make_open(self):
        self.color = color.Path_Open

    def make_open_astar(self):
        self.color = color.Path_Open_Astar

    def make_open_bfs(self):
        self.color = color.Path_Open_BFS

    def make_open_dfs(self):
        self.color = color.Path_Open_DFS

    def make_open_bestfs(self):
        self.color = color.Path_Open_BestFS

    def make_wall(self):
        self.color = color.Wall
    
    def make_outer_wall(self):
        self.color = color.Outer_Wall
    
    def make_start(self):
        self.color = color.Start

    def make_end(self):
        self.color = color.Finish

    def make_path(self):
        self.color = color.Path

    def is_closed(self):
        return self.color == color.Path_Close

    def is_opened(self):
        return self.color == color.Path_Open

    def is_wall(self):
        return self.color == color.Wall
    
    def is_outer_wall(self):
        return self.color == color.Outer_Wall
    
    def is_astar_open(self):
        return self.color == color.Path_Open_Astar
    
    def is_bfs_open(self):
        return self.color == color.Path_Open_BFS
    
    def is_dfs_open(self):
        return self.color == color.Path_Open_DFS
    
    def is_bestfs_open(self):
        return self.color == color.Path_Open_BestFS
    
    def is_astar_close(self):
        return self.color == color.Path_Close_Astar
    
    def is_bfs_close(self):
        return self.color == color.Path_Close_BFS
    
    def is_dfs_close(self):
        return self.color == color.Path_Close_DFS
    
    def is_bestfs_close(self):
        return self.color == color.Path_Close_BestFS
    
    def is_start(self):
        return self.color == color.Start

    def is_end(self):
        return self.color == color.Finish
    
    def is_path(self):
        return self.color == color.Path

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []
        # checks for neighbours in -y axis
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall() and not grid[self.row + 1][self.col].is_outer_wall():
            self.neighbours.append(grid[self.row + 1][self.col])

        # checks for neighbours in y axis
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall() and not grid[self.row - 1][self.col].is_outer_wall():
            self.neighbours.append(grid[self.row - 1][self.col])

        # checks for neighbours in -x axis
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall() and not grid[self.row][self.col + 1].is_outer_wall():
            self.neighbours.append(grid[self.row][self.col + 1])

        # checks for neighbours in x axis
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall() and not grid[self.row][self.col - 1].is_outer_wall():
            self.neighbours.append(grid[self.row][self.col - 1])