import sys
import pygame

#project 1

class AlienInvasion:
    #class to manage game

    def __init__(self):
        #initialize game and resources
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        #start loop for the game
        while True:
            #listen for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #make most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #make game instance and run it
    ai = AlienInvasion()
    ai.run_game()

