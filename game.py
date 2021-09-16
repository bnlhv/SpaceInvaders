from typing import List

from bullet import Bullet
from enemy import Enemy
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
        self.enemies: List[Enemy] = []
        self.bullets: List[Bullet] = []
        self.player: Figure = None

    @property
    def player(self) -> Figure:
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    def add_enemy(self, fig: Enemy):
        self.enemies.append(fig)

    def remove_enemy(self, fig: Enemy) -> None:
        self.enemies.remove(fig)

    def add_bullet(self, fig: Bullet):
        self.bullets.append(fig)

    def remove_bullet(self, fig: Bullet) -> None:
        self.bullets.remove(fig)

    def draw_fig(self, fig: Figure) -> None:
        self.screen.blit(fig.img, (fig.x, fig.y))

    def draw_all_figs(self) -> None:
        for enemy in self.enemies:
            self.draw_fig(enemy)

        for bullet in self.bullets:
            bullet.y += bullet.y_change
            self.draw_fig(bullet)

        self.draw_fig(self.player)

    def move_enemies(self) -> None:
        for fig in self.enemies:
            fig.move_enemy()

    def check_collision(self):
        for bullet in self.bullets:
            bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.img.get_size()[0], bullet.img.get_size()[1])
            for enemy in self.enemies:
                enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.img.get_size()[0], enemy.img.get_size()[1])
                if enemy_rect.colliderect(bullet_rect):
                    self.remove_bullet(bullet)
                    self.player.score += 1
                    print(f"hit! score is {self.player.score}")
