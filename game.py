from typing import List

from figure import Figure
from globals import pygame, WIN_SIZE, ICON


def init_game():
    # Init pygame
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode(WIN_SIZE)

    # Title and Icon(32pix)
    pygame.display.set_caption("Space Invaders")
    pygame.display.set_icon(ICON)

    return Game(screen)


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.figures: List = []
        self.player: Figure = None

    @property
    def player(self) -> Figure:
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    def add_fig(self, fig: Figure):
        if fig.name == "Player":
            for f in self.figures:
                if "Player" == f.name:
                    raise ValueError

            self.player: Figure = fig

        self.figures.append(fig)

    def remove_fig(self, fig: Figure) -> None:
        self.figures.remove(fig)

    def draw_fig(self, fig: Figure) -> None:
        self.screen.blit(fig.img, (fig.x, fig.y))

    def draw_figs(self, figs: List) -> None:
        for fig in figs:
            self.draw_fig(fig)

    def draw_all_figs(self) -> None:
        for fig in self.figures:
            self.draw_fig(fig)
