def CheckNum(No):
    if No% 2==0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    a= int(input("Enter Number: "))
    CheckNum(a)

if __name__=="__main__":
    main()                