# PROJECT 3: BOOLEANS AND CONDITIONS
# Concepts: Boolean variables, if statements, logical operators
# Based on CodeHS Lessons 4.1 (Booleans) and 4.4 (If Statements)

import pygame

# Initialize PyGame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def main():
    """Main function demonstrating booleans and if statements"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 3: Conditional Colors")
    clock = pygame.time.Clock()
    
    # Boolean variables - these can only be True or False
    is_red = True
    is_large = False
    is_moving = False
    
    # Position variables
    circle_x = SCREEN_WIDTH // 2
    circle_y = SCREEN_HEIGHT // 2
    move_speed = 3
    
    print("Project 3: Conditional Colors")
    print("This demonstrates boolean variables and if statements")
    print("Controls:")
    print("- SPACE: Toggle color (red/blue)")
    print("- S: Toggle size (small/large)")
    print("- M: Toggle movement")
    print("- Close window to exit")
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Toggle the boolean variable using 'not'
                    is_red = not is_red
                    print(f"Color changed! is_red = {is_red}")
                elif event.key == pygame.K_s:
                    # Toggle size
                    is_large = not is_large
                    print(f"Size changed! is_large = {is_large}")
                elif event.key == pygame.K_m:
                    # Toggle movement
                    is_moving = not is_moving
                    print(f"Movement changed! is_moving = {is_moving}")
        
        # Update position if moving
        if is_moving:
            circle_x += move_speed
            # Bounce off edges
            if circle_x <= 50 or circle_x >= SCREEN_WIDTH - 50:
                move_speed = -move_speed
        
        # Clear screen
        screen.fill(WHITE)
        
        # Use if statements to determine color
        if is_red:
            color = RED
            color_name = "Red"
        else:
            color = BLUE
            color_name = "Blue"
        
        # Use if statements to determine size
        if is_large:
            radius = 80
            size_name = "Large"
        else:
            radius = 40
            size_name = "Small"
        
        # Draw the circle based on our boolean conditions
        pygame.draw.circle(screen, color, (int(circle_x), circle_y), radius)
        
        # Display current state information
        font = pygame.font.Font(None, 36)
        
        # Instructions
        instructions = [
            "Press SPACE to change color",
            "Press S to change size", 
            "Press M to toggle movement"
        ]
        
        for i, instruction in enumerate(instructions):
            text = font.render(instruction, True, BLACK)
            screen.blit(text, (10, 10 + i * 30))
        
        # Status information using boolean values
        status_font = pygame.font.Font(None, 28)
        status_y = 120
        
        status_texts = [
            f"is_red = {is_red} → Color: {color_name}",
            f"is_large = {is_large} → Size: {size_name}",
            f"is_moving = {is_moving}"
        ]
        
        for i, status in enumerate(status_texts):
            text = status_font.render(status, True, BLACK)
            screen.blit(text, (10, status_y + i * 25))
        
        # Demonstrate compound boolean conditions
        if is_red and is_large:
            bonus_text = status_font.render("Special: Big Red Circle!", True, RED)
            screen.blit(bonus_text, (10, status_y + 100))
        elif not is_red and is_large:
            bonus_text = status_font.render("Special: Big Blue Circle!", True, BLUE)
            screen.blit(bonus_text, (10, status_y + 100))
        
        # Update display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("You learned about:")
    print("- Boolean variables (True/False)")
    print("- If statements for making decisions")
    print("- Logical operators (and, or, not)")
    print("- How conditions control program behavior")

if __name__ == "__main__":
    main()