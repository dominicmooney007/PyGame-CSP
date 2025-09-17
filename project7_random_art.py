# PROJECT 7: RANDOM NUMBERS
# Concepts: Random number generation, random.choice(), random.randint()
# Based on CodeHS Lesson 4.9 (Random Numbers)

import pygame
import random

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
CYAN = (0, 255, 255)
PINK = (255, 192, 203)

def generate_random_art(screen):
    """Generate random art using various random functions"""
    print("Generating new random art...")
    
    # List of possible colors
    colors = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN, PINK]
    
    # Clear screen with a random background color
    background_colors = [WHITE, (240, 240, 240), (250, 250, 250)]
    bg_color = random.choice(background_colors)
    screen.fill(bg_color)
    
    # Generate random shapes
    num_shapes = random.randint(15, 25)  # Random number of shapes
    print(f"Creating {num_shapes} random shapes")
    
    for i in range(num_shapes):
        # Random position within screen bounds
        margin = 50
        x = random.randint(margin, SCREEN_WIDTH - margin)
        y = random.randint(margin, SCREEN_HEIGHT - margin)
        
        # Random color from our list
        color = random.choice(colors)
        
        # Random shape type (1, 2, or 3)
        shape_type = random.randint(1, 3)
        
        if shape_type == 1:
            # Random circle
            radius = random.randint(10, 50)
            pygame.draw.circle(screen, color, (x, y), radius)
            print(f"Circle at ({x}, {y}) with radius {radius}")
            
        elif shape_type == 2:
            # Random rectangle
            width = random.randint(30, 100)
            height = random.randint(30, 100)
            pygame.draw.rect(screen, color, (x, y, width, height))
            print(f"Rectangle at ({x}, {y}) size {width}x{height}")
            
        else:
            # Random line
            end_x = random.randint(margin, SCREEN_WIDTH - margin)
            end_y = random.randint(margin, SCREEN_HEIGHT - margin)
            thickness = random.randint(2, 8)
            pygame.draw.line(screen, color, (x, y), (end_x, end_y), thickness)
            print(f"Line from ({x}, {y}) to ({end_x}, {end_y})")

def draw_random_dice(screen):
    """Draw random dice rolls"""
    dice_x = 50
    dice_y = 50
    dice_size = 80
    
    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    print(f"Dice roll: {die1} and {die2} (Total: {die1 + die2})")
    
    # Draw dice backgrounds
    pygame.draw.rect(screen, WHITE, (dice_x, dice_y, dice_size, dice_size))
    pygame.draw.rect(screen, BLACK, (dice_x, dice_y, dice_size, dice_size), 3)
    
    pygame.draw.rect(screen, WHITE, (dice_x + 100, dice_y, dice_size, dice_size))
    pygame.draw.rect(screen, BLACK, (dice_x + 100, dice_y, dice_size, dice_size), 3)
    
    # Draw dots on dice
    dot_positions = {
        1: [(40, 40)],
        2: [(20, 20), (60, 60)],
        3: [(20, 20), (40, 40), (60, 60)],
        4: [(20, 20), (20, 60), (60, 20), (60, 60)],
        5: [(20, 20), (20, 60), (40, 40), (60, 20), (60, 60)],
        6: [(20, 20), (20, 40), (20, 60), (60, 20), (60, 40), (60, 60)]
    }
    
    # Draw dots for first die
    for dot_x, dot_y in dot_positions[die1]:
        pygame.draw.circle(screen, BLACK, (dice_x + dot_x, dice_y + dot_y), 6)
    
    # Draw dots for second die
    for dot_x, dot_y in dot_positions[die2]:
        pygame.draw.circle(screen, BLACK, (dice_x + 100 + dot_x, dice_y + dot_y), 6)
    
    # Show the values and total
    font = pygame.font.Font(None, 32)
    dice_text = font.render(f"Dice: {die1} + {die2} = {die1 + die2}", True, BLACK)
    screen.blit(dice_text, (dice_x, dice_y + dice_size + 10))

