"""
File Name: PoliceOfficer.py
Description:
Defines the PoliceOfficer class, responsible for inspecting cars and
issuing ParkingTicket objects when violations occur.
"""

from ParkingTicket import ParkingTicket

class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    def inspect_car(self, car, meter):
        if car.minutes_parked > meter.minutes_purchased:
            illegal_minutes = car.minutes_parked - meter.minutes_purchased
            return ParkingTicket(car, self, illegal_minutes)
        else:
            return None