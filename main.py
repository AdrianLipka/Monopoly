import pygame
import functions
from menu import Menu, Rules
WIDTH, HEIGHT = 1200, 800


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Monopoly Poland")

        main_menu = Menu(self.screen)
        showing_menu = True
        while showing_menu:
            match main_menu.show():
                case "EXIT":
                    functions.end_game()
                case "RULES":
                    rules_menu = Rules(self.screen)
                    showing_menu = rules_menu.show()
                case "PLAY":
                    showing_menu = False



if __name__ == "__main__":
    game = Game()
