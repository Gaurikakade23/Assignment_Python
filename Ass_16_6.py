def CheckNum(No):
    if No>0:
        print("Positive Number")
    elif No<0:
        print("Negative Number")
    else:
        print("Zero")

a= int(input("Enter Number: "))
CheckNum(a)                