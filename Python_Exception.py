# 1. Write a program to generate Arithmetic Exception without exception handling

a=10/0
print(a)

# 2. Handle the Arithmetic exception using try-catch block

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught an Arithmetic Exception:", e)


# 3. Write a method which throws exception, Call that method in main class without try block

def throw_exception():
    raise ValueError("This method throws an exception!")

# Calling the method without handling the exception
throw_exception()

# 4. Write a program with multiple catch blocks

try:
    x = int(input("Enter a number: "))  # Could cause ValueError
    result = 10 / x  # Could cause ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
except Exception as e:
    print("Some other error occurred:", e)
    
# 5. Write a program to throw exception with your own message

def check_value(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed!")

check_value(-5)

# 6. Write a program to create your own exception

class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

raise MyCustomException("This is my own custom exception!")

# 7. Write a program with finally block

try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This is the finally block. It always executes!")

# 8. Write a program to generate Arithmetic Exception

result = 10 / 0  

# 9. Write a program to generate FileNotFoundException

try:
    f = open("non_existent_file.txt", "r") 
except FileNotFoundError as e:
    print("Caught FileNotFoundException:", e)

# 10. Write a program to generate ClassNotFoundException

try:
    import non_existent_module 
except ImportError as e:
    print("Caught ClassNotFoundException :", e)

# 11. Write a program to generate IOException

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except OSError as e:
    print("Caught IOException :", e)

# 12. Write a program to generate NoSuchFieldException

class Demo:
    def __init__(self):
        self.value = 10
obj = Demo()
try:
    print(obj.non_existent_field) 
except AttributeError as e:
    print("Caught NoSuchFieldException :", e)
