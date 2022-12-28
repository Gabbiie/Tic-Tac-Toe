from tictactoe import TicTacToe
from logo import logo

game = TicTacToe()


print(logo)
print("Welcome to Tic Tac Toe.")
keep_playing = True

players = game.choose_players()

while keep_playing:
    game.play_game(players)

    more_rounds = input("Play another round? (Type 'yes')\n"
                        "Start a new game? (Type new)\n"
                        "Enter 'stop' to quit: ").lower()

    if more_rounds == "stop":
        keep_playing = False
    elif more_rounds == "new":
        print(logo)
        print("Welcome to Tic Tac Toe.")
        # Clear the score and the board
        game.reset_score()
        game.clear_board()

        # Add new players
        players = game.choose_players()
        game.play_game(players)
    else:
        # Keep current players and reset the board
        game.clear_board()

