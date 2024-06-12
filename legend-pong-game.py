# Pong Game
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Legend Pong Game")

# Clock
clock = pygame.time.Clock()

# Set up the colors
GREEN = (8, 143, 143)
BLACK = (0, 0, 0)
BLUE = (137, 207, 240)

# Set up the paddles
paddle1 = pygame.Rect(50, 250, 20, 100)
paddle2 = pygame.Rect(1130, 250, 20, 100)

# Set up the ball
ball = pygame.Rect(600, 400, 20, 20)
ball_speed_x = 7
ball_speed_y = 7

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5
    if keys[pygame.K_UP]:
        paddle2.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.y += 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce the ball off the top and bottom walls
    if ball.top <= 0 or ball.bottom >= 800:
        ball_speed_y = -ball_speed_y

    # Bounce the ball off the paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x

    # Check if the ball goes out of bounds
    if ball.left <= 0 or ball.right >= 1200:
        ball.x = 600
        ball.y = 400

    # Fill the window with black color
    window.fill(BLUE)

    # Draw the paddles
    pygame.draw.rect(window, BLACK, paddle1)
    pygame.draw.rect(window, BLACK, paddle2)

    # Draw the ball
    pygame.draw.ellipse(window, BLACK, ball)

    # Update the display
    pygame.display.update()

    # Set the frames per second
    clock.tick(60)