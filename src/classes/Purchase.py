class Purchase():

    # TODO: make list of all purchases

    def __init__(self, person, makeup_item, date):
        self.person = person
        self.makeup_item = makeup_item
        self.date = date

        # TODO: construct purchase object as SSOT

    # TODO: make property for person (must be instance of People class)
    # TODO: make property for makeup_item (must be instance of Makeup class)

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date

    # TODO: calculate most popular makeup brand

    def __str__(self):
        return f"Purchaser: {self.person}\nMakeup Item: {self.makeup_item}\nDate: {self.date}"