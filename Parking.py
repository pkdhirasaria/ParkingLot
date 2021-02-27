from Car import Car
import enum
from tabulate import tabulate


class SlotStatus(enum.Enum):
    NoSlot = 1
    Empty = 2
    Left = 3


class Parking:

    def __init__(self):
        self.capacity = 0
        self.slotId = 0
        self.occupiedSlot = 0

    def createLot(self, capacity):
        self.slot = [SlotStatus.Empty] * capacity
        self.capacity = capacity
        return self.capacity

    def getEmptySlot(self):
        for idx in range(self.capacity):
            if self.slot[idx] == SlotStatus.Empty:
                return idx

    def parkCar(self, regis, age):
        if self.occupiedSlot < self.capacity:
            slotId = self.getEmptySlot()
            self.slot[slotId] = Car(age, regis)
            self.occupiedSlot = self.occupiedSlot + 1
            self.ParkingLotInformation()
            return slotId + 1  # As index is Zero Based so returning +1
        else:
            return SlotStatus.NoSlot  # Indicating no slot is available

    def leave(self, slotID):
        if self.slot[slotID - 1] != SlotStatus.Empty:
            info = self.slot[slotID-1]
            self.slot[slotID - 1] = SlotStatus.Empty
            self.occupiedSlot = self.occupiedSlot - 1
            return info
        return SlotStatus.Empty

    def getSlotNumberFromRegistrationNumber(self, registNumber):
        for idx, car in enumerate(self.slot):
            if car != SlotStatus.Empty and car.registration_number == registNumber:
                return idx + 1
        return SlotStatus.Empty

    def getRegistrationNumberFromSlotNumber(self, slotID):
        if self.slot[slotID - 1] != SlotStatus.Empty:
            return self.slot[slotID - 1].registration_number
        return SlotStatus.Empty

    def getSlotNumbersFromDriverAge(self, age):
        slot = []
        for idx, car in enumerate(self.slot):
            if self.slot[idx] != SlotStatus.Empty and car.age == age:
                slot.append(str(idx + 1))
        return slot

    def getRegistrationNumberFromDriverAge(self, age):
        regis = []
        for idx, car in enumerate(self.slot):
            if self.slot[idx] != SlotStatus.Empty and car.age == age:
                regis.append(car.registration_number)
        return regis

    def ParkingLotInformation(self):
        # print("{:<8} {:<15} {:<10}".format('Slot No', 'Registration No', 'Age')
        data = []
        print()
        for slotID, car in enumerate(self.slot):
            if car != SlotStatus.Empty:
                data.append([slotID + 1, car.registration_number, car.age])
                # print("{:<8} {:<15} {:<10}".format(slotID + 1, car.regis, car.age))
        print(tabulate(data, headers=['Slot No', 'Registration No', 'Age']))
        print()
