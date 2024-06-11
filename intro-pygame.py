import pygame, sys

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My First Pygame')

# # Set up the colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)

# # Set up the fonts
# font = pygame.font.Font(None, 48)

# # Set up the text
# text = font.render('Hello Pygame', True, WHITE)

# # Set up the text position
# text_rect = text.get_rect()
# text_rect.centerx = window.get_rect().centerx
# text_rect.centery = window.get_rect().centery

# # Fill the background
# window.fill(BLACK)

# # Draw the text
# window.blit(text, text_rect)

# # Show the window
# pygame.display.flip()

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    pygame.time.delay(100)
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (50, 50, 100, 100))
    pygame.draw.circle(window, (0, 255, 0), (200, 200), 50)
    pygame.draw.line(window, (0, 0, 255), (400, 400), (500, 500), 5)
    pygame.draw.polygon(window, (255, 255, 0), ((600, 100), (700, 100), (650, 50)))

