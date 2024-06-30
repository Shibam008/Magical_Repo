
#* Whenever we use double underScore, means we are making that private

#* __init__ is known as constructor

#* when we use @staticmethod we need not to use (self) parameter.

class Car:
   def __init__(self, brand, model):
      self.__brand = brand
      self.model = model
   
   def get_brand(self):
      return self.__brand + " !"
   
   def fullName(self):
      return f"{self.__brand} {self.model}"
   
   def fuel_type(self): #polymorphism
      return "petrol or diesel"
   
   @staticmethod #decorators
   def get_description():
      return "Car means to transport"
   
   
# Inheritence
class ElectricCar(Car):
   def __init__(self, brand, model, battery_size):
      super().__init__(brand, model)
      self.battery_size = battery_size
   
   def fuel_type(self): #polymorphism
      return "Electric charge"


# my_car = Car("Toyota", "corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())


# # Inheritence
# my_EV = ElectricCar("Tesla", "Model-S", "85kwh")
# print(my_EV.brand)
# print(my_EV.fullName())


# # Encapsulation
# my_EV = ElectricCar("Tesla", "Model-S", "85kwh")
# print(my_EV.get_brand())


# # Polymorphism
# new_ev = ElectricCar("Tesla", "Model-k", "95kwh")
# print(new_ev.fuel_type())

# new_car = Car("Tata", "Safari")
# print(new_car.fuel_type())


# # Static method / decorators
# new_car = Car("Tata", "Safari")
# print(Car.get_description())


# my_EV = ElectricCar("Tesla", "Model-S", "85kwh")
# print(isinstance(my_EV, Car))
# print(isinstance(my_EV, ElectricCar))





# ----------- Multiple Inheritance -----------
class Battery:
   def battery_info(self):
      return "This is battery"

class Engine:
   def engine_info(self):
      return "This is engine"

class NewElectricCar(Battery, Engine, Car): # multiple inheritance
   pass

my_new_car = NewElectricCar("Tata", "Thar")
print(my_new_car.battery_info())
print(my_new_car.engine_info())