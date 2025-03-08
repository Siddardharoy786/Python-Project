class A:
    def __init__(self):
        print("In class A")
    def one(self,call):
        print("I am in class in A")

class B(A):
    def __init__(self):
        print("In class B")
    def two(self):
        print("I am in class in B")

class C(B):
    def __init__(self):
        print("In class C")
    def one(self,name):
        print("I am in class in C")

a=A()
b=B()
c=C()
a.one("leela")