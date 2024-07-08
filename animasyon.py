import tkinter as tk
from tkinter import font
import subprocess
import sys

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

        bg_color = '#140B69'
        self.app.configure(bg=bg_color)

        self.button = tk.Button(self.app, text="?", bg=bg_color, fg="white", command=self.open_music, relief=tk.FLAT)
        self.button.place(relx=0.98, rely=0.98, anchor='se')  # Sağ alt köşe için

        self.font_size = 12
        self.font_direction = 1
        self.animate_font()

    def animate_font(self):
        self.font_size += self.font_direction
        if self.font_size > 16:
            self.font_direction = -1
        elif self.font_size < 12:
            self.font_direction = 1
        self.button.config(font=("Arial", self.font_size))
        self.app.after(100, self.animate_font)

    def open_music(self):
        subprocess.Popen(["python", "music.py"])

if __name__ == "__main__":
    root = tk.Tk()
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]
    app = Main(root, language)
    root.mainloop()
