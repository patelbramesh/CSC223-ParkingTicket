"""
File Name: ParkingMeter.py
Description:
Defines the ParkingMeter class, which represents purchased parking time.
"""

class ParkingMeter:
    def __init__(self, minutes_purchased=60):
        self._minutes_purchased = 60
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self):
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, minutes):
        if minutes <= 0:
            raise ValueError("Minutes purchased must be positive.")
        self._minutes_purchased = minutes