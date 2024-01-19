import pygame
from fields_info import field_info
import functions

COLORS_OF_DISTRICTS = ({"Position": (1, 3), "Color": "Brown"},
                       {"Position": (6, 7, 9), "Color": "Light blue"},
                       {"Position": (11, 13, 14), "Color": "Pink"},
                       {"Position": (16, 18, 19), "Color": "Orange"},
                       {"Position": (21, 23, 24), "Color": "Red"},
                       {"Position": (26, 27, 29), "Color": "Yellow"},
                       {"Position": (31, 32, 34), "Color": "Green"},
                       {"Position": (37, 39), "Color": "Dark blue"})

POSITION_ON_BOARD = ((1050, 1050), (950, 1050), (850, 1050), (750, 1050), (650, 1050), (550, 1050), (450, 1050),
                     (350, 1050), (250, 1050), (150, 1050), (0, 1050), (0, 950), (0, 850), (0, 750), (0, 650),
                     (0, 550), (0, 450), (0, 350), (0, 250), (0, 150), (0, 0), (150, 0), (250, 0), (350, 0),
                     (450, 0), (550, 0), (650, 0), (750, 0), (850, 0), (950, 0), (1050, 0), (1050, 150), (1050, 250),
                     (1050, 350), (1050, 450), (1050, 550), (1050, 650), (1050, 750), (1050, 850), (1050, 950))

ROTATION_OF_IMAGE = {17: -90, 33: 90, 36: 90, 38: 90}

GREEN = (0, 255, 0)
DARK_RED = (139, 0, 0)


class Field:
    def __init__(self, screen, position, name):
        self.screen = screen
        self.name = name
        self.position = position
        self.properties = {"Occupied": False, "To buy": False, "To pay": False, "Cost": 0, "Special": False}
        self.owner = None
        self.rent = None
        image_path = "images/board/"
        if self.position not in ROTATION_OF_IMAGE:
            self.image = pygame.image.load(image_path + f"{self.name.replace(" ", "")}.jpg")
        else:
            self.image = pygame.transform.rotate(pygame.image.load(image_path + f"{self.name.replace(" ", "")}.jpg"),
                                                 ROTATION_OF_IMAGE[self.position])
        self.placing_on_board()

    def placing_on_board(self):
        self.screen.blit(self.image, POSITION_ON_BOARD[self.position])

    def buying(self, player):
        self.owner = player
        self.properties["Occupied"] = True
        self.properties["To pay"] = True
        self.rent = self.properties["Rent"][1]
        player.money -= self.properties["Cost"]

    def field_to_buy(self):
        self.properties["To buy"] = True
        title_deed_card_image = pygame.image.load(f"images/title_deed_cards/{self.name.replace(" ", "")}.png")
        self.properties["Title deed card"] = title_deed_card_image

    def paying_rent(self, font, color):
        rent_to_pay_text = functions.create_text(f"Rent paid: {functions.money_amount(self.rent)}", font, color, (1400, 700))
        return rent_to_pay_text

    def __str__(self):
        return f"{self.name} ({self.position})"


class City(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)
        for item in COLORS_OF_DISTRICTS:
            if position in item["Position"]:
                self.color = item["Color"]
        self.field_to_buy()
        self.properties.update(field_info(self.name))
        self.builded = 0

    def building(self):
        self.owner.money -= self.properties["Building cost"]
        self.builded += 1
        self.rent = self.properties["Rent"][self.builded]

    def buying(self, player):
        self.owner = player
        self.properties["Occupied"] = True
        self.properties["To pay"] = True
        self.rent = self.properties["Rent"][0]
        player.money -= self.properties["Cost"]

    def showing_buildings(self):
        if self.builded > 0:
            if self.position < 10:
                rotation = 0
            elif self.position < 20:
                rotation = 1
            elif self.position < 30:
                rotation = 2
            else:
                rotation = 3
            if self.builded == 5:
                position = list(POSITION_ON_BOARD[self.position])
                match rotation:
                    case 0 | 2:
                        position[0] += 50
                        position[1] += 18
                    case 1:
                        position[0] += 150 - 18
                        position[1] += 50
                    case 3:
                        position[0] += 18
                        position[1] += 50
                pygame.draw.circle(self.screen, DARK_RED, position, 10)
            else:
                for i in range(self.builded):
                    position = list(POSITION_ON_BOARD[self.position])
                    match rotation:
                        case 0 | 2:
                            position[0] += 18 + i * 20 + 2
                            position[1] += 18
                        case 1:
                            position[0] += 150 - 18
                            position[1] += 18 + i * 20 + 2
                        case 3:
                            position[0] += 18
                            position[1] += 18 + i * 20 + 2
                    pygame.draw.circle(self.screen, GREEN, position, 10)

    def __str__(self):
        return f"{self.name} ({self.position}, {self.color})"


class Transport(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)
        self.properties["Cost"] = 2000000
        self.properties["Rent"] = {1: 250000, 2: 500000, 3: 1000000, 4: 2000000}
        self.field_to_buy()


class CommunityChest(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)
        self.properties["Special"] = True


class ChanceCard(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)
        self.properties["Special"] = True


class Communication(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)
        self.properties["Cost"] = 1500000
        self.properties["Rent"] = {1: 40000, 2: 100000}
        self.field_to_buy()


class IncomeTax(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)
        self.properties["To pay"] = True
        self.rent = 2000000

    def paying_rent(self, font, color):
        rent_to_pay_text = functions.create_text(f"Tax paid: {functions.money_amount(self.rent)}", font, color, (1400, 700))
        return rent_to_pay_text


class Corner(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)
