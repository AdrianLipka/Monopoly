import pygame


class Window:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.h1_font = pygame.font.Font(None, 100)

    def bliting_on_scren(self, parameters):
        """Showing object to the screen"""
        obj, surface = parameters
        self.screen.blit(obj, surface)