class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.Radius = radius
        self.Area = 0.0
        self.Circumference = 0.0

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius ** 2

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius:", self.Radius)
        print("Area of Circle:", self.Area)
        print("Circumference of Circle:", self.Circumference)



cobj = Circle(5)


cobj.CalculateArea()
cobj.CalculateCircumference()

cobj.Display()
