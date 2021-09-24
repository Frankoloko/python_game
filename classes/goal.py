import pygame

class Goal:
    def __init__(self, screen, top, left):
        self.screen = screen
        self.rect = pygame.Rect(top, left, 20, 20)

        # Set colours
        # self.colour = (0, 255, 8) # Pure green
        # self.colour = (0, 240, 8) # Slightly darker green
        self.colour = (0, 219, 7) # Slightly darkerer green

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)

    def check_colissions(self, players):
        '''
            This will check all colissions with players and kill all the collided players
        '''
        for player in players:
            collided = self.rect.colliderect(player.rect)
            if collided:
                player.kill()