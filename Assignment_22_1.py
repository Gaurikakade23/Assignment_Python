class Demo:
    Value=10
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    def fun(self):
        print("Inside fun")
        print("Value of no1: ",self.no1)
        print("Value of no2: ",self.no2)
    def gun(self):
        print("Inside gun")
        print("Value of no1: ",self.no1)
        print("Value of no2: ",self.no2)

obj1 =Demo(11,21)
obj2 =Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()