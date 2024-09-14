from src.item import Item 
from src.client import Client

if __name__ == "__main__":
    #Lines of code testing go here
    item = Item()
    item.values = {
        "name" : "S Tyak BJerk",
        "desc" : "Teriyaki Beef Jerky (Small)",
        "category" : "Snacks",
        "price" : "6.99"
    }

    print(item)

    print("Testing connection to database...")
    client = Client()
    client.connect_to_database()
    print(client.fetch_all("inventory"))
    client.close_connection()
