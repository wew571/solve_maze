import pygame

import color

#UI
def draw_info_window(win, width, stats):
    info_width = 300  
    info_height = width  
    
    info_surface = pygame.Surface((info_width, info_height))
    info_surface.fill(color.UI_Back_Ground)  
    
    # Title
    font_title = pygame.font.SysFont('Arial', 28, bold=True)
    title = font_title.render("SEARCH STATISTICS", True, color.UI_Title)
    info_surface.blit(title, (20, 20))
    
    font = pygame.font.SysFont('Arial', 18)
     
    y_offset = 60
    line_height = 30
     
    info_items = [
        ("Algorithm:", stats.get('algorithm', 'None')),
        ("Time:", f"{stats.get('time', 0):.3f}s"),
        ("Nodes Opened:", str(stats.get('nodes_opened', 0))),
        ("Nodes Closed:", str(stats.get('nodes_closed', 0))),
        ("Path Length:", str(stats.get('path_length', 0))),
        ("Status:", stats.get('status', 'Ready'))
    ]
    
    for label, value in info_items:
        label_text = font.render(label, True, color.UI_Text)
        value_text = font.render(value, True, color.UI_Status_Text)
        info_surface.blit(label_text, (20, y_offset))
        info_surface.blit(value_text, (150, y_offset))
        y_offset += line_height
    
    y_offset += 25
    instructions = [
        "Left Click -- Place Start/End/Wall",
        "Right Click -- Remove Start/End/Wall",
        "M -- Generate Maze",
        "Q -- Clear Path",
        "E -- Reset Grid"
    ]
    
    mid_title = pygame.font.SysFont('Arial', 30, bold=True)
    title = mid_title.render("GUIDE", True, color.UI_Title)
    info_surface.blit(title, (40, y_offset))

    y_offset += 35
    
    for instruction in instructions[0 :]:
        inst_text = font.render(instruction, True, color.UI_Guide)
        info_surface.blit(inst_text, (30, y_offset))
        y_offset += 20
    
    y_offset += 20
    end_title = pygame.font.SysFont('Arial' , 30 , bold=True)
    title = end_title.render("ALGORITHM" , True , color.UI_Title)
    info_surface.blit(title , (40 , y_offset))


    y_offset += 35
    algorithm_items = [
        "R --- A* Search",
        "T --- Breath First Search",
        "Y --- Depth First Search", 
        "U --- Best First Search",
        "I --- Dijkstra",
    ]

    for algorithm_item in algorithm_items:
        algorithm_text = font.render(algorithm_item , True , color.UI_Text)
        info_surface.blit(algorithm_text , (30 , y_offset))
        y_offset += 20

    win.blit(info_surface, (width, 0))