import pygame


class Sprite:
    def __init__(self, size: tuple[int, int], start_coordinates: tuple[int, int],
                 speed: int, health: int, image: pygame.Surface | None):
        self._rect_ = pygame.rect.Rect(*start_coordinates, *size)
        self._speed_ = speed
        self._health_ = health
        self._image_ = image

    def get_coordinates(self) -> tuple[int, int]:
        return self._rect_.x, self._rect_.y

    def get_image(self) -> pygame.Surface:
        return self._image_

    def get_health(self) -> int:
        return self._health_

    def get_speed(self) -> int:
        return self._speed_

    def set_coordinates(self, x: int, y: int) -> None:
        self._rect_.x = x
        self._rect_.y = y

    def change_coordinates(self, x=0, y=0) -> None:
        self._rect_.x += x
        self._rect_.y += y

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._image_, self.get_coordinates())

    def move(self, *args, **kwargs) -> None:
        """Add the implementation"""
        ...

    def shoot(self, *args, **kwargs) -> None:
        """Add the implementation"""
        ...
