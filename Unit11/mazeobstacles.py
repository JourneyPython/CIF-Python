import pygame

# Initialize Pygame
pygame.init()

# Window size
WIDTH = 400
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Maze")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Maze layout (1 = wall, 0 = open space)
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,1,0,0,0,1,1],
    [1,0,0,0,1,0,1,0,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,0,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,1,0,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

ROWS = len(maze)
COLS = len(maze[0])
CELL_SIZE = WIDTH // COLS  # Size of each square

# Player position
player_row = 1
player_col = 1

# Game loop
running = True
while running:
    pygame.time.delay(100)  # Slows down the loop so it's easier to control

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and maze[player_row][player_col - 1] == 0:
        player_col -= 1
    if keys[pygame.K_RIGHT] and maze[player_row][player_col + 1] == 0:
        player_col += 1
    if keys[pygame.K_UP] and maze[player_row - 1][player_col] == 0:
        player_row -= 1
    if keys[pygame.K_DOWN] and maze[player_row + 1][player_col] == 0:
        player_row += 1

    # Draw everything
    WINDOW.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            color = BLACK if maze[row][col] == 1 else WHITE
            pygame.draw.rect(WINDOW, color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw player
    pygame.draw.rect(WINDOW, RED, (player_col*CELL_SIZE, player_row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update display
    pygame.display.update()

pygame.quit()