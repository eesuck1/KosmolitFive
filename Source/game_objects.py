import pygame

from Source import constants

from Source.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, start_coordinates: tuple[int, int], size: tuple[int, int], speed: int,
                 color: tuple[int, int, int]):
        super().__init__(size, start_coordinates, speed, 1)

        self._color_ = color

    def draw(self, surface: pygame.Surface) -> None:
        """Implementation for bullet"""

        pygame.draw.rect(surface, self._color_, self._rect_)

    def move(self, direction=-1) -> None:
        self.change_coordinates(y=direction * self._speed_)


class ShootInterface(Sprite):
    def __init__(self, size: tuple[int, int], start_coordinates: tuple[int, int], speed: int, health: int,
                 image: pygame.Surface):
        super().__init__(size, start_coordinates, speed, health, image)
        self._bullets_ = []

    def shoot(self) -> None:
        if len(self._bullets_) < 3:
            self._bullets_.append(Bullet(self.get_coordinates(), (constants.BULLET_WIDTH, constants.BULLET_HEIGHT),
                                         constants.BULLET_SPEED, (255, 255, 255)))

    def get_bullets(self) -> list[Bullet]:
        return self._bullets_


class Player(ShootInterface):
    def __init__(self, size: tuple[int, int], start_coordinates: tuple[int, int], speed: int, health: int,
                 image: pygame.Surface):
        super().__init__(size, start_coordinates, speed, health, image)
        self._bullets_ = []

    def move(self, key_pressed: pygame.key.ScancodeWrapper) -> None:
        if self.get_coordinates()[0] > 0 and key_pressed[pygame.K_a]:
            self.change_coordinates(x=-self._speed_)
        if self.get_coordinates()[0] < constants.WIDTH - self._rect_.width and key_pressed[pygame.K_d]:
            self.change_coordinates(x=self._speed_)


class Enemy(ShootInterface):
    def __init__(self, size: tuple[int, int], start_coordinates: tuple[int, int], speed: int, health: int,
                 image: pygame.Surface):
        super().__init__(size, start_coordinates, speed, health, image)

    def move(self) -> None:
        self.change_coordinates(y=self._speed_)
