import pygame
import functions
from menu import Menu, Rules, EndGame
from board import Board
WIDTH, HEIGHT = 1600, 1200


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
                    board = Board(self.screen)
                    player_lost = board.game()
                    end_game = EndGame(self.screen, player_lost)
                    if end_game.show():
                        showing_menu = True
                    else:
                        functions.end_game()


if __name__ == "__main__":
    game = Game()
