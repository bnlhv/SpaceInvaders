from enum import Enum

from figure import Figure, FIGURES


class BulletState(Enum):
    READY = 0,
    FIRE = 1


class Bullet(Figure):
    def __init__(self, img_path, initial_x, initial_y):
        super(Bullet, self).__init__(img_path, initial_x, initial_y, FIGURES.BULLET, 0)
        self.y_change = -9
