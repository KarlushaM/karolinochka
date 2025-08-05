class Vehicle:
   
    def __init__(self, max_speed, mileage):
        self._max_speed = max_speed
        self.__mileage = mileage
    
    def display_info(self):
        print("Max speed:", self._max_speed)
        print("Mileage:", self.__mileage)

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, passenger_capacity):
        super().__init__(max_speed, mileage)
        self.passenger_capacity = passenger_capacity

    def display_info(self):
        super().display_info()
        print("Passenger Capacity:", self.passenger_capacity)
    




bus = Bus(180, 10000, 50)
bus.display_info()