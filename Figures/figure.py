from enum import Enum

from globals import pygame, WIN_SIZE


class FIGURES(Enum):
    PLAYER = 0,
    ENEMY = 1,
    BULLET = 2


class Figure:
    """
    This class represents class variables that
    is shared between all figure in the game
    """
    def __init__(self, img_path: str, initial_x: int, initial_y: int, fig_kind: FIGURES, x_change: int):
        self.fig_kind: FIGURES = fig_kind
        self.img = pygame.image.load(img_path)
        self.x: int = initial_x
        self.y: int = initial_y
        self.x_change: int = x_change

    @property
    def x_change(self) -> int:
        return self._x_change

    @x_change.setter
    def x_change(self, value: int) -> None:
        self._x_change = value

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, new_x: int):
        self._x = new_x
        if self.fig_kind is FIGURES.PLAYER:
            self.check_x_boundaries()

    def check_x_boundaries(self) -> int:
        """
        Check if figure is out of window boundaries and correct it, else return the x
        :return: the new x place
        """
        if self.x <= 0:
            return 0
        elif self.x >= WIN_SIZE[0] - self.img.get_size()[0]:
            self.x = WIN_SIZE[0] - self.img.get_size()[0]
        else:
            return self.x
