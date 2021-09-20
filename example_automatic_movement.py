from random import randint
import pygame
pygame.init()

CLOCK = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND_COLOUR = (0, 0, 0)
SCREEN.fill(BACKGROUND_COLOUR)

PLAYER = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 10, 10)
PLAYER_COLOUR = (180, 180, 180)

while True:
    # Basics
    CLOCK.tick(40)
    if pygame.event.get(pygame.QUIT): break

    # Check for keys and move player
    PLAYER.move_ip((randint(-2, 2), randint(-2, 2)))

    # Redraw everything
    SCREEN.fill(BACKGROUND_COLOUR)
    pygame.draw.rect(SCREEN, PLAYER_COLOUR, PLAYER)
    pygame.display.flip()