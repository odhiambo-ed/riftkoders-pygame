import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("This Legend's First Pygame")

# Set up the colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#Draw a rectangle
pygame.draw.rect(window, GREEN, (50, 50, 100, 100))

#update the display
pygame.display.update()

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # pygame.time.delay(100)
    # window.fill(BLACK)
    # pygame.draw.rect(window, GREEN, (50, 50, 100, 100))
    # pygame.display.update()