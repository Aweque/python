# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:02:37 2022

@author: Vasil
"""


import tkinter as tk
from tkinter import ttk


if __name__ == '__main__':
    root = tk.Tk()

    root.minsize(600, 300)
    root.title('Hobby House')
    root.option_add("*Font", 'Verdana 11')

    mainframe = ttk.Frame(root, padding="2 5 2 2")
    mainframe.pack(side=tk.BOTTOM, fill=tk.X)

    mainmenu = tk.Menu(mainframe)
    mainmenu.option_add("*Font", 'Verdana 11')
    root.config(menu=mainmenu)

    handbook_menu = tk.Menu(mainmenu, tearoff=0)
    handbook_menu.add_command(label="Студенти")
    handbook_menu.add_command(label="Хоббі")
    handbook_menu.add_command(label="Боббі")

    exit_menu = tk.Menu(mainmenu, tearoff=0)
    # .quit - close frame - do not stop root
    exit_menu.add_command(label="Закрити програму", command=root.destroy)  # root.quit

    mainmenu.add_cascade(label="Довідники", menu=handbook_menu)
    mainmenu.add_cascade(label="Вихід", menu=exit_menu)

    root.mainloop()