def coin_flip():
    """Simulate a coin flip"""
    flip = random.choice(["Heads", "Tails"])
    print(f"Coin flip: {flip}")
    return flip

def draw_random_colors_demo(screen):
    """Show random color selection"""
    colors = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]
    color_names = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"]
    
    y_start = 200
    
    font = pygame.font.Font(None, 28)
    title = font.render("Random Color Selection:", True, BLACK)
    screen.blit(title, (50, y_start - 30))
    
    for i in range(6):
        # Random color selection
        random_index = random.randint(0, len(colors) - 1)
        chosen_color = colors[random_index]
        chosen_name = color_names[random_index]
        
        # Draw color square
        square_x = 50 + i * 110
        square_y = y_start
        pygame.draw.rect(screen, chosen_color, (square_x, square_y, 80, 60))
        pygame.draw.rect(screen, BLACK, (square_x, square_y, 80, 60), 2)
        
        # Label the color
        small_font = pygame.font.Font(None, 20)
        color_text = small_font.render(chosen_name, True, BLACK)
        screen.blit(color_text, (square_x + 5, square_y + 65))

def main():
    """Main function demonstrating random numbers"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 7: Random Art Generator")
    clock = pygame.time.Clock()
    
    print("Project 7: Random Art Generator")
    print("This demonstrates random number generation")
    print("Functions demonstrated:")
    print("- random.randint(a, b): Random integer between a and b")
    print("- random.choice(list): Random item from a list")  
    print("- Using randomness for art, games, and simulations")
    print("Controls:")
    print("- SPACE: Generate new random art")
    print("- D: Roll dice")
    print("- C: Flip coin")
    print("- Close window to exit")
    
    # Start with instructions
    screen.fill(WHITE)
    font = pygame.font.Font(None, 48)
    instruction_text = font.render("Press SPACE for Random Art!", True, BLACK)
    instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.blit(instruction_text, instruction_rect)
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Generate new random art
                    generate_random_art(screen)
                    
                elif event.key == pygame.K_d:
                    # Roll dice
                    screen.fill(WHITE)
                    draw_random_dice(screen)
                    
                    # Add instruction
                    font = pygame.font.Font(None, 24)
                    instruction = font.render("Press SPACE for art, D for new dice roll", True, BLACK)
                    screen.blit(instruction, (250, 50))
                    
                elif event.key == pygame.K_c:
                    # Flip coin
                    screen.fill(WHITE)
                    
                    # Perform multiple flips to show randomness
                    flips = []
                    for i in range(10):
                        flips.append(coin_flip())
                    
                    # Display results
                    font = pygame.font.Font(None, 36)
                    title = font.render("Coin Flip Results:", True, BLACK)
                    screen.blit(title, (300, 100))
                    
                    heads_count = flips.count("Heads")
                    tails_count = flips.count("Tails")
                    
                    for i, flip in enumerate(flips):
                        color = GREEN if flip == "Heads" else BLUE
                        flip_text = font.render(f"{i+1}. {flip}", True, color)
                        screen.blit(flip_text, (200 + (i % 5) * 120, 150 + (i // 5) * 40))
                    
                    # Show totals
                    summary_font = pygame.font.Font(None, 32)
                    summary = summary_font.render(f"Heads: {heads_count}, Tails: {tails_count}", True, BLACK)
                    screen.blit(summary, (300, 300))
                    
                    # Add instruction
                    instruction_font = pygame.font.Font(None, 24)
                    instruction = instruction_font.render("Press SPACE for art, C for new coin flips", True, BLACK)
                    screen.blit(instruction, (250, 350))
        
        # Update display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("You learned about:")
    print("- random.randint() for random integers")
    print("- random.choice() for random selection from lists")
    print("- How randomness makes programs more interesting")
    print("- Applications in games, art, and simulations")
    print("- Pseudorandom vs truly random numbers")

if __name__ == "__main__":
    main()