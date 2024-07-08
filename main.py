import time
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
import threading
import pygame
import imageio
import time

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

        

        logo_image = Image.open(r"C:\Users\brr_c\OneDrive\Masaüstü\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\xox_logo.png")
        logo_image = logo_image.resize((300, 300))
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(self.app, image=self.logo_photo, bg=bg_color)
        logo_label.pack(expand=True, pady=5)

        button_frame = tk.Frame(self.app, bg=bg_color)
        button_frame.pack(expand=True)

        # Pygame'in başlatılması
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
        new_button.place(x=325, y=10, width=50, height=50)

        settings_button = tk.Button(self.app, text="⚙️", command=self.settings_click, font=('Helvetica', 12, 'bold'), bg='gray', fg='black')
        settings_button.place(x=390, y=10, width=50, height=50)

        if self.current_language == 'tr':
            singleplayer_text = "Tek Oyunculu"
            multiplayer_text = "Çok Oyunculu"
        else:
            singleplayer_text = "Singleplayer"
            multiplayer_text = "Multiplayer"
            patica_text ='Arcade'

        self.button1 = tk.Button(self.app, text=singleplayer_text, command=self.singleplayer_click, font=('Helvetica', 12, 'bold'), bg='gray', fg='black')
        self.button1.place(x=150, y=300, width=150, height=50)  # Butonun yerini ayarlayın

        self.button2 = tk.Button(self.app, text=multiplayer_text, command=self.multiplayer_click, font=('Helvetica', 12, 'bold'), bg='gray', fg='black')
        self.button2.place(x=150, y=360, width=150, height=50)  # Butonun yerini ayarlayın

        self.button2 = tk.Button(self.app, text=patica_text, command=self.patica_click, font=('Helvetica', 12, 'bold'), bg='gray', fg='black')
        self.button2.place(x=150, y=420, width=150, height=50)  # Butonun yerini ayarlayın

        # Butonlara fare olaylarını bağla
        self.button1.bind("<Enter>", self.on_enterm)
        self.button1.bind("<Leave>", self.on_leavem)

        self.button2.bind("<Enter>", self.on_enterm)
        self.button2.bind("<Leave>", self.on_leavem)

        settings_button.bind("<Enter>", self.on_enter)
        settings_button.bind("<Leave>", self.on_leave)

        new_button.bind("<Enter>", self.on_enter)
        new_button.bind("<Leave>", self.on_leave)

        self.rules_button = tk.Button(self.app, text="?", bg=bg_color, fg="white", command=self.open_rule, relief=tk.FLAT)
        self.rules_button.place(relx=0.98, rely=0.98, anchor='se')  

        self.font_size = 12
        self.font_direction = 1
        self.animate_font()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        
        

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

    def animate_font(self):
        self.font_size += self.font_direction
        if (self.font_size > 16):
            self.font_direction = -1
        elif (self.font_size < 12):
            self.font_direction = 1
        self.rules_button.config(font=("Arial", self.font_size))
        self.app.after(100, self.animate_font)

    def open_rule(self):
        self.app.destroy()
        subprocess.run(["python", "rule.py"])

    def load_music(self):
        self.music = pygame.mixer.music.load(r"C:\Users\brr_c\OneDrive\Masaüstü\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\music.mp3")
        pygame.mixer.music.play(-1)

    def toggle_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def singleplayer_click(self, event=None):
        pygame.mixer.music.stop()
        print("Tek oyunculu başlatılıyor...")
        self.app.destroy()
        subprocess.run(["python", "singleplayer2.py", str(self.current_language)])
        self.play_sound()

    def patica_click(self, event=None):
        pygame.mixer.music.stop()
        print("Tek oyunculu başlatılıyor...")
        self.app.destroy()
        subprocess.run(["python", "level_main.py", str(self.current_language)])
        self.play_sound()

    def multiplayer_click(self, event=None):
        pygame.mixer.music.stop()
        print("Çok oyunculu başlatılıyor...")
        self.app.destroy()
        subprocess.run(["python", "multiplayer.py", str(self.current_language)])
        self.play_sound()

    def settings_click(self):
        pygame.mixer.music.stop()
        self.app.destroy()
        subprocess.run(["python", "settings.py", str(self.current_language)])
        self.play_sound()

    def on_closing(self):
        pygame.mixer.music.stop()
        self.root.destroy()

    def on_enterm(self, event):
        event.widget.place_configure(width=155, height=55)  # Buton boyutunu artır

    def on_leavem(self, event):
        event.widget.place_configure(width=150, height=50)  # Buton boyutunu eski haline getir
        
    def on_enter(self, event):
        event.widget.place_configure(width=55, height=55)  # Buton boyutunu artır

    def on_leave(self, event):
        event.widget.place_configure(width=50, height=50) 

    

if __name__ == "__main__":
    root = tk.Tk()
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]
    app = Main(root, language)
    root.mainloop()
