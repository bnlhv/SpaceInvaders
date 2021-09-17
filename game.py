import random
from typing import List

from bullet import Bullet
from enemy import Enemy
from figure import Figure
from globals import pygame, WIN_SIZE, ICON, FIG_SIZE


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.enemies: List[Enemy] = []
        self.bullets: List[Bullet] = []
        self.player: Figure = None

    @classmethod
    def init_game(cls):
        """This is the init game function"""
        # Init pygame
        pygame.init()

        # Create screen
        screen = pygame.display.set_mode(WIN_SIZE)

        # Title and Icon(32pix)
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(ICON)

        return cls(screen)

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
        try:
            self.bullets.remove(fig)
        except ValueError:
            pass

    def draw_fig(self, fig: Figure) -> None:
        """
        draw one fig to screen
        :param fig: the figure to draw
        """
        self.screen.blit(fig.img, (fig.x, fig.y))

    def draw_all_figs(self) -> None:
        """Function that go through all figures in game and draw them"""
        for enemy in self.enemies:
            self.draw_fig(enemy)

        for bullet in self.bullets:
            bullet.y += bullet.y_change
            self.draw_fig(bullet)

        self.draw_fig(self.player)

    def move_enemies(self) -> None:
        """For each enemy, move it on the board"""
        for fig in self.enemies:
            fig.move_enemy()

    def check_collision(self) -> None:
        """
        Check collision between a bullet and an enemy,
        if True - remove enemy and bullet and update the score
        """
        for bullet in self.bullets:
            if bullet.y <= 0:
                self.remove_bullet(bullet)
            bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.img.get_size()[0], bullet.img.get_size()[1])
            for enemy in self.enemies:
                enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.img.get_size()[0], enemy.img.get_size()[1])

                # check if there is a collision between these 2 rectangles
                if enemy_rect.colliderect(bullet_rect):
                    self.remove_bullet(bullet)
                    self.remove_enemy(enemy)
                    self.player.live_score += 1
                    print(f"hit! score is {self.player.live_score}")
                    self.add_enemy(Enemy(img_path='enemy.png',
                                         initial_x=random.randint(0, 800 - FIG_SIZE),
                                         initial_y=random.randint(50, 150)
                                         )
                                   )