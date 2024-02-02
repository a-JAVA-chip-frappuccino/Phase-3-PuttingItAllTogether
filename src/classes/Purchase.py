class Purchase():

    all = []

    def __init__(self, makeup_item, person, date):
        self.makeup_item = makeup_item
        self.person = person
        self.date = date

        # add links for People object
        self.person._makeup_items.append(self.makeup_item)
        self.person._purchases.append(self)

        # add links for Makeup object
        self.makeup_item._owners.append(self.person)
        # self.makeup_item.add_owner(self.person) # adds using method
        self.makeup_item._purchases.append(self)

        Purchase.all.append(self)

    @property
    def makeup_item(self):
        return self._makeup_item
    
    @makeup_item.setter
    def makeup_item(self, new_makeup_item):
        from Makeup import Makeup
        if isinstance(new_makeup_item, Makeup):
            self._makeup_item = new_makeup_item
        else:
            raise Exception("Makeup item must be an instance of Makeup class!")
        
    @property
    def person(self):
        return self._person
    
    @person.setter
    def person(self, new_person):
        from People import People
        if isinstance(new_person, People):
            self._person = new_person
        else:
            raise Exception("Person must be an instance of People class!")
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, new_date):
        if type(new_date) == str:
            self._date = new_date
        else:
            raise Exception("Date must be a string!")
        
    def get_most_popular_brand():
        brand_freq = {}

        for purchase in Purchase.all:
            brand = purchase.makeup_item.brand

            if brand not in brand_freq:
                brand_freq[brand] = 1
            else:
                brand_freq[brand] += 1 # brand_freq[brand] = brand_freq[brand] + 1

        return max(brand_freq, key = lambda brand : brand_freq[brand])
        return max(brand_freq, key = brand_freq.get)