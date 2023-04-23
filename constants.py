import pygame
import os


FOLDER = "Assets"
WIDTH, HEIGHT = 600, 800
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(FOLDER, "background.jfif")), (WIDTH, HEIGHT))
