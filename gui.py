import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from mutagen.mp3 import MP3
import threading
import time
from pygame import mixer
import os
from ttkthemes import themed_tk as tk
from tkinter import ttk

root = tk.ThemedTk()
root.get_themes()
root.set_theme("keramik")

statusbar = ttk.Label(root, text="Музыкальный проигрыватель", relief=SUNKEN, anchor=W, font='Times 16  bold italic')
statusbar.pack(side=BOTTOM, fill=X)

menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)
playlist = []

def browse_file(): 
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)
    
def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1

menubar.add_cascade(label="Файл", menu=subMenu)
subMenu.add_command(label="Открыть", command=browse_file)
subMenu.add_command(label="Выход", command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo('О программе', 'Это приложение сделано на Python')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Помощь", menu=subMenu)
subMenu.add_command(label="О нас", command=about_us)

mixer.init()

root.geometry('500x500')
root.title("Музыкальный проигрыватель")
root.iconbitmap(r'music.ico')

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30)

playlistbox = Listbox(leftframe)
playlistbox.pack()

addbtn = ttk.Button(leftframe, text="+ Добавить", command=browse_file)
addbtn.pack(side=LEFT)

def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)

delbtn = ttk.Button(leftframe, text="- Удалить", command=del_song)
delbtn.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack()

topframe = Frame(rightframe)
topframe.pack()

lengthlabel = ttk.Label(topframe, text='Общая продолжительность : --:--')
lengthlabel.pack(pady=5)

currenttimelabel = ttk.Label(topframe, text='Текущее состояние : --:--', relief=GROOVE)
currenttimelabel.pack()

text=Label(root, text='Включите музыку')
text.pack(pady=10)




def show_details(play_song):
    
    file_data = os.path.splitext(play_song)

    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()

    
    mins,secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Общая продолжительность" + ' - ' + timeformat
    
    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


def start_count(t):
    global paused
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Текущее состояние" + ' - ' + timeformat
            time.sleep(1)
            current_time += 1

def play_btn():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Воспроизведение продолжено"
        paused = FALSE
    else:
        try:
            stop_btn()
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text'] = "Сейчас играет" + ' - ' + os.path.basename(play_it)
            show_details(play_it)
        except:
            tkinter.messagebox.showerror('Файл не найден', 'Приложение не нашло этот файл')
     
def rewind_music():
    play_btn()
    statusbar['text'] = "Музыка перемотана"

paused=FALSE

def pause_btn():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Воспроизведение приостановлено"


def stop_btn():
    mixer.music.stop()
    statusbar['text'] = "Воспроизведение остановлено"




def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

muted = FALSE


def mute_music():
    global muted
    if muted:  
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = FALSE
    else:  
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE

photo=PhotoImage(file='play.png')
photo1=PhotoImage(file='stop.png')
photo2=PhotoImage(file='pause.png')


middleframe = Frame(root)
middleframe.pack(pady=30,padx=30)

btn=ttk.Button(middleframe, image=photo,command=play_btn)
btn.grid(row=0, column=0, padx=10)
btn1=ttk.Button(middleframe, image=photo1,command=stop_btn)
btn1.grid(row=0, column=1, padx=10)
btn2 = ttk.Button(middleframe, image=photo2, command=pause_btn)
btn2.grid(row=0, column=2, padx=10)


scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack(pady=15)



bottomframe = Frame(root)
bottomframe.pack()

rewindPhoto = PhotoImage(file='rewind.png')
rewindBtn = ttk.Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindBtn.pack()

mutePhoto = PhotoImage(file='mute.png')
volumePhoto = PhotoImage(file='volume.png')
volumeBtn = Button(bottomframe, image=volumePhoto, command=mute_music)
volumeBtn.pack()

def on_closing():
    stop_btn()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
