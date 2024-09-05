# Write a Python program with a base class Vehicle that has a constructor initializing brand and a method get_brand(). Derive a class Car from Vehicle, and in its constructor, add model. Write a method get_car_details() to display both brand and model.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
    def get_brand(self):
        return self.brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def get_car_details(self):
      return self.brand + " " + self.model

car = Car("Toyota", "Camry")
print(car.get_car_details())
