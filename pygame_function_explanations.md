# PyGame Functions Explained - Easy Reference Guide

This guide explains every PyGame function used in our CodeHS examples, with simple explanations and practical examples.

---

## 🎮 Core PyGame Setup Functions

### `pygame.init()`
**What it does:** Starts up PyGame and gets everything ready to work.

**Why you need it:** This MUST be the first PyGame command in your program.

**Example:**
```python
import pygame
pygame.init()  # Always do this first!
```

**Think of it like:** Turning on a video game console - you have to power it on before you can play.

---

### `pygame.display.set_mode((width, height))`
**What it does:** Creates the window where your game will appear.

**Parameters:**
- `width`: How wide the window should be (in pixels)
- `height`: How tall the window should be (in pixels)

**Returns:** A "screen" object that you draw on

**Example:**
```python
screen = pygame.display.set_mode((800, 600))  # Makes 800x600 window
screen = pygame.display.set_mode((1200, 800)) # Makes 1200x800 window
```

**Think of it like:** Getting a blank canvas to paint on - you choose the size.

---

### `pygame.display.set_caption("Your Title")`
**What it does:** Sets the title that appears at the top of your window.

**Example:**
```python
pygame.display.set_caption("My Awesome Game")
pygame.display.set_caption("Snake Game v1.0")
```

**Think of it like:** Putting a title on your artwork.

---

### `pygame.display.flip()`
**What it does:** Shows everything you've drawn on the screen.

**Why you need it:** Without this, you won't see anything! You draw things, then "flip" to display them.

**Example:**
```python
# Draw some stuff
pygame.draw.circle(screen, (255, 0, 0), (100, 100), 50)
# Now show it
pygame.display.flip()  # This makes it appear!
```

**Think of it like:** Flipping a page to reveal what you've drawn on it.

---

### `pygame.time.Clock()`
**What it does:** Creates a timer to control how fast your game runs.

**Returns:** A clock object you can use to control timing

**Example:**
```python
clock = pygame.time.Clock()
# Later in your game loop:
clock.tick(60)  # Run at 60 frames per second
```

**Think of it like:** A metronome that keeps your game running at a steady beat.

---

### `clock.tick(fps)`
**What it does:** Controls how many times per second your game loop runs.

**Parameters:**
- `fps`: Frames per second (usually 60 for smooth animation)

**Example:**
```python
clock = pygame.time.Clock()
while running:
    # Game code here
    clock.tick(60)  # Limits to 60 FPS
```

**Think of it like:** Setting the speed limit for your game.

---

### `pygame.quit()`
**What it does:** Properly closes PyGame when you're done.

**Why you need it:** Good programming practice - cleans up properly.

**Example:**
```python
pygame.quit()  # Put this at the very end
sys.exit()     # This too
```

**Think of it like:** Turning off the video game console when you're done playing.

---

## 🎨 Drawing Functions

### `screen.fill(color)`
**What it does:** Fills the entire screen with one color (like painting over everything).

**Parameters:**
- `color`: RGB color tuple like (red, green, blue)

**Example:**
```python
screen.fill((255, 255, 255))  # Fill with white
screen.fill((0, 0, 0))        # Fill with black
screen.fill((100, 150, 200))  # Fill with light blue
```

**Think of it like:** Painting over your entire canvas with a paint roller.

---

### `pygame.draw.circle(surface, color, center, radius)`
**What it does:** Draws a filled circle.

**Parameters:**
- `surface`: Where to draw (usually `screen`)
- `color`: RGB color tuple
- `center`: (x, y) position of circle center
- `radius`: How big the circle is

**Example:**
```python
# Draw a red circle at position (400, 300) with radius 50
pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)

# Draw a blue circle at mouse position
mouse_x, mouse_y = pygame.mouse.get_pos()
pygame.draw.circle(screen, (0, 0, 255), (mouse_x, mouse_y), 30)
```

**Optional border:**
```python
# Draw just the outline (border width = 3)
pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50, 3)
```

**Think of it like:** Using a compass to draw a perfect circle.

---

### `pygame.draw.rect(surface, color, (x, y, width, height))`
**What it does:** Draws a filled rectangle.

**Parameters:**
- `surface`: Where to draw (usually `screen`)
- `color`: RGB color tuple
- `(x, y, width, height)`: Rectangle position and size

**Example:**
```python
# Draw a green rectangle at position (100, 200) that's 150 wide and 100 tall
pygame.draw.rect(screen, (0, 255, 0), (100, 200, 150, 100))

# Draw a square (width = height)
pygame.draw.rect(screen, (255, 255, 0), (50, 50, 80, 80))
```

**Optional border:**
```python
# Draw just the outline (border width = 5)
pygame.draw.rect(screen, (255, 0, 0), (100, 200, 150, 100), 5)
```

**Think of it like:** Drawing a rectangle with a ruler.

---

### `pygame.draw.line(surface, color, start_pos, end_pos, width)`
**What it does:** Draws a straight line between two points.

