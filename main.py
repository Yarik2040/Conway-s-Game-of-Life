import pygame

pygame.init()
sc = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    sc.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick()
