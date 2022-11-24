import random
from gamestats import GameStats
import pygame
from settings import Settings
import sys
from pigs import Pigs
from button import Button
import random
from scoreboard1 import Scoreboard1
from scoreboard2 import Scoreboard2
from time import sleep
from stop_button import StopButton
from launch_pigs_button import LaunchButton


class Game:
    """game class"""
    def __init__(self):
        """init"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800),
                                              pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED,
                                              vsync=1)

        self.settings = Settings()
        self.pigs = Pigs()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen.fill(self.settings.bg_color)
        self.init_pigs()
        self.stats = GameStats(self)
        self.play_button = Button(self, "PLAYER 1")
        self.play_button_2 = Button(self, "PLAYER 2")
        self.play_button_3 = Button(self, "PLAYER 1")
        self.scoreboard1 = Scoreboard1(self)
        self.scoreboard2 = Scoreboard2(self)
        self.play_button.draw_button()
        pygame.display.set_caption("Pass The Pigs")
        self.p1_won = Button(self, "P1 WIN")
        self.p2_won = Button(self, "P2 WIN")
        self.list_pigs = ["pig_razorback", "pig_trotter", "pig_snouter",
                          "pig_dot_up", "pig_dot_down", "pig_leaning_jowler"]
        self.score_player_1 = self.stats.score_player_1
        self.score_player_2 = self.stats.score_player_2
        self.P1 = True
        self.stop_button = StopButton(self, "STOP")
        self.launch_button = LaunchButton(self, "ROLL")
        pygame.display.update()
        self.roll_enable = False

    def run_game(self):
        """run loop"""
        while True:
            self.check_events()

    def check_events(self):
        """checking events while playing"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_player_1_button(mouse_pos)
                self.check_stop_button(mouse_pos)
                self.check_player_2_button(mouse_pos)
                self.check_launch_button(mouse_pos)
                self.check_play_button_3(mouse_pos)

    def check_launch_button(self, mouse_pos):
        launch_clicked = self.launch_button.rect.collidepoint(mouse_pos)
        if launch_clicked and self.roll_enable:
            self.random_pigs()

    def check_play_button_3(self, mouse_pos):
        button3_clicked = self.play_button_3.rect.collidepoint(mouse_pos)
        if button3_clicked:
            pass

    def check_player_2_button(self, mouse_pos):
        button2_clicked = self.play_button_2.rect.collidepoint(mouse_pos)
        if button2_clicked and not self.P1:
            self.enter_game()
            self.update_screen()
            self.stop_button.draw_button()
            self.launch_button.draw_button()
            pygame.display.flip()

    def check_player_1_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.P1:
            print("player 1 button clicked")
            print(f"{self.stats.game_active}")
            self.settings.initialize_dynamic_settings()
            self.enter_game()
            self.update_screen()
            self.stop_button.draw_button()
            self.launch_button.draw_button()
            pygame.display.flip()
            self.stats.game_active = True
            self.roll_enable = True

    def check_stop_button(self, mouse_pos):
        stop_clicked = self.stop_button.rect.collidepoint(mouse_pos)
        if stop_clicked and self.P1:
            self.P1 = False
            print(f"state: +{self.P1}")
            self.play_button_2.draw_button()
            pygame.display.update()
            self.stats.current_counter_1 = 0
        elif stop_clicked and not self.P1:
            self.play_button_3.draw_button()
            pygame.display.flip()
            self.P1 = True
            print(f"state P1: +{self.P1}")
            self.stats.current_counter_2 = 0

    def init_pigs(self):
        """include pigs png"""
        self.pig_dot_up = self.pigs.pig_dot_up
        self.screen.blit(self.pig_dot_up, (0, 0))
        self.screen.blit(self.pig_dot_up, (1100, 0))
        self.pig_dot_down = self.pigs.pig_dot_down
        self.screen.blit(self.pig_dot_down, (0, 100))
        self.screen.blit(self.pig_dot_down, (1100, 100))
        self.pig_leaning_jowler = self.pigs.pig_leaning_jowler
        self.screen.blit(self.pig_leaning_jowler, (0, 200))
        self.screen.blit(self.pig_leaning_jowler, (1100, 200))
        self.pig_snouter = self.pigs.pig_snouter
        self.screen.blit(self.pig_snouter, (0, 300))
        self.screen.blit(self.pig_snouter, (1100, 300))
        self.pig_trotter = self.pigs.pig_trotter
        self.screen.blit(self.pig_trotter, (0, 400))
        self.screen.blit(self.pig_trotter, (1100, 400))
        self.pig_razorback = self.pigs.pig_razorback
        self.screen.blit(self.pig_razorback, (0, 500))
        self.screen.blit(self.pig_razorback, (1100, 500))

    def enter_game(self):
        """show scoreboard while entering the game"""
        self.scoreboard1.prep_score()
        self.scoreboard2.prep_score()
        pygame.display.update()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.scoreboard1.show_score()
        self.scoreboard2.show_score()

    def random_pigs(self):
        """randomize the pigs"""

        pygame.draw.rect(self.screen, self.settings.bg_color,
                         pygame.Rect(0, 500,
                                     700, 100))
        pygame.display.flip()
        if self.roll_enable:

            pig_1 = (random.choices(self.list_pigs, weights=(0.20, 0.10, 0.04,
                                                             0.30, 0.35, 0.01),
                                    k=1))

            pig_2 = ((random.choices(self.list_pigs, weights=(0.20, 0.10, 0.04,
                                                              0.30, 0.35,
                                                              0.01),
                                     k=1)))

            # Michael F. Gorman, (2012) Analytics,
            # Pedagogy and the Pass the Pigs Game (INFORMS)
            # Transactions on Education
            # 13(1):57-64

            pig_1 = pig_1[0]
            pig_2 = pig_2[0]
            print(pig_1)
            print(pig_2)
            mixed = False
            if pig_1 == "pig_dot_up" and pig_2 == "pig_dot_up":
                print("+1")
                self.screen.blit(self.pig_dot_up, (400, 500))
                self.screen.blit(self.pig_dot_up, (600, 500))
                if self.P1:
                    self.stats.score_player_1 += 1
                    self.stats.current_counter_1 += 1
                else:
                    self.stats.score_player_2 += 1
                    self.stats.current_counter_2 += 1
            elif pig_1 == "pig_dot_down" and pig_2 == "pig_dot_down":
                print("+1")
                self.screen.blit(self.pig_dot_down, (400, 500))
                self.screen.blit(self.pig_dot_down, (600, 500))
                if self.P1:
                    self.stats.score_player_1 += 1
                    self.stats.current_counter_1 += 1
                else:
                    self.stats.score_player_2 += 1
                    self.stats.current_counter_2 += 1
            elif pig_1 == "pig_razorback" and pig_2 == "pig_razorback":
                print("+20")
                self.screen.blit(self.pig_razorback, (400, 500))
                self.screen.blit(self.pig_razorback, (600, 500))
                if self.P1:
                    self.stats.score_player_1 += 20
                    self.stats.current_counter_1 += 20
                else:
                    self.stats.score_player_2 += 20
                    self.stats.current_counter_2 += 20
            elif pig_1 == "pig_trotter" and pig_2 == "pig_trotter":
                print("+20")
                self.screen.blit(self.pig_trotter, (400, 500))
                self.screen.blit(self.pig_trotter, (600, 500))
                if self.P1:
                    self.stats.score_player_1 += 20
                    self.stats.current_counter_1 += 20
                else:
                    self.stats.score_player_2 += 20
                    self.stats.current_counter_2 += 20
            elif pig_1 == "pig_snouter" and pig_2 == "pig_snouter":
                print("+40")
                self.screen.blit(self.pig_snouter, (400, 500))
                self.screen.blit(self.pig_snouter, (600, 500))
                if self.P1:
                    self.stats.score_player_1 += 40
                    self.stats.current_counter_1 += 40
                else:
                    self.stats.score_player_2 += 40
                    self.stats.current_counter_2 += 40
            elif pig_1 == "pig_leaning_jowler" and pig_2 == "pig_leaning_jowler":
                print("+60")
                self.screen.blit(self.pig_leaning_jowler, (400, 500))
                self.screen.blit(self.pig_leaning_jowler, (600, 500))
                if self.P1:
                    self.stats.score_player_1 += 60
                    self.stats.current_counter_1 += 60
                else:
                    self.stats.score_player_2 += 60
                    self.stats.current_counter_2 += 60
            elif pig_1 == "pig_dot_up" and pig_2 == "pig_dot_down":
                print("+ pig out +")
                self.screen.blit(self.pig_dot_up, (400, 500))
                self.screen.blit(self.pig_dot_down, (600, 500))
                if self.P1:
                    self.P1 = False
                    self.play_button_2.draw_button()
                    self.stats.score_player_1 = (self.stats.score_player_1 -
                                                 self.stats.current_counter_1)
                    if self.stats.score_player_1 <= 0:
                        self.stats.score_player_1 = 0
                    self.stats.current_counter_1 = 0

                else:
                    self.P1 = True
                    self.play_button_3.draw_button()
                    self.stats.score_player_2 = (self.stats.score_player_2 -
                                                 self.stats.current_counter_2)
                    if self.stats.score_player_2 <= 0:
                        self.stats.score_player_2 = 0
                    self.stats.current_counter_2 = 0

            elif pig_1 == "pig_dot_down" and pig_2 == "pig_dot_up":
                print("+ pig out +")
                self.screen.blit(self.pig_dot_down, (400, 500))
                self.screen.blit(self.pig_dot_up, (600, 500))
                if self.P1:
                    self.P1 = False
                    self.play_button_2.draw_button()

                    self.stats.score_player_1 = (self.stats.score_player_1 -
                                                 self.stats.current_counter_1)
                    if self.stats.score_player_1 <= 0:
                        self.stats.score_player_1 = 0
                    self.stats.current_counter_1 = 0
                else:
                    self.P1 = True
                    self.play_button_3.draw_button()
                    self.stats.score_player_2 = (self.stats.score_player_2 -
                                                 self.stats.current_counter_2)
                    if self.stats.score_player_2 <= 0:
                        self.stats.score_player_2 = 0
                    self.stats.current_counter_2 = 0

            ##########
            else:
                mixed = True
            if mixed:
                if pig_1 == "pig_dot_up":
                    if pig_2 == "pig_razorback":
                        print("+5")
                        self.screen.blit(self.pig_dot_up, (400, 500))
                        self.screen.blit(self.pig_razorback, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 5
                            self.stats.current_counter_1 += 5
                        else:
                            self.stats.score_player_2 += 5
                            self.stats.current_counter_2 += 5
                    elif pig_2 == "pig_trotter":
                        print("+5")
                        self.screen.blit(self.pig_dot_up, (400, 500))
                        self.screen.blit(self.pig_trotter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 5
                            self.stats.current_counter_1 += 5
                        else:
                            self.stats.score_player_2 += 5
                            self.stats.current_counter_2 += 5
                    elif pig_2 == "pig_snouter":
                        print("+10")
                        self.screen.blit(self.pig_dot_up, (400, 500))
                        self.screen.blit(self.pig_snouter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 10
                            self.stats.current_counter_1 += 10
                        else:
                            self.stats.score_player_2 += 10
                            self.stats.current_counter_2 += 10
                    elif pig_2 == "pig_leaning_jowler":
                        print("+15")
                        self.screen.blit(self.pig_dot_up, (400, 500))
                        self.screen.blit(self.pig_leaning_jowler, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 15
                            self.stats.current_counter_1 += 15
                        else:
                            self.stats.score_player_2 += 15
                            self.stats.current_counter_2 += 15
                elif pig_1 == "pig_dot_down":
                    if pig_2 == "pig_razorback":
                        print("+5")
                        self.screen.blit(self.pig_dot_down, (400, 500))
                        self.screen.blit(self.pig_razorback, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 5
                            self.stats.current_counter_1 += 5
                        else:
                            self.stats.score_player_2 += 5
                            self.stats.current_counter_2 += 5
                    elif pig_2 == "pig_trotter":
                        print("+5")
                        self.screen.blit(self.pig_dot_down, (400, 500))
                        self.screen.blit(self.pig_trotter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 5
                            self.stats.current_counter_1 += 5
                        else:
                            self.stats.score_player_2 += 5
                            self.stats.current_counter_2 += 5
                    elif pig_2 == "pig_snouter":
                        print("+10")
                        self.screen.blit(self.pig_dot_down, (400, 500))
                        self.screen.blit(self.pig_snouter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 10
                            self.stats.current_counter_1 += 10
                        else:
                            self.stats.score_player_2 += 10
                            self.stats.current_counter_2 += 10
                    elif pig_2 == "pig_leaning_jowler":
                        print("+15")
                        self.screen.blit(self.pig_dot_down, (400, 500))
                        self.screen.blit(self.pig_leaning_jowler, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 15
                            self.stats.current_counter_1 += 15
                        else:
                            self.stats.score_player_2 += 15
                            self.stats.current_counter_2 += 15
                elif pig_1 == "pig_razorback":
                    if pig_2 == "pig_dot_up":
                        print("+5")
                        self.screen.blit(self.pig_razorback, (400, 500))
                        self.screen.blit(self.pig_dot_up, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 5
                            self.stats.current_counter_1 += 5
                        else:
                            self.stats.score_player_2 += 5
                            self.stats.current_counter_2 += 5
                    elif pig_2 == "pig_dot_down":
                        print("+5")
                        self.screen.blit(self.pig_razorback, (400, 500))
                        self.screen.blit(self.pig_dot_down, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 5
                            self.stats.current_counter_1 += 5
                        else:
                            self.stats.score_player_2 += 5
                            self.stats.current_counter_2 += 5
                    elif pig_2 == "pig_trotter":
                        print("+10")
                        self.screen.blit(self.pig_razorback, (400, 500))
                        self.screen.blit(self.pig_trotter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 10
                            self.stats.current_counter_1 += 10
                        else:
                            self.stats.score_player_2 += 10
                            self.stats.current_counter_2 += 10
                    elif pig_2 == "pig_snouter":
                        print("+15")
                        self.screen.blit(self.pig_razorback, (400, 500))
                        self.screen.blit(self.pig_snouter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 15
                            self.stats.current_counter_1 += 15
                        else:
                            self.stats.score_player_2 += 15
                            self.stats.current_counter_2 += 15
                    elif pig_2 == "pig_leaning_jowler":
                        print("+20")
                        self.screen.blit(self.pig_razorback, (400, 500))
                        self.screen.blit(self.pig_leaning_jowler, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 20
                            self.stats.current_counter_1 += 20
                        else:
                            self.stats.score_player_2 += 20
                            self.stats.current_counter_2 += 20

                elif pig_1 == "pig_trotter":
                    if pig_2 == "pig_dot_up":
                        print("+5")
                        self.screen.blit(self.pig_trotter, (400, 500))
                        self.screen.blit(self.pig_dot_up, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 5
                            self.stats.current_counter_1 += 5
                        else:
                            self.stats.score_player_2 += 5
                            self.stats.current_counter_2 += 5
                    elif pig_2 == "pig_dot_down":
                        print("+5")
                        self.screen.blit(self.pig_trotter, (400, 500))
                        self.screen.blit(self.pig_dot_down, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 5
                            self.stats.current_counter_1 += 5
                        else:
                            self.stats.score_player_2 += 5
                            self.stats.current_counter_2 += 5
                    elif pig_2 == "pig_razorback":
                        print("+10")
                        self.screen.blit(self.pig_trotter, (400, 500))
                        self.screen.blit(self.pig_razorback, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 10
                            self.stats.current_counter_1 += 10
                        else:
                            self.stats.score_player_2 += 10
                            self.stats.current_counter_2 += 10
                    elif pig_2 == "pig_snouter":
                        print("+15")
                        self.screen.blit(self.pig_trotter, (400, 500))
                        self.screen.blit(self.pig_snouter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 15
                            self.stats.current_counter_1 += 15
                        else:
                            self.stats.score_player_2 += 15
                            self.stats.current_counter_2 += 15
                    elif pig_2 == "pig_leaning_jowler":
                        print("+20")
                        self.screen.blit(self.pig_trotter, (400, 500))
                        self.screen.blit(self.pig_leaning_jowler, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 20
                            self.stats.current_counter_1 += 20
                        else:
                            self.stats.score_player_2 += 20
                            self.stats.current_counter_2 += 20

                elif pig_1 == "pig_snouter":
                    if pig_2 == "pig_dot_up":
                        print("+10")
                        self.screen.blit(self.pig_snouter, (400, 500))
                        self.screen.blit(self.pig_dot_up, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 10
                            self.stats.current_counter_1 += 10
                        else:
                            self.stats.score_player_2 += 10
                            self.stats.current_counter_2 += 10
                    elif pig_2 == "pig_dot_down":
                        print("+10")
                        self.screen.blit(self.pig_snouter, (400, 500))
                        self.screen.blit(self.pig_dot_down, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 10
                            self.stats.current_counter_1 += 10
                        else:
                            self.stats.score_player_2 += 10
                            self.stats.current_counter_2 += 10
                    elif pig_2 == "pig_trotter":
                        print("+15")
                        self.screen.blit(self.pig_snouter, (400, 500))
                        self.screen.blit(self.pig_trotter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 15
                            self.stats.current_counter_1 += 15
                        else:
                            self.stats.score_player_2 += 15
                            self.stats.current_counter_2 += 15
                    elif pig_2 == "pig_razorback":
                        print("+15")
                        self.screen.blit(self.pig_snouter, (400, 500))
                        self.screen.blit(self.pig_razorback, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 15
                            self.stats.current_counter_1 += 15
                        else:
                            self.stats.score_player_2 += 15
                            self.stats.current_counter_2 += 15
                    elif pig_2 == "pig_leaning_jowler":
                        print("+25")
                        self.screen.blit(self.pig_snouter, (400, 500))
                        self.screen.blit(self.pig_leaning_jowler, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 25
                            self.stats.current_counter_1 += 25
                        else:
                            self.stats.score_player_2 += 25
                            self.stats.current_counter_2 += 25

                elif pig_1 == "pig_leaning_jowler":
                    if pig_2 == "pig_dot_up":
                        print("+15")
                        self.screen.blit(self.pig_leaning_jowler, (400, 500))
                        self.screen.blit(self.pig_dot_up, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 15
                            self.stats.current_counter_1 += 15
                        else:
                            self.stats.score_player_2 += 15
                            self.stats.current_counter_2 += 15
                    elif pig_2 == "pig_dot_down":
                        print("+15")
                        self.screen.blit(self.pig_leaning_jowler, (400, 500))
                        self.screen.blit(self.pig_dot_down, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 15
                            self.stats.current_counter_1 += 15
                        else:
                            self.stats.score_player_2 += 15
                            self.stats.current_counter_2 += 15
                    elif pig_2 == "pig_trotter":
                        print("+20")
                        self.screen.blit(self.pig_leaning_jowler, (400, 500))
                        self.screen.blit(self.pig_trotter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 20
                            self.stats.current_counter_1 += 20
                        else:
                            self.stats.score_player_2 += 20
                            self.stats.current_counter_2 += 20
                    elif pig_2 == "pig_razorback":
                        print("+20")
                        self.screen.blit(self.pig_leaning_jowler, (400, 500))
                        self.screen.blit(self.pig_razorback, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 20
                            self.stats.current_counter_1 += 20
                        else:
                            self.stats.score_player_2 += 20
                            self.stats.current_counter_2 += 20
                    elif pig_2 == "pig_snouter":
                        print("+25")
                        self.screen.blit(self.pig_leaning_jowler, (400, 500))
                        self.screen.blit(self.pig_snouter, (600, 500))
                        if self.P1:
                            self.stats.score_player_1 += 25
                            self.stats.current_counter_1 += 25
                        else:
                            self.stats.score_player_2 += 25
                            self.stats.current_counter_2 += 25
            print("---")

            pygame.draw.rect(self.screen, self.settings.bg_color,
                             pygame.Rect(0, 0, 1200, 200))

            self.scoreboard1.prep_score()
            self.scoreboard1.show_score()
            self.scoreboard2.prep_score()
            self.scoreboard2.show_score()
            print(f"P1 {self.stats.score_player_1}")
            print(f"P2 {self.stats.score_player_2}")

            if self.stats.score_player_1 >= 100:
                if self.stats.score_player_2 < self.stats.score_player_1:
                    sleep(3)
                    print("player 1 win")
                    self.p1_won.draw_button()
                    pygame.display.flip()
                    pygame.display.update()
                    sleep(5)
                    sys.exit()

            if self.stats.score_player_2 >= 100:
                if self.stats.score_player_1 < self.score_player_2:
                    print("player 2 win")
                    self.p2_won.draw_button()
                    pygame.display.flip()
                    pygame.display.update()
                    sleep(5)
                    sys.exit()

            pygame.display.flip()
            pygame.display.update()


if __name__ == "__main__":
    # create an instance of the game and run it
    g = Game()
    g.run_game()
