import tkinter as tk
from PIL import Image, ImageTk
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

        bg_color = '#FFFFFF'
        red_color ='#9A031E'
        black_color = '#212529'
        grey_color = '#8D99AE'
        self.app.configure(bg=bg_color)

        logo_image = Image.open(r"C:\Users\hasan\Desktop\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\19May_Tic-Tac-Toe.png")
        logo_image = logo_image.resize((300, 300))
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        baloons_image = Image.open(r"C:\Users\hasan\Desktop\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\19may.png")
        baloons_image = baloons_image.resize((int(baloons_image.width * 0.15), int(baloons_image.height * 0.15)))

        self.baloons_photo = ImageTk.PhotoImage(baloons_image)

        logo_label = tk.Label(self.app, image=self.logo_photo, bg=bg_color)
        logo_label.pack(expand=True, pady=5)

        baloons_label = tk.Label(self.app, image=self.baloons_photo, bg=bg_color)
        baloons_label.place(x=5,y=5)

        #baloons2_label = tk.Label(self.app, image=self.baloons_photo, bg=bg_color)
        #baloons2_label.place(x=150, y=0)

        #baloons3_label = tk.Label(self.app, image=self.baloons_photo, bg=bg_color)
        #baloons3_label.place(x=280, y=0)



        button_frame = tk.Frame(self.app, bg=bg_color)
        button_frame.pack(expand=True)

        settings_button = tk.Button(self.app, text="⚙️", command=self.settings_click, font=('Helvetica', 12, 'bold'), bg='#8D99AE', fg='black', height=1, width=2)
        settings_button.place(x=410, y=10)

        singleplayer_button_config = {'height': 2, 'width': 18, 'bg': '#212529', 'fg': 'white', 'font': ('Helvetica', 12, 'bold')}
        multiplayer_button_config = {'height': 2, 'width': 18, 'bg': '#9A031E', 'fg': 'white', 'font': ('Helvetica', 12, 'bold')}

        if self.current_language == 'tr':
            singleplayer_text = "Tek Oyunculu"
        else:
            singleplayer_text = "Singleplayer"

        singleplayer_button = tk.Button(button_frame, text=singleplayer_text, command=self.singleplayer_click, **singleplayer_button_config)
        singleplayer_button.grid(row=0, pady=5)

        if self.current_language == 'tr':
            multiplayer_text = "Çok Oyunculu"
        else:
            multiplayer_text = "Multiplayer"

        multiplayer_button = tk.Button(button_frame, text=multiplayer_text, command=self.multiplayer_click, **multiplayer_button_config)
        multiplayer_button.grid(row=1, pady=5)

        self.button = tk.Button(self.app, text="?", bg=bg_color, fg=black_color, command=self.open_rule, relief=tk.FLAT)
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

    def open_rule(self):
        self.app.destroy()
        
        subprocess.run(["python", "may19_rule.py"])

    def singleplayer_click(self):
        print("Singleplayer başlatılıyor...")
        self.app.destroy()
        subprocess.run(["python", "may19_singleplayer.py",str(self.current_language)])

    def multiplayer_click(self):
        print("Multiplayer başlatılıyor...")
        self.app.destroy()
        subprocess.run(["python", "may19_multiplayer.py",str(self.current_language)])

    def settings_click(self):
        self.app.destroy()
        subprocess.run(["python", "may19_settings.py", str(self.current_language)])

if __name__ == "__main__":
    root = tk.Tk()
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]
    app = Main(root, language)
    root.mainloop()

