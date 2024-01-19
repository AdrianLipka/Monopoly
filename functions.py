"""FUNCTIONS MODULE"""
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


def same_owner(curnt_player, field_owner):
    """Checking if owners are the same player"""
    if not field_owner == curnt_player:
        return False
    return True


def money_amount(money):
    """Changing money amount to desired format"""
    if money > 1000000:
        return f"${round(money/1000000, 4)}M"
    return f"${money//1000}K"
