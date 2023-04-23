import sys

import constants

import pygame


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Космоліт 5")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(constants.BACKGROUND_IMAGE, (0, 0))
            pygame.display.update()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
