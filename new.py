import tkinter as tk
from time import *
import customtkinter as ctk
import time 
import tkinter.messagebox
import configparser
from tkinter import filedialog

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class AppWindow(ctk.CTk):
    def __init__(self,title,size):
        # creating main window skeleton
        super().__init__()
        self.size = 
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.maxsize(size[0], size[1])
        #self.eval('tk::PlaceWindow . center')
        #self.after(0, lambda:AppWindow.state('zoomed'))
        
        # adding instances of classes
        self.tabview = TabView(self)
        
        
        # ensuring the app actually runs
        self.mainloop()
        

class TabView(ctk.CTkTabview):
    def __init__(self ,parent):
        super().__init__(parent)
        self.pack(pady=0, padx=0, fill="both", expand=True)
        self.add("Main Office")
        self.add("Middle Office")
        self.add("Back Office")
        self.add("Datoteka")
        
AppWindow("Tablica",(1920,1080))