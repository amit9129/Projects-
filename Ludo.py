import random

class LudoGame:
    def __init__(self):
        self.board = [0] * 40  # Represents the Ludo board with 40 spaces
        self.players = []
        self.current_player = None

    def add_player(self, player_name):
        self.players.append({"name": player_name, "position": 0})

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player_index, steps):
        self.players[player_index]["position"] += steps
        if self.players[player_index]["position"] >= 40:
            self.players[player_index]["position"] -= 40

    def play_turn(self):
        if not self.players:
            print("No players in the game.")
            return

        self.current_player = (self.current_player + 1) % len(self.players)
        player = self.players[self.current_player]
        print(f"{player['name']}'s turn.")
        input("Press Enter to roll the dice...")

        dice_roll = self.roll_dice()
        print(f"{player['name']} rolled a {dice_roll}.")
        self.move_player(self.current_player, dice_roll)

        print(f"{player['name']} is at position {player['position']} on the board.")
        input("Press Enter to end the turn...")

    def play_game(self):
        if not self.players:
            print("No players in the game.")
            return

        while True:
            self.play_turn()

            if self.players[self.current_player]["position"] == 40:
                print(f"{self.players[self.current_player]['name']} wins!")
                break

def main_menu():
    print("Welcome to Ludo Game")
    print("1. Start a new game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        num_players = int(input("Enter the number of players (2-4): "))
        if num_players < 2 or num_players > 4:
            print("Invalid number of players. The game supports 2-4 players.")
        else:
            ludo_game = LudoGame()
            for i in range(num_players):
                player_name = input(f"Enter player {i + 1}'s name: ")
                ludo_game.add_player(player_name)
            ludo_game.current_player = -1  # Initialize current player
            ludo_game.play_game()
    elif choice == "2":
        exit()
    else:
        print("Invalid choice. Please select 1 or 2.")
        main_menu()

if __name__ == "__main__":
    main_menu()
