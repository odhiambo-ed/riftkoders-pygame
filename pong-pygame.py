# Pong game
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong Game")

# Clock
clock = pygame.time.Clock()

# Set up the colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set up the paddles
paddle1 = pygame.Rect(50, 250, 20, 100)
paddle2 = pygame.Rect(730, 250, 20, 100)

# Set up the ball
ball = pygame.Rect(400, 300, 20, 20)
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
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y = -ball_speed_y

    # Bounce the ball off the paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x

    # Check if the ball goes out of bounds
    if ball.left <= 0 or ball.right >= 800:
        ball.x = 400
        ball.y = 300
        ball_speed_x = 7
        ball_speed_y = 7

    # Fill the window with black color
    window.fill(BLACK)

    # Draw the paddles and ball
    pygame.draw.rect(window, GREEN, paddle1)
    pygame.draw.rect(window, GREEN, paddle2)
    pygame.draw.ellipse(window, GREEN, ball)

    # Update the display
    pygame.display.update()
    clock.tick(60)