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

        #Bind command
        self.view.bind_commands()

        #Insert items into listbox
        items = self.fetch_inventory()
        self.view.update_inventory_listbox(items)

        self.view.run()
    

    def fetch_inventory(self):
        items = self.client.fetch_all("inventory")

        #Process the fetched items into a list of strings
        items = [",".join([str(value) for value in item[1:]]) for item in items]
        print(items)
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

        if not self.client.is_connected:
            self.view.show_connection_error_popup()
            return

        self.client.insert("inventory", product_name, product_desc, product_category, product_price)
        