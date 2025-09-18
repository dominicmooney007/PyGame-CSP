"""
Interactive PyGame Installation Test
-----------------------------------
This file tests PyGame functionality with interactive elements including:
- Mouse interaction
- Keyboard input
- Moving objects
- Collision detection
- Sound (if available)

If this runs smoothly, your PyGame installation supports all major features.
"""

import pygame
import sys
import random
import math

# Initialize PyGame
pygame.init()

# Try to initialize mixer for sound (optional)
try:
    pygame.mixer.init()
    sound_available = True
except:
    sound_available = False

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def update(self):
        # Move the ball
        self.x += self.speed_x
        self.y += self.speed_y
        
        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= WINDOW_WIDTH:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0 or self.y + self.radius >= WINDOW_HEIGHT:
            self.speed_y = -self.speed_y
        
        # Keep ball in bounds
        self.x = max(self.radius, min(WINDOW_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(WINDOW_HEIGHT - self.radius, self.y))
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    
    def distance_to(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

def create_random_ball():
    """Create a ball with random properties"""
    x = random.randint(50, WINDOW_WIDTH - 50)
    y = random.randint(50, WINDOW_HEIGHT - 50)
    radius = random.randint(10, 30)
    color = random.choice([RED, GREEN, BLUE, YELLOW, ORANGE, CYAN])
    speed_x = random.uniform(-3, 3)
    speed_y = random.uniform(-3, 3)
    return Ball(x, y, radius, color, speed_x, speed_y)

def main():
    # Create the display window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("PyGame Installation Test - Interactive")
    
    # Create a clock object
    clock = pygame.time.Clock()
    
    # Create fonts
    font_large = pygame.font.Font(None, 48)
    font_medium = pygame.font.Font(None, 32)
    font_small = pygame.font.Font(None, 24)
    
    # Create some bouncing balls
    balls = []
    for _ in range(5):
        balls.append(create_random_ball())
    
    # Game variables
    mouse_x, mouse_y = 0, 0
    keys_pressed = set()
    score = 0
    frame_count = 0
    
    print("Interactive PyGame Test Started!")
    print(f"PyGame Version: {pygame.version.ver}")
    print("Controls:")
    print("  - Move mouse to see cursor tracking")
    print("  - Click to add balls")
    print("  - Press SPACE to clear balls")
    print("  - Press R to add random balls")
    print("  - Press ESC to quit")
    if sound_available:
        print("  - Sound system initialized successfully")
    else:
        print("  - Sound system not available (this is normal)")
    
    # Main game loop
    running = True
    while running:
        frame_count += 1
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keys_pressed.add(event.key)
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    balls.clear()
                    score = 0
                elif event.key == pygame.K_r:
                    balls.append(create_random_ball())
            elif event.type == pygame.KEYUP:
                keys_pressed.discard(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_x, mouse_y = event.pos
                    # Add a new ball at mouse position
                    balls.append(Ball(mouse_x, mouse_y, 15, RED, 
                                    random.uniform(-2, 2), random.uniform(-2, 2)))
        
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Update balls
        for ball in balls:
            ball.update()
            # Check if mouse is close to ball
            if ball.distance_to(mouse_x, mouse_y) < ball.radius + 10:
                score += 1
        
        # Fill background
        screen.fill(WHITE)
        
        # Draw balls
        for ball in balls:
            ball.draw(screen)
        
        # Draw mouse cursor indicator
        pygame.draw.circle(screen, BLACK, (mouse_x, mouse_y), 5, 2)
        pygame.draw.line(screen, BLACK, (mouse_x - 10, mouse_y), (mouse_x + 10, mouse_y), 2)
        pygame.draw.line(screen, BLACK, (mouse_x, mouse_y - 10), (mouse_x, mouse_y + 10), 2)
        
        # Draw UI text
        title_text = font_large.render("Interactive PyGame Test", True, BLACK)
        screen.blit(title_text, (10, 10))
        
        # Draw stats
        stats_y = 70
        stats = [
            f"Balls: {len(balls)}",
            f"Score: {score}",
            f"FPS: {int(clock.get_fps())}",
            f"Mouse: ({mouse_x}, {mouse_y})"
        ]
        
        for stat in stats:
            text = font_medium.render(stat, True, BLACK)
            screen.blit(text, (10, stats_y))
            stats_y += 30
        
        # Draw controls
        controls = [
            "Controls:",
            "Click: Add ball",
            "SPACE: Clear balls",
            "R: Add random ball",
            "ESC: Quit"
        ]
        
        controls_y = WINDOW_HEIGHT - len(controls) * 20 - 10
        for control in controls:
            if control == "Controls:":
                text = font_medium.render(control, True, BLACK)
            else:
                text = font_small.render(control, True, BLACK)
            screen.blit(text, (WINDOW_WIDTH - 200, controls_y))
            controls_y += 20
        
        # Draw a sine wave for visual effect
        wave_points = []
        for x in range(0, WINDOW_WIDTH, 5):
            y = WINDOW_HEIGHT // 2 + 30 * math.sin((x + frame_count) * 0.02)
            wave_points.append((x, y))
        
        if len(wave_points) > 1:
            pygame.draw.lines(screen, BLUE, False, wave_points, 2)
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(FPS)
    
    print("Test completed successfully!")
    print("If you saw moving balls, mouse interaction, and smooth animation,")
    print("your PyGame installation is fully functional!")
    
    # Quit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error running interactive PyGame test: {e}")
        print("This might indicate an installation issue.")
        import traceback
        traceback.print_exc()
        sys.exit(1)
