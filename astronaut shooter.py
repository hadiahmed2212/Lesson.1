import pygame

# Start Pygame
pygame.init()

# Create the game window (800 pixels wide, 600 pixels tall)
screen = pygame.display.set_mode((800, 600))
# Set the title of your game window
pygame.display.set_caption("My Space Game")

# This loop keeps your window open until you close it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If you click the 'X' button
            running = False
    
    pygame.display.flip() # Shows everything you've drawn on the screen

pygame.quit() # Quits Pygame when the loop ends
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Space Game")

# Define colors (RGB values)
BLUE = (0, 0, 255) # Red, Green, Blue

# Spaceship position and size
player_x = 375 # X-coordinate (left to right)
player_y = 500 # Y-coordinate (top to bottom)
player_width = 50
player_height = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black each time to "clear" the screen
    screen.fill((0, 0, 0)) # Black background

    # Draw the player (spaceship)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    
    pygame.display.flip()

pygame.quit()
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Space Game")

BLUE = (0, 0, 255) 
player_x = 375 
player_y = 500
player_width = 50
player_height = 50
player_speed = 5 # How many pixels the spaceship moves per press

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for key presses
        if event.type == pygame.KEYDOWN: # If a key is pressed down
            if event.key == pygame.K_LEFT: # If it's the left arrow key
                player_x -= player_speed # Move left
            if event.key == pygame.K_RIGHT: # If it's the right arrow key
                player_x += player_speed # Move right

    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.display.flip()

pygame.quit()