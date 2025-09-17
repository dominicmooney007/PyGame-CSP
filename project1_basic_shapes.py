# PROJECT 1: BASIC GRAPHICS AND VARIABLES
# Concepts: Variables, print statements, basic graphics
# Based on CodeHS Lesson 3.5 (User Input) and 3.6 (Basic Math)

import pygame

# Initialize PyGame
pygame.init()

# Constants - these are variables that don't change
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def main():
    """Main function to run the basic shapes program"""
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 1: Basic Shapes with Variables")
    clock = pygame.time.Clock()
    
    # Variables for the circle
    circle_x = 200
    circle_y = 200
    circle_radius = 50
    
    # Variables for the rectangle
    rect_x = 400
    rect_y = 300
    rect_width = 100
    rect_height = 80
    
    print("Project 1: Basic Shapes with Variables")
    print("This program demonstrates how to use variables to draw shapes")
    print(f"Circle center: ({circle_x}, {circle_y}), radius: {circle_radius}")
    print(f"Rectangle position: ({rect_x}, {rect_y}), size: {rect_width}x{rect_height}")
    print("Close the window to exit.")
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen with white background
        screen.fill(WHITE)
        
        # Draw shapes using our variables
        pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)
        pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
        
        # Add some text to show variable values
        font = pygame.font.Font(None, 24)
        circle_text = font.render(f"Circle: ({circle_x}, {circle_y}), r={circle_radius}", True, BLACK)
        rect_text = font.render(f"Rectangle: ({rect_x}, {rect_y}), {rect_width}x{rect_height}", True, BLACK)
        
        screen.blit(circle_text, (10, 10))
        screen.blit(rect_text, (10, 35))
        
        # Update the display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("Program ended. Variables help us store and reuse values!")

if __name__ == "__main__":
    main()