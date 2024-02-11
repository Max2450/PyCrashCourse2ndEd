import pygame

class Ship:
    # this class manages the ship

    def __init__(self, ai_game):
        # initialize ship and starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start new ships at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag for continuous movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # use movement flag to update ship's position
        # Update ship x value, not the rect's
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
            # draw ship at current location
        self.screen.blit(self.image, self.rect)