# PROJECT 5: KEY EVENTS AND MOVEMENT
# Concepts: Keyboard events, variable updates, boundary checking
# Based on CodeHS Lesson 4.5 (Key Events)

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

def main():
    """Main function demonstrating keyboard events and movement"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 5: Keyboard Movement")
    clock = pygame.time.Clock()
    
    # Player properties
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    player_size = 40
    speed = 5
    
    # Color change variables
    player_color = RED
    color_index = 0
    colors = [RED, GREEN, BLUE]
    color_names = ["Red", "Green", "Blue"]
    
    print("Project 5: Keyboard Movement")
    print("This demonstrates keyboard event handling")
    print("Controls:")
    print("- Arrow keys OR WASD: Move the circle")
    print("- SPACE: Change color")
    print("- The circle stays within the screen boundaries")
    print("- Close window to exit")
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Change color when space is pressed
                    color_index = (color_index + 1) % len(colors)
                    player_color = colors[color_index]
                    print(f"Color changed to {color_names[color_index]}")
        
        # Check for continuous key presses (for smooth movement)
        keys = pygame.key.get_pressed()
        
        # Movement with arrow keys or WASD
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y += speed
        
        # Keep player within screen boundaries
        # This demonstrates comparison operators and if statements
        if player_x < player_size:
            player_x = player_size
        elif player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size
            
        if player_y < player_size:
            player_y = player_size
        elif player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size
        
        # Clear screen
        screen.fill(WHITE)
        
        # Draw player
        pygame.draw.circle(screen, player_color, (player_x, player_y), player_size)
        
        # Draw boundary indicators
        pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2)
        
        # Display instructions and information
        font = pygame.font.Font(None, 28)
        instructions = [
            "Use arrow keys or WASD to move!",
            "Press SPACE to change color",
            f"Position: ({player_x}, {player_y})",
            f"Color: {color_names[color_index]}"
        ]
        
        for i, instruction in enumerate(instructions):
            if i == 3:  # Color the color text with current color
                text = font.render(instruction, True, player_color)
            else:
                text = font.render(instruction, True, BLACK)
            screen.blit(text, (10, 10 + i * 30))
        
        # Show which keys are currently pressed (for educational purposes)
        pressed_keys = []
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pressed_keys.append("LEFT")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pressed_keys.append("RIGHT")
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pressed_keys.append("UP")
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pressed_keys.append("DOWN")
        
        if pressed_keys:
            keys_text = font.render(f"Pressed: {', '.join(pressed_keys)}", True, BLACK)
            screen.blit(keys_text, (10, 130))
        
        # Draw coordinate system reference
        small_font = pygame.font.Font(None, 20)
        corner_text = small_font.render("(0,0)", True, BLACK)
        screen.blit(corner_text, (5, 5))
        
        max_text = small_font.render(f"({SCREEN_WIDTH},{SCREEN_HEIGHT})", True, BLACK)
        screen.blit(max_text, (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 20))
        
        # Update display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print(f"Final position: ({player_x}, {player_y})")
    print("You learned about:")
    print("- Keyboard event handling")
    print("- Continuous key press detection")
    print("- Boundary checking with comparison operators")
    print("- Smooth character movement")
    print("- Coordinate systems")

if __name__ == "__main__":
    main()