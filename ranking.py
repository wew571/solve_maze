import color

import pygame

# This class is a binary search tree (BST)
class rankingTimeNode:
    def __init__(self , stats):
        self.stat = stats
        self.left = None
        self.right = None

class rankingExplorationRatioNode:
    def __init__(self , stats):
        self.stat = stats
        self.left = None
        self.right = None

def insertTimeNode(root , stats):
    new_node = rankingTimeNode(stats)
    if root is None:
        return new_node
    
    new_time = stats['time']
    current_time = root.stat['time']

    if new_time < current_time:
        root.left = insertTimeNode(root.left , stats)
    if new_time > current_time:
        root.right = insertTimeNode(root.right , stats)

    return root


def insertExplorationRatioNode(root , stats):
    new_node = rankingExplorationRatioNode(stats)
    if root is None:
        return new_node
    
    new_exploration_ratio = stats['exploration_ratio']
    current_exploration_ratio = root.stat['exploration_ratio']

    if new_exploration_ratio < current_exploration_ratio:
        root.left = insertExplorationRatioNode(root.left , stats)
    if new_exploration_ratio > current_exploration_ratio:
        root.right = insertExplorationRatioNode(root.right , stats)

    return root

def findSlowestTime(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.stat

def findLowestExplorationRatio(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.stat

def resetTimeNode(root_time):
    return None

def resetExplorationRatio(root_exploration_ratio):
    return None

def drawCompareWindow(win , width , root_time , root_exploration_ratio , speed):
    compare_width = 600
    compare_height = 310

    compare_surface  = pygame.Surface((compare_width , compare_height))
    compare_surface.fill(color.Compare_Back_Ground)

    y_offset = 0

    font = pygame.font.SysFont('Arial' , 20 )

    best_time = findSlowestTime(root_time)
    best_exploration_ratio = findLowestExplorationRatio(root_exploration_ratio)

    # Draw title 
    front_title = pygame.font.SysFont('Courier New' , 40 , bold=True)
    title = front_title.render("Ranking" , True , color.Compare_Front_Title)
    compare_surface.blit(title , ( 250 , y_offset))

    # If there's no history data, show a message and exit
    if root_time is None or root_exploration_ratio is None:
        font = pygame.font.SysFont('Arial' , 20)
        no_data_text = pygame.font.SysFont('Comic Sans MS' , 30 , bold=True)
        title = no_data_text.render("No Data", True, color.Compare_Error_Text)
        compare_surface.blit(title, (100, 100))
        win.blit(compare_surface, (width + 300, 690))
        return
    
    # Draw time 
    y_offset += 40
    time_title = pygame.font.SysFont('Times New Roman' , 30 , bold=True)
    title = time_title.render("Best Time Solve" , True , color.Compare_Title)
    compare_surface.blit(title , ( 20 , y_offset))

    y_offset += 35
    ranking_time_list  = [
        ("Algorithm:" , best_time.get('algorithm' , 'None')),
        ("Time:", f"{best_time.get('time', 0):.3f}s"),
        ("Nodes Opened:", str(best_time.get('nodes_opened', 0))),
        ("Nodes Closed:", str(best_time.get('nodes_closed', 0))),
        ("Exploration Ratio:" , f"{best_time.get('exploration_ratio' , 0):.3f}%"),
        ("Path Length:", str(best_time.get('path_length', 0))),
        ("Status:", best_time.get('status', 'Ready')),
        ("Speed:" , str(best_time.get('speed', speed))),
        ("Difficult:" , best_time.get('difficult' , 'None'))
    ]

    for lable , value in ranking_time_list:
        lable_text = font.render(lable , True , color.Compare_Text)
        value_text = font.render(value , True , color.Compare_Status)
        compare_surface.blit(lable_text , ( 20 , y_offset))
        compare_surface.blit(value_text , ( 160 , y_offset))
        y_offset += 20

    # Draw exploration ratio in other size
    y_offset = 40
    exploration_ratio_title = pygame.font.SysFont('Times New Roman' , 30 , bold=True)
    title = exploration_ratio_title.render("Best Exploration Ratio" , True , color.Compare_Title)
    compare_surface.blit(title , (300 , y_offset))

    y_offset += 35
    ranking_exploration_ratio_list = [
        ("Algorithm:" , best_exploration_ratio.get('algorithm' , 'None')),
        ("Time:", f"{best_exploration_ratio.get('time', 0):.3f}s"),
        ("Nodes Opened:", str(best_exploration_ratio.get('nodes_opened', 0))),
        ("Nodes Closed:", str(best_exploration_ratio.get('nodes_closed', 0))),
        ("Exploration Ratio:" , f"{best_exploration_ratio.get('exploration_ratio' , 0):.3f}%"),
        ("Path Length:", str(best_exploration_ratio.get('path_length', 0))),
        ("Status:", best_exploration_ratio.get('status', 'Ready')),
        ("Speed:" , str(best_exploration_ratio.get('speed', speed))),
        ("Difficult:" , best_exploration_ratio.get('difficult' , 'None'))
    ]

    for lable , value in ranking_exploration_ratio_list:
        lable_text = font.render(lable , True , color.Compare_Text)
        value_text = font.render(value , True , color.Compare_Status)
        compare_surface.blit(lable_text , ( 300 , y_offset))
        compare_surface.blit(value_text , ( 460 , y_offset))
        y_offset += 20

    win.blit(compare_surface, (width + 300, 690))
