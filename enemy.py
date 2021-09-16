from figure import Figure, FIGURES
from globals import WIN_SIZE, FIG_SIZE


class Enemy(Figure):
    def __init__(self,img_path: str, initial_x: int, initial_y: int):
        super().__init__(img_path, initial_x, initial_y, FIGURES.ENEMY, 5)
        self.change_x: int = 5

    def move_enemy(self) -> None:
        if self.x <= 0:
            self.change_x = 5
            self.y += 40
        elif self.x >= WIN_SIZE[0] - FIG_SIZE:
            self.change_x = -5
            self.y += 40

        self.x += self.change_x

