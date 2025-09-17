# PyGame Setup and Quick Start Guide

## 🚀 Installation Instructions

### Step 1: Install Python
If you don't have Python installed:
1. Go to [python.org](https://python.org)
2. Download Python 3.8 or newer
3. Run the installer and **check "Add Python to PATH"**
4. Verify installation by opening a terminal/command prompt and typing:
   ```bash
   python --version
   ```

### Step 2: Install PyGame
Open a terminal/command prompt and run:
```bash
pip install pygame
```

### Step 3: Verify Installation
Create a test file called `test_pygame.py`:
```python
import pygame
print("PyGame version:", pygame.version.ver)
print("Installation successful!")
```

Run it:
```bash
python test_pygame.py
```

---

## 📁 File Structure for CodeHS Projects

```
pygame_codehs_projects/
├── README.md
├── setup_test.py
├── examples/
│   ├── 01_variables_constants.py
│   ├── 02_user_input.py
│   ├── 03_booleans_conditionals.py
│   ├── 04_mouse_events.py
│   ├── 05_keyboard_events.py
│   ├── 06_for_loops.py
│   ├── 07_random_numbers.py
│   ├── 08_while_loops.py
│   ├── 09_functions_parameters.py
│   └── 10_comprehensive_game.py
├── utils/
│   ├── pygame_helpers.py
│   └── colors.py
└── assets/
    ├── sounds/
    └── images/
```

---

## 🎯 Quick Start Template

Every PyGame program should start with this basic template:

```python
import pygame
import sys

# Initialize PyGame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My PyGame Program")
clock = pygame.time.Clock()

# Game variables
running = True

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(WHITE)
    
    # Draw everything here
    pygame.draw.circle(screen, RED, (WIDTH//2, HEIGHT//2), 50)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit
pygame.quit()
sys.exit()
```

---

## 🛠️ Essential PyGame Functions Reference Card

### Window and Display
```python
# Create window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Window Title")

# Update display
pygame.display.flip()          # Update entire screen
pygame.display.update()        # Update entire screen
pygame.display.update(rect)    # Update specific area
```

### Drawing Functions
```python
# Fill screen with color
screen.fill((255, 255, 255))  # White background

# Draw shapes
pygame.draw.circle(surface, color, (x, y), radius)
pygame.draw.rect(surface, color, (x, y, width, height))
pygame.draw.line(surface, color, start_pos, end_pos, width)
pygame.draw.polygon(surface, color, points_list)

# With borders (add width parameter)
pygame.draw.circle(surface, color, (x, y), radius, border_width)
```

### Event Handling
```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            # Space key pressed
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left click
            mouse_x, mouse_y = event.pos
```

### Continuous Input
```python
# Get all currently pressed keys
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    x -= speed

# Get mouse position and buttons
mouse_x, mouse_y = pygame.mouse.get_pos()
left, middle, right = pygame.mouse.get_pressed()
```

### Text Rendering
```python
font = pygame.font.SysFont("Arial", 24)
text_surface = font.render("Hello World", True, (0, 0, 0))
screen.blit(text_surface, (x, y))
```

---

## 🎨 Color Palette for Educational Projects

```python
# Basic Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

# Educational Friendly Colors
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_PINK = (255, 182, 193)
ORANGE = (255, 165, 0)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (211, 211, 211)

# Random color generator
import random
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
```

---

## 🔧 Common Patterns and Helper Functions

### Movement and Boundary Checking
```python
def move_with_boundaries(x, y, dx, dy, obj_size, screen_width, screen_height):
    """Move object while keeping it within screen boundaries"""
    new_x = x + dx
    new_y = y + dy
    
    # Check boundaries
    if new_x < obj_size:
        new_x = obj_size
    elif new_x > screen_width - obj_size:
        new_x = screen_width - obj_size
    
    if new_y < obj_size:
        new_y = obj_size
    elif new_y > screen_height - obj_size:
        new_y = screen_height - obj_size
    
    return new_x, new_y
```

### Collision Detection
```python
def circle_collision(x1, y1, r1, x2, y2, r2):
    """Check if two circles collide"""
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance < (r1 + r2)

def point_in_rect(px, py, rx, ry, rw, rh):
    """Check if point is inside rectangle"""
    return rx <= px <= rx + rw and ry <= py <= ry + rh
```

### Text Utilities
```python
def draw_text(surface, text, x, y, size=24, color=(0, 0, 0), center=False):
    """Helper function to draw text easily"""
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(str(text), True, color)
    
    if center:
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)
    else:
        surface.blit(text_surface, (x, y))

def draw_text_center(surface, text, y, size=24, color=(0, 0, 0)):
    """Draw text centered horizontally"""
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(str(text), True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = surface.get_width() // 2
    text_rect.y = y
    surface.blit(text_surface, text_rect)
```

### Animation Helpers
```python
def lerp(start, end, t):
    """Linear interpolation between start and end"""
    return start + t * (end - start)

def bounce_value(value, min_val, max_val, speed):
    """Create bouncing animation between min and max values"""
    import math
    return min_val + (max_val - min_val) * (1 + math.sin(value * speed)) / 2
```

---

## 📚 Lesson-Specific Code Snippets

### Variables and Math (Lessons 3.5-3.6)
```python
# Constants
WINDOW_WIDTH = 800
CIRCLE_RADIUS = 50

# Variables
player_x = 100
player_y = 100

# Math operations
area = 3.14159 * CIRCLE_RADIUS ** 2
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
```

### Boolean Logic (Lessons 4.1, 4.4)
```python
# Boolean variables
game_running = True
player_has_key = False
door_is_open = False

# Conditional logic
if player_has_key and not door_is_open:
    door_is_open = True
    
# Color based on condition
color = GREEN if player_has_key else RED
```

### Loops (Lessons 4.6, 4.7, 4.10)
```python
# For loop examples
for i in range(10):                    # 0 to 9
    draw_circle(i * 50, 100)

for i in range(5, 15, 2):             # 5, 7, 9, 11, 13
    draw_square(i * 30, 200)

# Nested loops for grids
for row in range(4):
    for col in range(6):
        x = col * 80
        y = row * 60
        draw_rect(x, y)

# While loop pattern (game loop)
running = True
while running:
    handle_events()
    update_game()
    draw_everything()
```

### Random Numbers (Lesson 4.9)
```python
import random

# Random integers
x = random.randint(0, 800)
y = random.randint(0, 600)

# Random choice from list
colors = [RED, GREEN, BLUE, YELLOW]
random_color = random.choice(colors)

# Random float between 0 and 1
speed = random.random() * 5
```

### Functions (Lessons 5.3, 5.5)
```python
def draw_house(surface, x, y, width, height, color):
    """Function with multiple parameters"""
    pygame.draw.rect(surface, color, (x, y, width, height))
    # Draw roof
    points = [(x, y), (x + width//2, y - 20), (x + width, y)]
    pygame.draw.polygon(surface, RED, points)

def calculate_distance(x1, y1, x2, y2):
    """Function that returns a value"""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def is_collision(obj1, obj2):
    """Function that returns boolean"""
    return calculate_distance(obj1['x'], obj1['y'], obj2['x'], obj2['y']) < 50
```

---

## 🐛 Common Issues and Solutions

### Problem: "pygame.error: No available video device"
**Solution:** This usually happens on headless systems. Make sure you have a display available.

### Problem: "ImportError: No module named 'pygame'"
**Solution:** Install pygame with `pip install pygame`

### Problem: Window appears but is black/unresponsive
**Solutions:**
- Make sure you're calling `pygame.display.flip()` or `pygame.display.update()`
- Ensure your event loop includes `pygame.event.get()`
- Check that you're filling the screen each frame

### Problem: Shapes flicker or disappear
**Solution:** Make sure to clear the screen with `screen.fill()` before drawing new content

### Problem: Movement is too fast or choppy
**Solutions:**
- Use `clock.tick(60)` to limit frame rate
- Implement delta time for frame-independent movement
- Adjust movement speed values

### Problem: Events don't register
**Solutions:**
- Make sure event handling is inside the main game loop
- Check that you're using the correct event types and key constants
- Ensure the window has focus

---

## 🎓 Teaching Tips

### Getting Started
1. Start with the basic template and modify it gradually
2. Always test after adding each new feature
3. Use print statements to debug values
4. Encourage experimentation with colors and sizes

### Progressive Learning
1. **Week 1-2:** Basic shapes and colors
2. **Week 3-4:** User input and interaction
3. **Week 5-6:** Loops and patterns
4. **Week 7-8:** Functions and organization
5. **Week 9-10:** Complete projects

### Best Practices for Students
1. Use meaningful variable names
2. Add comments to explain complex logic
3. Keep functions small and focused
4. Test frequently during development
5. Don't be afraid to experiment!

---

## 📝 Assignment Ideas

### Beginner Projects
- Draw your house using basic shapes
- Create a simple calculator display
- Make a traffic light that changes colors

### Intermediate Projects
- Build a simple drawing program
- Create a basic game of Pong
- Make an interactive story with choices

### Advanced Projects
- Develop a complete game with levels
- Create an educational simulation
- Build a creative art generator

---

This guide provides everything needed to get started with PyGame for CodeHS lesson implementation!