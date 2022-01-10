## mainwindow.py
'''
This code creates and displays the application top window frame
'''

from tkinter import *
from tkinter import ttk
import tkinter

class MainWindow:
    def __init__(self):
        mainWindow = tkinter.Tk()
        print("an output")

        mainWindowFrame = ttk.Frame(mainWindow, padding=10)
        mainWindowFrame.grid()
        ttk.Label(mainWindowFrame, text="Olá Mundo! =D").grid(column=0, row=0)
        ttk.Button(mainWindowFrame, text="Quit", command=mainWindow.destroy).grid(column=1, row=0)

        self.mainWindow = mainWindow

    def startWindow(self):
        self.mainWindow.mainloop()