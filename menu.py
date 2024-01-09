import pygame
from button import Button
from window import Window
import functions

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


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
        running = True
        while running:
            self.screen.blit(play_button.create_surf(play_button.is_hover()), play_button.hit_box)
            self.screen.blit(rules_button.create_surf(rules_button.is_hover()), rules_button.hit_box)
            self.screen.blit(quit_button.create_surf(quit_button.is_hover()), quit_button.hit_box)
            self.bliting_on_scren(play_button.create_text())
            self.bliting_on_scren(rules_button.create_text())
            self.bliting_on_scren(quit_button.create_text())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and quit_button.is_hover():
                    running = False
                    functions.end_game()
            pygame.display.flip()
