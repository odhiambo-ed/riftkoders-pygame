#Pygame
import pygame, sys

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My First Pygame')

# Set up the colors
GREEN = (26, 188, 156)
RED = (192, 57, 43)

# #Draw a circle
# pygame.draw.circle(screen, RED, (400, 300), 50)

# # Update the display
# pygame.display.update()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.delay(100)
    screen.fill(GREEN)
    pygame.draw.circle(screen, RED, (400, 300), 50)
    pygame.display.update()