import pygame
from random import randint

import functions

YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
COLORS_OF_PLAYER = {1: YELLOW, 2: GREEN}
POSITION_PLAYER = (((1160, 1090), (980, 1150), (880, 1150), (780, 1150), (680, 1150), (580, 1150), (480, 1150),
                    (380, 1150), (280, 1150), (180, 1150), (120, 1170), (50, 980), (50, 880), (50, 780), (50, 680),
                    (50, 580), (50, 480), (50, 380), (50, 280), (50, 180),(30, 120), (220, 100), (320, 100), (420, 100),
                    (520, 100), (620, 100), (720, 100), (820, 100), (920, 100), (1020, 100), (1175, 30), (1150, 220),
                    (1150, 320), (1150, 420), (1150, 520), (1150, 620), (1150, 720), (1150, 820), (1150, 920),
                    (1150, 1020)),
                   ((1120, 1140), (1025, 1150), (925, 1150), (825, 1150), (725, 1150), (625, 1150), (525, 1150),
                    (425, 1150), (325, 1150), (225, 1150),(25, 1140), (50, 1025), (50, 925), (50, 825), (50, 725),
                    (50, 625), (50, 525), (50, 425), (50, 325), (50, 225), (120, 30), (175, 100), (275, 100),
                    (375, 100), (475, 100), (575, 100), (675, 100), (775, 100), (875, 100), (975, 100),
                    (1075, 120), (1150, 175), (1150, 275), (1150, 375), (1150, 475), (1150, 575), (1150, 675),
                    (1150, 775), (1150, 875), (1150, 975)))

CIRCLE_RADIUS = 20


class Player:
    def __init__(self, screen, number):
        self.fpsClock = pygame.time.Clock()
        self.screen = screen
        self.number = number
        self.position = 0
        pygame.draw.circle(self.screen, COLORS_OF_PLAYER[self.number], POSITION_PLAYER[self.number-1][self.position], CIRCLE_RADIUS)

    def walk_to(self, pos):
        x, y = POSITION_PLAYER[self.number-1][self.position]
        target_x, target_y = POSITION_PLAYER[self.number-1][pos]
        while x != target_x or y != target_y:
            x, y = POSITION_PLAYER[self.number-1][self.position]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    functions.end_game()

            pygame.draw.circle(self.screen, COLORS_OF_PLAYER[self.number], POSITION_PLAYER[self.number-1][self.position], CIRCLE_RADIUS)
            pygame.display.flip()
            self.fpsClock.tick(5)

            if self.position + 1 > 39:
                self.position = 0
            else:
                self.position += 1

    def move(self):
        move_step = randint(1, 12)
        if self.position + move_step > 39:
            new_position = self.position + move_step - 40
        else:
            new_position = self.position + move_step

        self.walk_to(new_position)

    def update(self):
        pygame.draw.circle(self.screen, COLORS_OF_PLAYER[self.number], POSITION_PLAYER[self.number - 1][self.position], CIRCLE_RADIUS)
