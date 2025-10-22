import color

import random
import pygame

class history_node:
    def __init__(self, stats):
        self.stat = stats
        self.next = None

def number_node(head):
    count = 0
    if head is None:
        return 0
    tmp = head
    while tmp is not None:
        tmp = tmp.next
        count += 1
    return count

def insert(head, stats, max_size=5):
    new_node = history_node(stats)
    if head is None:
        return new_node
    
    new_node.next = head
    head = new_node
    
    if number_node(head) > max_size:
        current = head
        for _ in range(max_size - 1):
            if current.next is not None:
                current = current.next
        current.next = None
    
    return head

def reset_node(head):
    return None

def draw_sub_window(win , width , head ,speed):
    sub_width = 600
    sub_height = width

    sub_surface  = pygame.Surface((sub_width , sub_height))
    sub_surface.fill(color.History_Back_Ground)

    # Draw title
    front_title = pygame.font.SysFont('Comic Sans MS' , 30 , bold=True )
    title = front_title.render("History" , True , color.History_Front_Title)
    sub_surface.blit(title , (250 , 0))

    # If there's no history data, show a message and exit
    if head is None:
        font = pygame.font.SysFont('Arial' , 20)
        no_data_text = pygame.font.SysFont('Comic Sans MS' , 30 , bold=True)
        title = no_data_text.render("No History Data", True, color.History_Error_Text)
        sub_surface.blit(title, (100, 100))
        win.blit(sub_surface, (width + 300, 0))
        return

    font = pygame.font.SysFont('Arial' , 20)
    current = head
    node_number = 1

    # Draw up to 5 history nodes
    while current is not None and node_number <= 5:
        stats = current.stat
        node_title = pygame.font.SysFont('Consolas', 30, bold=True)

        # Calculate row and column position for layout
        row = 0
        col = 0

        if node_number <= 3:
            col = 0 
            row = node_number - 1
        else:
            col = 1
            row = node_number - 4
        
        x_offset = 75 + col * 250
        y_offset = 35 +  row * 220

        title = node_title.render(f"Node {node_number}", True, color.History_Title)
        sub_surface.blit(title, (x_offset, y_offset))

        y_offset += 30
        
        # Prepare and draw node statistics
        node_list = [
            ("Algorithm:", stats.get('algorithm', 'None')),
            ("Time:", f"{stats.get('time', 0.0):.3f}s"),  
            ("Nodes Opened:", str(stats.get('nodes_opened', 0))),
            ("Nodes Closed:", str(stats.get('nodes_closed', 0))),
            ("Exploration Ratio" , f"{stats.get('exploration_ratio' , 0.0):.3f}%"),
            ("Path Length:", str(stats.get('path_length', 0))),
            ("Status:", stats.get('status', 'Ready')),
            ("Speed:", str(stats.get('speed', speed))),
            ("Difficult:", stats.get('difficult', 'None'))
        ]

        # Render each label and value pair
        for label, value in node_list:
            label_text = font.render(label, True, color.History_Text)
            value_text = font.render(value, True, color.History_Status)
            sub_surface.blit(label_text, (x_offset, y_offset))
            sub_surface.blit(value_text, (x_offset + 130 , y_offset))
            y_offset += 20
        
        current = current.next
        node_number += 1

    win.blit(sub_surface, (width + 300, 0))
