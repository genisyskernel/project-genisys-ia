# Class GUI #

# IMPORTS #
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from functions import ScreenCenter, DefaultColors

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        python_image = ImageTk.PhotoImage(file='../resources/banners/ImgPerfilProjeto2.png')
        ttk.Label(self, image=python_image).pack()



app = App()
app.mainloop()