import tkinter as tk
from tkinter import Image, messagebox
import os
import subprocess
import sys
import threading
import pygame
import imageio
import time
from PIL import Image, ImageTk

class SettingsPage:
    def __init__(self, root):
        self.root = root
        self.app = root
        self.language = None


        self.app.title('Settings')
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

        pygame.init()
        pygame.mixer.init()

        self.load_music()

        self.video_label = tk.Label(self.app)
        self.video_label.place(x=0, y=0, relwidth=1, relheight=1)  # Video etiketini tüm pencereyi kaplayacak şekilde yerleştir

        self.video_path = 'C://Users//brr_c//OneDrive//Masaüstü//HasanGündüz_BerraÇelik_EngineeringProject_SecondJury//arkaplan.mp4'  # Buraya video dosyanızın yolunu ekleyin
        self.video_thread = threading.Thread(target=self.play_video)
        self.video_thread.daemon = True
        self.video_thread.start()

        new_button = tk.Button(self.app, text="♪ ", command=self.toggle_music, font=('Helvetica', 12, 'bold'), bg='gray', fg='black')
        new_button.place(x=390, y=10, width=50, height=50)

        language_label = tk.Label(self.app, text="Language", font=('Helvetica', 16, 'bold'), bg='gray', fg='black')
        language_label.place(x=180, y=120)

        reverse_button = tk.Button(self.app, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg='gray', fg='black')
        reverse_button.place(x=10, y=490, width=50, height=50)

        setting_button = tk.Button(self.app, text="SETTINGS", command=self.select_setting, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=2, width=10)
        setting_button.place(x=178, y=60)

        tr_button = tk.Button(self.app, text="TR", command=self.select_tr, font=('Helvetica', 12, 'bold'), bg='gray', fg='black')
        tr_button.place(x=150, y=160, width=65 , height=50)

        eng_button = tk.Button(self.app, text="ENG", command=self.select_eng, font=('Helvetica', 12, 'bold'), bg='gray', fg='black')
        eng_button.place(x=240, y=160, width=65 , height=50)


        


        moods_button = tk.Button(self.app, text="Moods", command=self.select_moods, font=('Helvetica', 12, 'bold'), bg='gray', fg='black')
        moods_button.place(x=150, y=230, width=150, height=50)

        new_button.bind("<Enter>", self.on_enter)
        new_button.bind("<Leave>", self.on_leave)

        tr_button.bind("<Enter>", self.on_enters)
        tr_button.bind("<Leave>", self.on_leaves)

        reverse_button.bind("<Enter>", self.on_enter)
        reverse_button.bind("<Leave>", self.on_leave)

        eng_button.bind("<Enter>", self.on_enters)
        eng_button.bind("<Leave>", self.on_leaves)

        

        moods_button.bind("<Enter>", self.on_enterm)
        moods_button.bind("<Leave>", self.on_leavem)

    
    def on_enterm(self, event):
        event.widget.place_configure(width=155, height=55)  # Buton boyutunu artır

    def on_leavem(self, event):
        event.widget.place_configure(width=150, height=50)

    def on_enter(self, event):
        event.widget.place_configure(width=55, height=55)  # Buton boyutunu artır

    def on_leave(self, event):
        event.widget.place_configure(width=50, height=50)

    def on_enters(self, event):
        event.widget.place_configure(width=70, height=55)  # Buton boyutunu artır

    def on_leaves(self, event):
        event.widget.place_configure(width=65, height=50)

    def play_sound(self):
        pygame.mixer.music.load("C:/Users/brr_c/OneDrive/Masaüstü/Animasyon_deneme/Button.mp3")
        pygame.mixer.music.play()

    def play_video(self):
        video = imageio.get_reader(self.video_path, 'ffmpeg')
        fps = video.get_meta_data()['fps']
        frame_duration = 0.9 / fps
        
        while True:
            for frame in video:
                frame_image = Image.fromarray(frame)
                frame_photo = ImageTk.PhotoImage(frame_image)
                self.video_label.config(image=frame_photo)
                self.video_label.image = frame_photo
                self.root.update()
                time.sleep(frame_duration)
            video.set_image_index(0)

    def load_music(self):
        self.music = pygame.mixer.music.load(r"C:\Users\brr_c\OneDrive\Masaüstü\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\music.mp3")
        pygame.mixer.music.play(-1)
    
    def toggle_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def select_setting(self):
         """setting"""


    def select_music(self):
         self.app.destroy()
         subprocess.run(["python","music.py"])
         self.play_sound()

    def select_generic(self):
         """generic"""
         self.play_sound()
    
    def select_tr(self):
          print("Dil Türkçe olarak ayarlandı.")
          self.language = 'tr'
          self.play_sound()
          

    def select_eng(self):
          print("Dil İngilizce olarak ayarlandı.")
          self.language = 'en'
          self.play_sound()
          

    def select_reverse_button(self):
          pygame.mixer.music.stop()
          self.app.destroy()
          subprocess.run(["python", "main.py", str(self.language)])
          self.play_sound()

    def select_moods(self):
          self.app.destroy()
          subprocess.run(["python", "moods.py"])
          self.play_sound()


    

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsPage(root)
    root.mainloop()
