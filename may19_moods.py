import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys


class Moods:
    def __init__(self, root, language=None):
        self.root = root
        self.app = root
        self.app.title('Moods')

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
        black_color = '#212529'
        self.app.configure(bg=bg_color)

        reverse_button = tk.Button(self.app, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg=black_color, fg='white', height=1, width=3)
        reverse_button.place(x=10, y=10)

        label = tk.Label(self.app, text="Select Mode", font=('Helvetica', 20, 'bold'), bg=bg_color, fg=black_color)
        label.place(x=150,y=45)

        logo_image = Image.open(r"C:\Users\hasan\Desktop\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\xox_logo.png")
        logo_image = logo_image.resize((150, 150))
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        logo_button = tk.Button(self.app, image=self.logo_photo,command=self.select_normal, bg=bg_color)
        logo_button.place(x=50, y=150)

        logo2_image = Image.open(r"C:\Users\hasan\Desktop\HasanGündüz_BerraÇelik_EngineeringProject_SecondJury\19May_Tic-Tac-Toe.png")
        logo2_image = logo2_image.resize((150, 150))
        self.logo2_photo = ImageTk.PhotoImage(logo2_image)

        logo2_button = tk.Button(self.app, image=self.logo2_photo,command=self.select_may19, bg=bg_color)
        logo2_button.place(x=250, y=150)
    
    def select_normal(self):
        self.app.destroy()

        subprocess.run(["python","main.py"])

    def select_may19(self):
        self.app.destroy()

        subprocess.run(["python","may19_main.py"])

    def select_reverse_button(self):
        
        self.app.destroy()
        
        subprocess.run(["python", "may19_settings.py"])

if __name__ == "__main__":
    root = tk.Tk()
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]
    app = Moods(root, language)
    root.mainloop()