class Service:
    def __init__(self, type, cost, dogID):
        self._type = type
        self._cost = cost
        self._dogID = dogID
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, new_type):
        self._type = new_type

    @property
    def cost(self):
        return self._cost
    
    @cost.setter
    def cost(self, new_cost):
        self._cost = new_cost

    @property
    def dogID(self):
        return self._dogID
    
    @dogID.setter
    def dogID(self, new_dogID):
        self._dogID = new_dogID
    

    