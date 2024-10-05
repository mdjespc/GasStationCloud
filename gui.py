import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, scrolledtext

import os


class ProjectWindow:
    def __init__(self):
        self.callbacks = {}
        self._show_project_window()


    def _show_project_window(self):
        self.root = tk.Tk()
        self.root.title("Gas Station Cloud")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        #Application Icon
        icon_path = os.path.join("resources", "images", "icon.ico")
        self.root.iconbitmap(default = icon_path)

        #Background image
        background_image_path = os.path.join("resources", "images", "background.png")
        background_image = tk.PhotoImage(file = background_image_path)
        #Create a canvas to show the background image
        canvas = tk.Canvas(self.root)
        canvas.create_image(0, 0, image = background_image, anchor = tk.NW)
        canvas.grid(row = 0, column = 0)
        canvas.pack(fill = tk.BOTH, expand = True)
    

        
        #Create a  bar
        menubar = tk.Menu(self.root)
        self.root.config(menu = menubar)

        #Help menu
        help_menu = tk.Menu(menubar, tearoff = 0)


        #Connection management button
        self.database_connection_button = tk.Button(self.root, text = "Connect")


    def add_callbacks(self, key, method):
        '''
        This method makes connections, and lets the controller share its own methods
        to the view, and prevents the view from being dependent on the controller.
        This method will be used specifically by the controller
        '''
        self.callbacks[key] = method


    def run(self):
        self.root.mainloop()
