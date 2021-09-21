import pygame
from random import randint
import cmath

class Player:
    def __init__(self, screen_height, screen_width, screen, rounds):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width

        # Set colours
        # self.colour = (180, 180, 180) # Darker
        # self.colour = (201, 201, 201) # Lighter
        # self.colour = (227, 227, 227) # More lighter
        self.colour = (242, 242, 242) # More more lighter

        self.moves = [(1, 2), (3, 4), (5, 6)]
        self.move_counter = 0
        self.dead = False
        self.size = 10

        # Create X amount of moves for the player
        self.moves = []
        for _ in range(rounds):
            self.moves.append((randint(-2, 2), randint(-2, 2)))

        # Start at bottom of screen
        self.rect = pygame.Rect(self.screen_width / 2, self.screen_height - 20, self.size, self.size)

    # PUBLIC FUNCTIONS

    def run_next_move(self):
        if not self.dead:
            self.rect.move_ip(self.moves[self.move_counter])
            self.move_counter += 1
            self.__check_outside_screen()

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)

    def distance_to(self, x, y):
        # distance = root( square(x2 - x1) + square(y2 - y1) )
        # square: 5 ** 2
        # root: cmath.sqrt()

        distance = round( cmath.sqrt( ( (x - self.rect.x) ** 2 ) + ( (y - self.rect.y) ** 2 ) ).real )
        return distance

    def draw_winner(self):
        # self.colour = (200, 255, 0) # Yellow
        # self.colour = (0, 170, 255) # Blue
        # self.colour = (69, 137, 255) # Blue 2 whiter
        self.colour = (0, 94, 255) # Blue 2
        self.draw()

    # PRIVATE FUNCTIONS

    def __kill(self):
        if not self.dead:
            self.dead = True
            self.colour = (219, 0, 0) # Red

    def __check_outside_screen(self):
        # Check if the self.rect is outside the screen borders, if so, kill it
        if self.rect.y >= self.screen_height - self.size:
            self.__kill()
        if self.rect.y <= 0- self.size:
            self.__kill()
        if self.rect.x >= self.screen_width - self.size:
            self.__kill()
        if self.rect.x <= 0 - self.size:
            self.__kill()