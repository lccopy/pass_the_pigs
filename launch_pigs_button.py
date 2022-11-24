import pygame


class LaunchButton:
    """button class"""

    def __init__(self, game, msg):
        """init button"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.x = 200
        self.y = 200
        self.width, self.height = 300, 50
        self.button_color = (220, 20, 60)
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(200, 200, self.width, self.height)
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """turn msg into an image and center txt into button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.blit(self.msg_image, (self.x, self.y))


