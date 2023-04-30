import sys

import pygame

from Source import constants
from Source.game_objects import Player, Enemy


class Game:
    def __init__(self):
        self.__screen__ = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.__clock__ = pygame.time.Clock()

        self._player_ = Player((constants.SPRITE_WIDTH, constants.SPRITE_HEIGHT),
                               ((constants.WIDTH - constants.SPRITE_WIDTH) // 2,
                                constants.HEIGHT - 2 * constants.SPRITE_HEIGHT),
                               constants.PLAYER_SPEED, constants.SPRITE_HEALTH, constants.PLAYER_IMAGE)
        self._player_.shoot()

        self._enemies_ = self.__init_enemies__(5)

        pygame.display.set_caption("Космоліт 5")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__screen__.blit(constants.BACKGROUND_IMAGE, (0, 0))
            self.__draw_sprites__()

            self.__move_objects()

            self.__clock__.tick(constants.FPS)
            pygame.display.update()

    def __draw_sprites__(self) -> None:
        self._player_.draw(self.__screen__)

        for enemy in self._enemies_:
            enemy.draw(self.__screen__)

            for bullet in enemy.get_bullets():
                bullet.draw(self.__screen__)

        for bullet in self._player_.get_bullets():
            bullet.draw(self.__screen__)

    def __move_objects(self) -> None:
        self._player_.move(pygame.key.get_pressed())

        for enemy in self._enemies_:
            enemy.move()

            for bullet in enemy.get_bullets():
                bullet.move(1)

                if bullet.check_collision(self._player_.get_rect()):
                    bullet.take_damage()
                    if bullet.check_death():
                        enemy.get_bullets().remove(bullet)

                    self._player_.take_damage()
                    if self._player_.check_death():
                        ...

        for bullet in self._player_.get_bullets():
            bullet.move()

    @staticmethod
    def __init_enemies__(number_of_enemies: int) -> list[Enemy]:
        step = (constants.WIDTH - 2 * constants.SPRITE_WIDTH) // number_of_enemies

        return [Enemy((constants.SPRITE_WIDTH, constants.SPRITE_HEIGHT),
                      (constants.SPRITE_WIDTH + step + index * constants.SPRITE_WIDTH, constants.SPRITE_HEIGHT),
                      constants.ENEMY_SPEED, constants.SPRITE_HEALTH, constants.ENEMY_IMAGE) for index in
                range(number_of_enemies)]
