import pygame

WIN_SIZE = (800, 600)
TITLE = 'Space Invaders'

ICON = pygame.image.load("Assets/icon.png")
BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/space_background.jpg"), WIN_SIZE)

FIG_SIZE = 64
FONT_NAME = '/Assets/goblin_font.otf'
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
CLOCK = pygame.time.Clock()
FPS = 60

NUM_OF_ENEMIES = 10
