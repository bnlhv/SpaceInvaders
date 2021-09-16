import random
import pygame

from figure import Figure
from game import init_game
from globals import WIN_SIZE, FIG_SIZE


def run_game() -> None:
    """
    Main game loop
    :return: None
    """

    game = init_game()

    player = Figure(
        name='Player',
        img_path='player.png',
        initial_x=(WIN_SIZE[0] / 2) - (FIG_SIZE / 2),
        initial_y=(WIN_SIZE[1] * (3/4)) + (FIG_SIZE / 2)
    )
    enemy1 = Figure(
        name='Enemy1',
        img_path='enemy.png',
        initial_x=random.randint(0, 800 - FIG_SIZE),
        initial_y=random.randint(50, 150)
    )

    game.add_fig(player)
    game.add_fig(enemy1)

    player_x_change = 0
    enemy_x_change = 0

    # Game loop
    running = True
    while running:

        # RGB
        game.screen.fill((0, 128, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check if it's right or left
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    player_x_change = 0.3
                if e.key == pygame.K_LEFT:
                    player_x_change = -0.3
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    player_x_change = 0

        # update players place with boundary check and draw them
        game.player.x += player_x_change
        game.move_enemies()
        game.draw_all_figs()

        # display always updating
        pygame.display.update()


if __name__ == '__main__':
    run_game()