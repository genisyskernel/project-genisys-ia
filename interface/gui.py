# Class GUI #

# IMPORTS #
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from functions import ScreenCenter, DefaultColors

# Program to draw concentric circles in Python Turtle
import turtle


class GUI:

    # FUNCTIONS #
    def __init__(self, master):

        ## MASTER ##

        self.master = master

        # Frame title #
        self.master.title("Genisys")

        # Frame icon #
        #self.master.iconbitmap("../package_resources/eltsistemas_icon01_original_256x256.ico")

        # Center screen #
        ScreenCenter.FrameCenter.center(self, 400, 400)

        # Disable frame maximize and minimize #
        self.master.resizable(0, 0)

        # -------------------------------------------------------------------------------------------------------------#

        # Containers #
        self.container_main = tk.Frame(self.master)

        # Widgets configurations #
        self.container_main['bg'] = DefaultColors.default_gui_color

        # Add widgets in frame #
        self.container_main.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        # -------------------------------------------------------------------------------------------------------------#


# START PROGRAM #
# Create frame #
root = tk.Tk()

# Set configurations to frame #
GUI(root)

# Start frame loop #
root.mainloop()

# END #