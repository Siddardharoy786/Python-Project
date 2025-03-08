class FirstSchool:


    def __init__(self,var1,var2):
        self.var1 = var1
        self.__var2 = var2

    def PublicDisplay(self):
        print(self.var1)

    def __PrivateDisplay(self):
        print(self.__var2)

    def accessPrivate(self):
        self.__PrivateDisplay()

class SecondSchool(FirstSchool):
    def __init__(self,var1,var2):
        FirstSchool.__init__(self,var1,var2)

obj = SecondSchool("I am Public","I am Private")
obj.PublicDisplay()
obj.accessPrivate()

