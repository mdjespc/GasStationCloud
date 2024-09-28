from model.item import Item 
from model.client import Client

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
    client.insert("inventory", '20', 'Air Freshener', 'Mint-Scented Air Freshener', 'Home', 5.99)
    print(client.fetch_all("inventory"))
    client.delete("inventory", "20")

    print(client.search_by("inventory", "id", "19"))
    client.close_connection()
