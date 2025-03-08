def arithmetic(a,symbol,b):
    if symbol=="+":
        return a+b
    elif symbol == "-":
        return a-b
    elif symbol == "*":
        return a*b
    else:
        return a/b
a,symbol,b=map(str,input().split())
a=int(a)
b=int(b)
print(arithmetic(a,symbol,b))

class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1
        return self.value

    def decrement(self):
        self.value -= 1
        return self.value

# Example Usage
counter = Counter(int(input()))
print("Increment",counter.increment())  
print("Decrement",counter.decrement())  

a=int(input("Enter your first number"))
b=int(input("Enter your second number"))
if a==b:
    print("Two numbers are equal")
else:
    print("Two numbers are not equal")
    
a,b=map(int, input().split())
if a<b:
    print("a < b")
elif a>b:
    print("a > b")
else:
    print("a == b")
    
a=list(map(int, input("Enter list of number with spaces").split()))
print("Large number",max(a))
print("Smaller number",min(a))