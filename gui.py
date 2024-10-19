import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, scrolledtext
from PIL import Image, ImageTk
import os


class ProjectWindow:
    def __init__(self):
        self.callbacks = {}
        self._show_main_window()


    def _show_main_window(self):
        self.root = tk.Tk()
        self.root.title("Gas Station Cloud")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        #Application Icon
        icon_path = os.path.join("resources", "images", "icon.ico")
        self.root.iconbitmap(default = icon_path)

        #Background image
        background_image_path = os.path.join("resources", "images", "background.png")
        background_image = Image.open(background_image_path)
        background_image = ImageTk.PhotoImage(background_image)
        
        #Create a canvas to show the background image
        canvas = tk.Canvas(self.root)
        canvas.create_image(0, 0, image = background_image, anchor = tk.NW)
        canvas.grid(row = 0, column = 0, padx = 10, pady = 10)
    

        
        #Create a  bar
        menubar = tk.Menu(self.root)
        self.root.config(menu = menubar)

        #Help menu
        help_menu = tk.Menu(menubar, tearoff = 0)
        help_menu.add_command(label = "About", command = self._show_about_popup)
        menubar.add_cascade(label="Help", menu=help_menu)

        #Inventory management buttons
        self.create_button = tk.Button(self.root, text = "Insert to table")
        self.create_button.grid(row = 2, column = 5, padx = 10, pady = 10)

        self.filter_button = tk.Button(self.root, text = "Filter")
        self.filter_button.grid(row = 3, column = 5, padx = 10, pady = 10)

        self.edit_button = tk.Button(self.root, text = "Edit")
        self.edit_button.grid(row = 4, column = 5, padx = 10, pady = 10)

        self.delete_button = tk.Button(self.root, text = "Delete from table")
        self.delete_button.grid(row = 5, column = 5, padx = 10, pady = 10)

    
    def _show_about_popup(self):
        """Display an 'About' popup message."""
        about_text = "My Simple Application\nVersion 1.0"
        messagebox.showinfo("About", about_text)


    def add_callbacks(self, key, method):
        '''
        This method makes connections, and lets the controller share its own methods
        to the view, and prevents the view from being dependent on the controller.
        This method will be used specifically by the controller
        '''
        self.callbacks[key] = method


    def bind_commands(self):
        #List all buttons in the main window and bind them to a command
        pass


    def run(self):
        self.root.mainloop()
