# PROJECT 6: FOR LOOPS AND PATTERNS
# Concepts: For loops, range function, nested loops, modulus operator
# Based on CodeHS Lessons 4.6 (For Loops) and 4.7 (General For Loops)

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

def draw_pattern_1(screen):
    """Pattern 1: Single row of circles using for loop"""
    print("Drawing Pattern 1: Row of circles")
    
    # Draw title
    font = pygame.font.Font(None, 24)
    title = font.render("Pattern 1: For loop creating a row", True, BLACK)
    screen.blit(title, (20, 50))
    
    # Use for loop to create a row of circles
    for i in range(10):
        x = 50 + i * 70  # Calculate x position using loop variable
        y = 90
        pygame.draw.circle(screen, RED, (x, y), 25)
        
        # Show the loop variable value
        small_font = pygame.font.Font(None, 20)
        number = small_font.render(str(i), True, WHITE)
        number_rect = number.get_rect(center=(x, y))
        screen.blit(number, number_rect)

def draw_pattern_2(screen):
    """Pattern 2: Grid using nested loops"""
    print("Drawing Pattern 2: Grid with nested loops")
    
    # Draw title
    font = pygame.font.Font(None, 24)
    title = font.render("Pattern 2: Nested loops creating a grid", True, BLACK)
    screen.blit(title, (20, 180))
    
    # Nested for loops to create a grid
    for row in range(4):
        for col in range(6):
            x = 50 + col * 120
            y = 220 + row * 80
            
            # Use modulus operator to alternate colors
            if (row + col) % 2 == 0:
                color = BLUE
            else:
                color = GREEN
            
            pygame.draw.rect(screen, color, (x, y, 100, 60))
            
            # Show row and column numbers
            small_font = pygame.font.Font(None, 18)
            coord_text = small_font.render(f"({row},{col})", True, WHITE)
            text_rect = coord_text.get_rect(center=(x + 50, y + 30))
            screen.blit(coord_text, text_rect)

def draw_pattern_3(screen):
    """Pattern 3: Concentric circles with decreasing size"""
    print("Drawing Pattern 3: Concentric circles")
    
    # Draw title
    font = pygame.font.Font(None, 24)
    title = font.render("Pattern 3: Decreasing circles", True, BLACK)
    screen.blit(title, (500, 380))
    
    center_x = 600
    center_y = 480
    
    # For loop with decreasing values
    for i in range(6):
        radius = 90 - i * 15  # Decrease radius each iteration
        
        # Change color based on loop variable
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        color = colors[i % len(colors)]
        
        pygame.draw.circle(screen, color, (center_x, center_y), radius, 3)

def draw_pattern_4(screen):
    """Pattern 4: Demonstrate different range() parameters"""
    print("Drawing Pattern 4: Different range parameters")
    
    # Draw title
    font = pygame.font.Font(None, 24)
    title = font.render("Pattern 4: Different range() uses", True, BLACK)
    screen.blit(title, (20, 380))
    
    # Range with start, stop, and step
    y_pos = 420
    
    # Counting by 2s: range(start, stop, step)
    for i in range(2, 20, 2):  # Start at 2, go to 20, step by 2
        x = 20 + i * 10
        pygame.draw.rect(screen, PURPLE, (x, y_pos, 15, 30))
        
        # Show the value
        small_font = pygame.font.Font(None, 16)
        number = small_font.render(str(i), True, WHITE)
        number_rect = number.get_rect(center=(x + 7, y_pos + 15))
        screen.blit(number, number_rect)
    
    # Countdown: range(start, stop, negative_step)
    for i in range(10, 0, -1):  # Start at 10, go down to 1
        x = 300 + (10 - i) * 25
        pygame.draw.circle(screen, ORANGE, (x, y_pos + 15), i + 5)
        
        # Show the countdown number
        small_font = pygame.font.Font(None, 16)
        number = small_font.render(str(i), True, WHITE)
        number_rect = number.get_rect(center=(x, y_pos + 15))
        screen.blit(number, number_rect)

def main():
    """Main function demonstrating for loops and patterns"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 6: Loop Patterns")
    clock = pygame.time.Clock()
    
    print("Project 6: Loop Patterns")
    print("This demonstrates for loops and the range() function")
    print("You'll see several patterns created using different loop techniques:")
    print("1. Simple for loop with range()")
    print("2. Nested loops for grids")
    print("3. Loops with calculations")
    print("4. Different range() parameters")
    print("- Close window to exit")
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(WHITE)
        
        # Draw main title
        title_font = pygame.font.Font(None, 36)
        main_title = title_font.render("For Loop Patterns Demo", True, BLACK)
        screen.blit(main_title, (250, 10))
        
        # Draw all patterns
        draw_pattern_1(screen)
        draw_pattern_2(screen)
        draw_pattern_3(screen)
        draw_pattern_4(screen)
        
        # Add explanation text
        explanation_font = pygame.font.Font(None, 20)
        explanations = [
            "• range(10) creates numbers 0-9",
            "• range(2, 20, 2) creates 2, 4, 6, 8, ..., 18", 
            "• range(10, 0, -1) counts down 10, 9, 8, ..., 1",
            "• Nested loops: outer loop runs, inner loop completes fully",
            "• Modulus (%) creates alternating patterns"
        ]
        
        for i, explanation in enumerate(explanations):
            text = explanation_font.render(explanation, True, BLACK)
            screen.blit(text, (20, 520 + i * 15))
        
        # Update display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("You learned about:")
    print("- For loops with range()")
    print("- Different range() parameters (start, stop, step)")
    print("- Nested loops for creating grids")
    print("- Using loop variables in calculations")
    print("- Modulus operator (%) for patterns")
    print("- How loops help avoid repetitive code")

if __name__ == "__main__":
    main()