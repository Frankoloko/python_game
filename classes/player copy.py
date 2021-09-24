import pygame
from random import randint
import cmath
import math

class Player:
    def __init__(self, screen_height, screen_width, screen, rounds):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.rounds = rounds

        # Set colours
        # self.colour = (180, 180, 180) # Darker
        # self.colour = (201, 201, 201) # Lighter
        # self.colour = (227, 227, 227) # More lighter
        self.colour = (242, 242, 242) # More more lighter
        self.original_color = self.colour

        self.moves = [(1, 2), (3, 4), (5, 6)]
        self.move_counter = 0
        self.move_closer_counter = 0
        self.dead = False
        self.size = 10
        self.move_speed = 50

        # Create X amount of moves for the player
        self.moves = []
        for _ in range(rounds):
            # self.moves.append((randint(-self.move_speed, self.move_speed), randint(-self.move_speed, self.move_speed)))

            random_degree = randint(1, 360)
            self.moves.append(random_degree)

        # Start at bottom of screen
        self.rect = pygame.Rect(self.screen_width / 2, self.screen_height - 20, self.size, self.size)

    # PUBLIC FUNCTIONS

    def run_next_move(self):
        if not self.dead:
            degree = self.moves[self.move_counter]
            radians = degree * (math.pi / 180)
            # degree_vector = (math.cos(radians) * self.move_speed, math.sin(radians) * self.move_speed)
            degree_vector = (math.cos(radians) * 2, math.sin(radians) * 2)

            self.rect.move_ip(degree_vector)

            self.move_closer_counter += 1
            if self.move_closer_counter == self.move_speed:
                self.move_closer_counter = 0
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

    def evolve(self, change_percentage):
        '''
            Evolve will take this players moves, evolve them a bit, then return a new player object
            with those moves
        '''
        # Make the player the current player's moves, but with a percentage change
        array_left = len(self.moves)
        random_changes = round(array_left * (change_percentage / 100))
        used_indexes = []
        for _ in range(random_changes):
            random_index = randint(0, array_left - 1)
            while random_index in used_indexes:
                random_index = randint(0, array_left - 1)
            used_indexes.append(random_index)
            random_degree = randint(1, 360)
            self.moves[random_index] = random_degree

    def clone(self):
        '''
            This creates a copy of this player AND IT'S MOVES, but resets all other values
        '''
        new_player = Player(self.screen_height, self.screen_width, self.screen, self.rounds)
        new_player.moves = self.moves.copy()
        return new_player

    def kill(self):
        if not self.dead:
            self.dead = True
            self.colour = (219, 0, 0) # Red

    def draw_original_color(self):
        self.colour = self.original_color
        self.draw()

    # PRIVATE FUNCTIONS

    def __check_outside_screen(self):
        # Check if the self.rect is outside the screen borders, if so, kill it
        if self.rect.y >= self.screen_height - self.size:
            self.kill()
        if self.rect.y <= 0- self.size:
            self.kill()
        if self.rect.x >= self.screen_width - self.size:
            self.kill()
        if self.rect.x <= 0 - self.size:
            self.kill()