import pygame
import random
pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

bird_x = 50
bird_y = 300
bird_width = 30
bird_height = 30
bird_velocity = 0
gravity = 0.5
jump_strength = -8

pipe_width = 60
pipe_gap = 120
pipe_x = WIDTH
pipe_height = random.randint(100, 400)
pipe_speed = 3

score = 0
font = pygame.font.SysFont(None, 40)

running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    bird_velocity += gravity
    bird_y += bird_velocity

    bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
    pygame.draw.rect(screen, RED, bird_rect)

    pipe_x -= pipe_speed
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(
        pipe_x,
        pipe_height + pipe_gap,
        pipe_width,
        HEIGHT
    )

    pygame.draw.rect(screen, GREEN, top_pipe)
    pygame.draw.rect(screen, GREEN, bottom_pipe)

    if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
        running = False

    if bird_y < 0 or bird_y > HEIGHT:
        running = False

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if not running:
        game_over_text = font.render("Game Over!", True, WHITE)
        final_score_text = font.render(f"Final Score: {score}", True, WHITE)
        screen.fill(BLACK)
        
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(1000)
        break

    pygame.display.update()

pygame.quit()