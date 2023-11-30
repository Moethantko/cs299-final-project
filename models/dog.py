class Dog:
    def __init__(self, name, breed, age, customerID):
        self._name = name
        self._breed = breed
        self._age = age
        self._customerID = customerID
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, new_breed):
        self._breed = new_breed

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def customerID(self):
        return self._customerID
    
    @customerID.setter
    def customerID(self, new_customerID):
        self._customerID = new_customerID
    

    