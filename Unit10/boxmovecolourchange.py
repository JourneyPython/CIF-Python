import pygame
import random as rnd
pygame.init()

colouroption = (
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255)
)

colour = rnd.choice(colouroption)
black = (0, 0, 0)

width, height = 800, 600

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

box_x, box_y = 0, 0
rect_1 = pygame.Rect(box_x, box_y, 30, 30)

pygame.display.set_caption("Colour-Changing Box Move")
pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == CHANGE_COLOR_EVENT:
            colour = rnd.choice(colouroption)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box_x -= 5
    if keys[pygame.K_RIGHT]:
        box_x += 5
    if keys[pygame.K_UP]:
        box_y -= 5
    if keys[pygame.K_DOWN]:
        box_y += 5

    rect_1.topleft = (box_x, box_y)

    if box_x < 0:
        box_x = 0
    
    if box_x > width - rect_1.width:
        box_x = width - rect_1.width
    
    if box_y < 0:
        box_y = 0
    
    if box_y > height - rect_1.height:
        box_y = height - rect_1.height
    
    screen = pygame.display.get_surface()
    screen.fill(black)
    pygame.draw.rect(screen, colour, rect_1)
    pygame.display.update()