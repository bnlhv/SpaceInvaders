from figure import Figure, FIGURES


class Player(Figure):
    """This class represent the Player, inherit from Figure"""
    def __init__(self, name: str, img_path: str, initial_x: int, initial_y: int):
        super().__init__(img_path, initial_x, initial_y, FIGURES.PLAYER, 0)
        self.name = name
        self.live_score: int = 0
        self.count_score: int = 50

    # def stop_player(self):
    #     self.x_change = 0
    #
    # def move_player(self, key) -> None:
    #     if key == pygame.K_RIGHT:
    #         self.x_change = 3
    #     if key == pygame.K_LEFT:
    #         self.x_change = -3
    #
    #     self.x += self.x_change
