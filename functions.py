import sys
import pygame


def end_game():
    """Ending the game and ending the program"""
    pygame.quit()
    sys.exit()


def create_text(text, font, color, cords):
    """Creating text object"""
    text = font.render(text, True, color)
    text_hit_box = text.get_rect(center=cords)
    return text, text_hit_box
