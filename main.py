import random
import pygame

from bullet import Bullet
from enemy import Enemy
from figure import Figure
from game import init_game
from globals import WIN_SIZE, FIG_SIZE, CLOCK, FPS, BLACK, BACKGROUND
from player import Player


def run_game() -> None:
    """
    Main game loop
    :return: None
    """

    game = init_game()

    player = Player(
        name='Player',
        img_path='player.png',
        initial_x=(WIN_SIZE[0] / 2) - (FIG_SIZE / 2),
        initial_y=(WIN_SIZE[1] * (3/4)) + (FIG_SIZE / 2)
    )
    enemy1 = Enemy(
        img_path='enemy.png',
        initial_x=random.randint(0, 800 - FIG_SIZE),
        initial_y=random.randint(50, 150)
    )

    game.player = player
    game.add_enemy(enemy1)

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
                    bullet = Bullet('bullet.png', game.player.x, game.player.y - 30)
                    game.add_bullet(bullet)
            if e.type == pygame.KEYUP:
                game.player.x_change = 0

        game.player.x += game.player.x_change
        # update enemies place with boundary check and draw them
        game.move_enemies()
        game.draw_all_figs()
        game.check_collision()

        # display always updating
        pygame.display.update()


if __name__ == '__main__':
    run_game()