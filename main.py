import random

import pygame

from Figures.bullet import Bullet
from Figures.enemy import Enemy
from Figures.player import Player
from game import Game
from globals import WIN_SIZE, FIG_SIZE, CLOCK, FPS, BACKGROUND, NUM_OF_ENEMIES


def run_game() -> None:
    """
    Main game loop
    :return: None
    """

    game = Game.init_game()

    player = Player(
        name='Player',
        img_path='Assets/player.png',
        initial_x=(WIN_SIZE[0] / 2) - (FIG_SIZE / 2),
        initial_y=(WIN_SIZE[1] * (3 / 4)) + (FIG_SIZE / 2)
    )

    for i in range(NUM_OF_ENEMIES):
        game.add_enemy(Enemy(img_path='Assets/enemy.png',
                             initial_x=random.randint(0, 800 - FIG_SIZE),
                             initial_y=random.randint(50, 150)
                             )
                       )

    game.player = player

    player_x_change = 0
    enemy_x_change = 0

    # Game loop
    running = True
    while running:

        CLOCK.tick(FPS)
        game.screen.blit(BACKGROUND, (0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check if it's right or left
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    game.player.x_change = 3
                if e.key == pygame.K_LEFT:
                    game.player.x_change = -3
                if e.key == pygame.K_SPACE:
                    if len(game.bullets) <= 1:
                        bullet = Bullet('Assets/bullet.png', game.player.x, game.player.y - 30)
                        game.bullets.append(bullet)
                        pygame.mixer.Sound('Assets/shoot.wav').play()
            if e.type == pygame.KEYUP:
                game.player.x_change = 0

        game.player.x += game.player.x_change
        # update enemies place with boundary check and draw them
        game.move_enemies()
        game.draw_all_figs()
        game.show_score()
        game.check_collision()

        # display always updating
        pygame.display.update()


if __name__ == '__main__':
    run_game()
