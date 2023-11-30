class Service:
    def __init__(self, type, cost, dogID, completed):
        self._type = type
        self._cost = cost
        self._dogID = dogID
        self._completed = completed
    
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

    @property
    def completed(self):
        return bool(self._completed)
    
    @completed.setter
    def completed(self, new_complete_status):
        self._completed = new_complete_status
    

    