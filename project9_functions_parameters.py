# PROJECT 9: FUNCTIONS WITH PARAMETERS AND RETURN VALUES
# Concepts: Function definition, parameters, return values, code reuse
# Based on CodeHS Lessons 5.3 (Functions and Parameters) and 5.5 (Functions and Return Values)

import pygame
import math

# Initialize PyGame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BROWN = (101, 67, 33)
GRAY = (128, 128, 128)

# Function definitions demonstrating parameters and return values

def draw_house(screen, x, y, width, height, roof_color, wall_color):
    """
    Function with multiple parameters to draw a house
    Parameters: screen, x, y, width, height, roof_color, wall_color
    No return value (None)
    """
    print(f"Drawing house at ({x}, {y}) with size {width}x{height}")
    
    # Draw walls using parameters
    pygame.draw.rect(screen, wall_color, (x, y, width, height))
    
    # Draw roof using parameters  
    roof_height = height // 3
    roof_points = [(x, y), (x + width//2, y - roof_height), (x + width, y)]
    pygame.draw.polygon(screen, roof_color, roof_points)
    
    # Draw door using parameters for positioning
    door_width = width // 4
    door_height = height // 2
    door_x = x + width//2 - door_width//2
    door_y = y + height - door_height
    pygame.draw.rect(screen, BROWN, (door_x, door_y, door_width, door_height))
    
    # Draw windows
    window_size = width // 8
    window1_x = x + width//4 - window_size//2
    window2_x = x + 3*width//4 - window_size//2
    window_y = y + height//3
    
    pygame.draw.rect(screen, YELLOW, (window1_x, window_y, window_size, window_size))
    pygame.draw.rect(screen, YELLOW, (window2_x, window_y, window_size, window_size))
    pygame.draw.rect(screen, BLACK, (window1_x, window_y, window_size, window_size), 2)
    pygame.draw.rect(screen, BLACK, (window2_x, window_y, window_size, window_size), 2)

def draw_star(screen, x, y, size, color):
    """
    Function with parameters to draw a star
    Parameters: screen, x, y, size, color
    No return value (None)
    """
    print(f"Drawing star at ({x}, {y}) with size {size}")
    
    # Calculate star points using the size parameter
    points = []
    for i in range(10):
        angle = i * math.pi / 5
        if i % 2 == 0:
            radius = size
        else:
            radius = size // 2
        
        point_x = x + radius * math.cos(angle)
        point_y = y + radius * math.sin(angle)
        points.append((point_x, point_y))
    
    pygame.draw.polygon(screen, color, points)

def calculate_distance(x1, y1, x2, y2):
    """
    Function that takes parameters and RETURNS a value
    Parameters: x1, y1, x2, y2 (coordinates of two points)
    Returns: distance between the points (float)
    """
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance  # This function returns a value!

def get_color_by_distance(distance):
    """
    Function that takes a parameter and returns a value based on conditions
    Parameter: distance (float)
    Returns: color tuple based on distance
    """
    if distance < 50:
        return RED
    elif distance < 100:
        return YELLOW
    elif distance < 150:
        return GREEN
    else:
        return BLUE

def draw_tree(screen, x, y, height):
    """
    Function with parameters, uses calculations with the parameters
    Parameters: screen, x, y, height
    No return value (None)
    """
    # Trunk dimensions based on height parameter
    trunk_width = height // 8
    trunk_height = height // 3
    trunk_x = x - trunk_width // 2
    trunk_y = y
    
    # Draw trunk
    pygame.draw.rect(screen, BROWN, (trunk_x, trunk_y, trunk_width, trunk_height))
    
    # Leaves dimensions based on height parameter
    leaves_radius = height // 4
    leaves_y = y - trunk_height // 2
    
    # Draw leaves
    pygame.draw.circle(screen, GREEN, (x, leaves_y), leaves_radius)

def is_point_in_circle(point_x, point_y, circle_x, circle_y, radius):
    """
    Function that returns a boolean value
    Parameters: point coordinates, circle center, radius
    Returns: True if point is inside circle, False otherwise
    """
    distance = calculate_distance(point_x, point_y, circle_x, circle_y)
    return distance <= radius  # Returns True or False

def main():
    """Main function demonstrating functions with parameters and return values"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 9: Functions with Parameters")
    clock = pygame.time.Clock()
    
    print("Project 9: Functions with Parameters and Return Values")
    print("This demonstrates:")
    print("- Functions with multiple parameters")
    print("- Functions that return values")
    print("- Using returned values in calculations")
    print("- Code reuse through functions")
    print("- Move mouse to see distance calculations")
    print("- Close window to exit")
    
    # Initial mouse position
    mouse_x, mouse_y = 0, 0
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Clear screen
        screen.fill(WHITE)
        
        # Title
        title_font = pygame.font.Font(None, 32)
        title = title_font.render("Functions with Parameters Demo", True, BLACK)
        screen.blit(title, (200, 10))
        
        # Draw multiple houses using the same function with different parameters
        draw_house(screen, 50, 400, 120, 100, RED, YELLOW)      # Small yellow house
        draw_house(screen, 200, 350, 150, 120, BLUE, GREEN)     # Medium green house  
        draw_house(screen, 400, 380, 100, 90, GREEN, PURPLE)    # Small purple house
        
        # Draw stars using the same function with different parameters
        draw_star(screen, 100, 100, 30, YELLOW)   # Medium star
        draw_star(screen, 250, 80, 20, YELLOW)    # Small star
        draw_star(screen, 180, 120, 35, YELLOW)   # Large star
        
        # Draw trees with different heights
        draw_tree(screen, 600, 450, 120)  # Tall tree
        draw_tree(screen, 700, 470, 80)   # Short tree
        
        # Demonstrate return values with distance calculation
        center_x, center_y = 400, 200
        
        # Use the function that returns a value
        distance = calculate_distance(center_x, center_y, mouse_x, mouse_y)
        
        # Use the returned distance in another function
        circle_color = get_color_by_distance(distance)
        
        # Circle size based on returned distance value
        circle_size = max(20, min(80, int(distance / 3)))
        
        pygame.draw.circle(screen, circle_color, (center_x, center_y), circle_size)
        
        # Show if mouse is inside the circle using boolean return function
        mouse_in_circle = is