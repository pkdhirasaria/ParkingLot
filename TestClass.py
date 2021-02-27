import unittest
from Parking import Parking
from Parking import SlotStatus


class TestParking(unittest.TestCase):

    def test_create_parking_lot(self):
        parkingLot = Parking()
        res = parkingLot.createLot(6)
        self.assertEqual(6, res)

    def test_park(self):
        parkingLot = Parking()
        res = parkingLot.createLot(6)
        res = parkingLot.parkCar("KA-01-HH-1234", 23)
        self.assertNotEqual(SlotStatus.NoSlot, res)

    def test_leave(self):
        parkingLot = Parking()
        res = parkingLot.createLot(6)
        res = parkingLot.parkCar("KA-01-HH-1234", 32)
        res = parkingLot.leave(1)
        self.assertEqual(32, res.age)
        self.assertEqual("KA-01-HH-1234", res.registration_number)

    def test_getRegistrationNumberFromSlotNumber(self):
        parkingLot = Parking()
        res = parkingLot.createLot(6)
        res = parkingLot.parkCar("KA-01-HH-1234", 23)
        res = parkingLot.parkCar("KA-01-HH-9999", 32)
        regnos = parkingLot.getRegistrationNumberFromSlotNumber(1)
        self.assertEqual("KA-01-HH-1234", regnos)
        self.assertFalse("KA-01-HH-9999", regnos)

    def test_getSlotNumberFromRegistrationNumber(self):
        parkingLot = Parking()
        res = parkingLot.createLot(6)
        res = parkingLot.parkCar("KA-01-HH-1234", 23)
        res = parkingLot.parkCar("KA-01-HH-9999", 32)
        slotno = parkingLot.getSlotNumberFromRegistrationNumber("KA-01-HH-9999")
        self.assertEqual(2, slotno)

    def test_getSlotNumbersFromDriverAge(self):
        parkingLot = Parking()
        res = parkingLot.createLot(6)
        res = parkingLot.parkCar("KA-01-HH-1234", 23)
        res = parkingLot.parkCar("KA-01-HH-9999", 32)
        slotnos = parkingLot.getSlotNumbersFromDriverAge(23)
        self.assertIn("1", slotnos)
        self.assertNotIn("2", slotnos)

    def test_getRegistrationNumberFromDriverAge(self):
        parkingLot = Parking()
        res = parkingLot.createLot(6)
        res = parkingLot.parkCar("KA-01-HH-1234", 23)
        res = parkingLot.parkCar("KA-01-HH-9999", 32)
        regis = parkingLot.getRegistrationNumberFromDriverAge(32)
        self.assertIn("KA-01-HH-9999", regis)


if __name__ == '__main__':
    unittest.main()
