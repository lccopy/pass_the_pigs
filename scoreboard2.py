import pygame.font


class Scoreboard2:
    """class to print score info"""

    def __init__(self, game):
        """initialise score """
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        self.text_color = (250, 220, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        score_2 = self.stats.score_player_2
        score_2_str = "{:,}".format(score_2).replace(",", " ")
        self.score_image = self.font.render(score_2_str, True,
                                            self.text_color,
                                            self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):

        self.screen.blit(self.score_image, self.score_rect)
