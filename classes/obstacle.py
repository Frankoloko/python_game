import pygame

class Obstacle:
    def __init__(self, screen, position_vector, size_vector):
        self.screen = screen

        # Set colours
        # self.colour = (180, 180, 180) # Darker
        # self.colour = (201, 201, 201) # Lighter
        # self.colour = (227, 227, 227) # More lighter
        # self.colour = (242, 242, 242) # More more lighter
        self.colour = (92, 92, 92) # Grey

        self.rect = pygame.Rect(
            position_vector[0] - (size_vector[0] / 2),
            position_vector[1] - (size_vector[1] / 2),
            size_vector[0],
            size_vector[1]
        )

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