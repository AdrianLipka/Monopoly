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
                    (425, 1150), (325, 1150), (225, 1150),(15, 1175), (50, 1025), (50, 925), (50, 825), (50, 725),
                    (50, 625), (50, 525), (50, 425), (50, 325), (50, 225), (120, 30), (175, 100), (275, 100),
                    (375, 100), (475, 100), (575, 100), (675, 100), (775, 100), (875, 100), (975, 100),
                    (1075, 120), (1150, 175), (1150, 275), (1150, 375), (1150, 475), (1150, 575), (1150, 675),
                    (1150, 775), (1150, 875), (1150, 975)))

PRISON_POSITION = ((90, 1070), (25, 1140))
CIRCLE_RADIUS = 20


class Player:
    def __init__(self, screen, number):
        self.fpsClock = pygame.time.Clock()
        self.screen = screen
        self.number = number
        self.position = 0
        self.money = 15000000
        self.prison = {"State": False, "Card": 0}
        pygame.draw.circle(self.screen, COLORS_OF_PLAYER[self.number], POSITION_PLAYER[self.number-1][self.position], CIRCLE_RADIUS)

    def walk_to(self, pos):
        if type(pos) is int:
            target_x, target_y = POSITION_PLAYER[self.number - 1][pos]
        else:
            target_x, target_y = pos[0], pos[1]
        x, y = POSITION_PLAYER[self.number-1][self.position]
        while x != target_x or y != target_y:
            if type(pos) is not int:
                if self.position == 9:
                    self.position = 10
                    break
            x, y = POSITION_PLAYER[self.number-1][self.position]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    functions.end_game()

            pygame.draw.circle(self.screen, COLORS_OF_PLAYER[self.number], (x, y), CIRCLE_RADIUS)
            pygame.display.flip()
            self.fpsClock.tick(5)

            if self.position + 1 > 39:
                if type(pos) is int:
                    self.money += 2000000
                self.position = 0
            else:
                self.position += 1

    def move(self, move_step):
        if self.position + move_step > 39:
            new_position = self.position + move_step - 40
        else:
            new_position = self.position + move_step - 1
        self.walk_to(new_position)

    def update(self):
        if not self.prison["State"]:
            pygame.draw.circle(self.screen, COLORS_OF_PLAYER[self.number],
                               POSITION_PLAYER[self.number - 1][self.position], CIRCLE_RADIUS)
        else:
            pygame.draw.circle(self.screen, COLORS_OF_PLAYER[self.number], PRISON_POSITION[self.number - 1],
                               CIRCLE_RADIUS)

    def __str__(self):
        return f"{self.number}"


class Dice:
    def __init__(self, screen):
        self.screen = screen
        self.position = ((1300, 600), (1450, 600))
        dice1 = pygame.transform.scale(pygame.image.load("images/dice/dice1.png"), (50, 50))
        dice2 = pygame.transform.scale(pygame.image.load("images/dice/dice2.png"), (50, 50))
        dice3 = pygame.transform.scale(pygame.image.load("images/dice/dice3.png"), (50, 50))
        dice4 = pygame.transform.scale(pygame.image.load("images/dice/dice4.png"), (50, 50))
        dice5 = pygame.transform.scale(pygame.image.load("images/dice/dice5.png"), (50, 50))
        dice6 = pygame.transform.scale(pygame.image.load("images/dice/dice6.png"), (50, 50))
        self.dice_images = [dice1, dice2, dice3, dice4, dice5, dice6]
        self.move_step1 = None
        self.move_step2 = None

    def rolling(self):
        self.move_step1 = randint(1, 6)
        self.move_step2 = randint(1, 6)
    #    self.move_step2, self.move_step1 = 1, 1      # Moving per 2 for testing
        return self.move_step1 + self.move_step2

    def rolling_in_prison(self):
        self.move_step1 = randint(1, 6)
        self.move_step2 = randint(1, 6)
        if self.move_step2 == 6 and self.move_step1 == 6:
            return True
        else:
            return False

    def showing(self):
        self.screen.blit(self.dice_images[self.move_step1 - 1], self.position[0])
        self.screen.blit(self.dice_images[self.move_step2 - 1], self.position[1])
