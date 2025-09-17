# PROJECT 8: WHILE LOOPS AND ANIMATION
# Concepts: While loops, continuous updates, counters, collision detection
# Based on CodeHS Lesson 4.10 (While Loops)

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
ORANGE = (255, 165, 0)

def main():
    """Main function demonstrating while loop concepts with animation"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 8: Bouncing Ball - While Loop Demo")
    clock = pygame.time.Clock()
    
    print("Project 8: Bouncing Ball Animation")
    print("This demonstrates while loop concepts:")
    print("- The main game loop is a while loop (while running)")
    print("- Counters that increment during the loop")
    print("- Continuous updates and condition checking")
    print("- Variables that change each iteration")
    print("Controls:")
    print("- SPACE: Pause/Resume animation")
    print("- R: Reset ball position and counters")
    print("- Close window to exit")
    
    # Ball properties (variables that will change in the while loop)
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    ball_radius = 30
    ball_speed_x = 5
    ball_speed_y = 3
    ball_color = RED
    
    # Counter variables (demonstrating while loop counters)
    bounce_counter = 0
    frame_counter = 0
    color_counter = 0
    
    # List of colors to cycle through
    colors = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]
    color_names = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"]
    
    # Animation control
    is_paused = False
    
    print("Starting the while loop animation...")
    
    running = True
    # This while loop demonstrates the main concept from the While Loops lesson
    while running:  # This is our main while loop!
        frame_counter += 1  # Counter increments each loop iteration
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_paused = not is_paused
                    print(f"Animation {'paused' if is_paused else 'resumed'}")
                elif event.key == pygame.K_r:
                    # Reset all variables (like restarting the while loop conditions)
                    ball_x = SCREEN_WIDTH // 2
                    ball_y = SCREEN_HEIGHT // 2
                    ball_speed_x = 5
                    ball_speed_y = 3
                    bounce_counter = 0
                    frame_counter = 0
                    color_counter = 0
                    ball_color = RED
                    print("Ball reset! Counters reset!")
        
        # Only update if not paused
        if not is_paused:
            # Update ball position (variables change each while loop iteration)
            ball_x += ball_speed_x
            ball_y += ball_speed_y
            
            # Collision detection with boundaries
            # These if statements run every while loop iteration
            if ball_x <= ball_radius or ball_x >= SCREEN_WIDTH - ball_radius:
                ball_speed_x = -ball_speed_x  # Reverse direction
                bounce_counter += 1  # Increment counter
                color_counter += 1
                ball_color = colors[color_counter % len(colors)]
                print(f"Horizontal bounce #{bounce_counter}! Color: {color_names[color_counter % len(colors)]}")
            
            if ball_y <= ball_radius or ball_y >= SCREEN_HEIGHT - ball_radius:
                ball_speed_y = -ball_speed_y  # Reverse direction
                bounce_counter += 1  # Increment counter
                color_counter += 1
                ball_color = colors[color_counter % len(colors)]
                print(f"Vertical bounce #{bounce_counter}! Color: {color_names[color_counter % len(colors)]}")
        
        # Clear screen
        screen.fill(WHITE)
        
        # Draw ball
        pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)
        
        # Draw boundary lines to show collision areas
        pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 3)
        
        # Display while loop information
        font = pygame.font.Font(None, 28)
        info_texts = [
            "While Loop Animation Demo",
            f"Frame count: {frame_counter} (increments each loop)",
            f"Bounces: {bounce_counter} (increments on condition)",
            f"Ball position: ({int(ball_x)}, {int(ball_y)}) (changes each loop)",
            f"Ball speed: ({ball_speed_x}, {ball_speed_y})",
            f"Current color: {color_names[color_counter % len(colors)]}"
        ]
        
        for i, text in enumerate(info_texts):
            if i == 0:  # Title
                color = BLACK
                font_size = 32
                title_font = pygame.font.Font(None, font_size)
                rendered_text = title_font.render(text, True, color)
            else:
                color = BLACK
                rendered_text = font.render(text, True, color)
            
            screen.blit(rendered_text, (10, 10 + i * 30))
        
        # Show pause status
        if is_paused:
            pause_font = pygame.font.Font(None, 48)
            pause_text = pause_font.render("PAUSED", True, RED)
            pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(pause_text, pause_rect)
        
        # Instructions
        instruction_font = pygame.font.Font(None, 24)
        instructions = [
            "SPACE: Pause/Resume",
            "R: Reset ball and counters"
        ]
        
        for i, instruction in enumerate(instructions):
            text = instruction_font.render(instruction, True, BLACK)
            screen.blit(text, (10, SCREEN_HEIGHT - 50 + i * 25))
        
        # Show while loop pseudocode
        code_font = pygame.font.Font(None, 20)
        code_lines = [
            "while running:",
            "    frame_counter += 1",
            "    ball_x += ball_speed_x", 
            "    ball_y += ball_speed_y",
            "    if collision:",
            "        bounce_counter += 1",
            "        change_color()"
        ]
        
        code_bg = pygame.Surface((200, len(code_lines) * 22 + 10))
        code_bg.fill((240, 240, 240))
        screen.blit(code_bg, (SCREEN_WIDTH - 210, 10))
        
        for i, line in enumerate(code_lines):
            text = code_font.render(line, True, BLUE)
            screen.blit(text, (SCREEN_WIDTH - 205, 15 + i * 22))
        
        # Update display
        pygame.display.flip()
        clock.tick(60)  # Control the while loop speed
    
    # When we exit the while loop
    pygame.quit()
    print(f"While loop ended after {frame_counter} iterations")
    print(f"Total bounces: {bounce_counter}")
    print("You learned about:")
    print("- While loops continue until a condition is false")
    print("- Counters that increment each loop iteration")
    print("- Variables that update continuously in loops")
    print("- Conditional statements inside loops")
    print("- How while loops control program flow")

if __name__ == "__main__":
    main()