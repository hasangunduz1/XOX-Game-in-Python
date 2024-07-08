import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import sys



class MultiPlayer:
    def __init__(self, root,language):
        self.root = root
        self.starting_symbol = None
        self.total_rounds = None
        
        self.current_language = language
        
        self.app = root
        self.app.title('MultiPlayer')

        window_width = 450
        window_height = 550
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.app.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        self.app.resizable(False, False)

        bg_color = '#FFFFFF'
        red_color ='#9A031E'
        black_color = '#212529'
        grey_color = '#8D99AE'

        self.app.configure(bg=bg_color)

        settings_button = tk.Button(self.app, text="⚙️", command=self.select_settings_button, font=('Helvetica', 12, 'bold'), bg=black_color, fg='white', height=1, width=2)
        settings_button.place(x=410, y=10)

        reverse_button = tk.Button(self.app, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg=black_color, fg='white', height=1, width=3)
        reverse_button.place(x=10, y=10)

        if self.current_language == 'tr':
            select_character_text = "Karakter Seçiniz"
        else:
            select_character_text = "Select Character"

        select_character_label = tk.Label(self.app, text=select_character_text, font=('Helvetica', 16, 'bold'), bg=bg_color, fg=black_color)
        select_character_label.pack(pady=10)

       
        if self.current_language == 'tr':
            player1_text = "1.Oyuncu"
        else:
            player1_text = "First Player"

        player1_label = tk.Label(self.app, text=player1_text, font=('Helvetica', 12, 'bold'), bg=bg_color, fg=black_color)
        player1_label.place(x=25, y=90)


        x_button = tk.Button(self.app, text="☾", command=self.select_x, font=('Helvetica', 12, 'bold'), bg=red_color, fg='white', height=2, width=4)
        x_button.place(x=150, y=75)

        o_button = tk.Button(self.app, text="✰", command=self.select_o, font=('Helvetica', 12, 'bold'), bg=red_color, fg='white', height=2, width=4)
        o_button.place(x=250, y=75)

        if self.current_language == 'tr':
            player2_text = "2.Oyuncu"
        else:
             player2_text = "Second Player"

        player2_label = tk.Label(self.app, text=player2_text, font=('Helvetica', 12, 'bold'), bg=bg_color, fg=black_color)
        player2_label.place(x=25, y=180)

        o_x_button = tk.Button(self.app, text="☾/✰", command=self.select_o_x, font=('Helvetica', 12, 'bold'), bg=red_color, fg='white', height=2, width=4)
        o_x_button.place(x=150, y=165)


        if self.current_language == 'tr':
            select_tour_text = "Tur Sayısını Seçiniz"
        else:
            select_tour_text = "Select Number of Tours"

        label = tk.Label(self.app, text=select_tour_text, font=('Helvetica', 16, 'bold'), bg=bg_color, fg=black_color)
        label.pack(pady=210) 

        one_button = tk.Button(self.app, text="1", command=self.select_one_button, font=('Helvetica', 12, 'bold'), bg=grey_color, fg='white', height=2, width=4)
        one_button.place(x=30, y=330)
        
        three_button = tk.Button(self.app, text="3", command=self.select_three_button, font=('Helvetica', 12, 'bold'), bg=grey_color, fg='white', height=2, width=4)
        three_button.place(x=140, y=330)
        
        five_button = tk.Button(self.app, text="5", command=self.select_five_button, font=('Helvetica', 12, 'bold'), bg=grey_color, fg='white', height=2, width=4)
        five_button.place(x=250, y=330)
        
        eleven_button = tk.Button(self.app, text="11", command=self.select_eleven_button, font=('Helvetica', 12, 'bold'), bg=grey_color, fg='white', height=2, width=4)
        eleven_button.place(x=360, y=330)

        if self.current_language == 'tr':
            play_text = "OYNA"
        else:
            play_text = "PLAY"
        play_button = tk.Button(self.app, text=play_text, command=self.select_play, font=('Helvetica', 12, 'bold'), bg=black_color, fg='white', height=2, width=15)
        play_button.place(x=140, y=440)

    def select_x(self):
        self.starting_symbol = "☾"

    def select_o(self):
        self.starting_symbol = "✰"

    def select_o_x(self):
        print("X or ✰ selected")

    def select_one_button(self):
        self.total_rounds = 1
    
    def select_three_button(self):
        self.total_rounds = 3
    
    def select_five_button(self):
        self.total_rounds = 5

    def select_eleven_button(self):
        self.total_rounds = 11

    def select_settings_button(self):
        """Settings button click event."""
        # Multiplayer penceresini kapat
        self.app.destroy()
        # settings.py dosyasını aç
        subprocess.run(["python", "may19_settings_multi.py"])


    def select_reverse_button(self):
        
        self.app.destroy()
        
        subprocess.run(["python", "may19_main.py"])

    def select_play(self):
        if self.starting_symbol is None:
            messagebox.showerror("Error", "Please select a symbol.")
        elif self.total_rounds is None:
            messagebox.showerror("Error", "Please select the number of rounds.")
        else:
            self.app.destroy()
            
            if self.total_rounds == 1:
                tur_file = "may19_tur_1.py"
            elif self.total_rounds == 3:
                tur_file = "may19_tur_3.py"
            elif self.total_rounds == 5:
                tur_file = "may19_tur_5.py"
            elif self.total_rounds == 11:
                tur_file = "may19_tur_11.py"
            else:
                messagebox.showerror("Error", "Invalid number of rounds.")
                return

            tur_path = os.path.join(os.path.dirname(__file__), tur_file)
            subprocess.run(["python", tur_path, str(self.starting_symbol), str(self.total_rounds),str(self.current_language)], shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]
    app = MultiPlayer(root, language)
    root.mainloop()
