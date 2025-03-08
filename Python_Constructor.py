# 1. Write a class with a default constructor, one argument constructor and two argumentconstructors. Instantiate the class to call all the constructors of that class from a main class
# 2. Call the constructors(both default and argument constructors) of super class from a child class
# 3. Apply private, public, protected and default access modifiers to the constructor
class Super:
    def __init__(slef,a1=0,a2=0):
        if a1==0 and a2==0:
            print("No parameters was passed")
        elif a1>0 or a2>0:
            print("One parameter is passed")
        else:
            print("Two parameters are passed")

    def _ProtectedClass(self):
        print("Protected Class called")

    def __PrivateClass(self):
        print("Private Class was called")
if __name__ == "__main__":
    obj = Super()
    obj = Super(21)
    obj = Super(21,21)
print()
obj = Super()
obj = Super(21)
obj = Super(21,21)

print()

obj = Super()
obj._ProtectedClass()

# 4. Write a program which illustrates the concept of attributes of a constructor.

class Super:
    def __init__(self,name,RollNo):
        self.name = name
        self.RollNo = RollNo

    def display(self):
        print(f"Student name {self.name} and Roll Number {self.RollNo}")

if __name__ == "__main__" :
    student1 = Super("leela",21)
    student1.display()
    
    print(student1.name)
    print(student1.RollNo)

student1.Group = "DSSTCS"
print(student1.Group)