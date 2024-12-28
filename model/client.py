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
        

    def search_by(self, table_name, search_filter, search_key):
        if not self.cursor:
            raise ConnectionError("Database connection has not yet been established.")
        
        try:
            query = f'''
                    SELECT *
                    FROM {table_name}
                    WHERE {search_filter} = {search_key}
                    '''
            self.cursor.execute(query)
            return self.cursor.fetchall()

        except mysql.connector.Error as err:
            raise ConnectionError("Error retrieving table data:", err)


    def insert(self, table_name, *values):
        if not self.cursor:
            raise ConnectionError("Database connection has not yet been established.")
        
        try:
            query = f'''
                    INSERT INTO {table_name}
                    VALUES (NULL,{",".join(["%s" for value in values])})
                    '''
            #Execute the SQL query with new entry information
            self.cursor.execute(query, values)
            self.db.commit()
            print(f"Data row inserted successfully into {table_name}")

        except mysql.connector.Error as err:
            raise ConnectionError("Error inserting data into table:", err)
        


    def delete(self, table_name, id):
        if not self.cursor:
            raise ConnectionError("Database connection has not yet been established.")
        
        try:
            query= f'''
                    DELETE FROM {table_name}
                    WHERE id = %s
                    '''
            self.cursor.execute(query, (id,))
            self.db.commit()
            print(f"Data row deleted from {table_name} successfully.")
        except mysql.connector.Error as err:
            raise ConnectionError("Error deleting data from table:", err)
    
    def update(self, table_name, id, *values):
        if not self.cursor:
            raise ConnectionError("Database connection has not yet been established.")
        try:
            query = f'''
                    REPLACE INTO {table_name}
                    VALUES (%s,{",".join(["%s" for value in values])})
                    '''
            self.cursor.execute(query, (id, *values))
            self.db.commit()
            print(f"Data row updated in {table_name} successfully.")
        except mysql.connector.Error as err:
            raise ConnectionError("Error updating data row:", err)
        