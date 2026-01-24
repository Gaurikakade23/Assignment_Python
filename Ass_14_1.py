Square = lambda No:(No**2)
def main():
    Value = 0

    print("Enter number: ")
    Value= int(input())

    Ret = Square(Value)
    print("Square is: ",Ret)
if __name__ == "__main__":
    main()    