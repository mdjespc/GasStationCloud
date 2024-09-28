class Item:
    '''
    Some suggested attributes/data that each Item node should contain:

    -id
    -product_name
    -product_desc
    -category
    -price
    -timestamp (tentative)
    '''
    def __init__(self):
        self._id = hash(self)
        self._values = {
            "name" : "",
            "desc" : "",
            "category" : "",
            "price" : ""
        }

    @property
    def id(self):
        return self._id
    
    @property
    def values(self):
        return self._values
    
    @id.setter
    def id(self, id):
        self._id = id

    @values.setter
    def values(self, values):
        self._values = values

    def __str__(self):
        return f'''\n
        Item Object at {hex(id(self))}
        Values: {self._values}
        ID: {self._id}\n
        '''