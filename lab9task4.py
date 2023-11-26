"""
Написать GUI приложение, которое представляет собой
упрощенный файловый менеджер, с возможностью создания,
удаления и переименования директорий и файлов.
"""

from tkinter import *
import os
from pathlib import Path
window = Tk()
window.title("Файловый менеджер")
window.geometry('800x110')
entry = Entry(window, width=70)
entry.place(x=350, y=30)
entrylabel = Label(text="Полный путь создаваемого/удаляемого/переименовываемого файла/папки")
entrylabel.place(x=350, y=5)
entry2 = Entry(window, width=70)
entry2.place(x=350, y=80)
entry2label = Label(text="Название, НА которое переименовывается файл/папка, полный путь")
entry2label.place(x=350, y=55)


def create_file_click():
    my_file=open(entry.get(), "w+")
    my_file.close()

def create_folder_click():
    os.mkdir(entry.get())

def rename_click():
    p=Path(entry.get())
    target=Path(entry2.get())
    p.rename(target)

def delete_folder_click():
    os.rmdir(entry.get())

def delete_file_click():
    os.remove(entry.get())



create_file= Button (window, text="Создать файл", command = create_file_click)
create_file.place(x=15, y=15)
rename_file=Button(window, text="Переименовать", command = rename_click)
rename_file.place(x=220, y=15)
delete_file=Button(window, text="Удалить файл", command = delete_file_click)
delete_file.place(x=115, y=15)
create_dir=Button(window, text="Создать папку", command = create_folder_click)
create_dir.place(x=15, y=65)
delete_dir=Button(window, text="Удалить папку", command = delete_folder_click)
delete_dir.place(x=115, y=65)

window.mainloop()
