
class ClassOne:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Hello from ClassOne, Name: {self.name}")
class ClassTwo:
    def __init__(self, age):
        self.age = age

    def show(self):
        print(f"Hello from ClassTwo, Age: {self.age}")
# Creating objects for both classes
obj1 = ClassOne("Leela")
obj2 = ClassTwo(23)

# Calling methodspa
obj1.display()
obj2.show()

from class1 import ClassOne
from class2 import ClassTwo