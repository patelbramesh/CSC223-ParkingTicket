"""
File Name: ParkedCar.py
Description:
Defines the ParkedCar class, which represents a vehicle parked at a meter.
Stores identifying information and minutes parked.
"""

class ParkedCar:
    def __init__(self, make, model, color, license_number, minutes_parked=60):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self._minutes_parked = 60
        self.minutes_parked = minutes_parked

    @property
    def minutes_parked(self):
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, minutes):
        if minutes <= 0:
            raise ValueError("Minutes parked must be positive.")
        self._minutes_parked = minutes

    def __str__(self):
        return f"{self.make} {self.model}, {self.color}, {self.license_number}"