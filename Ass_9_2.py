def ChkGreater(No1,No2):

    if(No1>No2):
        print(No1,"is greater number.")
    else:
        print(No2,"is grater number.")    

def main():

    a= int(input("Enter the first number: "))
    b= int(input("Enter the second number: "))
    ChkGreater(a,b)

if __name__ == "__main__":
    main()    