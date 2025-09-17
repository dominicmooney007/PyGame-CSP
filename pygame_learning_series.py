# PyGame Learning Series - Progressive Projects
# Based on CodeHS lesson plans for Python fundamentals

import pygame
import random
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

# ============================================================================
# PROJECT 1: BASIC GRAPHICS AND VARIABLES
# Concepts: Variables, print statements, basic graphics
# Based on Lesson 3.5 (User Input) and 3.6 (Basic Math)
# ============================================================================

def project1_basic_shapes():
    """Draw basic shapes using variables"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 1: Basic Shapes with Variables")
    clock = pygame.time.Clock()
    
    # Variables for shapes
    circle_x = 200
    circle_y = 200
    circle_radius = 50
    
    rect_x = 400
    rect_y = 300
    rect_width = 100
    rect_height = 80
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(WHITE)
        
        # Draw shapes using variables
        pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)
        pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# PROJECT 2: USER INPUT AND MATH
# Concepts: User input, basic math operations
# Based on Lessons 3.5 (User Input) and 3.6 (Basic Math)
# ============================================================================

def project2_user_input_shapes():
    """Create shapes based on user input and math calculations"""
    # Get user input before starting pygame
    print("Welcome to Shape Creator!")
    circle_radius = int(input("Enter circle radius (10-100): "))
    rect_width = int(input("Enter rectangle width (50-200): "))
    rect_height = int(input("Enter rectangle height (50-200): "))
    
    # Calculate positions using math
    circle_x = SCREEN_WIDTH // 4
    circle_y = SCREEN_HEIGHT // 2
    
    rect_x = (SCREEN_WIDTH * 3) // 4 - rect_width // 2
    rect_y = SCREEN_HEIGHT // 2 - rect_height // 2
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 2: User Input Shapes")
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        
        # Draw user-customized shapes
        pygame.draw.circle(screen, GREEN, (circle_x, circle_y), circle_radius)
        pygame.draw.rect(screen, PURPLE, (rect_x, rect_y, rect_width, rect_height))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# PROJECT 3: BOOLEANS AND CONDITIONS
# Concepts: Boolean variables, if statements
# Based on Lessons 4.1 (Booleans) and 4.4 (If Statements)
# ============================================================================

def project3_conditional_colors():
    """Change colors based on boolean conditions"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 3: Conditional Colors")
    clock = pygame.time.Clock()
    
    # Boolean variables
    is_red = True
    is_large = False
    
    circle_x = SCREEN_WIDTH // 2
    circle_y = SCREEN_HEIGHT // 2
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_red = not is_red  # Toggle color
                elif event.key == pygame.K_s:
                    is_large = not is_large  # Toggle size
        
        screen.fill(WHITE)
        
        # Use if statements to determine color and size
        if is_red:
            color = RED
        else:
            color = BLUE
        
        if is_large:
            radius = 80
        else:
            radius = 40
        
        pygame.draw.circle(screen, color, (circle_x, circle_y), radius)
        
        # Display instructions
        font = pygame.font.Font(None, 36)
        text1 = font.render("Press SPACE to change color", True, BLACK)
        text2 = font.render("Press S to change size", True, BLACK)
        screen.blit(text1, (10, 10))
        screen.blit(text2, (10, 50))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# PROJECT 4: MOUSE EVENTS
# Concepts: Event handling, mouse clicks
# Based on Lesson 3.8 (Mouse Events)
# ============================================================================

