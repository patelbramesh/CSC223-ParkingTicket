"""
File Name: ParkingTicket.py
Description:
Defines the ParkingTicket class, which represents a citation issued
for parking violations and calculates fines.
"""

import math

class ParkingTicket:

    def __init__(self, car, officer, illegal_minutes):
        self.car = car
        self.officer_name = officer.name
        self.badge_number = officer.badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        hours = math.ceil(self.illegal_minutes / 60)
        return 25 + (hours - 1) * 10

    def __str__(self):
        return (
            f"\n--- Parking Ticket ---\n"
            f"Car: {self.car}\n"
            f"Illegal Minutes: {self.illegal_minutes}\n"
            f"Fine: ${self.fine:.2f}\n"
            f"Issued by Officer {self.officer_name}, Badge {self.badge_number}\n"
        )