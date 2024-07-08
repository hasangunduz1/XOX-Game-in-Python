import tkinter as tk
import random
from tkinter import messagebox
import subprocess

class RockPaperScissorsGame:
    def __init__(self,starting_symbol='X'):
        self.app = tk.Tk()
        self.app.title("Taş Kağıt Makas")
        self.window_width = 450
        self.window_height = 550
        self.set_window_position()
        self.set_window_size()
        self.set_window_bg_color()
        self.starting_symbol=starting_symbol
        self.current_player=None

        bg_color = '#140B69'
        y_coordinate = 100 

        label = tk.Label(self.app, text="Lütfen bir seçim yapın:", font=('Helvetica', 15, 'bold'), bg=bg_color, fg='white', height=2, width=30)
        label.place(x=45, y=10)



        choices = ["Taş", "Kağıt", "Makas"]
        for choice in choices:
            button = tk.Button(self.app, text=choice, font=('Helvetica', 12),  bg='white', fg=bg_color, height=3, width=15,command=lambda choice=choice: self.user_choice_selected(choice))
            button.place(x=160, y=y_coordinate)
            y_coordinate += 100

    def set_window_size(self):
        self.app.geometry(f'{self.window_width}x{self.window_height}')

    def set_window_position(self):
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x = (screen_width / 2) - (self.window_width / 2)
        y = (screen_height / 2) - (self.window_height / 2)
        self.app.geometry(f'+{int(x)}+{int(y)}')

    def set_window_bg_color(self):
        bg_color = '#140B69'
        self.app.configure(bg=bg_color)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            print("Berabere!")
            messagebox.showinfo("Rock Paper Scissors","Tie")
            return None  # Berabere
        elif (user_choice == "Taş" and computer_choice == "Makas") or \
                (user_choice == "Kağıt" and computer_choice == "Taş") or \
                (user_choice == "Makas" and computer_choice == "Kağıt"):
            print("Kullanıcı kazandı!")
            messagebox.showinfo("Rock Paper Scissors","Congratulations you won !!")
              # Kullanıcı kazandı
            if self.starting_symbol=='X':
                self.current_player ='X'
            else:
                self.current_player ='O'
            self.app.destroy()
            subprocess.run(["python", "stur_1.py"], str(self.starting_symbol))
            return "user"
        else:
            print("Bilgisayar kazandı!")
            messagebox.showinfo("Rock Paper Scissors","You lost :(")
            if self.starting_symbol=='X':
                self.current_player ='O'
            else:
                self.current_player ='X'
             # Bilgisayar kazandı
            self.app.destroy()
            subprocess.run(["python", "stur_1.py"], str(self.current_player))
            return "computer" 


    def user_choice_selected(self, choice):
        print(f"Kullanıcı seçimi: {choice}")
        computer_choices = ["Taş", "Kağıt", "Makas"]
        computer_choice = random.choice(computer_choices)
        print(f"Bilgisayar seçimi: {computer_choice}")
        winner = self.determine_winner(choice, computer_choice)
        if winner == "user":
            # Kullanıcı kazandığında, bilgisayarın hamle yapmasını sağla
            self.make_computer_move()

    def make_computer_move(self):
        # Burada bilgisayarın hamle yapmasını sağlayacak kodlar olmalı
        pass

    def start(self):
        self.app.mainloop()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.start()

    