import pygame
pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
CLOCK = pygame.time.Clock()

PLAYER = pygame.Rect(150, 180, 10, 7)
PLAYER_COLOUR = (180, 180, 180)
BACKGROUND_COLOUR = (0, 0, 0)

while True:
    # Basics
    CLOCK.tick(40)
    if pygame.event.get(pygame.QUIT): break

    # Check for keys and move player
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: PLAYER.move_ip((-4, 0))
    if pressed[pygame.K_RIGHT]: PLAYER.move_ip((4, 0))

    # Redraw everything
    SCREEN.fill(BACKGROUND_COLOUR)
    pygame.draw.rect(SCREEN, PLAYER_COLOUR, PLAYER)    
    pygame.display.flip()