import pygame
from fields import City, Transport, Communication, ChanceCard, IncomeTax, CommunityChest, Corner

BOARD = {0: "Start", 1: "Świętochłowice", 2: "Community chest", 3: "Bełchatów", 4: "Income tax", 5: "Railway station",
         6: "Warszawa", 7: "Lublin", 8: "Chance card",9: "Katowice", 10: "Jail", 11: "Toruń", 12: "Mobile network",
         13: "Rybnik", 14: "Łódź", 15: "Airport", 16: "Chojnice", 17: "Community Chest", 18: "Elbląg", 19: "Szczecin",
         20: "Parking", 21: "Zielona góra", 22: "Chance card", 23: "Bydgoszcz", 24: "Tarnów", 25: "Metro station",
         26: "Piotrków Trybunalski", 27: "Wrocław", 28: "Social media", 29: "Kalisz", 30: "Go to jail", 31: "Kraków",
         32: "Gdynia", 33: "Community chest", 34: "Poznań", 35: "Sea port", 36: "Chance card", 37: "Gorzów",
         38: "Income tax", 39: "Białystok"}

SPECIALPLACES = ({"Type": "Transport", "Position": (5, 15, 25, 35)},
                 {"Type": "Community chest", "Position": (2, 17, 33)},
                 {"Type": "Income tax", "Position": (4, 38)},
                 {"Type": "Chance card", "Position": (8, 22, 36)},
                 {"Type": "Communication", "Position": (12, 28)})


class Board:
    def __init__(self, screen):
        self.board = BOARD
        self.screen = screen
        self.fields = []
        middle_image = pygame.transform.scale(pygame.image.load("images/board/middle.jpg"), (900, 900))
        screen.blit(middle_image, (150, 150))
        for position in self.board:
            if position in (0, 10, 20, 30):
                self.fields.append(Corner(self.screen, position, BOARD[position]))
                continue
            special_place = False
            for item in SPECIALPLACES:
                if position in item["Position"]:
                    match item["Type"]:
                        case "Transport":
                            self.fields.append(Transport(self.screen, position, BOARD[position]))
                        case "Community chest":
                            self.fields.append(CommunityChest(self.screen, position, BOARD[position]))
                        case "Income tax":
                            self.fields.append(IncomeTax(self.screen, position, BOARD[position]))
                        case "Chance card":
                            self.fields.append(ChanceCard(self.screen, position, BOARD[position]))
                        case "Communication":
                            self.fields.append(Communication(self.screen, position, BOARD[position]))
                    special_place = True
                    break
            if not special_place:
                self.fields.append(City(self.screen, position, BOARD[position]))

