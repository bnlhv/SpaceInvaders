import pygame

WIN_SIZE = (800, 600)
TITLE = 'Space Invaders'

ICON = pygame.image.load("Assets/icon.png")
BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/space_background.jpg"), WIN_SIZE)

FIG_SIZE = 64
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = None

CLOCK = pygame.time.Clock()
FPS = 60

NUM_OF_ENEMIES = 10
