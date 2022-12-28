import random

WINNING_COMBINATIONS = [[(1, 1), (1, 2), (1, 3)], [(2, 1), (2, 2), (2, 3)], [(3, 1), (3, 2), (3, 3)],
                        [(1, 1), (2, 1), (3, 1)], [(1, 2), (2, 2), (3, 2)], [(1, 3), (2, 3), (3, 3)],
                        [(1, 1), (2, 2), (3, 3)], [(1, 3), (2, 2), (3, 1)]]


class TicTacToe:
    def __init__(self):
        self.board = []
        self.player_1 = None
        self.player_2 = None
        self.player_1_name = None
        self.player_2_name = None
        self.player_1_moves = []
        self.player_2_moves = []
        self.winner = None
        self.player_1_score = 0
        self.player_2_score = 0

    def create_board(self):
        """Creates the Tic Tac Toe Board"""
        for i in range(3):
            row = []
            for j in range(3):
                row.append("_")
            self.board.append(row)
        return self.board

    def display_board(self):
        """Displays the Board onto the console"""
        for item in self.board:
            print("-----------------------")
            for char in item:
                print(f" {char}    |", end=" ")
            print()

    def display_scoreboard(self):
        print("--------ScoreBoard---------")
        print(f"{self.player_1_name}: {self.player_1_score}")
        print(f"{self.player_2_name}: {self.player_2_score}")
        print("---------------------------")

    def choose_players(self):
        """Gets the names of the users and assigns game characters"""

        self.player_1_name = input("Player 1 👨‍💻👩‍💻\n Enter your name: ").title()
        self.player_2_name = input("Player 2 👨‍💻‍👩‍💻\n Enter your name: ").title()

        print(f"{self.player_1_name}, choose your character.")
        choice = input("Enter 1 for 'X'.\nEnter 2 for 'O'.\n").upper()

        if choice == "X":
            self.player_1 = "X"
            self.player_2 = "O"
        else:
            self.player_1 = "O"
            self.player_2 = "X"

        return self.player_1, self.player_2

    def make_move(self, player, player_moves):
        """Allows a user to place 'X' or 'O' on the board"""
        self.display_board()
        print(f"Player {player}'s turn.")

        # User chooses where to place their character.
        choose_pos = True
        while choose_pos:
            try:
                row = int(input("Pick a row from 1 to 3 to make your move: "))
                col = int(input("Pick a column from 1 to 3 to make your move: "))

            except ValueError:
                # Keeps prompting user to pick the correct row or column
                print("Please enter valid numbers!")
            else:
                if (1 <= row <= 3) and (1 <= col <= 3):
                    choose_pos = False

                    if ((row, col) not in self.player_1_moves) and ((row, col) not in self.player_2_moves):

                        self.board[row - 1][col - 1] = player

                        # Tracks the player's moves
                        player_moves.append((row, col))
                        # print(player_moves)
                    else:
                        print("Position has already been taken!")

                else:
                    print("Please enter numbers from 1 to 3.")
                    print("\n")

        return self.board

    def check_for_winner(self, player_moves, player):
        """Checks if a current player has won the game"""
        for combo in WINNING_COMBINATIONS:
            if all(item in player_moves for item in combo):
                self.winner = player
                return self.winner

        return False

    def check_board(self):
        """Checks whether the board has been filled."""
        is_filled = True

        for row in self.board:
            if "_" in row:
                is_filled = False

        return is_filled

    def clear_board(self):
        self.board = []
        self.player_2_moves = []
        self.player_1_moves = []

    def reset_score(self):
        self.player_1_score = 0
        self.player_2_score = 0

    def play_game(self, players):
        """Controls functionality of the game"""

        self.create_board()

        # Randomly chooses a player to play the game first
        current_player = random.choice(players)

        if current_player == self.player_1:
            current_player_moves = self.player_1_moves
        else:
            current_player_moves = self.player_2_moves

        keep_playing = True

        while keep_playing:

            is_full = self.check_board()
            # print(is_full)

            # print(self.board)

            if is_full:
                # Prints feedback because the players have run out of moves and breaks the loop
                keep_playing = False

                print(f"It\'s a draw!")

            else:

                # Current player makes their move
                self.make_move(current_player, current_player_moves)
                winner = self.check_for_winner(current_player_moves, current_player)
                # print(winner)
                # print(current_player_moves)

                # Prints feedback because the players have run out of moves and breaks the loop
                if winner:
                    # Updates the winner's score
                    if winner == self.player_1:
                        self.player_1_score += 1
                    else:
                        self.player_2_score += 1

                    print(f"'{winner}' won the game!")

                    keep_playing = False

                # Swaps the players
                if current_player == self.player_1:
                    current_player = self.player_2
                    current_player_moves = self.player_2_moves
                else:
                    current_player = self.player_1
                    current_player_moves = self.player_1_moves

        self.display_board()
        self.display_scoreboard()
        print("\n")
