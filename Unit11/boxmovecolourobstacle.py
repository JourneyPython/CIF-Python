import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colour-Changing Box Move")

black = (0, 0, 0)
pink = (255, 192, 203)
green = (152, 251, 152)
blue = (173, 216, 230)

box_colour = green

box_x, box_y = 0, 0
rect_1 = pygame.Rect(box_x, box_y, 30, 30)

middle_rect = pygame.Rect(
    width // 2 - 25,
    height // 2 - 25,
    50,
    50
)

collision_font = pygame.font.SysFont("courier", 36, bold=True)
collision_text = collision_font.render("COLLISION!", True, (255, 255, 255))
collision_rect = collision_text.get_rect(center=(width // 2, 80))

clock = pygame.time.Clock()

flash_counter = 0 
flash_interval = 30 

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box_x -= 5
    if keys[pygame.K_RIGHT]:
        box_x += 5
    if keys[pygame.K_UP]:
        box_y -= 5
    if keys[pygame.K_DOWN]:
        box_y += 5

    box_x = max(0, min(box_x, width - rect_1.width))
    box_y = max(0, min(box_y, height - rect_1.height))
    rect_1.topleft = (box_x, box_y)

    if rect_1.colliderect(middle_rect):
        box_colour = blue
        collision = True
    else:
        box_colour = green
        collision = False

    screen.fill(black)
    pygame.draw.rect(screen, pink, rect_1)
    pygame.draw.rect(screen, box_colour, middle_rect)

    if collision:
        flash_counter += 1
        if flash_counter // flash_interval % 2 == 0:
            screen.blit(collision_text, collision_rect)
    else:
        flash_counter = 0 

    pygame.display.update()

pygame.quit()