from figure import Figure
from globals import WIN_SIZE, FIG_SIZE


class Enemy(Figure):
    def __init__(self, name, img_path, initial_x, initial_y):
        super.__init__(name, img_path, initial_x, initial_y)
        self.change_x: float = 0

    def move_enemy(self) -> float:
        if super(Enemy, self).x <= 0:
            self.change_x = 0.3
        elif super(Enemy, self).x >= WIN_SIZE[0] - FIG_SIZE:
            self.change_x = -0.3

        return self.change_x