**Parameters:**
- `surface`: Where to draw
- `color`: RGB color tuple
- `start_pos`: (x, y) where line starts
- `end_pos`: (x, y) where line ends
- `width`: How thick the line is (optional, default is 1)

**Example:**
```python
# Draw a thin black line from (0,0) to (800,600)
pygame.draw.line(screen, (0, 0, 0), (0, 0), (800, 600), 1)

# Draw a thick red line
pygame.draw.line(screen, (255, 0, 0), (100, 100), (300, 200), 5)
```

**Think of it like:** Drawing a line with a ruler and pencil.

---

### `pygame.draw.polygon(surface, color, points_list)`
**What it does:** Draws a shape by connecting multiple points.

**Parameters:**
- `surface`: Where to draw
- `color`: RGB color tuple
- `points_list`: List of (x, y) coordinates

**Example:**
```python
# Draw a triangle
triangle_points = [(400, 100), (350, 200), (450, 200)]
pygame.draw.polygon(screen, (255, 0, 255), triangle_points)

# Draw a star shape
star_points = [(400, 50), (380, 150), (450, 100), (350, 100), (420, 150)]
pygame.draw.polygon(screen, (255, 255, 0), star_points)
```

**Think of it like:** Playing connect-the-dots to make a shape.

---

## 🖱️ Mouse Functions

### `pygame.mouse.get_pos()`
**What it does:** Gets the current position of the mouse cursor.

**Returns:** (x, y) tuple of mouse coordinates

**Example:**
```python
mouse_x, mouse_y = pygame.mouse.get_pos()
print(f"Mouse is at ({mouse_x}, {mouse_y})")

# Draw a circle that follows the mouse
pygame.draw.circle(screen, (255, 0, 0), (mouse_x, mouse_y), 20)
```

**Think of it like:** Asking "Where is the mouse cursor right now?"

---

### `pygame.mouse.get_pressed()`
**What it does:** Checks which mouse buttons are currently held down.

**Returns:** (left, middle, right) - True if pressed, False if not

**Example:**
```python
left_click, middle_click, right_click = pygame.mouse.get_pressed()

if left_click:
    print("Left mouse button is held down!")

if right_click:
    print("Right mouse button is held down!")
```

**Think of it like:** Checking "Is someone pressing any mouse buttons right now?"

---

## ⌨️ Keyboard Functions

### `pygame.key.get_pressed()`
**What it does:** Checks which keyboard keys are currently held down.

**Returns:** A list of all keys and whether they're pressed

**Example:**
```python
keys = pygame.key.get_pressed()

if keys[pygame.K_SPACE]:
    print("Space bar is held down!")

if keys[pygame.K_LEFT]:
    player_x -= 5  # Move left

if keys[pygame.K_a]:
    player_x -= 5  # Also move left with 'a' key
```

**Think of it like:** Checking "Which keys is someone pressing right now?"

---

### Common Key Constants
These are the names PyGame uses for different keys:

| Key | PyGame Constant |
|-----|----------------|
| Space bar | `pygame.K_SPACE` |
| Enter | `pygame.K_RETURN` |
| Escape | `pygame.K_ESCAPE` |
| Left arrow | `pygame.K_LEFT` |
| Right arrow | `pygame.K_RIGHT` |
| Up arrow | `pygame.K_UP` |
| Down arrow | `pygame.K_DOWN` |
| Letter keys | `pygame.K_a`, `pygame.K_b`, etc. |
| Number keys | `pygame.K_0`, `pygame.K_1`, etc. |

---

## 📝 Text Functions

### `pygame.font.SysFont(name, size)`
**What it does:** Creates a font object for drawing text.

**Parameters:**
- `name`: Font name (like "Arial", "Times", etc.)
- `size`: How big the text should be

**Returns:** A font object

**Example:**
```python
small_font = pygame.font.SysFont("Arial", 18)
big_font = pygame.font.SysFont("Arial", 48)
title_font = pygame.font.SysFont("Times", 36)
```

**Think of it like:** Choosing what handwriting style and size to use.

---

### `font.render(text, antialias, color)`
**What it does:** Creates an image of text that you can draw on screen.

**Parameters:**
- `text`: The words you want to display
- `antialias`: True for smooth text, False for pixelated (usually True)
- `color`: RGB color for the text

**Returns:** A text surface you can draw

**Example:**
```python
font = pygame.font.SysFont("Arial", 24)
text_surface = font.render("Hello, World!", True, (0, 0, 0))
text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
```

**Think of it like:** Writing words on a piece of paper that you can then paste onto your canvas.

---

### `screen.blit(surface, position)`
**What it does:** Draws one image/surface onto another (like pasting a sticker).

**Parameters:**
- `surface`: What you want to draw (like text or an image)
- `position`: (x, y) where to place it

**Example:**
```python
# Create text
font = pygame.font.SysFont("Arial", 24)
text = font.render("Game Over!", True, (255, 0, 0))

# Draw it on screen at position (100, 200)
screen.blit(text, (100, 200))
```

