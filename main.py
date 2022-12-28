from tkinter import *
import tkinter.font as fnt

WINNING_COMBINATIONS = [[(1, 1), (1, 2), (1, 3)], [(2, 1), (2, 2), (2, 3)], [(3, 1), (3, 2), (3, 3)],
                        [(1, 1), (2, 1), (3, 1)], [(1, 2), (2, 2), (3, 2)], [(1, 3), (2, 3), (3, 3)],
                        [(1, 1), (2, 2), (3, 3)], [(1, 3), (2, 2), (3, 1)]]


class Game:
    def __init__(self, master):
        self.current_player = "X"
        self.x_cells = []
        self.o_cells = []
        self.x_coor = []
        self.o_coor = []
        self.all_cells = []
        self.x_score = 0
        self.o_score = 0

        self.master = master
        self.master.config(width=500, height=500)
        self.master.title("Tic Tac Toe")

        self.game_board = Frame(width=300, height=300, bg="#FFCACA", padx=50, pady=50)
        self.game_board.grid(row=3, column=1)

        self.title_label = Label(text="Tic Tac Toe", font=("Courier", 28), bg="snow", fg="#CB1C8D")
        self.title_label.grid(row=0, column=1, sticky="news")

        self.status_label = Label(text="X's turn", font=("Ariel", 20), bg="#D989B5", fg="snow")
        self.status_label.grid(row=1, column=1, sticky="news")

        self.score_label = Label(text=f"X: {self.x_score} |  O: {self.o_score}", font=("Courier", 22), bg="#FF8DC7")
        self.score_label.grid(row=2, column=1, sticky="news")

    def check_for_winner(self, player_moves, player):
        """Checks if a current player has won the game"""
        for combo in WINNING_COMBINATIONS:
            if all(item in player_moves for item in combo):
                return player


root = Tk()
game = Game(root)


class GameCell:
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.value = None
        self.button = Button(board, text="", width=12, height=5, command=self.pick_cell,
                             font=fnt.Font(size=15), bg="snow")
        self.button.grid(row=x, column=y)

    def pick_cell(self):
        """Contains the functionality of the game. """
        winner = False
        # User makes their move by clicking on a button
        if not self.value:
            self.value = game.current_player

            if game.current_player == "X":
                game.status_label.configure(text="X's turn")
                game.x_cells.append(self)
                self.button.configure(text=game.current_player, bg='#009EFF', fg='black')
                # Track X's positions
                for item in game.x_cells:
                    cell = (item.x, item.y)

                    if cell not in game.x_coor:
                        game.x_coor.append(cell)
                # print(x_coor)
                winner = game.check_for_winner(game.x_coor, game.current_player)

                if winner:
                    print(f"{winner} wins!")
                    game.status_label.configure(text="X won!")
                    game.x_score += 1
                    game.score_label.configure(text=f"X: {game.x_score} |  O: {game.o_score}", font=("Courier", 22))
                    disable_game()

                # Swap players
                game.current_player = "O"

            elif game.current_player == "O":
                game.status_label.configure(text="O's turn")
                self.button.configure(text=game.current_player, bg='#00E7FF', fg='black')
                game.o_cells.append(self)
                # Track O's positions
                for item in game.o_cells:
                    cell = (item.x, item.y)

                    if cell not in game.o_coor:
                        game.o_coor.append(cell)
                # print(o_coor)
                winner = game.check_for_winner(game.o_coor, game.current_player)

                if winner:
                    print(f"{winner} wins!")
                    game.status_label.configure(text="O won!")
                    game.o_score += 1
                    game.score_label.configure(text=f"X: {game.x_score}  |  O: {game.o_score}", font=("Courier", 22))
                    disable_game()

                # Swap players
                game.current_player = "X"

        # Checks for a draw
        if len(game.x_coor) + len(game.o_coor) == 9 and not winner:
            print("It's a draw!")
            game.status_label.configure(text="It's a draw!")
            disable_game()

    def reset_cells(self):
        """Resets the game"""

        self.button.configure(text="", bg='snow')
        if self.value == "X":
            game.x_coor = []
            game.x_cells.remove(self)
        elif self.value == "O":
            game.o_coor = []
            game.o_cells.remove(self)
        self.value = None


# Creates all the cells on the board
for xcor in range(1, 4):
    for ycor in range(1, 4):
        game.all_cells.append((GameCell(xcor, ycor, game.game_board)))


def play_again():
    """Starts a new round of the game"""

    game.current_player = 'X'

    for point in game.all_cells:
        point.button.configure(state=NORMAL)
        point.reset_cells()

    game.status_label.configure(text="X's turn")
    play_again_button.grid_forget()


def disable_game():
    """Disables the buttons when the game is over."""
    for cell in game.all_cells:
        cell.button.configure(state=DISABLED)
        play_again_button.grid(row=4, column=1)


play_again_button = Button(text='Play again', font=('Ariel', 20), command=play_again, bg="#FF9494")

root.mainloop()
