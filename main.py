"""
File Name: main.py
Author: Bramesh Patel
Course: CSC 223
Project: Parking Ticket Simulation
Date: March 13, 2026

Description:
This program simulates a parking enforcement system using object-oriented
programming principles. A PoliceOfficer inspects parked cars and issues
ParkingTicket objects when violations occur. The project demonstrates
encapsulation, aggregation, and composition across multiple classes.
"""

from ParkedCar import ParkedCar
from ParkingMeter import ParkingMeter
from PoliceOfficer import PoliceOfficer


def run_scenario(car, meter, officer):
    ticket = officer.inspect_car(car, meter)

    if ticket:
        print(ticket)
    else:
        print(f"{car} is legally parked. No ticket issued.\n")


def main():

    # -----------------------------
    # Scenario 1 – Legally Parked
    # -----------------------------
    car1 = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter1 = ParkingMeter(40)
    officer1 = PoliceOfficer("John Doe", "5678")

    run_scenario(car1, meter1, officer1)

    # -----------------------------
    # Scenario 2 – Minor Violation
    # -----------------------------
    car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter2 = ParkingMeter(60)
    officer2 = PoliceOfficer("Jane Smith", "1234")

    run_scenario(car2, meter2, officer2)

    # -----------------------------
    # Scenario 3 – Multiple Hours
    # -----------------------------
    car3 = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter3 = ParkingMeter(60)
    officer3 = PoliceOfficer("James Brown", "4321")

    run_scenario(car3, meter3, officer3)

    # -----------------------------
    # Scenario 4 – Multiple Cars
    # -----------------------------
    officer4 = PoliceOfficer("Sarah Green", "9999")

    cars = [
        (ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)),
        (ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)),
        (ParkedCar("BMW", "X5", "Black", "BMW999", 500), ParkingMeter(60)),
        (ParkedCar("Mazda", "3", "Blue", "MAZ321", 45), ParkingMeter(60)),
    ]

    for car, meter in cars:
        run_scenario(car, meter, officer4)


if __name__ == "__main__":
    main()