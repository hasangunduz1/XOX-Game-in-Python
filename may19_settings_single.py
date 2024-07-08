import tkinter as tk
from tkinter import messagebox
import os
import subprocess

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

        bg_color = '#ffffff'
        red_color ='#9A031E'
        black_color = '#212529'
        grey_color = '#8D99AE'
        self.app.configure(bg=bg_color)

        language_label = tk.Label(self.app, text="Language", font=('Helvetica', 16, 'bold'), bg=bg_color, fg=black_color)
        language_label.place(x=180, y=120)

        reverse_button = tk.Button(self.app, text="←", command=self.select_reverse_button, font=('Arial', 14, 'bold'), bg=black_color, fg='white', height=1, width=3)
        reverse_button.place(x=10, y=10)

        setting_button = tk.Button(self.app, text="SETTINGS", command=self.select_setting, font=('Helvetica', 12, 'bold'), bg=black_color, fg='white', height=2, width=45)
        setting_button.place(x=0, y=60)

        tr_button = tk.Button(self.app, text="TR", command=self.select_tr, font=('Helvetica', 12, 'bold'), bg=red_color, fg='white', height=2, width=6)
        tr_button.place(x=150, y=160)

        eng_button = tk.Button(self.app, text="ENG", command=self.select_eng, font=('Helvetica', 12, 'bold'), bg=grey_color, fg='white', height=2, width=6)
        eng_button.place(x=240, y=160)


        music_button = tk.Button(self.app, text="Music", command=self.select_music, font=('Helvetica', 12, 'bold'), bg=black_color, fg='white', height=2, width=15)
        music_button.place(x=150, y=230)

        generic_button = tk.Button(self.app, text="Generic", command=self.select_generic, font=('Helvetica', 12, 'bold'), bg=black_color, fg='white', height=2, width=15)
        generic_button.place(x=150, y=300)

        moods_button = tk.Button(self.app, text="Moods", command=self.select_moods, font=('Helvetica', 12, 'bold'), bg=black_color, fg='white', height=2, width=15)
        moods_button.place(x=150, y=370)
    

     def select_setting(self):
         """setting"""


     def select_music(self):
         
         self.app.destroy()
         subprocess.run(["python","may19_music.py"])

     def select_generic(self):
         """generic"""
    
     def select_tr(self):
          print("Dil Türkçe olarak ayarlandı.")
          self.language = 'tr'
          

     def select_eng(self):
          print("Dil İngilizce olarak ayarlandı.")
          self.language = 'en'
          

     def select_reverse_button(self):
          self.app.destroy()
          subprocess.run(["python", "may19_singleplayer.py", str(self.language)])

     def select_moods(self):
          self.app.destroy()
          subprocess.run(["python", "may19_moods.py"])


    

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsPage(root)
    root.mainloop()
