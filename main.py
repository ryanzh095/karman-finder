import pygame
import sys

# --- Constants ---
SCREEN_WIDTH = 800  # Width of the game window in pixels
SCREEN_HEIGHT = 600 # Height of the game window in pixels
FPS = 120           # Frames per second limit

# Define some basic colors (RGB tuples)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# --- Pygame Setup ---
# Initialize all the Pygame modules
pygame.init()

# Create the game window (surface)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Karman Finder") # Set window title

# Create a clock object to help control the frame rate
clock = pygame.time.Clock()

# --- Game Variables ---
# (We will add game-specific variables here later, like rocket position, velocity etc.)
# Example: rocket_y = SCREEN_HEIGHT - 50

# --- Main Game Loop ---
running = True
while running:
    # --- Event Handling ---
    # Check for all events happening each frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user clicks the close button (X)
            running = False # Exit the loop

        # Add other event handling here (e.g., keyboard presses)
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         print("Space bar pressed!")

    # --- Game Logic / State Updates ---
    # (Update game state here - e.g., move the rocket based on physics)
    # This is where your simulation calculations will happen each frame.
    # Example: rocket_y -= 1 # Move up slightly

    # --- Drawing ---
    # First, fill the screen with a background color (e.g., black)
    # This clears the previous frame.
    screen.fill(BLACK)

    # Draw game elements here (e.g., rocket, ground, UI text)
    # Example: pygame.draw.rect(screen, RED, (SCREEN_WIDTH/2 - 10, rocket_y, 20, 40)) # Draw a simple rectangle

    # --- Update Display ---
    # Make the most recently drawn frame visible.
    pygame.display.flip() # Or pygame.display.update()

    # --- Frame Rate Control ---
    # Wait/pause to ensure the loop runs at the desired FPS.
    clock.tick(FPS)

# --- Quit Pygame ---
# This runs after the loop ends (running = False)
print("Exiting simulator...")
pygame.quit() # Uninitialize Pygame modules
sys.exit()  # Exit the Python script cleanly