class Customer:
    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName = lastName
    

    @property
    def fullName(self):
        return self._firstName + " " + self._lastName
    

    