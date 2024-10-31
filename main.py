import pygame
from constants import *
from player import Player


clock = pygame.time.Clock()
dt = 0


def main(dt):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        screen.fill(("black"))
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        deltaTime = clock.tick(60) / 1000.0
        dt += deltaTime
        

if __name__ == "__main__":
    main(dt)