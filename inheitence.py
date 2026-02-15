class Vehicle:
    def __init__(self, fare):
        self.fare = fare
class Bus(Vehicle):
    def total_fare(self):
        return self.fare + 10   # extra charge
b = Bus(100)
print(b.total_fare())
