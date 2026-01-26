from Arithematic_17 import *

def main():
    a= int(input("Enter first Number: "))
    b= int(input("Enter Second Number: "))
    Addition = Add(a,b)
    print("Addition: ",Addition)
    Subtraction = Sub(a,b)
    print("Subtraction: ",Subtraction)
    Multiplication = Mul(a,b)
    print("Multiplication: ",Multiplication)
    Division = Div(a,b)
    print("Division: ",Division)
if __name__ == "__main__":
    main()    