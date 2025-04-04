
class Vehicle: # This shows the class for the Vehicle
    def __init__(self, vehicle_type):
        self.vehicle_type


class Automobile(Vehicle):# This shows the class for the Automobile which derive inherits from Vehicle class
    def __init__(self, year, make, model,doors, roof):
        super().__init__("Automobile")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Create an Automobile object
car = Automobile(year, make, model, doors, roof)

#User Input
year = input("Enter the year of the automobile:")
make = input("Enter the make of the automobile:")
model = input("Enter the model of the automobile:")
doors = input("Enter the door type of the automobile (ex. 2-doors, 4-doors): ")
roof = input("Enter the roof type of the Automobile (ex. sunroof, convertible):")

def display_car(car):#function that displays the information of the automobile
    print(f"Vehicle Type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Doors: {car.doors}")
    print(f"Roof: {car.roof}")


    