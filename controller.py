from model.client import Client
from model.item import Item
from gui import ProjectWindow


class Controller(object):
    def __init__(self):
        self.view = ProjectWindow()
        self.client = Client()
        self.client.connect_to_database()
        
        #Add callbacks
        self.view.add_callbacks("Insert", self.insert_button_pressed)
        self.view.add_callbacks("Delete", self.delete_button_pressed)

        #Bind command
        self.view.bind_commands()

        #Insert items into listbox
        items = self.fetch_inventory()
        self.view.update_inventory_listbox(items)

        self.view.run()
    

    def fetch_inventory(self):
        items = self.client.fetch_all("inventory")

        #Process the fetched items into a list of strings
        items = [",".join([str(value) for value in item]) for item in items]
        return items


    def insert_button_pressed(self):
        self.view.show_insert_window(self.submit_product_details)
        
        
    def submit_product_details(self):
        #Once the window is closed, grab all values entered and submit to client
        product_details = self.view.product_details
        product_name = product_details["product_name"]
        product_desc = product_details["product_desc"]
        product_category = product_details["product_category"]
        product_price = product_details["product_price"]
        product_quantity = product_details["product_quantity"]

        if not self.client.is_connected:
            self.view.show_connection_error_popup()
            return

        for i in range(product_quantity):
            self.client.insert("inventory", product_name, product_desc, product_category, product_price)
        
        self.view.update_inventory_listbox(self.fetch_inventory())

    def delete_button_pressed(self):
        if not self.view.selected_item_id:
            print("No item has been selected.")
            return
        
        self.client.delete("inventory", self.view.selected_item_id)
        self.view.selected_item_id = None
        self.view.update_inventory_listbox(self.fetch_inventory())