**Think of it like:** Pasting a sticker onto your canvas at a specific spot.

---

## 🎪 Event Handling

### `pygame.event.get()`
**What it does:** Gets a list of all things that just happened (clicks, key presses, etc.).

**Returns:** List of events

**Example:**
```python
for event in pygame.event.get():
    print(f"Something happened: {event.type}")
```

**Think of it like:** Checking your mailbox to see what new messages arrived.

---

### Event Types
These are the different things that can happen:

| Event Type | What It Means |
|------------|---------------|
| `pygame.QUIT` | User clicked the X to close window |
| `pygame.KEYDOWN` | User pressed a key |
| `pygame.KEYUP` | User released a key |
| `pygame.MOUSEBUTTONDOWN` | User clicked a mouse button |
| `pygame.MOUSEBUTTONUP` | User released a mouse button |

---

### Complete Event Handling Example
```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False  # Close the game
    
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("Space was pressed!")
        elif event.key == pygame.K_ESCAPE:
            running = False  # Close game with Escape
    
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            mouse_x, mouse_y = event.pos
            print(f"Left clicked at ({mouse_x}, {mouse_y})")
        elif event.button == 3:  # Right mouse button
            print("Right mouse button clicked!")
```

**Think of it like:** Having a secretary who tells you "Someone just knocked on the door" or "The phone is ringing."

---

## 📊 Useful Math and Utility Functions

### `math.sqrt(number)`
**What it does:** Calculates the square root of a number.

**Example:**
```python
import math
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Distance between points
```

---

### `random.randint(min, max)`
**What it does:** Gives you a random whole number between min and max (including both).

**Example:**
```python
import random
x = random.randint(0, 800)    # Random number from 0 to 800
dice = random.randint(1, 6)   # Random dice roll
```

---

### `random.choice(list)`
**What it does:** Picks a random item from a list.

**Example:**
```python
import random
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
random_color = random.choice(colors)  # Picks red, green, or blue
```

---

## 🎯 Common Patterns and How They Work

### The Main Game Loop
**What it does:** This is the heart of every game - it runs over and over.

```python
running = True
while running:          # Keep going until running becomes False
    # 1. Handle events (mouse clicks, key presses)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 2. Update game (move things, check collisions)
    player_x += player_speed
    
    # 3. Draw everything
    screen.fill((255, 255, 255))  # Clear screen
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 20)
    
    # 4. Show what we drew
    pygame.display.flip()
    
    # 5. Wait a bit (control game speed)
    clock.tick(60)
```

**Think of it like:** A flipbook animation - draw a picture, flip the page, draw the next picture, flip the page, repeat.

---

### Boundary Checking
**What it does:** Keeps things from going off the edge of the screen.

```python
# Keep player on screen
if player_x < 0:
    player_x = 0
if player_x > 800:
    player_x = 800
    
# Or with object size
if player_x < player_size:
    player_x = player_size
if player_x > WIDTH - player_size:
    player_x = WIDTH - player_size
```

**Think of it like:** Building a fence around your yard to keep your dog from running away.

---

### Collision Detection
**What it does:** Checks if two things are touching.

```python
def circles_touching(x1, y1, radius1, x2, y2, radius2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance < (radius1 + radius2)

# Use it like this:
if circles_touching(player_x, player_y, 20, enemy_x, enemy_y, 30):
    print("Player hit enemy!")
```

**Think of it like:** Checking if two bubbles are touching by measuring the distance between their centers.

---

## 🔧 Debugging Tips

### Print Statements
**Use these to see what's happening:**
```python
print(f"Player position: ({player_x}, {player_y})")
print(f"Mouse position: {pygame.mouse.get_pos()}")
print(f"Number of enemies: {len(enemies)}")
```

### Common Issues and Solutions

**Problem:** Nothing appears on screen
**Solution:** Make sure you call `pygame.display.flip()`

**Problem:** Game runs too fast/slow
**Solution:** Use `clock.tick(60)` to control speed

**Problem:** Can't see what you drew
**Solution:** Make sure you call `screen.fill()` before drawing new things

**Problem:** Events don't work
**Solution:** Make sure your event handling is inside the main game loop

---

## 🎓 Learning Progression

### Start Here (Beginner):
1. `pygame.init()`
2. `pygame.display.set_mode()`
3. `screen.fill()`
4. `pygame.draw.circle()`
5. `pygame.display.flip()`
6. Basic game loop

### Add Next (Intermediate):
1. `pygame.event.get()`
2. Mouse and keyboard input
3. Text rendering
4. Simple animation

### Master These (Advanced):
1. Complex event handling
2. Collision detection
3. Game states
4. Sound effects
5. Multiple objects and lists

---

Remember: You don't need to memorize all of these! Start with the basics and add more functions as you need them. Each function is a tool - learn what each tool does, and you can build amazing games!