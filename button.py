import pygame


class Button:
    """button class"""

    def __init__(self, game, msg):
        """init button"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 300, 50
        self.button_color = (250, 220, 30)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """turn msg into an image and center txt into button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


