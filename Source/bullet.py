import pygame

from sprite import Sprite
from player import Player
from enemy import Enemy


class Bullet(Sprite):
    def __init__(self, size: tuple[int, int], speed: int,
                 color: tuple[int, int, int], shooter: Player | Enemy):
        super().__init__(size, shooter.get_coordinates(), speed, 1)

        self._shooter_ = shooter
        self._color_ = color

    def draw(self, surface: pygame.Surface) -> None:
        """Implementation for bullet"""

        pygame.draw.rect(surface, self._color_, self._rect_)

    def move(self) -> None:
        if isinstance(self._shooter_, Player):
            self.change_coordinates(y=-self._speed_)
        if isinstance(self._shooter_, Enemy):
            self.change_coordinates(y=self._speed_)
