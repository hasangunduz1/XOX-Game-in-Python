import subprocess
import tkinter as tk
from tkinter import messagebox
import sys
import multiplayer
from PIL import Image, ImageTk
import threading
import pygame
import imageio
import time

class TicTacToe:
    def __init__(self, master, starting_symbol):
        self.master = master
        self.master.title("XOX Game")

         # Create a canvas to display the background image
        self.canvas = tk.Canvas(self.master, width=window_width, height=window_height)
        self.canvas.pack(fill="both", expand=True)

        # Load and display the background image
        self.bg_image = Image.open(r"C:\Users\brr_c\OneDrive\Masaüstü\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\tahta_3.jpeg")
        self.bg_image = self.bg_image.resize((450, 550), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)

        pygame.init()
        pygame.mixer.init()

        self.load_music()

        new_button = tk.Button(self.master, text="♪ ", command=self.toggle_music, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=1, width=2)
        new_button.place(x=410, y=10)

        reverse_button = tk.Button(self.master, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg='gray', fg='black', height=1, width=3)
        reverse_button.place(x=10, y=10)

        self.score_label = tk.Label(self.master, text="X: 0  O: 0", font=("Helvetica", 30),bg=bg_color, fg='black')
        self.score_label.place(x= 135, y=70)

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.current_player = starting_symbol
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.frame, text="", font=("Helvetica", 16), width=5, height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

        self.frame.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        self.player_x_score = 0
        self.player_o_score = 0
        self.total_rounds = 3
        self.current_round = 0

    def load_music(self):
        self.music = pygame.mixer.music.load(r"C:\Users\brr_c\OneDrive\Masaüstü\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\music.mp3")
        pygame.mixer.music.play(-1)

    def toggle_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()


    def select_settings_button(self):
        """Settings button click event."""
        # Multiplayer penceresini kapat
        self.master.destroy()
        # settings.py dosyasını aç
        subprocess.run(["python", "settings.py"])


    def select_reverse_button(self):
        
        self.master.destroy()
        
        subprocess.run(["python", "multiplayer.py"])

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

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]  # Horizontal win
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]  # Vertical win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]  # Diagonal win
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]  # Diagonal win

        
        is_board_full = all(self.board[i][j] != "" for i in range(3) for j in range(3))
        if is_board_full:
            return "Draw"  
        return None  

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_round(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = starting_symbol

    def update_score(self):
        winner = self.check_winner()
        if winner and winner != "Draw":  
            if winner == "X":
                self.player_x_score += 1
            else:
                self.player_o_score += 1

            self.update_score_display()

    def update_score_display(self):
        score_text = f"X: {self.player_x_score}  O: {self.player_o_score}"
        self.score_label.config(text=score_text)

    def display_winner(self):
        if self.player_x_score > self.player_o_score:
            winner = "X"
        elif self.player_o_score > self.player_x_score:
            winner = "O"
        else:
            winner = "None (Draw)"

        messagebox.showinfo("Game Over", f"Winner: {winner} has won the game!")

        
        self.reset_round()

        
        self.master.destroy()
        self.multiplayer_page()


    def multiplayer_page(self):
        root = tk.Tk()
        app = multiplayer.MultiPlayer(root)
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

    bg_color = 'gray'
    root.configure(bg=bg_color)

    game = TicTacToe(root, starting_symbol)
    root.mainloop()
