# PROJECT 10: COMPREHENSIVE GAME
# Concepts: All previous concepts combined - variables, input, conditions, loops, functions, events
# Based on all CodeHS lessons - a culminating project

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
ORANGE = (255, 165, 0)

# Game functions demonstrating function parameters and return values

def create_star():
    """
    Function to create a new falling star
    Uses random numbers and returns a dictionary
    """
    colors = [YELLOW, (255, 215, 0), (255, 255, 224), ORANGE]
    
    star = {
        'x': random.randint(30, SCREEN_WIDTH - 30),
        'y': -30,
        'color': random.choice(colors),
        'speed': random.randint(2, 6),
        'size': random.randint(15, 25)
    }
    return star

def draw_star(screen, x, y, size, color):
    """
    Function with parameters to draw a star shape
    Demonstrates functions with multiple parameters
    """
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

def check_collision(star_x, star_y, star_size, player_x, player_y, player_size):
    """
    Function that returns a boolean value
    Uses math to calculate distance and return True/False
    """
    distance = math.sqrt((star_x - player_x)**2 + (star_y - player_y)**2)
    return distance < (star_size + player_size)

def update_stars(stars):
    """
    Function that modifies a list (demonstrates working with data structures)
    Uses for loops to update all stars
    """
    for star in stars:
        star['y'] += star['speed']  # Update position each frame

def remove_off_screen_stars(stars):
    """
    Function using list comprehension and conditions
    Returns a new list with only on-screen stars
    """
    return [star for star in stars if star['y'] <= SCREEN_HEIGHT]

def draw_game_ui(screen, score, level, lives, high_score):
    """
    Function to draw user interface elements
    Demonstrates functions organizing code
    """
    font = pygame.font.Font(None, 36)
    
    # Score display
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Level display  
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(level_text, (10, 50))
    
    # Lives display
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (SCREEN_WIDTH - 150, 10))
    
    # High score
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(high_score_text, (SCREEN_WIDTH - 200, 50))

def get_difficulty_settings(level):
    """
    Function that returns multiple values based on input parameter
    Demonstrates how functions can return calculated values
    """
    base_spawn_rate = 60
    base_max_stars = 8
    
    spawn_rate = max(20, base_spawn_rate - level * 5)
    max_stars = min(20, base_max_stars + level * 2)
    star_speed_bonus = level
    
    return spawn_rate, max_stars, star_speed_bonus

