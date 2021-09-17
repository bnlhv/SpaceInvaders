from figure import Figure, FIGURES
from globals import WIN_SIZE, FIG_SIZE


class Enemy(Figure):
    """This class represents one Enemy Figure"""
    def __init__(self, img_path: str, initial_x: int, initial_y: int):
        super().__init__(img_path, initial_x, initial_y, FIGURES.ENEMY, 5)

    def move_enemy(self) -> None:
        """This function moves the enemy back and fourth automatically"""
        if self.x <= 0:
            self.x_change = 5
            self.y += 40
        elif self.x >= WIN_SIZE[0] - FIG_SIZE:
            self.x_change = -5
            self.y += 40

        self.x += self.x_change
