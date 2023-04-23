import pygame

import constants
from sprite import Sprite


class Player(Sprite):
    def __init__(self, size: tuple[int, int], start_coordinates: tuple[int, int], speed: int, health: int,
                 image: pygame.Surface):
        super().__init__(size, start_coordinates, speed, health, image)

    def move(self, key_pressed: pygame.key.ScancodeWrapper) -> None:
        if self.get_coordinates()[0] > 0 and key_pressed[pygame.K_a]:
            self.change_coordinates(x=-self._speed_)
        if self.get_coordinates()[1] < constants.WIDTH - self._rect_.width and key_pressed[pygame.K_d]:
            self.change_coordinates(x=self._speed_)

    def shoot(self):
        ...
