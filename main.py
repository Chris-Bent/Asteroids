import pygame
from constants import *

clock = pygame.time.Clock()
dt = 0


def main(dt):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        deltaTime = clock.tick(60) / 1000.0
        dt += deltaTime


if __name__ == "__main__":
    main(dt)