import pygame
from button import Button
from window import Window
import functions

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PAGES_WITH_INSTRUCTIONS = 3


class Menu(Window):
    def __init__(self, screen):
        super().__init__(screen)
        self.menu_image = pygame.image.load("images/menu.jpg")

    def show(self):
        play_button = Button(self.width / 2, self.height * 2 / 5, "PLAY!", 200, 50)
        rules_button = Button(self.width / 2, self.height * 3 / 5, "RULES", 200, 50)
        quit_button = Button(self.width / 2, self.height * 4 / 5, "QUIT", 200, 50)
        self.screen.blit(self.menu_image, (0, 0))
        title_text = functions.create_text("MONOPOLY POLAND", self.h1_font, WHITE,(self.width / 2, self.height * 1 / 5))[0]
        text_rect = title_text.get_rect()
        background_surface = pygame.Surface((text_rect.width, text_rect.height))
        background_surface.fill(RED)
        background_surface.blit(title_text, (0, 0))
        self.screen.blit(background_surface, (self.width / 2 - text_rect.width / 2, self.height * 1 / 5 - text_rect.height / 2))
        while True:
            self.screen.blit(play_button.create_surf(play_button.is_hover()), play_button.hit_box)
            self.screen.blit(rules_button.create_surf(rules_button.is_hover()), rules_button.hit_box)
            self.screen.blit(quit_button.create_surf(quit_button.is_hover()), quit_button.hit_box)
            self.bliting_on_scren(play_button.create_text())
            self.bliting_on_scren(rules_button.create_text())
            self.bliting_on_scren(quit_button.create_text())
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN and quit_button.is_hover()) or event.type == pygame.QUIT:
                    return "EXIT"
                elif event.type == pygame.MOUSEBUTTONDOWN and rules_button.is_hover():
                    return "RULES"
                elif event.type == pygame.MOUSEBUTTONDOWN and play_button.is_hover():
                    return "PLAY"

            pygame.display.flip()


class Rules(Window):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen

    def show(self):
        rule_displayed = 1
        rules_image1 = pygame.image.load("images/rules1.jpg")
        rules_image2 = pygame.image.load("images/rules2.jpg")
        rules_image3 = pygame.image.load("images/rules3.jpg")
        next_button = Button(self.width * 2 / 3, self.height * 4 / 5, "NEXT!", 200, 50)
        previous_button = Button(self.width * 1 / 3, self.height * 4 / 5, "PREVIOUS!", 200, 50)
        back_button = Button(self.width * 1 / 2, self.height * 9 / 10, "BACK TO MENU!", 300, 50)
        keys = None
        while True:
            match rule_displayed:
                case 1:
                    self.screen.blit(rules_image1, (0, 0))
                case 2:
                    self.screen.blit(rules_image2, (0, 0))
                case 3:
                    self.screen.blit(rules_image3, (0, 0))
            self.screen.blit(next_button.create_surf(next_button.is_hover()), next_button.hit_box)
            self.screen.blit(previous_button.create_surf(previous_button.is_hover()), previous_button.hit_box)
            self.screen.blit(back_button.create_surf(back_button.is_hover()), back_button.hit_box)
            self.bliting_on_scren(next_button.create_text())
            self.bliting_on_scren(previous_button.create_text())
            self.bliting_on_scren(back_button.create_text())
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    functions.end_game()
                if event.type == pygame.MOUSEBUTTONDOWN and back_button.is_hover():
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN and next_button.is_hover() and rule_displayed < PAGES_WITH_INSTRUCTIONS:
                    rule_displayed += 1
                if event.type == pygame.MOUSEBUTTONDOWN and previous_button.is_hover() and rule_displayed > 1:
                    rule_displayed -= 1
                if keys:
                    if keys[pygame.K_ESCAPE]:
                        return True

            pygame.display.flip()
