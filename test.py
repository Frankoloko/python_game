from classes.player import Player
from classes.obstacle import Obstacle
from classes.goal import Goal
from classes.text import Text
import pygame
from pygame.locals import * # https://www.pygame.org/docs/ref/key.html#module-pygame.key

pygame.init()
CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))

rect_1 = pygame.Rect(800 / 2, 800 / 2, 10, 10)
rect_2 = pygame.Rect(800 / 2, 800 / 2, 10, 10)


while True:
    CLOCK.tick(1)
    # CLOCK.tick(1000)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

    screen.fill((36, 36, 36))
    rect_1.move_ip((1, 1))
    rect_2.move_ip((1, 1))

    pygame.draw.rect(screen, (242, 242, 242), rect_1)
    pygame.draw.rect(screen, (242, 242, 242), rect_2)

    pygame.display.flip()
