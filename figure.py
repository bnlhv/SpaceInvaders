from globals import pygame, WIN_SIZE


class Figure:
    def __init__(self,
                 name: str,
                 img_path: str,
                 initial_x: int,
                 initial_y: int):
        self.name: str = name
        self.img = pygame.image.load(img_path)
        self.x = initial_x
        self.y = initial_y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, new_x: int):
        self._x = new_x
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