def project4_mouse_circles():
    """Create circles where the user clicks"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 4: Click to Create Circles")
    clock = pygame.time.Clock()
    
    circles = []  # List to store circle positions
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Add new circle at mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                circles.append((mouse_x, mouse_y))
        
        screen.fill(WHITE)
        
        # Draw all circles
        for i, (x, y) in enumerate(circles):
            # Use different colors for variety
            colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
            color = colors[i % len(colors)]
            pygame.draw.circle(screen, color, (x, y), 30)
        
        # Display instructions
        font = pygame.font.Font(None, 36)
        text = font.render("Click anywhere to create circles!", True, BLACK)
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# PROJECT 5: KEY EVENTS AND MOVEMENT
# Concepts: Keyboard events, variable updates
# Based on Lesson 4.5 (Key Events)
# ============================================================================

def project5_keyboard_movement():
    """Move a shape with keyboard input"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 5: Keyboard Movement")
    clock = pygame.time.Clock()
    
    # Player position
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    player_size = 40
    speed = 5
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y += speed
        
        # Keep player on screen
        player_x = max(player_size, min(SCREEN_WIDTH - player_size, player_x))
        player_y = max(player_size, min(SCREEN_HEIGHT - player_size, player_y))
        
        screen.fill(WHITE)
        
        # Draw player
        pygame.draw.circle(screen, RED, (player_x, player_y), player_size)
        
        # Display instructions
        font = pygame.font.Font(None, 36)
        text = font.render("Use arrow keys or WASD to move!", True, BLACK)
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# PROJECT 6: FOR LOOPS AND PATTERNS
# Concepts: For loops, range function, patterns
# Based on Lessons 4.6 (For Loops) and 4.7 (General For Loops)
# ============================================================================

