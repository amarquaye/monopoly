# Monopoly game in python
import random

class MonopolyGame:
    def __init__(self):
        self.board = [Property(*prop) for prop in BOARD_PROPERTIES]
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        player.position = 0

    def play(self):
        for player in self.players:
            print(f"{player.name}'s turn")
            dice1, dice2 = self.roll_dice()
            print(f"{player.name} rolls {dice1} + {dice2} = {dice1 + dice2}")
            player.move(dice1 + dice2)
            property = self.board[player.position]
            if property.owner is None:
                if player.money >= property.cost:
                    choice = input(f"{player.name}, do you want to buy {property.name} for ${property.cost}? (y/n): ")
                    if choice.lower() == 'y':
                        player.buy(property)
            elif property.owner is not player:
                player.pay_rent(property)
                if player.money < 0:
                    print(f"{player.name} is broke and eliminated from the game")
                    self.players.remove(player)

    @staticmethod
    def roll_dice():
        return random.randint(1, 6), random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0

    def move(self, steps):
        self.position = (self.position + steps) % len(game.board)

    def buy(self, property):
        property.owner = self
        self.money -= property.cost
        print(f"{self.name} bought {property.name} for ${property.cost}")

    def pay_rent(self, property):
        rent = property.rent
        self.money -= rent
        property.owner.money += rent
        print(f"{self.name} pays ${rent} rent to {property.owner.name}")

    def buy_house(self, property):
        if self.money >= property.house_cost:
            choice = input(f"{self.name}, do you want to buy a house for ${property.house_cost}? (y/n): ")
            if choice.lower() == 'y':
                property.houses += 1
                self.money -= property.house_cost
                print(f"{self.name} bought a house for ${property.house_cost}")
    
    def buy_hotel(self, property):
        if self.money >= property.hotel_cost:
            choice = input(f"{self.name}, do you want to buy a hotel for ${property.hotel_cost}? (y/n): ")
            if choice.lower() == 'y':
                property.houses = 0
                property.hotel = True
                self.money -= property.hotel_cost
                print(f"{self.name} bought a hotel for ${property.hotel_cost}")
    
class Property:
    def __init__(self, name, cost, rent):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = None
        self.houses = 0
        self.hotel = False
        self.house_cost = cost // 2
        self.hotel_cost = self.house_cost * 5

    def __str__(self):
        return f"{self.name} ({self.cost})"

# Board properties
BOARD_PROPERTIES = [("Mediterranean Avenue", 60, 2),
                    ("Baltic Avenue", 60, 4),
                    ("Oriental Avenue", 100, 6),
                    ("Vermont Avenue", 100, 6),
                    ("Connecticut Avenue", 120, 8),
                    ("St. Charles Place", 140, 10),
                    ("States Avenue", 140, 10),
                    ("Virginia Avenue", 160, 12),
                    ("St. James Place", 180, 14),
                    ("Tennessee Avenue", 180, 14),
                    ("New York Avenue", 200, 16),
                    ("Kentucky Avenue", 220, 18),
                    ("Indiana Avenue", 220, 18),
                    ("Illinois Avenue", 240, 20),
                    ("Atlantic Avenue", 260, 22),
                    ("Ventnor Avenue", 260, 22),
                    ("Marvin Gardens", 280, 24),
                    ("Pacific Avenue", 300, 26),
                    ("North Carolina Avenue", 300, 26),
                    ("Pennsylvania Avenue", 320, 28),
                    ("Park Place", 350, 35),
                    ("Boardwalk", 400, 50),
                    ]

# Starting the game
game = MonopolyGame()

# Adding players
num_players = int(input("Enter number of players: "))
for i in range(num_players):
    player_name = input(f"Enter name of player {i + 1}: ")
    player = Player(player_name.title())
    game.add_player(player)

game.play()
