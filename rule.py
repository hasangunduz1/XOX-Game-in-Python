import subprocess
import tkinter as tk
import sys


class Main:
    def __init__(self, root, language=None):
        self.root = root
        self.app = root
        self.app.title('How to Play Tic Tac Toe Game')

        self.current_language = language

        window_width = 450
        window_height = 550
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.app.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        self.app.resizable(False, False)

        bg_color = '#140B69'
        self.app.configure(bg=bg_color)

        reverse_button = tk.Button(self.app, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg='#EF802F', fg='white', height=1, width=3)
        reverse_button.place(x=10, y=10)
        # Oyun kurallarını içeren metin
        rules_text = """
        Tic Tac Toe is a strategy game played 
        between two players.
        The game board is a 3x3 grid.
        Players take turns placing X and O symbols.
        Your goal is to get three symbols in a row, 
        either vertically, horizontally, or diagonally.
        The player who first gets three 
        symbols in a row wins the game.
        If the board fills up and no player 
        wins, the game ends in a draw.
        """

        # Metin etiketi oluşturma ve metni pencereye yerleştirme
        label = tk.Label(self.app, text=rules_text, bg=bg_color, fg='white', font=('Arial', 14), justify='left')
        label.pack(padx=10, pady=50, fill='both', expand=True)

    def select_reverse_button(self):
        
        self.app.destroy()
        
        subprocess.run(["python", "main.py"])


if __name__ == "__main__":
    root = tk.Tk()
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]
    app = Main(root, language)
    root.mainloop()
