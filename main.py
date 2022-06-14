import pygame
from field import *

pygame.init()
 
sc = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
fld = snowflake() # airforce()
generate_new_field = 0
speed = 10
speed_add = 10
speed_mod = 70

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = event.pos[0] // 10
                y = event.pos[1] // 10
                fld[y][x] = not fld[y][x]
            elif event.button == 3:
                generate_new_field = not generate_new_field
            else:
                speed = (speed + speed_add) % speed_mod


    sc.fill((0, 0, 0))

    for i in range(0, 1290, 10):
        pygame.draw.line(sc, (50, 50, 50), (i, 0), (i, 720))
    for i in range(0, 730, 10):
        pygame.draw.line(sc, (50, 50, 50), (0, i), (1280, i))

    for x in range(HEIGHT):
        for y in range(WIDTH):
            if fld[x][y]:
                pygame.draw.rect(sc, (125, 125, 125), (10 * y, 10 * x, 10, 10))
    if generate_new_field:
        fld = get_new_iteration(fld)
    pygame.display.flip()
    clock.tick(speed)
