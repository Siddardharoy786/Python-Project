name=input("Enter Your Name: ")
print(name)

a='''hi
hello 
hi
'''
print(a)

a=12
b=True
c="Leela"
d=12.4
print("a",type(a))
print("b",type(b))
print("c",type(c))
print("d",type(d))

a=10
def variable():
    a=20
    print(f"local variable{a}")
variable()
print(a)