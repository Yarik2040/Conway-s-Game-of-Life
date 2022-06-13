import pygame

pygame.init()

sc = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    sc.fill((0, 0, 0))

    for i in range(0, 1290, 10):
        pygame.draw.line(sc, (125, 125, 125), (i, 0), (i, 720))
    for i in range(0, 730, 10):
        pygame.draw.line(sc, (125, 125, 125), (0, i), (1280, i))
    pygame.display.flip()
    clock.tick()
