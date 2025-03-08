# 1. Write two methods with the same name but different number of parameters of same type and call the methods

class Student:
    def __init__(self):
        pass

    def method1(self, a=0, b=0, c=None):
        if c is None:
            print("I'm in method1_1")
        else:
            print("I'm in method1_2")

student1 = Student()
student1.method1()          
student1.method1(1, 2)      
student1.method1(1, 2, 3)   

# 2. Write two methods with the same name but different number of parameters of different data type and call the methods


class Student:
    def __init__(self):
        pass

    def method1(self, a=0, b=None, c=None):
        if isinstance(b, int) and c is None:
            print("I'm in method1_1 (integer parameter)")
        elif isinstance(b, str) and isinstance(c, float):
            print("I'm in method1_2 (string and float parameters)")
        else:
            print("Invalid input")

student1 = Student()
student1.method1(10, 20)        
student1.method1(10, "NUNE", 22.4)  

# 3. Write two methods with the same name and same number of parameters of same type

class Student:
    def __init__(self):
        pass

    def method1(self, a=0, b=0):
        if a == 0 and b == 0:
            print("I'm in method1_1 (Default parameters)")
        else:
            print("I'm in method1_2 (Custom parameters)")

student1 = Student()
student1.method1()         
student1.method1(5, 10)    

