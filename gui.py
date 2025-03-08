import tkinter as tk
from tkinter import Label, Button, Entry, Text, Listbox, Scrollbar
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
        self.root.geometry("435x500")
        self.root.resizable(True, True)

        self.text_font = ("comfortaa", 9)

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
        canvas.grid(row = 0, column = 0, padx = 10, pady = 10, rowspan= 4, columnspan=4)
    

        
        #Create a  bar
        menubar = tk.Menu(self.root)
        self.root.config(menu = menubar)

        #Help menu
        help_menu = tk.Menu(menubar, tearoff = 0)
        help_menu.add_command(label = "About", command = self._show_about_popup)
        menubar.add_cascade(label="Help", menu=help_menu)

        #Inventory labels for the business metrics
        # self.net_value_label = Label(self.root, text = "Net Value")
        # self.net_value_label.grid(row = 0, column = 0)

        # self.average_value_label = Label(self.root, text = "Average Value per Unit")
        # self.average_value_label.grid(row = 1, column = 0)

        # self.unit_count_label = Label(self.root, text = "Number of units in inventory")
        # self.unit_count_label.grid(row = 2, column = 0)

        # self.category_count_label = Label(self.root, text = "Number of categories")
        # self.category_count_label.grid(row = 3, column = 0)


        #Inventory scrollable listbox
        self.inventory_listbox = Listbox(self.root,
                                         width=50,
                                         height=20,
                                         bd=7,
                                         font=self.text_font,
                                         highlightcolor="#60db81",
                                         highlightbackground="#60db81", 
                                         highlightthickness=10,                                                              
                                         selectbackground="#119634",
                                         relief="flat"
                                         )
        self.inventory_listbox.grid(row = 1, column = 0, rowspan=4, columnspan=4, padx = 25, pady = 15)
        #Bind the selection event
        self.inventory_listbox.bind("<<ListboxSelect>>", self.on_listbox_select)
        self.selected_item_id = None
        self.selected_item = None

        #self.inventory_listbox_scrollbar = Scrollbar(self.inventory_listbox)
        #self.inventory_listbox_scrollbar.grid(row = 0 , column = 0)
        


        #Inventory management buttons
        self.create_button = Button(self.root, text = "Insert to table", font=self.text_font, bg="#107d60", fg="#ffffff")
        self.create_button.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.filter_button = Button(self.root, text = "Filter", font=self.text_font, bg="#107d60", fg="#ffffff")
        self.filter_button.grid(row = 0, column = 1)

        self.edit_button = Button(self.root, text = "Edit", font=self.text_font, bg="#107d60", fg="#ffffff")
        self.edit_button.grid(row = 0, column = 2)

        self.delete_button = Button(self.root, text = "Delete from table", font=self.text_font, bg="#7d1b10", fg="#ffffff")
        self.delete_button.grid(row = 0, column = 3)

    # Function to handle item selection
    def on_listbox_select(self, event):
        selection = self.inventory_listbox.curselection()
        if selection:
            index = selection[0]
            self.selected_item = self.inventory_listbox.get(index)
            self.selected_item_id = int(self.selected_item.split(",")[0])
            print("Selected:", self.selected_item)
            print("ID: ", self.selected_item_id)
            

    def update_inventory_listbox(self, items):
        self.inventory_listbox.delete(0, tk.END)
        for item in items:
            self.inventory_listbox.insert(tk.END, item)


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


        product_quantity_label = Label(insert_window, text = "Quantity: ")
        product_quantity_label.grid(row = 4, column = 0)
        product_quantity_entry = Entry(insert_window)
        product_quantity_entry.grid(row = 4, column = 2)
        product_quantity_entry.delete(0, tk.END)
        product_quantity_entry.insert(0, "1")
        

        #Callback for submit button
        def get_entries():
            self.product_details = {
                "product_name" : product_name_entry.get(),
                "product_desc" : product_desc_entry.get(),
                "product_category" : product_category_entry.get(),
                "product_price" : float(product_price_entry.get()),
                "product_quantity" : int(product_quantity_entry.get())
            }
            submit_product_details()
            insert_window.destroy()

            #messagebox.showinfo("New Item", "New item has been added to the database.")
            

        submit_button = Button(insert_window, text="Submit", command = get_entries)
        submit_button.grid(row = 6, column = 1)

    
    def show_update_window(self, submit_product_details):
        if not self.selected_item:
            print("Item must be selected before performing the EDIT button.")
            return

        update_window = tk.Toplevel(self.root)
        update_window.geometry("500x300")

        self.product_details = dict()
        product_name, product_desc, product_category, product_price = self.selected_item.split(",")[1:]


        product_name_label = Label(update_window, text = "Product name: ")
        product_name_label.grid(row = 0, column = 0)
        product_name_entry = Entry(update_window)
        product_name_entry.grid(row = 0, column = 2)
        product_name_entry.delete(0, tk.END)
        product_name_entry.insert(0, product_name)

        product_desc_label = Label(update_window, text = "Product description: ")
        product_desc_label.grid(row = 1, column = 0)
        product_desc_entry = Entry(update_window)
        product_desc_entry.grid(row = 1, column = 2)
        product_desc_entry.delete(0, tk.END)
        product_desc_entry.insert(0, product_desc)

        product_category_label = Label(update_window, text = "Product category: ")
        product_category_label.grid(row = 2, column = 0)
        product_category_entry = Entry(update_window)
        product_category_entry.grid(row = 2, column = 2)
        product_category_entry.delete(0, tk.END)
        product_category_entry.insert(0, product_category)

        product_price_label = Label(update_window, text = "Product price: ")
        product_price_label.grid(row = 3, column = 0)
        product_price_entry = Entry(update_window)
        product_price_entry.grid(row = 3, column = 2)
        product_price_entry.delete(0, tk.END)
        product_price_entry.insert(0, product_price)

        #Callback for submit button
        def get_entries():
            self.product_details = {
                "id" : str(self.selected_item_id),
                "product_name" : product_name_entry.get(),
                "product_desc" : product_desc_entry.get(),
                "product_category" : product_category_entry.get(),
                "product_price" : str(product_price_entry.get()),
            }
            submit_product_details()
            update_window.destroy()
            

        submit_button = Button(update_window, text="Submit", command = get_entries)
        submit_button.grid(row = 6, column = 1)

    def show_filter_window(self, submit_filter_settings):
        '''
        -The "Filter by name" entry searches in both item name and item desc categories
        -Category should be a single word (or drop-down menu)
        -Price value should be a range with a minimum and maximum value (can be a slider)

        Once the user enters "Submit", return a dictionary to the controller with all filter settings.
        Run the appropriate query for all filter settings selected (multi-functional query that works for all columns in DB)
        Display the search results by passing them on to the "update_inventory_listbox" method
        '''
        filter_window = tk.Toplevel(self.root)
        filter_window.geometry("500x300")

        self.filter_settings = dict()

        name_filter_label = Label(filter_window, text = "Filter by name:")
        name_filter_label.grid(row=0, column=0)
        name_filter_entry = Entry(filter_window)
        name_filter_entry.grid(row=0, column=1)
        name_filter_entry.delete(0, tk.END)

        category_filter_label = Label(filter_window, text = "Filter by category:")
        category_filter_label.grid(row=1, column=0)
        category_filter_entry = Entry(filter_window)
        category_filter_entry.grid(row=1, column=1)
        category_filter_entry.delete(0, tk.END)

        price_filter_label = Label(filter_window, text = "Filter by price:")
        price_filter_label.grid(row = 2, column = 0)
        min_price_label = Label(filter_window, text = "Min:")
        min_price_label.grid(row=3, column = 0)
        min_price_entry = Entry(filter_window)
        min_price_entry.grid(row=3, column=1)
        min_price_entry.delete(0, tk.END)
        max_price_label = Label(filter_window, text = "Max:")
        max_price_label.grid(row=3, column = 2)
        max_price_entry = Entry(filter_window)
        max_price_entry.grid(row=3, column=3)
        name_filter_entry.delete(0, tk.END)

        #Callback for submit button
        #TODO Validate user input (needs to be formatted as a float, but passed on as a string)
        def get_entries():
            self.filter_settings = {
                "name_filter" : name_filter_entry.get(),
                "desc_filter" : name_filter_entry.get(),
                "category_filter" : category_filter_entry.get(),
                "min_price_filter" : min_price_entry.get(),
                "max_price_filter" : max_price_entry.get()
            }

            submit_filter_settings()
            filter_window.destroy()

        submit_button = Button(filter_window, text="Filter", command = get_entries)
        submit_button.grid(row = 4, column = 1)

    def show_delete_window(self, matching_items, submit_delete_settings):
        '''
        Give option to delete single selected item, or similar items by percentage or amount.
        '''
        if not self.selected_item:
            print("Item must be selected before performing the DELETE operation.")
            return

        delete_window = tk.Toplevel(self.root)
        delete_window.geometry("500x300")

        matching_item_count = len(matching_items)
        info_message = f'''There are {matching_item_count} similar items in the database. 

        Select the amount or percentage of similar items you 
        would like to DELETE, or leave the fields below empty to DELETE a single item.
        '''
        info_label = Label(delete_window, text = info_message)
        info_label.grid(row=0, column=0, padx=20, pady=20)



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
        self.delete_button.config(command = self.callbacks["Delete"])
        self.edit_button.config(command = self.callbacks["Update"])
        self.filter_button.config(command = self.callbacks["Filter"])


    def run(self):
        self.root.mainloop()
