import sys
import pygame

from settings import Settings
from ship import Ship


# project 1

class AlienInvasion:
    # class to manage game

    def __init__(self):
        # initialize game and resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the background color (now in settings)
        #self.bg_color = (230, 230, 230)

    def run_game(self):
        # start loop for the game
        while True:
            # listen for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen each pass
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # make game instance and run it
    ai = AlienInvasion()
    ai.run_game()
