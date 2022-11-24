import pygame

DEFAULT_IMAGE_SIZE = (100, 100)


class Pigs:
    def __init__(self):
        self.pig_dot_down = pygame.image.load("images/dot-down.png")
        self.pig_dot_down = pygame.transform.scale(self.pig_dot_down,
                                                   DEFAULT_IMAGE_SIZE).convert_alpha()

        self.pig_dot_up = pygame.image.load("images/dot-up.png")
        self.pig_dot_up = pygame.transform.scale(self.pig_dot_up,
                                                 DEFAULT_IMAGE_SIZE).convert_alpha()

        self.pig_leaning_jowler = pygame.image.load(
            "images/leaning-jowler.png")
        self.pig_leaning_jowler = pygame.transform.scale(
            self.pig_leaning_jowler, DEFAULT_IMAGE_SIZE).convert_alpha()

        self.pig_snouter = pygame.image.load("images/snouter.png")
        self.pig_snouter = pygame.transform.scale(self.pig_snouter,
                                                  DEFAULT_IMAGE_SIZE).convert_alpha()

        self.pig_trotter = pygame.image.load("images/trotter.png")
        self.pig_trotter = pygame.transform.scale(self.pig_trotter,
                                                  DEFAULT_IMAGE_SIZE).convert_alpha()

        self.pig_razorback = pygame.image.load("images/razorback.png")
        self.pig_razorback = pygame.transform.scale(self.pig_razorback,
                                                    DEFAULT_IMAGE_SIZE).convert_alpha()
