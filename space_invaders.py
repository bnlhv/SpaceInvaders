from typing import List

from Figures.bullet import Bullet
from Figures.enemy import Enemy
from Figures.figure import Figure


class SpaceInvaders:
    def __init__(self):
        self.enemies: List[Enemy] = []
        self.bullets: List[Bullet] = []
        self.player: Figure = None
