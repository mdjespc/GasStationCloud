import tkinter as tk
from tkinter import Label, Button, Entry, Listbox, Scrollbar
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

        #Inventory labels for the business metrics
        self.net_value_label = Label(self.root, text = "Net Value")
        self.net_value_label.grid(row = 0, column = 0)

        self.average_value_label = Label(self.root, text = "Average Value per Unit")
        self.average_value_label.grid(row = 1, column = 0)

        self.unit_count_label = Label(self.root, text = "Number of units in inventory")
        self.unit_count_label.grid(row = 2, column = 0)

        self.category_count_label = Label(self.root, text = "Number of categories")
        self.category_count_label.grid(row = 3, column = 0)


        #Inventory scrollable listbox
        self.inventory_listbox = Listbox(self.root)
        self.inventory_listbox.grid(row = 1, column = 1)
        self.inventory_listbox_scrollbar = Scrollbar(self.inventory_listbox)
        self.inventory_listbox_scrollbar.grid(row = 0 , column = 0)


        #Inventory management buttons
        self.create_button = Button(self.root, text = "Insert to table")
        self.create_button.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.filter_button = Button(self.root, text = "Filter")
        self.filter_button.grid(row = 1, column = 2, padx = 10, pady = 10)

        self.edit_button = Button(self.root, text = "Edit")
        self.edit_button.grid(row = 2, column = 2, padx = 10, pady = 10)

        self.delete_button = Button(self.root, text = "Delete from table")
        self.delete_button.grid(row = 3, column = 2, padx = 10, pady = 10)

    def show_insert_window(self, submit_product_details):
        insert_window = tk.Toplevel(self.root)
        insert_window.geometry("500x300")

        self.product_details = dict()

        product_name_label = Label(insert_window, text = "Product name: ")
        product_name_label.grid(row = 0, column = 0)
        product_name_entry = Entry(insert_window)
        product_name_entry.grid(row = 0, column = 2)
        product_name_entry.delete(0, tk.END)

        product_desc_label = Label(insert_window, text = "Product description: ")
        product_desc_label.grid(row = 1, column = 0)
        product_desc_entry = Entry(insert_window)
        product_desc_entry.grid(row = 1, column = 2)
        product_desc_entry.delete(0, tk.END)

        product_category_label = Label(insert_window, text = "Product category: ")
        product_category_label.grid(row = 2, column = 0)
        product_category_entry = Entry(insert_window)
        product_category_entry.grid(row = 2, column = 2)
        product_category_entry.delete(0, tk.END)

        product_price_label = Label(insert_window, text = "Product price: ")
        product_price_label.grid(row = 3, column = 0)
        product_price_entry = Entry(insert_window)
        product_price_entry.grid(row = 3, column = 2)
        product_price_entry.delete(0, tk.END)

        #Callback for submit button
        def get_entries():
            self.product_details = {
                "product_name" : product_name_entry.get(),
                "product_desc" : product_desc_entry.get(),
                "product_category" : product_category_entry.get(),
                "product_price" : float(product_price_entry.get())
            }
            submit_product_details()
            insert_window.destroy()

            #messagebox.showinfo("New Item", "New item has been added to the database.")
            

        submit_button = Button(insert_window, text="Submit", command = get_entries)
        submit_button.grid(row = 4, column = 1)

    
    def show_connection_error_popup(self):
        """Display a database connection error popup message"""
        error_text = "You are currently disconnected from the database."
        messagebox.showerror("Operation Unavailable", error_text)

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
        self.create_button.config(command = self.callbacks["Insert"])


    def run(self):
        self.root.mainloop()
