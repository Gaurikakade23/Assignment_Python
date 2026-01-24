Cube = lambda No:(No**3)
def main():
    Value = 0

    print("Enter number: ")
    Value= int(input())

    Ret = Cube(Value)
    print("Cube is: ",Ret)

if __name__ == "__main__":
    main()    