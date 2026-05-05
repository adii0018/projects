import pygame
import random

# Initialize pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 235)

# Bird
bird_x = 50
bird_y = 250
bird_vel = 0
gravity = 0.5
jump = -8

# Pipes
pipe_width = 60
pipe_gap = 150
pipe_x = WIDTH
pipe_height = random.randint(100, 400)

# Clock
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 36)

def draw_bird():
    pygame.draw.circle(screen, (255, 255, 0), (bird_x, int(bird_y)), 15)

def draw_pipe():
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT))

def check_collision():
    if bird_y < 0 or bird_y > HEIGHT:
        return True
    if pipe_x < bird_x < pipe_x + pipe_width:
        if bird_y < pipe_height or bird_y > pipe_height + pipe_gap:
            return True
    return False

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = jump

    # Bird physics
    bird_vel += gravity
    bird_y += bird_vel

    # Pipe movement
    pipe_x -= 3
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    # Draw
    draw_bird()
    draw_pipe()

    # Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Collision
    if check_collision():
        print("Game Over! Score:", score)
        running = False

    pygame.display.update()

pygame.quit()