def project6_loop_patterns():
    """Create patterns using for loops"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 6: Loop Patterns")
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        
        # Pattern 1: Row of circles using for loop
        for i in range(10):
            x = 50 + i * 70
            y = 100
            pygame.draw.circle(screen, RED, (x, y), 25)
        
        # Pattern 2: Grid of rectangles
        for row in range(4):
            for col in range(6):
                x = 50 + col * 120
                y = 200 + row * 80
                # Use modulus to alternate colors
                if (row + col) % 2 == 0:
                    color = BLUE
                else:
                    color = GREEN
                pygame.draw.rect(screen, color, (x, y, 100, 60))
        
        # Pattern 3: Circles in decreasing size
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT - 100
        for i in range(5):
            radius = 80 - i * 15
            pygame.draw.circle(screen, PURPLE, (center_x, center_y), radius, 3)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# PROJECT 7: RANDOM NUMBERS
# Concepts: Random number generation, variety
# Based on Lesson 4.9 (Random Numbers)
# ============================================================================

def project7_random_art():
    """Generate random art with colors and positions"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 7: Random Art Generator")
    clock = pygame.time.Clock()
    
    # List of possible colors
    colors = [RED, GREEN, BLUE, YELLOW, PURPLE, (255, 165, 0), (0, 255, 255)]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Generate new random art
                    screen.fill(WHITE)
                    
                    # Draw random shapes
                    for i in range(20):
                        # Random position
                        x = random.randint(50, SCREEN_WIDTH - 50)
                        y = random.randint(50, SCREEN_HEIGHT - 50)
                        
                        # Random color
                        color = random.choice(colors)
                        
                        # Random shape choice
                        shape_type = random.randint(1, 3)
                        
                        if shape_type == 1:
                            # Random circle
                            radius = random.randint(10, 40)
                            pygame.draw.circle(screen, color, (x, y), radius)
                        elif shape_type == 2:
                            # Random rectangle
                            width = random.randint(30, 80)
                            height = random.randint(30, 80)
                            pygame.draw.rect(screen, color, (x, y, width, height))
                        else:
                            # Random line
                            end_x = random.randint(50, SCREEN_WIDTH - 50)
                            end_y = random.randint(50, SCREEN_HEIGHT - 50)
                            thickness = random.randint(2, 8)
                            pygame.draw.line(screen, color, (x, y), (end_x, end_y), thickness)
        
        # Initial instructions
        if pygame.get_ticks() < 100:  # Show for first frames
            screen.fill(WHITE)
            font = pygame.font.Font(None, 48)
            text = font.render("Press SPACE for Random Art!", True, BLACK)
            text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(text, text_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# PROJECT 8: WHILE LOOPS AND ANIMATION
# Concepts: While loops, continuous updates, counters
# Based on Lesson 4.10 (While Loops)
# ============================================================================

def project8_bouncing_ball():
    """Bouncing ball animation using while loop concepts"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 8: Bouncing Ball")
    clock = pygame.time.Clock()
    
    # Ball properties
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    ball_radius = 30
    ball_speed_x = 5
    ball_speed_y = 3
    ball_color = RED
    
    # Color change counter
    color_counter = 0
    colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
    
    running = True
    while running:  # This demonstrates while loop concept
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update ball position
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        # Bounce off walls and change color
        if ball_x <= ball_radius or ball_x >= SCREEN_WIDTH - ball_radius:
            ball_speed_x = -ball_speed_x
            color_counter += 1
            ball_color = colors[color_counter % len(colors)]
        
        if ball_y <= ball_radius or ball_y >= SCREEN_HEIGHT - ball_radius:
            ball_speed_y = -ball_speed_y
            color_counter += 1
            ball_color = colors[color_counter % len(colors)]
        
        screen.fill(WHITE)
        
        # Draw ball
        pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)
        
        # Display bounce count
        font = pygame.font.Font(None, 36)
        text = font.render(f"Bounces: {color_counter}", True, BLACK)
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# PROJECT 9: FUNCTIONS WITH PARAMETERS
# Concepts: Function definition, parameters, code reuse
# Based on Lessons 5.3 (Functions and Parameters) and 5.5 (Functions and Return Values)
# ============================================================================

def draw_star(screen, x, y, size, color):
    """Function to draw a star at given position with size and color"""
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

def draw_house(screen, x, y, width, height, roof_color, wall_color):
    """Function to draw a house with parameters"""
    # Draw walls
    pygame.draw.rect(screen, wall_color, (x, y, width, height))
    
    # Draw roof
    roof_points = [(x, y), (x + width//2, y - height//3), (x + width, y)]
    pygame.draw.polygon(screen, roof_color, roof_points)
    
    # Draw door
    door_width = width // 4
    door_height = height // 2
    door_x = x + width//2 - door_width//2
    door_y = y + height - door_height
    pygame.draw.rect(screen, (101, 67, 33), (door_x, door_y, door_width, door_height))

def calculate_distance(x1, y1, x2, y2):
    """Function that returns the distance between two points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def project9_functions_with_parameters():
    """Demonstrate functions with parameters and return values"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 9: Functions with Parameters")
    clock = pygame.time.Clock()
    
    mouse_x, mouse_y = 0, 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
        
        screen.fill(WHITE)
        
        # Draw multiple houses using function with parameters
        draw_house(screen, 50, 300, 120, 100, RED, YELLOW)
        draw_house(screen, 200, 250, 150, 120, BLUE, GREEN)
        draw_house(screen, 400, 280, 100, 90, GREEN, (255, 192, 203))
        
        # Draw stars using function with parameters
        draw_star(screen, 100, 100, 30, YELLOW)
        draw_star(screen, 200, 80, 25, (255, 215, 0))
        draw_star(screen, 300, 120, 35, YELLOW)
        
        # Demonstrate return values - calculate distance to mouse
        center_x, center_y = SCREEN_WIDTH//2, SCREEN_HEIGHT//2
        distance = calculate_distance(center_x, center_y, mouse_x, mouse_y)
        
        # Draw a circle that changes size based on distance
        circle_size = max(20, min(100, int(distance / 5)))
        pygame.draw.circle(screen, PURPLE, (center_x, center_y), circle_size)
        
        # Display distance
        font = pygame.font.Font(None, 36)
        text = font.render(f"Distance to mouse: {int(distance)}", True, BLACK)
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# PROJECT 10: COMPREHENSIVE GAME
# Concepts: All previous concepts combined
# Based on all lessons - variables, input, conditions, loops, functions, events
# ============================================================================

def project10_simple_game():
    """A simple game combining all learned concepts"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 10: Catch the Stars Game")
    clock = pygame.time.Clock()
    
    # Player
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - 50
    player_size = 30
    player_speed = 7
    
    # Game variables
    stars = []
    score = 0
    game_over = False
    spawn_timer = 0
    
    # Colors
    colors = [YELLOW, (255, 215, 0), (255, 255, 224)]
    
    def create_star():
        """Function to create a new falling star"""
        x = random.randint(30, SCREEN_WIDTH - 30)
        y = -30
        color = random.choice(colors)
        speed = random.randint(2, 5)
        return {'x': x, 'y': y, 'color': color, 'speed': speed}
    
    def check_collision(star_x, star_y, player_x, player_y):
        """Function to check if star collides with player"""
        distance = math.sqrt((star_x - player_x)**2 + (star_y - player_y)**2)
        return distance < (20 + player_size)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    # Restart game
                    stars = []
                    score = 0
                    game_over = False
                    spawn_timer = 0
        
        if not game_over:
            # Player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > player_size:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
                player_x += player_speed
            
            # Spawn stars using timer (like a simplified while loop condition)
            spawn_timer += 1
            if spawn_timer > 60:  # Spawn every second at 60 FPS
                stars.append(create_star())
                spawn_timer = 0
            
            # Update stars
            for star in stars[:]:  # Use slice to avoid issues when removing
                star['y'] += star['speed']
                
                # Check collision with player
                if check_collision(star['x'], star['y'], player_x, player_y):
                    stars.remove(star)
                    score += 10
                
                # Remove stars that fall off screen
                elif star['y'] > SCREEN_HEIGHT:
                    stars.remove(star)
            
            # Game over condition
            if len(stars) > 15:  # Too many stars missed
                game_over = True
        
        # Draw everything
        screen.fill(BLACK)
        
        if not game_over:
            # Draw stars
            for star in stars:
                draw_star(screen, int(star['x']), int(star['y']), 20, star['color'])
            
            # Draw player
            pygame.draw.circle(screen, GREEN, (player_x, player_y), player_size)
            
            # Draw score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            # Instructions
            inst_text = font.render("Use arrow keys to catch stars!", True, WHITE)
            screen.blit(inst_text, (10, 50))
        
        else:
            # Game over screen
            font = pygame.font.Font(None, 72)
            game_over_text = font.render("Game Over!", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            screen.blit(game_over_text, game_over_rect)
            
            font = pygame.font.Font(None, 48)
            final_score_text = font.render(f"Final Score: {score}", True, WHITE)
            final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(final_score_text, final_score_rect)
            
            restart_text = font.render("Press R to restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
            screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# ============================================================================
# MAIN MENU TO RUN PROJECTS
# ============================================================================

def main_menu():
    """Display menu to choose which project to run"""
    print("\n" + "="*60)
    print("PYGAME LEARNING SERIES - Choose a project:")
    print("="*60)
    print("1. Basic Shapes with Variables")
    print("2. User Input Shapes")
    print("3. Conditional Colors (Booleans & If Statements)")
    print("4. Mouse Click Circles")
    print("5. Keyboard Movement")
    print("6. Loop Patterns")
    print("7. Random Art Generator")
    print("8. Bouncing Ball (While Loops)")
    print("9. Functions with Parameters")
    print("10. Catch the Stars Game (All Concepts)")
    print("0. Exit")
    print("="*60)
    
    try:
        choice = int(input("Enter your choice (0-10): "))
        
        if choice == 1:
            project1_basic_shapes()
        elif choice == 2:
            project2_user_input_shapes()
        elif choice == 3:
            project3_conditional_colors()
        elif choice == 4:
            project4_mouse_circles()
        elif choice == 5:
            project5_keyboard_movement()
        elif choice == 6:
            project6_loop_patterns()
        elif choice == 7:
            project7_random_art()
        elif choice == 8:
            project8_bouncing_ball()
        elif choice == 9:
            project9_functions_with_parameters()
        elif choice == 10:
            project10_simple_game()
        elif choice == 0:
            print("Goodbye!")
            return
        else:
            print("Invalid choice! Please enter a number between 0-10.")
        
        # Ask if user wants to try another project
        again = input("\nWould you like to try another project? (y/n): ").lower()
        if again == 'y' or again == 'yes':
            main_menu()
            
    except ValueError:
        print("Invalid input! Please enter a number.")
        main_menu()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return

if __name__ == "__main__":
    main_menu()