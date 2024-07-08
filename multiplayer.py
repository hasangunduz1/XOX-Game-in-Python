import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import sys
import sys
import threading
import pygame
import imageio
import time
from PIL import Image, ImageTk


class MultiPlayer:
    def __init__(self, root,language=None):
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

        bg_color = 'gray'
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
        new_button.place(x=330, y=10, width=50, height=50)

        settings_button = tk.Button(self.app, text="⚙️", command=self.select_settings_button, font=('Helvetica', 12, 'bold'), bg=b'gray', fg='black')
        settings_button.place(x=385, y=10, width=50, height=50)

        reverse_button = tk.Button(self.app, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg='gray', fg='black')
        reverse_button.place(x=10, y=490, width=50, height=50)

        if self.current_language == 'tr':
            select_character_text = "Karakter Seçiniz"
        else:
            select_character_text = "Select Character"

        select_character_label = tk.Label(self.app, text=select_character_text, font=('Helvetica', 16, 'bold'), bg=bg_color, fg='black')
        select_character_label.pack(pady=10)

       
        if self.current_language == 'tr':
            player1_text = "1.Oyuncu"
        else:
            player1_text = "First Player"

        player1_label = tk.Label(self.app, text=player1_text, font=('Helvetica', 12, 'bold'), bg=bg_color, fg='black')
        player1_label.place(x=25, y=90)


        x_button = tk.Button(self.app, text="X", command=self.select_x, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=2, width=4)
        x_button.place(x=150, y=75)

        o_button = tk.Button(self.app, text="O", command=self.select_o, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=2, width=4)
        o_button.place(x=250, y=75)

        if self.current_language == 'tr':
            player2_text = "2.Oyuncu"
        else:
             player2_text = "Second Player"

        player2_label = tk.Label(self.app, text=player2_text, font=('Helvetica', 12, 'bold'), bg=bg_color, fg='black')
        player2_label.place(x=25, y=180)

        o_x_button = tk.Button(self.app, text="X/O", command=self.select_o_x, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=2, width=4)
        o_x_button.place(x=150, y=165)


        if self.current_language == 'tr':
            select_tour_text = "Tur Sayısını Seçiniz"
        else:
            select_tour_text = "Select Number of Tours"

        label = tk.Label(self.app, text=select_tour_text, font=('Helvetica', 16, 'bold'), bg=bg_color, fg='black')
        label.pack(pady=210) 

        one_button = tk.Button(self.app, text="1", command=self.select_one_button, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=2, width=4)
        one_button.place(x=30, y=330)
        
        three_button = tk.Button(self.app, text="3", command=self.select_three_button, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=2, width=4)
        three_button.place(x=140, y=330)
        
        five_button = tk.Button(self.app, text="5", command=self.select_five_button, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=2, width=4)
        five_button.place(x=250, y=330)
        
        eleven_button = tk.Button(self.app, text="11", command=self.select_eleven_button, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=2, width=4)
        eleven_button.place(x=360, y=330)

        if self.current_language == 'tr':
            play_text = "OYNA"
        else:
            play_text = "PLAY"
        play_button = tk.Button(self.app, text=play_text, command=self.select_play, font=('Helvetica', 12, 'bold'), bg='gray', fg='black', height=2, width=15)
        play_button.place(x=140, y=440)

        new_button.bind("<Enter>", self.on_enter)
        new_button.bind("<Leave>", self.on_leave)

        settings_button.bind("<Enter>", self.on_enter)
        settings_button.bind("<Leave>", self.on_leave)

        reverse_button.bind("<Enter>", self.on_enter)
        reverse_button.bind("<Leave>", self.on_leave)

        x_button.bind("<Enter>", self.on_enter)
        x_button.bind("<Leave>", self.on_leave)

        o_button.bind("<Enter>", self.on_enter)
        o_button.bind("<Leave>", self.on_leave)

        o_x_button.bind("<Enter>", self.on_enter)
        o_x_button.bind("<Leave>", self.on_leave)

        one_button.bind("<Enter>", self.on_enter)
        one_button.bind("<Leave>", self.on_leave)

        three_button.bind("<Enter>", self.on_enter)
        three_button.bind("<Leave>", self.on_leave)

        five_button.bind("<Enter>", self.on_enter)
        five_button.bind("<Leave>", self.on_leave)

        eleven_button.bind("<Enter>", self.on_enter)
        eleven_button.bind("<Leave>", self.on_leave)

        play_button.bind("<Enter>", self.on_enterm)
        play_button.bind("<Leave>", self.on_leavem)

    def on_enterm(self, event):
        event.widget.place_configure(width=155, height=55)  # Buton boyutunu artır

    def on_leavem(self, event):
        event.widget.place_configure(width=150, height=50)  # Buton boyutunu eski haline getir

    def on_enter(self, event):
        event.widget.place_configure(width=55, height=55)  # Buton boyutunu artır

    def on_leave(self, event):
        event.widget.place_configure(width=50, height=50)

    def play_sound(self):
        pygame.mixer.music.load("C:/Users/hasan/Desktop/Animasyon_deneme/Button.mp3")
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
        self.music = pygame.mixer.music.load(r"C:\Users\brr_c\OneDrive\Masaüstü\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\music2.mp3")
        pygame.mixer.music.play(-1)

    def toggle_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    
    def select_x(self):
        self.starting_symbol = "X"
        self.play_sound()

    def select_o(self):
        self.starting_symbol = "O"
        self.play_sound()

    def select_o_x(self):
        print("X or O selected")
        self.play_sound()

    def select_one_button(self):
        self.total_rounds = 1
        self.play_sound()
    
    def select_three_button(self):
        self.total_rounds = 3
        self.play_sound()
    
    def select_five_button(self):
        self.total_rounds = 5
        self.play_sound()

    def select_eleven_button(self):
        self.total_rounds = 11
        self.play_sound()

    def select_settings_button(self):
        pygame.mixer.music.stop()
        """Settings button click event."""
        # Multiplayer penceresini kapat
        self.app.destroy()
        # settings.py dosyasını aç
        subprocess.run(["python", "settings_multi.py"])
        self.play_sound()


    def select_reverse_button(self):
        pygame.mixer.music.stop()
        self.app.destroy()
        subprocess.run(["python", "main.py"])
        self.play_sound()

    def select_play(self):
        self.play_sound()
        if self.starting_symbol is None:
            messagebox.showerror("Error", "Please select a symbol.")
        elif self.total_rounds is None:
            messagebox.showerror("Error", "Please select the number of rounds.")
        else:
            self.app.destroy()
            
            if self.total_rounds == 1:
                tur_file = "tur_1.py"
            elif self.total_rounds == 3:
                tur_file = "tur_3.py"
            elif self.total_rounds == 5:
                tur_file = "tur_5.py"
            elif self.total_rounds == 11:
                tur_file = "tur_11.py"
            else:
                messagebox.showerror("Error", "Invalid number of rounds.")
                return

            tur_path = os.path.join(os.path.dirname(__file__), tur_file)
            subprocess.run(["python", tur_path, str(self.starting_symbol), str(self.total_rounds)], shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]
    app = MultiPlayer(root, language)
    root.mainloop()
