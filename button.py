"""BUTTON MODULE"""
import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BRIGHT_RED = (255, 100, 100)


class Button:
    """Button class"""

    def __init__(self, position_x, position_y, text, button_width, button_height):
        """Initiating button class"""
        self.x = position_x
        self.y = position_y
        self.button_width = button_width
        self.button_height = button_height
        self.text = text
        self.create_surf(RED)
        self.create_text()
        self.hit_box = self.create_surf(False).get_rect(center=(self.x, self.y))

    def create_surf(self, hover):
        """Creating surface of the button"""
        button_color = BRIGHT_RED if hover else RED
        button = pygame.Surface((self.button_width, self.button_height))
        button.fill(button_color)
        self.hit_box = button.get_rect(center=(self.x, self.y))
        return button

    def create_text(self):
        """Creating text on the button"""
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        return text_surface, text_rect

    def is_hover(self):
        """Checking if player is hovering button"""
        return bool(self.hit_box.collidepoint(pygame.mouse.get_pos()))
