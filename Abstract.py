# Create an abstract class with abstract and non-abstract methods.

from abc import ABC, abstractmethod 

class Vehicle:
    def start():
        pass

    def ready(self,):
        print("Vehicle is ready to start")

# Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods

class Car(Vehicle):
    def start(self):
        print("Vehicle started")
car1 = Car()
car1.ready()

# Create an instance for the child class in child class and call abstract methods

car1.start()

# 4. Create an instance for the child class in child class and call non-abstract methods

car1.ready()
