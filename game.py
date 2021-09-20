import os
import random
from typing import List

from Figures.bullet import Bullet
from Figures.enemy import Enemy
from Figures.figure import Figure
from globals import pygame, WIN_SIZE, ICON, FIG_SIZE, WHITE, BLACK, FONT_NAME


class Game:
    """This is Game class and responsible for managing the game"""
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.display_width = 800
        self.display_height = 600
        self.display = pygame.surface((self.display_width, self.display_height))
        self.window = pygame.display.set_mode((self.display_width, self.display_height))
        self.font_name = '/Assets/goblin_font.otf'
        self.game_over: bool = False

    def game_loop(self):
        pygame.mixer.music.load('Assets/spaceinvaders1.mpeg')
        pygame.mixer.music.play(-1)

        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(ICON)

        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(BLACK)
            self.draw_text('Thanks for playing', 28, self.display_width / 2, self.display_height / 2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True

    def reset_keys(self) -> None:
        self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False,\
                                                                                                   False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(FONT_NAME, size)
        surface = font.render(text, True, WHITE)
        text_rect = surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(BLACK)


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

    def show_score(self) -> None:
        score = self.font.render(f"Score: {self.player.live_score}", True, WHITE)
        self.screen.blit(score, (10, 10))

    def show_game_over(self) -> None:
        score = FONT.render(f"Game Over", True, WHITE)
        self.screen.blit(score, (WIN_SIZE[0]//2 - score.get_size()[0]//2, WIN_SIZE[1]//2 - score.get_size()[1]//2))

    def is_game_over(self):
        """This function check if invaders arrived close to player"""
        player_rect = pygame.Rect(
            self.player.x,
            self.player.y,
            self.player.img.get_size()[0],
            self.player.img.get_size()[1]
        )

        for enemy in self.enemies:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.img.get_size()[0], enemy.img.get_size()[1])
            # if there is a collision
            if enemy_rect.colliderect(player_rect):
                self.game_over = True
                break

        if self.game_over:
            # remove all enemies from screen
            for enemy in self.enemies:
                self.remove_enemy(enemy)

        return self.game_over

    def check_hit(self) -> None:
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
                if self.is_game_over():
                    self.game_over = True
                    return

                # check if there is a collision between these 2 rectangles
                if enemy_rect.colliderect(bullet_rect):
                    self.remove_bullet(bullet)
                    self.remove_enemy(enemy)
                    pygame.mixer.Sound('Assets/invaderkilled.wav').play()
                    self.player.live_score += 1
                    self.add_enemy(Enemy(img_path='Assets/enemy.png',
                                         initial_x=random.randint(0, 800 - FIG_SIZE),
                                         initial_y=random.randint(50, 150)
                                         )
                                   )