def main():
    """Main game function combining all programming concepts"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Project 10: Catch the Stars Game - All Concepts")
    clock = pygame.time.Clock()
    
    print("Project 10: Catch the Stars Game")
    print("This game combines ALL the concepts you've learned:")
    print("- Variables and constants")
    print("- User input (keyboard)")
    print("- Boolean logic and if statements") 
    print("- For loops and while loops")
    print("- Functions with parameters and return values")
    print("- Random number generation")
    print("- Mouse and keyboard events")
    print("- Lists and data management")
    print("\nGame Rules:")
    print("- Use arrow keys to move")
    print("- Catch falling stars to score points")
    print("- Avoid letting too many stars fall")
    print("- Game gets harder as you progress")
    print("- Press R to restart when game over")
    
    # Game state variables
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - 50
    player_size = 30
    player_speed = 7
    
    # Game data
    stars = []
    score = 0
    lives = 3
    level = 1
    high_score = 0
    game_over = False
    paused = False
    
    # Timing variables (demonstrating counters in while loops)
    spawn_timer = 0
    frame_count = 0
    
    # Game loop - this is our main while loop!
    running = True
    while running:
        frame_count += 1  # Counter increments each loop iteration
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    # Reset all variables (like restarting conditions)
                    player_x = SCREEN_WIDTH // 2
                    stars = []
                    score = 0
                    lives = 3
                    level = 1
                    game_over = False
                    spawn_timer = 0
                    frame_count = 0
                    print("Game restarted!")
                elif event.key == pygame.K_p:
                    paused = not paused
                    print(f"Game {'paused' if paused else 'resumed'}")
        
        # Game logic (only when not paused or game over)
        if not game_over and not paused:
            # Player movement with keyboard input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > player_size:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
                player_x += player_speed
            if keys[pygame.K_UP] and player_y > player_size:
                player_y -= player_speed  
            if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
                player_y += player_speed
            
            # Get difficulty settings using function with return values
            spawn_rate, max_stars, speed_bonus = get_difficulty_settings(level)
            
            # Spawn new stars using timer and random generation
            spawn_timer += 1
            if spawn_timer >= spawn_rate and len(stars) < max_stars:
                new_star = create_star()  # Function that returns a value
                new_star['speed'] += speed_bonus  # Increase speed based on level
                stars.append(new_star)
                spawn_timer = 0
            
            # Update all stars using function
            update_stars(stars)
            
            # Check collisions using for loop and function
            for star in stars[:]:  # Use slice to avoid modification during iteration
                # Use function that returns boolean
                if check_collision(star['x'], star['y'], star['size'], player_x, player_y, player_size):
                    stars.remove(star)
                    score += 10 * level  # Score increases with level
                    print(f"Star caught! Score: {score}")
            
            # Remove off-screen stars and check for misses
            initial_count = len(stars)
            stars = remove_off_screen_stars(stars)  # Function returning filtered list
            missed_stars = initial_count - len(stars)
            
            if missed_stars > 0:
                lives -= missed_stars
                print(f"Missed {missed_stars} stars! Lives: {lives}")
            
            # Level progression using if statements
            if score > 0 and score % 200 == 0 and score // 200 == level:
                level += 1
                print(f"Level up! Now level {level}")
            
            # Game over condition
            if lives <= 0:
                game_over = True
                if score > high_score:
                    high_score = score
                    print(f"New high score: {high_score}!")
                print("Game Over!")
        
        # Drawing/Rendering
        screen.fill(BLACK)
        
        if not game_over:
            # Draw all stars using for loop and function
            for star in stars:
                draw_star(screen, int(star['x']), int(star['y']), star['size'], star['color'])
            
            # Draw player
            pygame.draw.circle(screen, GREEN, (player_x, player_y), player_size)
            
            # Draw UI using function
            draw_game_ui(screen, score, level, lives, high_score)
            
            # Show instructions
            if frame_count < 300:  # Show for first 5 seconds
                font = pygame.font.Font(None, 24)
                instructions = [
                    "Use arrow keys to move and catch stars!",
                    "Press P to pause"
                ]
                for i, instruction in enumerate(instructions):
                    text = font.render(instruction, True, WHITE)
                    screen.blit(text, (10, SCREEN_HEIGHT - 60 + i * 25))
            
            if paused:
                pause_font = pygame.font.Font(None, 72)
                pause_text = pause_font.render("PAUSED", True, WHITE)
                pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                screen.blit(pause_text, pause_rect)
        
        else:
            # Game over screen
            font = pygame.font.Font(None, 72)
            game_over_text = font.render("Game Over!", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
            screen.blit(game_over_text, game_over_rect)
            
            # Final statistics
            stats_font = pygame.font.Font(None, 36)
            stats = [
                f"Final Score: {score}",
                f"Level Reached: {level}",
                f"High Score: {high_score}",
                f"Stars Caught: {score // 10}"
            ]
            
            for i, stat in enumerate(stats):
                stat_text = stats_font.render(stat, True, WHITE)
                stat_rect = stat_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 30 + i * 40))
                screen.blit(stat_text, stat_rect)
            
            # Restart instruction
            restart_font = pygame.font.Font(None, 32)
            restart_text = restart_font.render("Press R to restart", True, YELLOW)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 150))
            screen.blit(restart_text, restart_rect)
        
        # Update display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print(f"Game ended after {frame_count} frames")
    print(f"Final high score: {high_score}")
    print("\nCongratulations! You've completed all programming concepts:")
    print("✓ Variables and constants")
    print("✓ User input and type conversion") 
    print("✓ Boolean logic and conditionals")
    print("✓ For loops and while loops")
    print("✓ Functions with parameters and return values")
    print("✓ Random number generation")
    print("✓ Event handling (keyboard/mouse)")
    print("✓ Lists and data structures")
    print("✓ Game state management")
    print("✓ Collision detection")
    print("You're ready for more advanced programming!")

if __name__ == "__main__":
    main()