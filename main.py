import pygame
from menu import Menu
WIDTH, HEIGHT = 1600, 1200


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Monopoly Poland")

        menu = Menu(self.screen)
        menu.show()


if __name__ == "__main__":
    game = Game()
