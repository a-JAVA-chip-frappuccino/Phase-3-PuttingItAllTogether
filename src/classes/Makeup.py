class Makeup():

    all = []

    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

        Makeup.all.append(self)

        self._owners = []
        self._purchases = []

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, new_brand):
        # if isinstance(new_brand, str):
        if type(new_brand) == str:
            self._brand = new_brand
        else:
            raise Exception("Brand must be a string!")
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, new_type):
        # if isinstance(new_type, str):
        if type(new_type) == str:
            self._type = new_type
        else:
            raise Exception("Type must be a string!")
        
    # example of how to add to list with methods
    def owners(self):
        return self._owners
        
    def add_owner(self, new_owner):
        from People import People
        if isinstance(new_owner, People):
            self._owners.append(new_owner)
        else:
            raise Exception("Owner must be an instance of Owner class!")
        
    owners = property(owners, add_owner)
        
    @classmethod
    def get_unique_types(cls):
        '''
        unique_types = []

        for makeup in cls.all:
            if makeup.type not in unique_types:
                unique_types.append(makeup.type)

        return unique_types
        '''

        return list(set([makeup.type for makeup in cls.all]))
        
    def __repr__(self):
        return f"Brand: {self.brand} Type: {self.type}"