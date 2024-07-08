import subprocess
import tkinter as tk
from tkinter import messagebox
import sys
import may19_multiplayer
from PIL import Image, ImageTk


class TicTacToe:
    def __init__(self, master, starting_symbol,language):
        self.master = master
        self.master.title("XOX Game")
        self.current_language=language

       # logo_image = Image.open(r"C:\Users\brr_c\OneDrive\Masaüstü\HasanGündüz_BerraÇelik_EngineeringProject_FirstJury\bayrak2.png")
        #logo_image = logo_image.resize((300, 300))
        #self.logo_photo = ImageTk.PhotoImage(logo_image)

        #logo_label = tk.Label(self.app, image=self.logo_photo, bg=bg_color)
        #logo_label.pack(expand=True, pady=5)

        #settings_button = tk.Button(self.master, text="⚙️", command=self.select_settings_button, font=('Helvetica', 12, 'bold'), bg=black_color, fg='white', height=1, width=2)
        #settings_button.place(x=410, y=10)

        reverse_button = tk.Button(self.master, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg=black_color, fg='white', height=1, width=3)
        reverse_button.place(x=10, y=10)

        self.score_label = tk.Label(self.master, text="☾ : 0  ✰: 0", font=("Helvetica", 30),bg=bg_color, fg=black_color,width=10, height=1)
        self.score_label.place(x= 105, y=70)

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.current_player = starting_symbol
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.frame, text="", font=("Helvetica", 20,'bold'),bg=red_color, width=5, height=2, fg='white',
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

        self.frame.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        self.player_x_score = 0
        self.player_o_score = 0
        self.turn_counter = 0
    
    def select_settings_button(self):
        """Settings button click event."""
        # Multiplayer penceresini kapat
        self.master.destroy()
        # settings.py dosyasını aç
        subprocess.run(["python", "settings.py"])


    def select_reverse_button(self):
        
        self.master.destroy()
        
        subprocess.run(["python", "may19_multiplayer.py"])

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                self.display_winner()
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
        self.current_player = "✰" if self.current_player == "☾" else "☾"

    def reset_round(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "☾"

    def update_scores(self):
        if self.current_player == "☾":
            self.player_x_score += 1
        else:
            self.player_o_score += 1

    def update_score_display(self):
        score_text = f"☾: {self.player_x_score}  O: {self.player_o_score}"
        self.score_label.config(text=score_text)

    def display_winner(self, draw=False):
        if draw:
            winner = "None (Draw)"
        else:
            winner = self.check_winner()

        if winner == "☾":
            self.player_x_score += 1
        elif winner == "✰":
            self.player_o_score += 1

        self.update_score_display()

        messagebox.showinfo("Game Over", f"Winner: {winner if winner != 'Draw' else 'None (Draw)'}")

        
        self.reset_round()

        
        self.master.destroy()
        self.multiplayer_page()

    def multiplayer_page(self):
        root = tk.Tk()
        app = may19_multiplayer.MultiPlayer(root,language=self.current_language)
        root.mainloop()

    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        starting_symbol = sys.argv[1]
    else:
        starting_symbol = "☾"  

    root = tk.Tk()
    window_width = 450
    window_height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    bg_color = '#fff0f3'
    red_color ='#9A031E'
    black_color = '#212529'
    grey_color = '#8D99AE'
    root.configure(bg=bg_color)
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]

    game = TicTacToe(root, starting_symbol,language)
    root.mainloop()
