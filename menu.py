import pygame

from globals import BLACK


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.display_width / 2, self.game.display_height / 2
        self.run_menu = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MenuItem:
    def __init__(self):


class MainMenu(Menu):
    def __init__(self, game):
        super(MainMenu, self).__init__(game)
        self.state = "Start Game"
        self.start_x, self.start_y = self.mid_w, self.mid_h + 30
        self.options_x, self.options_y = self.mid_w, self.mid_h + 50
        self.credit_x, self.credit_y = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):
        self.run_menu = True

        while self.run_menu:
            self.game.check_events()
            self.game.display.fill(BLACK)
            self.game.draw_text("Main Menu", 20, self.game.display_width, self.game.display_height - 20)
            self.game.draw_text("Start Game", 20, self.start_x, self.start_y)
            self.game.draw_text("Options", 20, self.options_x, self.options_y_y)
            self.game.draw_text("Credits", 20, self.credit_x, self.credit_y)
            self.draw_cursor()


    def move_cursor(self):


