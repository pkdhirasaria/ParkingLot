from Vehicle import Vehicle
from Driver import Driver


class Car(Vehicle, Driver):

    def __init__(self, age, resig):
        Vehicle.__init__(self, resig)
        Driver.__init__(self, age)