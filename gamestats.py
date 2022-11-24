class GameStats:
    """class to manage stats"""

    def __init__(self, game):
        """initialisation of stats"""

        self.settings = game.settings
        self.reset_stats()
        # start active
        self.game_active = False

    def reset_stats(self):
        """initialize stats who can vary while playing"""
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.current_counter_1 = 0
        self.current_counter_2 = 0
