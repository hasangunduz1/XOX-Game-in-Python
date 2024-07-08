import subprocess
import tkinter as tk
import os
import pygame

class Music(tk.Tk):
    def __init__(self):
        super().__init__()
        window_width = 450
        window_height = 550
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        self.resizable(False, False)

        self.bg_color = '#FFFFFF'
        self.black_color = '#212529'
        self.configure(bg=self.bg_color)

        self.selected_music = None
        self.music_playing = False
        self.music_state = "stopped"
        self.music_volume = 0.5

        self.create_widgets()

    def create_widgets(self):
        self.music_listbox = tk.Listbox(self, font=('Helvetica', 12),width=30,height=10)
        self.music_listbox.place(x=90, y=80)

        music_files = os.listdir("music")
        for music_file in music_files:
            self.music_listbox.insert(tk.END, music_file)

        self.select_button = tk.Button(self, text="Müzik Seç", command=self.select_music, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white')
        self.select_button.place(x=180,y=300)

        self.play_button = tk.Button(self, text="Oynat/Durdur", command=self.play_pause_music, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white', state="disabled")
        self.play_button.place(x=170,y=340)

        self.volume_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.change_volume, font=('Helvetica', 12, 'bold'))
        self.volume_scale.set(50)
        self.volume_scale.place(x=175,y=390)

        reverse_button = tk.Button(self, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg=self.black_color, fg='white', height=1, width=3)
        reverse_button.place(x=10, y=10)


    def select_reverse_button(self):
        
        self.destroy()
        
        subprocess.run(["python", "may19_settings.py"])

    def play_pause_music(self):
        if self.selected_music:
            if self.music_playing:
                pygame.mixer.music.stop()
                self.music_playing = False
                self.music_state = "stopped"
            else:
                pygame.mixer.music.load(self.selected_music)
                pygame.mixer.music.set_volume(self.music_volume)
                pygame.mixer.music.play(-1)
                self.music_playing = True
                self.music_state = "playing"

    def select_music(self):
        self.selected_music = os.path.join("music", self.music_listbox.get(tk.ACTIVE))
        self.play_button["state"] = "normal"

    def change_volume(self, value):
        self.music_volume = float(value) / 100
        if self.music_playing:
            pygame.mixer.music.set_volume(self.music_volume)

# Kullanım örneği:
pygame.mixer.init()
app = Music()
app.mainloop()
