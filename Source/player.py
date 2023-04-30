import pygame

from Source import constants
from Source.bullet import Bullet

from sprite import Sprite


class Player(Sprite):
    def __init__(self, size: tuple[int, int], start_coordinates: tuple[int, int], speed: int, health: int,
                 image: pygame.Surface):
        super().__init__(size, start_coordinates, speed, health, image)
        self._bullets_ = []

    def move(self, key_pressed: pygame.key.ScancodeWrapper) -> None:
        if self.get_coordinates()[0] > 0 and key_pressed[pygame.K_a]:
            self.change_coordinates(x=-self._speed_)
        if self.get_coordinates()[1] < constants.WIDTH - self._rect_.width and key_pressed[pygame.K_d]:
            self.change_coordinates(x=self._speed_)

    def shoot(self) -> None:
        if len(self._bullets_) <= 5:
            self._bullets_.append(Bullet((constants.BULLET_WIDTH, constants.BULLET_HEIGHT), 7, (255, 255, 255), self))

    def get_bullets(self) -> list[Bullet]:
        return self._bullets_
