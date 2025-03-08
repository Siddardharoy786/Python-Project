# 1. Define a static variable and access that through a class

class Car:
    name = "BMW"
    def __init__(self):
        pass
print(Car.name)

# 2. Define a static variable and access that through a instance

class Car:
    name = "BMW"
    def __init__(self):
        pass
car1  = Car() 
print(car1.name)

# 3. Define a static variable and change within the instance

class Car:
    car_name = "BMW"
    def __init__(self):
        pass
    def update_car_name(self,name):
        self.car_name = name 
        return self.car_name
car1 = Car()
print(car1.car_name)
name = input()
print(car1.update_car_name(name))

# 4. Define a static variable and change within the class

class Car:
    car_name = "BMW"
    def update(name):
        car_name = name 
        return car_name
print(Car.car_name)
print(Car.update(name="Hundai"))

