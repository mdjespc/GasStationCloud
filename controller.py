from model.client import Client
from model.item import Item
from gui import ProjectWindow


class Controller(object):
    def __init__(self):
        self.view = ProjectWindow()
        
        #Add callbacks
        self.view.add_callbacks("Insert", self.insert_button_pressed)


        #Bind command
        self.view.bind_commands()

        self.view.run()
    
    def insert_button_pressed(self):
        def get_product_details():
            #Once the window is closed, grab all values entered and submit to client
            product_details = self.view.product_details
            print(product_details)

        self.view._show_insert_window(get_product_details)
        
        
        
        