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

    def update_board(self):
        self.clearing_board()
        for player in self.players:
            player.update()

        for field in self.fields:
            if isinstance(field, City):
                field.showing_buildings()
        self.fpsClock.tick(30)
        pygame.display.flip()

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

    def if_game_over(self):
        for player in self.players:
            if player.money < 0:
                return True, player
        return False, None

    def game(self):
        turn1_text = functions.create_text("First player's turn", self.h2_font, WHITE, (1400, 50))
        turn2_text = functions.create_text("Second player's turn", self.h2_font, WHITE, (1400, 50))
        prison1_text = functions.create_text("First player in prison!", self.h2_font, WHITE, (1400, 50))
        prison2_text = functions.create_text("Second player in prison!", self.h2_font, WHITE, (1400, 50))
        end_turn_button = Button(1400, 200, "END TURN", 200, 50)
        roll_dice_button = Button(1400, 300, "ROLL DICE", 200, 50)
        buy_button = Button(1400, 400, "BUY FIELD", 200, 50)
        build_button = Button(1400, 500, "BUILD", 200, 50)
        buy_out_button = Button(1400, 400, "BUY OUT", 200, 50)
        use_card_button = Button(1400, 500, "USE YOUR CARD", 200, 50)
        pygame.display.flip()
        move_step = None
        diced = False
        current_field = None
        building_ability = None
        paid_rent = None
        got_reward = None
        while True:
            end_game, lost_player = self.if_game_over()
            if end_game:
                return lost_player

            self.drawing_controls_rectangle()
            budget_text = functions.create_text(f"Budget: {functions.money_amount(self.players[self.turn-1].money)}",
                                                self.h2_font, WHITE, (1400, 100))

            self.drawing_controls_rectangle()
            self.bliting_on_scren(budget_text)

            if not self.players[self.turn-1].prison["State"]:
                if move_step:
                    self.dice.showing()
                if self.turn == 1:
                    self.bliting_on_scren(turn1_text)
                elif self.turn == 2:
                    self.bliting_on_scren(turn2_text)
                if diced:
                    if current_field.properties["Special"]:
                        if isinstance(current_field, ChanceCard):
                            chance_card_text = functions.create_text(
                                f"You got: get out of jail!", self.h2_font, WHITE,
                                (1400, 700))
                            self.bliting_on_scren(chance_card_text)
                            if not got_reward:
                                self.players[self.turn-1].prison["Card"] += 1
                                got_reward = True
                        if isinstance(current_field, CommunityChest):
                            community_chest_text = functions.create_text(f"You got: {functions.money_amount(2000000)}!",
                                                                         self.h2_font, WHITE, (1400, 700))
                            self.bliting_on_scren(community_chest_text)
                            if not got_reward:
                                self.players[self.turn-1].money += 2000000
                                got_reward = True
                    if current_field.properties["To buy"]:
                        self.screen.blit(current_field.properties["Title deed card"], (1300, 800))
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
                        owner_text = functions.create_text(f"Owner: Player {current_field.owner}", self.h2_font, WHITE, (1400, 1150))
                        self.bliting_on_scren(owner_text)
                    if ((current_field.properties["To pay"] and current_field.properties["Occupied"]
                         and not functions.same_owner(self.players[self.turn-1], current_field.owner))
                            or current_field.name == "Income tax"):
                        if not paid_rent:
                            if self.turn == 1:
                                self.players[0].money -= current_field.rent
                                self.players[1].money += current_field.rent
                            elif self.turn == 2:
                                self.players[0].money += current_field.rent
                                self.players[1].money -= current_field.rent
                            paid_rent = True
                        self.bliting_on_scren(current_field.paying_rent(self.h2_font, WHITE))
                    self.screen.blit(roll_dice_button.create_surf(True), roll_dice_button.hit_box)
                    self.screen.blit(end_turn_button.create_surf(end_turn_button.is_hover()), end_turn_button.hit_box)
                else:
                    self.screen.blit(roll_dice_button.create_surf(roll_dice_button.is_hover()), roll_dice_button.hit_box)
                    self.screen.blit(buy_button.create_surf(True), buy_button.hit_box)
                    self.screen.blit(build_button.create_surf(True), build_button.hit_box)
                    self.screen.blit(end_turn_button.create_surf(True), end_turn_button.hit_box)

                self.bliting_on_scren(end_turn_button.create_text())
                self.bliting_on_scren(roll_dice_button.create_text())
                self.bliting_on_scren(buy_button.create_text())
                self.bliting_on_scren(build_button.create_text())

            else:
                if move_step:
                    self.dice.showing()
                if self.turn == 1:
                    self.bliting_on_scren(prison1_text)
                elif self.turn == 2:
                    self.bliting_on_scren(prison2_text)
                if not diced:
                    self.screen.blit(end_turn_button.create_surf(True), end_turn_button.hit_box)
                    self.screen.blit(roll_dice_button.create_surf(roll_dice_button.is_hover()),
                                     roll_dice_button.hit_box)
                else:
                    self.screen.blit(end_turn_button.create_surf(end_turn_button.is_hover()), end_turn_button.hit_box)
                    self.screen.blit(roll_dice_button.create_surf(True), roll_dice_button.hit_box)
                if self.players[self.turn-1].money > 500000 and not diced:
                    self.screen.blit(buy_out_button.create_surf(buy_out_button.is_hover()), buy_out_button.hit_box)
                else:
                    self.screen.blit(buy_out_button.create_surf(True), buy_out_button.hit_box)
                if self.players[self.turn-1].prison["Card"] > 0 and not diced:
                    self.screen.blit(use_card_button.create_surf(use_card_button.is_hover()), use_card_button.hit_box)
                else:
                    self.screen.blit(use_card_button.create_surf(True), use_card_button.hit_box)

                self.bliting_on_scren(end_turn_button.create_text())
                self.bliting_on_scren(use_card_button.create_text())
                self.bliting_on_scren(roll_dice_button.create_text())
                self.bliting_on_scren(buy_out_button.create_text())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    functions.end_game()

                if not self.players[self.turn-1].prison["State"]:
                    if event.type == pygame.MOUSEBUTTONDOWN and roll_dice_button.is_hover() and not diced: # deleted for testing and multiple throws
                        diced = True
                        move_step = self.dice.rolling()
                        self.dice.showing()
                        self.players[self.turn-1].move(move_step)
                        current_field = self.fields[self.players[self.turn-1].position]
                        if self.players[self.turn-1].position == 30:
                            self.players[self.turn-1].prison["State"] = True
                            if self.turn == 1:
                                self.players[self.turn - 1].walk_to((90, 1070))
                            elif self.turn == 2:
                                self.players[self.turn - 1].walk_to((25, 1140))
                            self.update_board()

                    if event.type == pygame.MOUSEBUTTONDOWN and end_turn_button.is_hover() and diced:
                        if self.turn == 1:
                            self.turn = 2
                        elif self.turn == 2:
                            self.turn = 1
                        move_step = None
                        diced = False
                        current_field = None
                        paid_rent = False
                        got_reward = False

                    if (event.type == pygame.MOUSEBUTTONDOWN and buy_button.is_hover() and diced
                            and not current_field.properties["Occupied"] and current_field.properties["To buy"]):
                        if isinstance(current_field, City):
                            current_field.buying(self.players[self.turn-1])
                        else:
                            current_field.buying(self.players[self.turn-1])
                            field_in_category_owning = []
                            for field in self.fields:
                                if isinstance(field, Transport) and isinstance(current_field, Transport):
                                    if functions.same_owner(current_field.owner, field.owner):
                                        field_in_category_owning.append(field)
                                elif isinstance(field, Communication) and isinstance(current_field, Communication):
                                    if functions.same_owner(current_field.owner, field.owner):
                                        field_in_category_owning.append(field)
                            amount_of_category_fields = len(field_in_category_owning)
                            for field in field_in_category_owning:
                                field.rent = field.properties["Rent"][amount_of_category_fields]
                    if (event.type == pygame.MOUSEBUTTONDOWN and build_button.is_hover() and diced and
                            building_ability and isinstance(current_field, City) and current_field.builded < 5 and
                            self.players[self.turn-1].money >= current_field.properties["Building cost"]):
                        current_field.building()

                else:
                    if event.type == pygame.MOUSEBUTTONDOWN and roll_dice_button.is_hover() and not diced: # deleted for testing and multiple throws
                        diced = True
                        if self.dice.rolling_in_prison():
                            self.players[self.turn-1].prison["State"] = False
                            self.dice.showing()
                            self.players[self.turn - 1].move(self.dice.move_step1+self.dice.move_step2)
                            current_field = self.fields[self.players[self.turn - 1].position]
                        move_step = self.dice.move_step1 + self.dice.move_step2
                        self.dice.showing()
                    if event.type == pygame.MOUSEBUTTONDOWN and end_turn_button.is_hover() and diced:
                        if self.turn == 1:
                            self.turn = 2
                        else:
                            self.turn = 1
                        move_step = None
                        diced = False
                        current_field = None
                        paid_rent = False
                        got_reward = False
                    if event.type == pygame.MOUSEBUTTONDOWN and buy_out_button.is_hover():
                        self.players[self.turn - 1].prison["State"] = False
                        self.players[self.turn - 1].money -= 500000
                        if self.turn == 1:
                            self.turn = 2
                        else:
                            self.turn = 1
                        move_step = None
                        diced = False
                        current_field = None
                        paid_rent = False
                        got_reward = False
                    if event.type == pygame.MOUSEBUTTONDOWN and use_card_button.is_hover():
                        self.players[self.turn - 1].prison["State"] = False
                        self.players[self.turn - 1].prison["Card"] -= 1
                        if self.turn == 1:
                            self.turn = 2
                        else:
                            self.turn = 1
                        move_step = None
                        diced = False
                        current_field = None
                        paid_rent = False
                        got_reward = False
            self.update_board()
