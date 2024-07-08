import tkinter as tk
import random
import os
import pygame

selected_character = None
selected_tour = None  # 
buttons = None

def select_x():
    global selected_character
    selected_character = "X"
    print("X selected")
    # Kullanıcı X karakterini seçtiğinde, bilgisayarın karakterini otomatik olarak ayarla
    set_computer_character()

def select_o():
    global selected_character
    selected_character = "O"
    print("O selected")
    # Kullanıcı O karakterini seçtiğinde, bilgisayarın karakterini otomatik olarak ayarla
    set_computer_character()

def set_computer_character():
    global selected_character
    global computer_character
    # Kullanıcının seçtiği karaktere göre bilgisayarın karakterini belirle
    if selected_character == "X":
        computer_character = "O"
    else:
        computer_character = "X"
    print(f"Computer selected: {computer_character}")



def select_one():
    global selected_tour
    selected_tour = 1
    print("1 tur Selected")

def select_three():
    global selected_tour
    selected_tour = 3
    print("3 tur Selected")

def select_five():
    global selected_tour
    selected_tour = 5
    print("5 tur Selected")

def select_eleven():
    global selected_tour
    selected_tour = 11
    print("11 tur Selected")

def rock_paper_scissors():
    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            print("Berabere!")
            # Berabere durumunda taş kağıt makas oyununu yeniden başlat
            rock_paper_scissors()
            return None  # Berabere
        elif (user_choice == "Taş" and computer_choice == "Makas") or \
            (user_choice == "Kağıt" and computer_choice == "Taş") or \
            (user_choice == "Makas" and computer_choice == "Kağıt"):
            print("Kullanıcı kazandı!")
            return "user"  # Kullanıcı kazandı
        else:
            print("Bilgisayar kazandı!")
            return "computer"  # Bilgisayar kazandı

    def user_choice_selected(choice):
        print(f"Kullanıcı seçimi: {choice}")
        computer_choices = ["Taş", "Kağıt", "Makas"]
        computer_choice = random.choice(computer_choices)
        print(f"Bilgisayar seçimi: {computer_choice}")
        winner = determine_winner(choice, computer_choice)
        # Kazanan belirlendiğinde, sadece kullanıcının kazanması durumunda hamle yap
        if winner == "user":
            # Kazanan belirlendiğinde, bilgisayarın kazandığı veya berabere kaldığı durumda hamle yap
            make_computer_move()
        
        # Kazanan belirlendiğinde taş kağıt makas penceresini kapat
        window.destroy()

    window = tk.Toplevel()
    window.title("Taş Kağıt Makas")

    label = tk.Label(window, text="Lütfen bir seçim yapın:", font=('Helvetica', 12, 'bold'))
    label.pack()

    choices = ["Taş", "Kağıt", "Makas"]
    for choice in choices:
        button = tk.Button(window, text=choice, font=('Helvetica', 12), command=lambda choice=choice: user_choice_selected(choice))
        button.pack(pady=5)

    window.wait_window(window)


def select_play():
    global selected_character
    global selected_tour
    global buttons
    global user_choice_selected

    if selected_character is None:
        print("Lütfen bir karakter seçin!")
        return

    if selected_tour is None:  
        print("Lütfen tur sayısını seçin!")
        return

    print(f"Oyun {selected_tour} tur oynanacak.")

    # Taş kağıt makas oyununu başlat
    rock_paper_scissors()

    # X-O-X oyununu başlat
    display_game_screen(selected_character)

    make_computer_move()


def mark_cell(row, col):
    global selected_character
    global buttons

    if selected_character is None:
        print("Lütfen bir karakter seçin!")
        return

    if buttons[row][col]["text"] == " " and not check_winner() and not is_board_full(): 
        buttons[row][col]["text"] = selected_character
        print(f"Cell ({row}, {col}) marked with {selected_character}")
        if not check_winner() and not is_board_full():  
            make_computer_move()
    else:
        print("Bu hücreye hamle yapılamaz!")

def make_computer_move():
    global buttons, computer_character

    if buttons is None:
        return  # Eğer buttons henüz tanımlanmamışsa, bu fonksiyonu sonlandır

    if not check_winner() and not is_board_full():
        # Öncelikle, kazanma durumunu kontrol et ve gerekirse kazanma hamlesini yap
        for i in range(3):
            for j in range(3):
                if buttons[i][j]["text"] == " ":
                    # Mevcut hücreyi geçici olarak işaretle
                    buttons[i][j]["text"] = computer_character
                    # Kazanma durumu kontrol et
                    if check_winner():
                        print(f"Computer marked Cell ({i}, {j}) to win")
                        return
                    # Kazanma durumu yoksa hücreyi geri al
                    buttons[i][j]["text"] = " "

        # Rakibin kazanma durumunu engelleme
        opponent_character = "O" if computer_character == "X" else "X"
        for i in range(3):
            for j in range(3):
                if buttons[i][j]["text"] == " ":
                    # Mevcut hücreyi geçici olarak rakibin karakteriyle işaretle
                    buttons[i][j]["text"] = opponent_character
                    # Rakibin kazanma durumu kontrol et
                    if check_winner():
                        # Rakibin kazanma durumunu engellemek için bu hücreye hamle yap
                        buttons[i][j]["text"] = computer_character
                        print(f"Computer marked Cell ({i}, {j}) to block opponent")
                        return
                    # Rakibin kazanma durumu yoksa hücreyi geri al
                    buttons[i][j]["text"] = " "

        # Köşeleri ve merkezi tercih etme
        corners_and_center = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]
        for corner in corners_and_center:
            if buttons[corner[0]][corner[1]]["text"] == " ":
                # Boş bir köşe veya merkez hücresi bulunduğunda hamle yap
                buttons[corner[0]][corner[1]]["text"] = computer_character
                print(f"Computer marked Cell ({corner[0]}, {corner[1]}) in corner or center")
                return

        # Önceden belirlenmiş stratejik hamleler yapılamazsa, rastgele bir hücreye hamle yap
        available_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]["text"] == " "]
        if available_cells:
            row, col = random.choice(available_cells)
            buttons[row][col]["text"] = computer_character
            print(f"Computer marked Cell ({row}, {col}) randomly")
        else:
            print("Oyun bitti!")


