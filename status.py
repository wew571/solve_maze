import pygame

import color

#UI
def draw_info_window(win, width, stats , speed):
    info_width = 300  
    info_height = width  
    
    info_surface = pygame.Surface((info_width, info_height))
    info_surface.fill(color.UI_Back_Ground)  
    
    # Title
    font_title = pygame.font.SysFont('Arial', 30, bold=True)
    title = font_title.render("Search Statistics", True, color.UI_Title)
    info_surface.blit(title, (75, 20))
    
    font = pygame.font.SysFont('Arial', 20)
     
    y_offset = 60
    line_height = 30
     
     # Status
    info_items = [
        ("Algorithm:", stats.get('algorithm', 'None')),
        ("Time:", f"{stats.get('time', 0):.3f}s"),
        ("Nodes Opened:", str(stats.get('nodes_opened', 0))),
        ("Nodes Closed:", str(stats.get('nodes_closed', 0))),
        ("Exploration Ratio:" , f"{stats.get('exploration_ratio' , 0):.3f}%"),
        ("Path Length:", str(stats.get('path_length', 0))),
        ("Status:", stats.get('status', 'Ready')),
        ("Speed:" , str(stats.get('speed', speed)))
    ]
    
    for label, value in info_items:
        label_text = font.render(label, True, color.UI_Text)
        value_text = font.render(value, True, color.UI_Status_Text)
        info_surface.blit(label_text, (20, y_offset))
        info_surface.blit(value_text, (150, y_offset))
        y_offset += line_height
    
    # Guide
    y_offset += 30
    guide_title = pygame.font.SysFont('Arial', 30, bold=True)
    title = guide_title.render("Guide", True, color.UI_Title)
    info_surface.blit(title, (75, y_offset))

    y_offset += 35
    instructions = [
        "Esc - Quit ",
        "Left Click - Place Start / End / Wall",
        "Right Click - Remove Start / End / Wall",
        "M - Generate Maze",
        "G - Delete History / Ranking",
        "Q - Clear Path",
        "E - Reset Maze",
        "W - Increase Speed",
        "S - Decrease Speed"
    ]

    for instruction in instructions:
        inst_text = font.render(instruction, True, color.UI_Guide)
        info_surface.blit(inst_text, (15, y_offset))
        y_offset += 20
    
    # Solve Algorithm
    y_offset += 30
    solve_algorithm_title = pygame.font.SysFont('Arial' , 30 , bold=True)
    title = solve_algorithm_title.render("Solve Algorithm" , True , color.UI_Title)
    info_surface.blit(title , (75 , y_offset))


    y_offset += 35
    solve_algorithm_items = [
        "R --- A* Search",
        "T --- Breath First Search",
        "Y --- Depth First Search", 
        "U --- Best First Search",
        "I --- Dijkstra",
    ]

    for algorithm_item in solve_algorithm_items:
        algorithm_text = font.render(algorithm_item , True , color.UI_Build_Maze_Text)
        info_surface.blit(algorithm_text , (20 , y_offset))
        y_offset += 20

    # Build Maze
    y_offset += 30
    build_maze = pygame.font.SysFont('Arial' , 30 , bold=True)
    title = build_maze.render("Build Maze" , True , color.UI_Title)
    info_surface.blit(title , (75 , y_offset))

    y_offset += 35
    label_part = font.render("Speed Build:" , True , color.UI_Text)
    speed_build_part = str(stats.get('speed_build' , 75))
    value_x = 30 + label_part.get_width() + 10
    value_part = font.render(speed_build_part , True , color.UI_Status_Text)

    info_surface.blit(label_part , (20 , y_offset))
    info_surface.blit(value_part , (value_x , y_offset))
    
    y_offset += 20
    build_maze_algorithm_items = [
        "M       DFS Algorithm",
        "N       Prims Algorithm",
        "B       Kruskals Algorithm"
    ]

    for buid_maze_algorithm_item in build_maze_algorithm_items:
        build_maze_text = font.render( buid_maze_algorithm_item , True , color.UI_Text)
        info_surface.blit(build_maze_text , (20 , y_offset))
        y_offset += 20

    # Difficult Maze
    y_offset += 30
    difficult_title = pygame.font.SysFont('Arial' , 30 , True)
    title = difficult_title.render("Difficult Maze" , True , color.UI_Title)
    info_surface.blit(title , (75 , y_offset)) 

    y_offset += 35
    label_part = font.render("Difficult:", True, color.UI_Text)
    info_surface.blit(label_part, (20, y_offset))
    difficult_value = stats.get('difficult', 'None')

    color_value = color.UI_Difficult_None

    if difficult_value == 'Easy':
        color_value = color.UI_Difficult_Easy
    elif difficult_value == 'Medium':
        color_value = color.UI_Difficult_Medium
    elif difficult_value == "Hard":
        color_value = color.UI_Difficult_Hard
    else:
        color_value = color.UI_Difficult_None

    value_part = font.render(difficult_value, True, color_value)
    value_x = 30 + label_part.get_width() + 10  
    info_surface.blit(value_part, (value_x, y_offset))

    win.blit(info_surface, (width, 0))
