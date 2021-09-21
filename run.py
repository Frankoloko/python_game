from classes.player import Player
from classes.goal import Goal
from classes.text import Text
import pygame
from pygame.locals import * # https://www.pygame.org/docs/ref/key.html#module-pygame.key

####################################################################################################

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Artificial Intelligence')

        self.CLOCK = pygame.time.Clock()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800
        self.ROUND_TIME = 300
        self.GENERATION = 0
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.BACKGROUND_COLOR = (36, 36, 36)
        self.SCREEN.fill(self.BACKGROUND_COLOR)
        self.GAME_PAUSED = False

        # Create all Players
        self.PLAYERS = []
        for _ in range(10):
            self.PLAYERS.append(Player(self.SCREEN_HEIGHT, self.SCREEN_WIDTH, self.SCREEN, self.ROUND_TIME))

        # Create Goals
        self.GLOALS = []
        self.GLOALS.append(Goal(self.SCREEN, self.SCREEN_HEIGHT / 2, 30))

        # Create Text
        FONT = pygame.font.SysFont('monospace', 20)
        # FONT = pygame.font.SysFont('Comic Sans MS', 15)
        self.TXT_GENENRATION = Text(self.SCREEN, FONT, (self.SCREEN_WIDTH - 170, 10))

        while True:
            self.CLOCK.tick(40)
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                    elif self.GAME_PAUSED and event.key == K_RETURN:
                        self.start_next_generation()

            self.update()

    def draw_everything(self):
        # Clear screen
        self.SCREEN.fill(self.BACKGROUND_COLOR)

        # Draw text
        self.TXT_GENENRATION.draw(f'Generation: {self.GENERATION}')

        # Draw Players
        for player in self.PLAYERS:
            player.run_next_move()
            player.draw()

        # Draw Goals
        for goal in self.GLOALS:
            goal.draw()

    def update(self):
        self.ROUND_TIME -= 1

        if self.ROUND_TIME <= 0:
            self.pause_game()
        else:
            self.draw_everything()

        pygame.display.flip()

    def pause_game(self):
            # Pause the game & draw the best player green
            best_player = self.PLAYERS[0]
            for player in self.PLAYERS:
                if player.distance_to(self.SCREEN_HEIGHT / 2, 30) < best_player.distance_to(self.SCREEN_HEIGHT / 2, 30):
                    best_player = player
            best_player.draw_winner()

            self.GENERATION += 1
            self.GAME_PAUSED = True

    def start_next_generation(self):
        # Create a new set of players

        # Redraw everything

        # Reset rounds

        # Unpause game

        pass

Game()