def check_winner():
    global buttons
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != " ":
            print(f"Kazanan: {buttons[i][0]['text']}")
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != " ":
            print(f"Kazanan: {buttons[0][i]['text']}")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ":
        print(f"Kazanan: {buttons[0][0]['text']}")
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ":
        print(f"Kazanan: {buttons[0][2]['text']}")
        return True
    return False

def is_board_full():
    global buttons
    for row in buttons:
        for button in row:
            if button["text"] == " ":
                return False
    return True

def display_game_screen(player_character):
    global buttons
    
    for widget in app.winfo_children():
        widget.destroy()

    
    game_board = tk.Frame(app, bg="white") 
    game_board.pack(pady=50)

    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(game_board, text=" ", font=('Helvetica', 20, 'bold'), fg='black', height=2, width=4, command=lambda i=i, j=j: mark_cell(i, j)) 
            button.grid(row=i, column=j, padx=5, pady=5)
            row.append(button)
        buttons.append(row)

app = tk.Tk()
app.title('SinglePlayer')

# Pygame'in başlatılması
pygame.init()

# Seçilen müziği saklamak için bir değişken
selected_music = None
# Müzik çalıyor mu?
music_playing = False
# Müziğin durumunu saklamak için bir değişken
music_state = "stopped"  # "stopped", "playing", "paused"
# Müzik ses seviyesi
music_volume = 0.5  # Default olarak yarısı

def open_settings():
    settings_window = tk.Toplevel(app)
    settings_window.title("Ayarlar")

    def go_back():
        settings_window.destroy()

    def play_pause_music():
        global selected_music, music_playing, music_state
        if selected_music:
            if music_playing:
                pygame.mixer.music.stop()  # Mevcut müziği durdur
                music_playing = False
                music_state = "stopped"
            else:
                pygame.mixer.music.load(selected_music)
                pygame.mixer.music.set_volume(music_volume)  # Ses seviyesini ayarla
                pygame.mixer.music.play(-1)  # Müziği sürekli çal
                music_playing = True
                music_state = "playing"

    def select_music():
        global selected_music
        selected_music = os.path.join("music", music_listbox.get(tk.ACTIVE))
        play_button["state"] = "normal"

    def change_volume(value):
        global music_volume
        music_volume = float(value) / 100  # Scale değerini 0.0 ile 1.0 arasına dönüştür
        if music_playing:
            pygame.mixer.music.set_volume(music_volume)  # Müzik çalıyorsa ses seviyesini ayarla

    back_button = tk.Button(settings_window, text="Geri", command=go_back, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white')
    back_button.pack()

    music_listbox = tk.Listbox(settings_window, font=('Helvetica', 12))
    music_listbox.pack(pady=10)

    music_files = os.listdir("music")
    for music_file in music_files:
        music_listbox.insert(tk.END, music_file)

    select_button = tk.Button(settings_window, text="Müzik Seç", command=select_music, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white')
    select_button.pack(pady=5)

    play_button = tk.Button(settings_window, text="Oynat/Durdur", command=play_pause_music, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white', state="disabled")
    play_button.pack(pady=5)

    # Ses seviyesini değiştirmek için bir Scale oluştur
    volume_scale = tk.Scale(settings_window, from_=0, to=100, orient=tk.HORIZONTAL, command=change_volume, font=('Helvetica', 12, 'bold'))
    volume_scale.set(50)  # Varsayılan değer yarısı
    volume_scale.pack(pady=5)

# Ayarlar butonunu eklemek için bir tkinter Button widget'i oluştur ve sol üst köşeye yerleştir
settings_button = tk.Button(app, text="Ayarlar", command=open_settings, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white')
settings_button.place(x=20, y=20)

window_width = 450
window_height = 550
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
app.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
app.resizable(False,False)


bg_color = '#140B69'
app.configure(bg=bg_color)


player1_label = tk.Label(app, text="Player 1", font=('Helvetica', 18, 'bold'), bg=bg_color, fg='white')
player1_label.pack(pady=10)


select_character_label= tk.Label(app, text="Select Character", font=('Helvetica', 15, 'bold'), bg=bg_color, fg='white').place(x=25, y=120)

x_button = tk.Button(app, text="X", command=select_x, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white', height=2, width=4).place(x=220,y=105)

o_button = tk.Button(app, text="O", command=select_o, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white', height=2, width=4).place(x=300,y=105)

label = tk.Label(app, text="Select Number of Tours", font=('Helvetica', 16, 'bold'), bg=bg_color, fg='white')
label.pack(pady=160) 

one_button = tk.Button(app, text="1", command=select_one, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white', height=2, width=4).place(x=30,y=300)
three_button = tk.Button(app, text="3", command=select_three, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white', height=2, width=4).place(x=140,y=300)
five_button = tk.Button(app, text="5", command=select_five, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white', height=2, width=4).place(x=250,y=300)
eleven_button = tk.Button(app, text="11", command=select_eleven, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white', height=2, width=4).place(x=360,y=300)

play_button = tk.Button(app, text="PLAY", command=select_play, font=('Helvetica', 12, 'bold'), bg='#EF802F', fg='white', height=2, width=15).place(x=140,y=440)

app.mainloop()