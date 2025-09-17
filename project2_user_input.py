# PROJECT 2: USER INPUT AND MATH
# Concepts: User input, basic math operations, type conversion
# Based on CodeHS Lessons 3.5 (User Input) and 3.6 (Basic Math)

import pygame

# Initialize PyGame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)

def get_user_input():
    """Function to get input from the user"""
    print("Welcome to Shape Creator!")
    print("Let's create custom shapes based on your input.")
    
    # Get user input for circle
    circle_radius = int(input("Enter circle radius (10-100): "))
    
    # Validate input using if statements
    if circle_radius < 10:
        circle_radius = 10
        print("Radius too small, setting to 10")
    elif circle_radius > 100:
        circle_radius = 100
        print("Radius too large, setting to 100")
    
    # Get user input for rectangle
    rect_width = int(input("Enter rectangle width (50-200): "))
    rect_height = int(input("Enter rectangle height (50-200): "))
    
    # Validate rectangle dimensions
    if rect_width < 50:
        rect_width = 50
    elif rect_width > 200:
        rect_width = 200
        
    if rect_height < 50:
        rect_height = 50
    elif rect_height > 200:
        rect_height = 200
    
    return circle_radius, rect_width, rect_height

def main():
    """Main function to run the user input shapes program"""
    # Get user input before starting pygame
    circle_radius, rect_width, rect_height = get_user_input()
    
    # Calculate positions using math operations
    circle_x = SCREEN_WIDTH // 4  # Integer division
    circle_y = SCREEN_HEIGHT // 2
    
    # More complex math for rectangle positioning
    rect_x = (SCREEN_WIDTH * 3) // 4 - rect_width // 2
    rect_y = SCREEN_HEIGHT // 2 - rect_height // 2
    
    # Calculate area of rectangle (demonstrating multiplication)
    rect_area = rect_width * rect_height
    
    # Calculate circumference of circle (demonstrating math operations)
    pi = 3.14159
    circle_circumference = 2 * pi * circle_radius
    
    print(f"Circle circumference: {circle_circumference:.2f}")
    print(f"Rectangle area: {rect_area}")
    print("Starting the graphics program...")
    
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 2: User Input Shapes")
    clock = pygame.time.Clock()
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(WHITE)
        
        # Draw user-customized shapes
        pygame.draw.circle(screen, GREEN, (circle_x, circle_y), circle_radius)
        pygame.draw.rect(screen, PURPLE, (rect_x, rect_y, rect_width, rect_height))
        
        # Display the calculations
        font = pygame.font.Font(None, 28)
        title_text = font.render("Your Custom Shapes!", True, BLACK)
        circle_info = font.render(f"Circle: radius = {circle_radius}, circumference = {circle_circumference:.1f}", True, BLACK)
        rect_info = font.render(f"Rectangle: {rect_width} x {rect_height}, area = {rect_area}", True, BLACK)
        
        screen.blit(title_text, (10, 10))
        screen.blit(circle_info, (10, 45))
        screen.blit(rect_info, (10, 75))
        
        # Update display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("Thanks for using Shape Creator!")
    print("You learned about user input, type conversion, and basic math!")

if __name__ == "__main__":
    main()