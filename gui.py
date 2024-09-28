import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, scrolledtext

import os


class UserInterface:
    def __init__(self):
        #TODO set up controller when view is finished
        controller = None

        self.root = tk.Tk()
        self.root.title("Gas Station Cloud")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        #Application Icon
        icon_path = os.path.join("resources", "images", "icon.ico")
        self.root.iconbitmap(default = icon_path)
