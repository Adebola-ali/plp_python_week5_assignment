# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

# Derived Class: Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

# Derived Class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

# Derived Class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing on water 🛥️"

# Derived Class: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling on a path 🚴"

# Polymorphism in action
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        print(f"{vehicle.__class__.__name__}: {vehicle.move()}")

# Create instances
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Test the move() method for each vehicle
vehicle_list = [car, plane, boat, bicycle]
demonstrate_movement(vehicle_list)
