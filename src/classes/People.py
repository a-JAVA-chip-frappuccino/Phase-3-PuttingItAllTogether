class People():

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self._makeup_items = []
        self._purchases = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, 'name') and type(new_name) == str:
            self._name = new_name
        else:
            raise Exception("Name must be a string and cannot be mutated!")
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if type(new_age) == int and new_age > 12:
            self._age = new_age
        else:
            raise Exception("Age must be an integer greater than 12!")
        
    def __repr__(self):
        return f"Name: {self.name}"