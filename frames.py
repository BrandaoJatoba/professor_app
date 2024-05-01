import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class HomePage(ttk.Frame):
    
    def __init__(self, container) -> None:
        super().__init__(container)

        self.config(width=1024, height=800)

        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.grid_rowconfigure(0, weight=1)
        self.label.grid_columnconfigure(0, weight=1)
        self.label.pack(side="top", fill="both", expand=True)

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

        # show the frame on the container
        self.pack()

    def button_clicked(self):
        messagebox.showinfo(title='Information', message='Hello, Tkinter!')

class Statistics(ttk.Frame):
    pass

class Schedule(ttk.Frame):
    pass

class NextEvents(ttk.Frame):
    pass