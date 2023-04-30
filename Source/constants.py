import os

import pygame


FOLDER = "Assets"

FPS = 60

WIDTH, HEIGHT = 600, 800
SPRITE_WIDTH, SPRITE_HEIGHT = 60, 80
BULLET_WIDTH, BULLET_HEIGHT = 6, 8
PLAYER_SPEED = 5
ENEMY_SPEED = 1
BULLET_SPEED = 7
SPRITE_HEALTH = 3

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(FOLDER, "background.jfif")), (WIDTH, HEIGHT))
PLAYER_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(FOLDER, "player.png")), (SPRITE_WIDTH, SPRITE_HEIGHT))
ENEMY_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(FOLDER, "first_enemy.jpg")), (SPRITE_WIDTH, SPRITE_HEIGHT))
