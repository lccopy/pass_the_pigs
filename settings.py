class Settings:

    def __init__(self):
        """initialisation of the game settings - static params"""
        # screen params
        self.player_2_score = None
        self.player_1_score = None
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (144, 161, 125)
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """changing params while game"""
        self.player_1_score = 0
        self.player_2_score = 0
