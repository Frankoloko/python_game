from classes.player import Player
from classes.obstacle import Obstacle
from classes.goal import Goal
from classes.text import Text
import pygame
from pygame.locals import * # https://www.pygame.org/docs/ref/key.html#module-pygame.key

####################################################################################################

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Artificial Intelligence')

        # self.AUTO_RUN = False
        self.AUTO_RUN = True

        self.CLOCK = pygame.time.Clock()
        self.PLAYER_COUNT = 50
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800
        self.ROUND_TIME = 100
        self.ROUNDS_LEFT = self.ROUND_TIME
        self.GENERATION = 0
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.BACKGROUND_COLOR = (36, 36, 36)
        self.SCREEN.fill(self.BACKGROUND_COLOR)
        self.GAME_PAUSED = False

        # Create all Players
        self.PLAYERS = []
        for _ in range(self.PLAYER_COUNT):
            self.PLAYERS.append(Player(self.SCREEN_HEIGHT, self.SCREEN_WIDTH, self.SCREEN, self.ROUND_TIME))

        # Create Obstacles
        self.OBSTACLES = [
            Obstacle(self.SCREEN, position_vector=(self.SCREEN_WIDTH / 2, 400), size_vector=(400, 200))
        ]

        # Create Goals
        self.GLOALS = []
        self.GLOALS.append(Goal(self.SCREEN, self.SCREEN_HEIGHT / 2, 30))

        # Create Text
        FONT = pygame.font.SysFont('monospace', 20)
        # FONT = pygame.font.SysFont('Comic Sans MS', 15)
        self.TXT_GENENRATION = Text(self.SCREEN, FONT, (self.SCREEN_WIDTH - 185, 10))

        while True:
            self.CLOCK.tick(15)
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        return
                    elif self.GAME_PAUSED and event.key == K_RETURN:
                        self.start_next_generation()

            self.update()

    def draw_everything(self):
        # THE ORDER IN WHICH YOU DRAW THINGS IS VERY IMPORTANT

        # Clear screen
        self.SCREEN.fill(self.BACKGROUND_COLOR)

        # Draw Obstacles and check collissions
        for obstacle in self.OBSTACLES:
            obstacle.draw()
            obstacle.check_colissions(self.PLAYERS)

        # Draw Players
        for player in self.PLAYERS:
            player.run_next_move()
            player.draw()

        # Draw Goals
        for goal in self.GLOALS:
            goal.draw()

        # Draw text
        self.TXT_GENENRATION.draw(f'Generation: {self.GENERATION}')

    def update(self):
        if self.GAME_PAUSED:
            return

        self.ROUNDS_LEFT -= 1

        if self.ROUNDS_LEFT <= 0:
            self.declare_winner_and_pause()
        else:
            self.draw_everything()

        pygame.display.flip()

    def declare_winner_and_pause(self):
        # Pause the game & draw the best player green
        self.PLAYERS[-1].draw_original_color()
        self.best_player = self.PLAYERS[0]
        for player in self.PLAYERS:
            # if not player.dead:
            if player.distance_to(self.SCREEN_HEIGHT / 2, 30) < self.best_player.distance_to(self.SCREEN_HEIGHT / 2, 30):
                self.best_player = player
        self.best_player.draw_winner()

        self.GENERATION += 1
        self.GAME_PAUSED = True        
            
        if self.AUTO_RUN:
            self.start_next_generation()

    def start_next_generation(self):
        # Create all Players
        self.PLAYERS = []
        for index in range(self.PLAYER_COUNT):
            # Create new players as clones from the best player, but evolve them
            new_player = self.best_player.clone()
            new_player.evolve(change_percentage=50)
            self.PLAYERS.append(new_player)

        # Keep the best player in case no one evolves better
        new_player = self.best_player.clone()
        new_player.draw_winner()
        self.PLAYERS.append(new_player)

        # Reset rounds
        self.ROUNDS_LEFT = self.ROUND_TIME
        self.GAME_PAUSED = False
        self.draw_everything()

Game()