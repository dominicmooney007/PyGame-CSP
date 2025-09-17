# PROJECT 4: MOUSE EVENTS
# Concepts: Event handling, mouse clicks, lists
# Based on CodeHS Lesson 3.8 (Mouse Events)

import pygame

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

def main():
    """Main function demonstrating mouse events"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 4: Click to Create Circles")
    clock = pygame.time.Clock()
    
    # List to store circle information
    # Each circle will be stored as a dictionary with position and color
    circles = []
    
    # Available colors
    colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
    color_names = ["Red", "Green", "Blue", "Yellow", "Purple"]
    
    print("Project 4: Mouse Click Circles")
    print("This demonstrates mouse event handling")
    print("- Click anywhere to create circles")
    print("- Each circle will have a different color")
    print("- Press C to clear all circles")
    print("- Close window to exit")
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse was clicked!
                if event.button == 1:  # Left mouse button
                    # Get mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    # Choose color based on number of circles (cycling through colors)
                    color_index = len(circles) % len(colors)
                    chosen_color = colors[color_index]
                    chosen_color_name = color_names[color_index]
                    
                    # Add new circle to our list
                    new_circle = {
                        'x': mouse_x,
                        'y': mouse_y,
                        'color': chosen_color,
                        'color_name': chosen_color_name
                    }
                    circles.append(new_circle)
                    
                    print(f"Circle #{len(circles)} created at ({mouse_x}, {mouse_y}) - {chosen_color_name}")
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    # Clear all circles
                    circles = []
                    print("All circles cleared!")
        
        # Clear screen
        screen.fill(WHITE)
        
        # Draw all circles
        for i, circle in enumerate(circles):
            pygame.draw.circle(screen, circle['color'], (circle['x'], circle['y']), 30)
            
            # Optional: Draw circle number
            font = pygame.font.Font(None, 24)
            number_text = font.render(str(i + 1), True, WHITE)
            text_rect = number_text.get_rect(center=(circle['x'], circle['y']))
            screen.blit(number_text, text_rect)
        
        # Display instructions and information
        font = pygame.font.Font(None, 32)
        instructions = [
            "Click anywhere to create circles!",
            "Press C to clear all circles",
            f"Circles created: {len(circles)}"
        ]
        
        for i, instruction in enumerate(instructions):
            text = font.render(instruction, True, BLACK)
            screen.blit(text, (10, 10 + i * 35))
        
        # Show what color will be next
        if len(circles) < 100:  # Avoid showing this when too many circles
            next_color_index = len(circles) % len(colors)
            next_color = colors[next_color_index]
            next_color_name = color_names[next_color_index]
            
            next_text = font.render(f"Next color: {next_color_name}", True, next_color)
            screen.blit(next_text, (10, 120))
        
        # Display mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_text = font.render(f"Mouse: ({mouse_x}, {mouse_y})", True, BLACK)
        screen.blit(mouse_text, (SCREEN_WIDTH - 200, 10))
        
        # Update display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print(f"Final count: {len(circles)} circles created")
    print("You learned about:")
    print("- Mouse event handling")
    print("- Storing data in lists")
    print("- Event types and properties")
    print("- Interactive program design")

if __name__ == "__main__":
    main()