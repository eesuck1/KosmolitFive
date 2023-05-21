import random
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

        self._enemies_ = self.__init_enemies__(5)

        pygame.display.set_caption("Космоліт 5")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._player_.shoot()

            self.__screen__.blit(constants.BACKGROUND_IMAGE, (0, 0))
            self.__draw_sprites__()

            self.__move_objects()

            self.__enemy_shoot__()

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

    def __move_objects__(self) -> None:
        self._player_.move(pygame.key.get_pressed())

        for enemy in self._enemies_:
            enemy.move()

            for bullet in enemy.get_bullets():
                bullet.move(1)

                if bullet.get_coordinates()[1] > constants.HEIGHT - bullet.get_rect().height:
                    enemy.get_bullets().remove(bullet)

                if bullet.check_collision(self._player_):
                    bullet.take_damage()
                    if bullet.check_death():
                        enemy.get_bullets().remove(bullet)

                    self._player_.take_damage()
                    if self._player_.check_death():
                        pygame.quit()
                        sys.exit()

        for bullet in self._player_.get_bullets():
            bullet.move()
            if bullet.get_coordinates()[1] < 0:
                self._player_.get_bullets().remove(bullet)

            collision_index = bullet.check_list_collision(self._enemies_)

            if collision_index != -1:
                self._enemies_.pop(collision_index)

    def __enemy_shoot__(self) -> None:
        for enemy in self._enemies_:
            if random.randint(0, 200) == 0:
                enemy.shoot()

    @staticmethod
    def __init_enemies__(number_of_enemies: int) -> list[Enemy]:
        step = (constants.WIDTH - (number_of_enemies + 1) * constants.SPRITE_WIDTH) // number_of_enemies

        return [Enemy((constants.SPRITE_WIDTH, constants.SPRITE_HEIGHT),
                      (constants.SPRITE_WIDTH + index * (constants.SPRITE_WIDTH + step), constants.SPRITE_HEIGHT),
                      constants.ENEMY_SPEED, constants.SPRITE_HEALTH, constants.ENEMY_IMAGE) for index in
                range(number_of_enemies)]
