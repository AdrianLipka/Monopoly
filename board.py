import pygame
from fields import City, Transport, Communication, ChanceCard, IncomeTax, CommunityChest, Corner
from player import Player, Dice
import functions
from button import Button
from window import Window

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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 139)


class Board(Window):
    def __init__(self, screen):
        super().__init__(screen)
        self.fields = []
        self.turn = 1
        middle_image = pygame.transform.scale(pygame.image.load("images/board/middle.jpg"), (900, 900))
        screen.blit(middle_image, (150, 150))
        for position in BOARD:
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
        player1 = Player(screen, 1)
        player2 = Player(screen, 2)
        self.players = [player1, player2]
        self.dice = Dice(screen)

    def clearing_board(self):
        for field in self.fields:
            field.placing_on_board()

    def drawing_controls_rectangle(self):
        controls_background = pygame.Surface((400, 1200))
        controls_background.fill(DARK_BLUE)
        self.screen.blit(controls_background, (1200, 0))

    def category_holder(self, curnt_field, curnt_player):
        same_owner = True
        for field in self.fields:
            if isinstance(curnt_field, City) and isinstance(field, City):
                if curnt_field.color == field.color:
                    same_owner = functions.same_owner(curnt_player, field.owner)
                if not same_owner:
                    return same_owner
            elif ((isinstance(curnt_field, Transport) and isinstance(field, Transport))
                  or (isinstance(curnt_field, Communication) and isinstance(field, Communication))):
                same_owner = functions.same_owner(curnt_player, field.owner)
                if not same_owner:
                    return same_owner
        return same_owner

    def game(self):
        turn1_text = functions.create_text("First player's turn", self.h2_font, WHITE, (1400, 50))
        turn2_text = functions.create_text("Second player's turn", self.h2_font, WHITE, (1400, 50))
        end_turn_button = Button(1400, 200, "END TURN", 200, 50)
        roll_dice_button = Button(1400, 300, "ROLL DICE", 200, 50)
        buy_button = Button(1400, 400, "BUY FIELD", 200, 50)
        build_button = Button(1400, 500, "BUILD", 200, 50)
        pygame.display.flip()
        move_step = None
        diced = False
        current_field = None
        building_ability = None
        while True:
            self.drawing_controls_rectangle()
            budget_text = functions.create_text(f"Budget: {functions.money_amount(self.players[self.turn-1].money)}",
                                                self.h2_font, WHITE, (1400, 100))
            if move_step:
                self.dice.showing()
            if self.turn == 1:
                self.bliting_on_scren(turn1_text)
            elif self.turn == 2:
                self.bliting_on_scren(turn2_text)
            self.bliting_on_scren(budget_text)
            if diced:
                if current_field.properties["To buy"]:
                    self.screen.blit(current_field.properties["Title deed card"], (1300, 700))
                if not current_field.properties["Occupied"] and current_field.properties["To buy"]:
                    self.screen.blit(buy_button.create_surf(buy_button.is_hover()), buy_button.hit_box)
                    self.screen.blit(build_button.create_surf(True), build_button.hit_box)
                else:
                    self.screen.blit(buy_button.create_surf(True), buy_button.hit_box)
                    self.screen.blit(build_button.create_surf(True), build_button.hit_box)
                if current_field.properties["Occupied"]:
                    building_ability = self.category_holder(current_field, self.players[self.turn-1])
                    if (building_ability and isinstance(current_field, City) and current_field.builded < 5 and
                            self.players[self.turn-1].money >= current_field.properties["Building cost"]):
                        self.screen.blit(build_button.create_surf(build_button.is_hover()), build_button.hit_box)
                    else:
                        self.screen.blit(build_button.create_surf(True), build_button.hit_box)
                    owner_text = functions.create_text(f"Owner: Player {current_field.owner}", self.h2_font, WHITE, (1400, 1050))
                    self.bliting_on_scren(owner_text)
                self.screen.blit(roll_dice_button.create_surf(True), roll_dice_button.hit_box)
            else:
                self.screen.blit(roll_dice_button.create_surf(roll_dice_button.is_hover()), roll_dice_button.hit_box)
                self.screen.blit(buy_button.create_surf(True), buy_button.hit_box)
                self.screen.blit(build_button.create_surf(True), build_button.hit_box)
            self.bliting_on_scren(roll_dice_button.create_text())
            self.screen.blit(end_turn_button.create_surf(end_turn_button.is_hover()), end_turn_button.hit_box)
            self.bliting_on_scren(end_turn_button.create_text())
            self.bliting_on_scren(buy_button.create_text())
            self.bliting_on_scren(build_button.create_text())
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    functions.end_game()
                if event.type == pygame.MOUSEBUTTONDOWN and end_turn_button.is_hover():
                    if self.turn == 1:
                        self.turn = 2
                    else:
                        self.turn = 1
                    move_step = None
                    diced = False
                    current_field = None
                if event.type == pygame.MOUSEBUTTONDOWN and roll_dice_button.is_hover(): #and not diced: # deleted for testing and multiple throws
                    diced = True
                    move_step = self.dice.rolling()
                    self.dice.showing()
                    self.players[self.turn-1].move(move_step)
                    current_field = self.fields[self.players[self.turn-1].position]
                if (event.type == pygame.MOUSEBUTTONDOWN and buy_button.is_hover() and diced
                        and not current_field.properties["Occupied"] and current_field.properties["To buy"]):
                    current_field.buying(self.players[self.turn-1])
                if (event.type == pygame.MOUSEBUTTONDOWN and build_button.is_hover() and diced and
                        building_ability and isinstance(current_field, City) and current_field.builded < 5 and
                        self.players[self.turn-1].money >= current_field.properties["Building cost"]):
                    current_field.building()
            self.clearing_board()
            for player in self.players:
                player.update()

            for field in self.fields:
                if isinstance(field, City):
                    field.showing_buildings()
            self.fpsClock.tick(30)
            pygame.display.flip()
