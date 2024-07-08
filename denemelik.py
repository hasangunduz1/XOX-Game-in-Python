import tkinter as tk
import sys
from PIL import Image, ImageTk

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

        # Arka plan resmini yükle
        bg_image = Image.open("C:/Users/brr_c/OneDrive/Masaüstü/HasanGündüz_BerraÇelik_EngineeringProject_FirstJury/arcade_2.png")
        bg_image = bg_image.resize((window_width, window_height), Image.BILINEAR)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Arka plan etiketini oluştur ve yerleştir
        self.bg_label = tk.Label(self.app, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

if __name__ == "__main__":
    root = tk.Tk()
    language = None
    if len(sys.argv) > 1:
        language = sys.argv[1]
    app = Main(root, language)
    root.mainloop()
