import pygame

from sprite import Sprite


class Enemy(Sprite):
    def __init__(self, size: tuple[int, int], start_coordinates: tuple[int, int], speed: int, health: int,
                 image: pygame.Surface):
        super().__init__(size, start_coordinates, speed, health, image)
