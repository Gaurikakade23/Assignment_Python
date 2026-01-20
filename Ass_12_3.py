def Calculate(No1,No2):
    add=No1+No2
    
    print("Addition is :",add)
    sub=No1-No2

    print("Subtraction is :",sub)
    mul=No1*No2
    
    print("Multiplication is :",mul)
    
    div=No1/No2
    print("Division is :",div)
    
def main():
    a=int(input("Enter Number: "))
    b=int(input("Enter Number: "))
    Calculate(a,b)

if __name__ == "__main__":
    main()    