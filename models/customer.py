class Customer:
    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName = lastName
    

    @property
    def firstName(self):
        return self._firstName
    
    @property
    def lastName(self):
        return self._lastName
    
    @property
    def fullName(self):
        return self._firstName + " " + self._lastName
    

    