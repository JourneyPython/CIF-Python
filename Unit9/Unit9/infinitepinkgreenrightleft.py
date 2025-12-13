import pygame
pygame.init()

pink = (255, 105, 180)
green = (0, 255, 0)
white = (255, 255, 255)
width, height = 800, 600

box_x, box_y = 0, 0
rect_1 = pygame.Rect(box_x, box_y, 30, 30)

box2_x, box2_y = width - 30, 100
rect_2 = pygame.Rect(box2_x, box2_y, 30, 30)

pygame.display.set_caption("Infinite Pink Green Right Left")
pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        box_x += 5

    rect_1.topleft = (box_x, box_y)

    if box_x > width:
        box_x = -rect_1.width
    if box_x < -rect_1.width:
        box_x = width

    if box_y < 0:
        box_y = 0
    if box_y > height - rect_1.height:
        box_y = height - rect_1.height

    if keys[pygame.K_a]:
        box2_x -= 5


    rect_2.topleft = (box2_x, box2_y)

    if box2_x < -rect_2.width:
        box2_x = width
    if box2_x > width:
        box2_x = -rect_2.width

    screen = pygame.display.get_surface()
    screen.fill(white)
    pygame.draw.rect(screen, green, rect_1)
    pygame.draw.rect(screen, pink, rect_2)
    pygame.display.update()