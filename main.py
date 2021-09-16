import pygame


def run_game() -> None:
    """
    Main game loop
    :return: None
    """
    # Init pygame
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode((800, 600))

    # Game loop
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    run_game()