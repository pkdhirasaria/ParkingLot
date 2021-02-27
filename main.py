from Parking import SlotStatus, Parking
import argparse
from tabulate import tabulate


def executeCommand(parkingLot, command):
    if command.startswith('Create_parking_lot'):
        n = int(command.split(' ')[1])
        res = parkingLot.createLot(n)
        print('Created a parking lot with ' + str(res) + ' slots')

    elif command.startswith('Park'):
        regno = command.split(' ')[1]
        age = command.split(' ')[3]
        res = parkingLot.parkCar(regno, age)
        if res == SlotStatus.NoSlot:
            print("Sorry, parking lot is full")
        else:
            print('Allocated slot number: ' + str(res) + ' for car ' + str(regno))

    elif command.startswith('Leave'):
        leave_slotid = int(command.split(' ')[1])
        info = parkingLot.leave(leave_slotid)
        if info != SlotStatus.Empty:
            print('Slot number ' + str(leave_slotid) + ' vacated, the car with vehicle registration number ' + str(
                info.registration_number)
                  + ' left the space, the driver age was ' + str(info.age))
        else:
            print('Slot Number ' + str(leave_slotid) + ' is free.')
    elif command.startswith('Status'):
        parkingLot.ParkingLotInformation()

    elif command.startswith('Slot_number_for_car_with_number'):
        regisNumber = command.split(' ')[1]
        slotNumber = parkingLot.getSlotNumberFromRegistrationNumber(regisNumber)
        print('Slot Number for car ' + str(regisNumber) + ' is ' + str(slotNumber))

    elif command.startswith('Slot_numbers_for_driver_of_age'):
        age = command.split(' ')[1]
        slotnos = parkingLot.getSlotNumbersFromDriverAge(age)
        print(', '.join(slotnos))

    elif command.startswith('Vehicle_registration_number_for_driver_of_age'):
        age = command.split(' ')[1]
        regisnumbers = parkingLot.getRegistrationNumberFromDriverAge(age)
        print('Vehicle registration number for driver with age ' + str(age) + ' : ', end=" ")
        print(', '.join(regisnumbers))
    elif command.startswith('Exit'):
        exit(0)


def main():
    parkingLot = Parking()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
    args = parser.parse_args()

    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip('\n')
                executeCommand(parkingLot, line)
    else:
        while True:
            line = input("$ ")
            executeCommand(parkingLot, line)


if __name__ == '__main__':
    main()
