import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

import pygame

class Main:
    def __init__(self, root, language=None):
        self.root = root
        self.app = root
        self.app.title('Ana Sayfa')

        self.current_language = language

        window_width = 450
        window_height = 550
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.app.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        self.app.resizable(False, False)

        bg_color = 'gray'
        self.app.configure(bg=bg_color)

        pygame.init()
        pygame.mixer.init()

        self.load_music()

        canvas = tk.Canvas(self.app, width=450, height=550, bg=bg_color, highlightthickness=0)
        canvas.pack()

        level_label = tk.Label(self.app, text="Select Level", font=('Helvetica', 18, 'bold'), bg=bg_color, fg='black')
        level_label.place(x=150, y=25)

        new_button = tk.Button(self.app, text="♪ ", command=self.toggle_music, font=('Helvetica', 14, 'bold'), bg='black', fg='white', height=1, width=3)
        new_button.place(x=400, y=10)

        reverse_button = tk.Button(self.app, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg='black', fg='white', height=1, width=3)
        reverse_button.place(x=10, y=10)
        # Patika yolu çizgileri
        path_points = [(100, 125), (300, 195), (100, 265), (300, 335), (100, 405), (300, 475)]
        for i in range(len(path_points) - 1):
            canvas.create_line(path_points[i], path_points[i + 1], fill='white', width=3)

        # Seviye butonları
        self.level_buttons = []
        for i in range(1, 7):
            x_pos = 100 if i % 2 != 0 else 300
            y_pos = 100 + (i - 1) * 70
            button = tk.Button(self.app, text=str(i), command=lambda idx=i: self.select_level(idx),
                               font=('Helvetica', 12, 'bold'), bg='black', fg='white', height=2, width=4)
            button.place(x=x_pos, y=y_pos)
            self.level_buttons.append(button)

        # Seviye kilitlerini ayarla
        self.lock_levels()

    def lock_levels(self):
        for button in self.level_buttons[2:]:
            button.config(state=tk.DISABLED)

    def unlock_levels(self):
        for button in self.level_buttons:
            button.config(state=tk.NORMAL)

    def select_reverse_button(self):  
        pygame.mixer.music.stop()
        self.app.destroy()
        subprocess.run(["python", "main.py"])
        self.play_sound()
    
    def load_music(self):
        self.music = pygame.mixer.music.load(r"C:\Users\brr_c\OneDrive\Masaüstü\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\music.mp3")
        pygame.mixer.music.play(-1)

    def toggle_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def select_level(self, level):
        level_file = f"level_{level}.py"
        level_path = os.path.join(os.path.dirname(__file__), level_file)
        if os.path.exists(level_path):
            self.app.destroy()
            subprocess.run(["python", level_path])
        else:
            messagebox.showerror("Error", "Invalid level file path.")

if __name__ == "__main__":
    root = tk.Tk()
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]
    app = Main(root, language)
    root.mainloop()
