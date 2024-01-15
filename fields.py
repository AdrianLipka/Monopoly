import pygame

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


class Field:
    def __init__(self, screen, position, name):
        self.screen = screen
        self.name = name
        self.position = position
        self.image_path = "images/board/"
        if self.position not in ROTATION_OF_IMAGE:
            image = pygame.image.load(self.image_path + f"{self.name.replace(" ", "")}.jpg")
        else:
            image = pygame.transform.rotate(pygame.image.load(self.image_path + f"{self.name.replace(" ", "")}.jpg"),
                                            ROTATION_OF_IMAGE[self.position])
        self.placing_on_board(image)

    def placing_on_board(self, image):
        self.screen.blit(image, POSITION_ON_BOARD[self.position])

    def __str__(self):
        return f"{self.name} ({self.position})"


class City(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)
        for item in COLORS_OF_DISTRICTS:
            if position in item["Position"]:
                self.color = item["Color"]

    def __str__(self):
        return f"{self.name} ({self.position}, {self.color})"


class Transport(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)



class CommunityChest(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)


class ChanceCard(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)


class Communication(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)


class IncomeTax(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)


class Corner(Field):
    def __init__(self, screen, position, name):
        Field.__init__(self, screen, position, name)
