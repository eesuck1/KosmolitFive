import pygame


class Sprite:
    def __init__(self, size: tuple[int, int] = (0, 0), start_coordinates: tuple[int, int] = (0, 0),
                 speed: int = 0, health: int = 0, image: pygame.Surface | None = None):
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

    def get_rect(self) -> pygame.rect.Rect:
        return self._rect_

    def set_coordinates(self, x: int, y: int) -> None:
        self._rect_.x = x
        self._rect_.y = y

    def change_coordinates(self, x=0, y=0) -> None:
        self._rect_.x += x
        self._rect_.y += y

    def take_damage(self, damage: int) -> None:
        self._health_ -= damage

    def death(self):
        if self._health_ <= 0:
            del self

    def check_collision(self, another_sprite_rect: pygame.rect.Rect) -> bool:
        return self._rect_.colliderect(another_sprite_rect)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._image_, self.get_coordinates())

    def move(self, *args, **kwargs) -> None:
        """Add the implementation"""
        ...

    def shoot(self, *args, **kwargs) -> None:
        """Add the implementation"""
        ...
