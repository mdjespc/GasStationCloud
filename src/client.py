import mysql.connector


class Client:
    def __init__(self):
        self.db = None
        self.cursor = None
        self.is_connected = False

    def connect_to_database(self):
        try:
            self.db = mysql.connector.connect(host = "localhost",
                                              user = "mdj_p",
                                              password = "",
                                              database = "gasstationcloud"

            ) 
            self.cursor = self.db.cursor()

            self.is_connected = True
            print("Connection to the database successful.")

        except mysql.connector.Error as err:
            self.is_connected = False
            print("Error connecting to database:", err)

    def close_connection(self):
        if self.db:
            self.db.close()
            self.is_connected = False
            print("Database connection closed.")

    
    #Retrieves all data entries in the given table and returns it as a two-dimensional list.
    def fetch_all(self, table_name):
        if not self.cursor:
            raise ConnectionError("Database connection has not yet been established.")
        
        try:
            query = f'''
                    SELECT *
                    FROM {table_name}
                    '''
            self.cursor.execute(query)
            return self.cursor.fetchall()

        except mysql.connector.Error as err:
            raise ConnectionError("Error retrieving table data:", err)