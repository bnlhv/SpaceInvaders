import pygame

WIN_SIZE = (800, 600)
TITLE = 'Space Invaders'
ICON = pygame.image.load("icon.png")
BACKGROUND = pygame.transform.scale(pygame.image.load("space_background.jpg"), WIN_SIZE)
FIG_SIZE = 64
CLOCK = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)
NUM_OF_ENEMIES = 5
