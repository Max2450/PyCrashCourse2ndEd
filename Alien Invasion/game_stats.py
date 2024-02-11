class GameStats:
    """Track stats for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        # start Alien Invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize dynamic stats"""
        self.ships_left = self.settings.ship_limit