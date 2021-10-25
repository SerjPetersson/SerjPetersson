import csv
from tkinter import *
import requests
import codecs
from contextlib import closing
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import filedialog


root=Tk()
root['bg'] = '#3f6565'
root.title('Обнаруженные экзопланеты') 
root.resizable(True, True)
root.geometry('800x500')
TableMargin = Frame(root, width=400)
TableMargin.pack(expand=True)

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Название","Статус", "Радиус(Юпитера)", "Дата обнаружения", "Дата обновления информации" ), height=200, selectmode="extended",
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y, expand=True)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X, expand=True)



tree.heading('Название', text="Название", anchor=W)
tree.heading('Статус', text="Статус", anchor=W)
tree.heading('Радиус(Юпитера)', text="Радиус(Юпитера)", anchor=W)
tree.heading('Дата обнаружения', text="Дата обнаружения", anchor=W)
tree.heading('Дата обновления информации', text="Дата обновления информации", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=150)
tree.column('#2', stretch=NO, minwidth=0, width=250)
tree.column('#3', stretch=NO, minwidth=0, width=170)
tree.column('#4', stretch=NO, minwidth=0, width=170)
tree.column('#5', stretch=NO, minwidth=0, width=180)
tree.pack()

exofile="http://exoplanet.eu/catalog/csv"

with closing(requests.get(exofile, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
    next(reader)
    for row in reader:
        name = row[0]
        status = row[1]
        radius = row[8]
        date1 = row[24]
        date2 = row[25]
        
        tree.insert("", 0, values=(name,status,radius,date1,date2))


def about_us():
                tkinter.messagebox.showinfo('Информация об экзопланетах', 'Программа написана на Python')

menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Помощь", menu=subMenu)
subMenu.add_command(label="О программе", command=about_us)
        

root.mainloop()        
