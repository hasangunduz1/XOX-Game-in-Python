import subprocess
import tkinter as tk
from tkinter import messagebox
import sys
import singleplayer2
import random

class TicTacToe:
    def __init__(self, master, user_symbol):
        self.master = master
        self.master.title("XOX Game")

        reverse_button = tk.Button(self.master, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg=bg_color, fg='white', height=1, width=3)
        reverse_button.place(x=10, y=10)

        self.score_label = tk.Label(self.master, text=f"{user_symbol}: 0  {self.get_com_symbol(user_symbol)}: 0", font=("Helvetica", 30),bg=bg_color, fg='white')
        self.score_label.place(x= 135, y=70)

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.user_symbol = user_symbol
        self.com_symbol = "X" if user_symbol == "O" else "O"
        self.current_player = user_symbol
        self.board = [["" for _ in range(4)] for _ in range(4)]

        self.buttons = [[None for _ in range(4)] for _ in range(4)]

        for i in range(4):
            for j in range(4):
                self.buttons[i][j] = tk.Button(
                    self.frame, text="", font=("Helvetica", 16), width=5, height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

        self.frame.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        self.user_score = 0
        self.com_score = 0
        self.total_rounds = 1
        self.current_round = 0

    def select_reverse_button(self):
        self.master.destroy()
        subprocess.run(["python", "singleplayer2.py"])

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                self.update_score()  
                self.current_round += 1
                if self.current_round == self.total_rounds:
                    self.display_winner()  
                else:
                    self.reset_round()
            else:
                self.switch_player()
                if self.current_player == self.com_symbol:
                    self.computer_move()

    def get_com_symbol(self, user_symbol):
        return "X" if user_symbol == "O" else "O"

    def computer_move(self):
        # Basit bir algoritma: Önce kendi kazanma hamlesi, sonra bloke etme, sonra rasgele hamle
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == "":
                    # Oyunu kazanabileceğimiz bir hamle var mı?
                    self.board[i][j] = self.com_symbol
                    if self.check_winner() == self.com_symbol:
                        self.buttons[i][j].config(text=self.com_symbol)
                        self.update_score()
                        self.current_round += 1
                        if self.current_round == self.total_rounds:
                            self.display_winner()
                        else:
                            self.reset_round()
                        return
                    else:
                        self.board[i][j] = ""  # Denemeyi geri al

        # Rakibin kazanma hamlesini engelleyebilir miyiz?
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == "":
                    self.board[i][j] = self.user_symbol
                    if self.check_winner() == self.user_symbol:
                        self.board[i][j] = self.com_symbol
                        self.buttons[i][j].config(text=self.com_symbol)
                        self.switch_player()
                        return
                    else:
                        self.board[i][j] = ""  # Denemeyi geri al

        # Rasgele bir hamle yap
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.com_symbol
            self.buttons[row][col].config(text=self.com_symbol)
            self.switch_player()

    def check_winner(self):
        for i in range(4):  # 4x4 tahta için güncellendi
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.board[i][3] != "":
                return self.board[i][0]  # Horizontal win
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.board[3][i] != "":
                return self.board[0][i]  # Vertical win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] != "":
            return self.board[0][0]  # Diagonal win
        if self.board[0][3] == self.board[1][2] == self.board[2][1] == self.board[3][0] != "":
            return self.board[0][3]  # Diagonal win

        is_board_full = all(self.board[i][j] != "" for i in range(4) for j in range(4))
        if is_board_full:
            return "Draw"  
        return None  

    def switch_player(self):
        self.current_player = self.user_symbol if self.current_player == self.com_symbol else self.com_symbol

    def reset_round(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = self.user_symbol

    def update_score(self):
        winner = self.check_winner()
        if winner and winner != "Draw":  
            if winner == self.user_symbol:
                self.user_score += 1
            else:
                self.com_score += 1
            self.update_score_display()
        elif winner == "Draw":
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_round()
            self.update_score_display()

    def update_score_display(self):
        score_text = f"{self.user_symbol}: {self.user_score}  {self.com_symbol}: {self.com_score}"
        self.score_label.config(text=score_text)

    def display_winner(self):
        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Winner: {winner} has won the game!")
        else:
            messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_round()
        self.update_score_display()

    def singleplayer_page(self):
        root = tk.Tk()
        app = singleplayer2.SinglePlayer(root)
        root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        starting_symbol = sys.argv[1]
    else:
        starting_symbol = "X"  

    root = tk.Tk()
    window_width = 450
    window_height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    bg_color = '#140B69'
    root.configure(bg=bg_color)

    game = TicTacToe(root, starting_symbol)
    root.mainloop()
