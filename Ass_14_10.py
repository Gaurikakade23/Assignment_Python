Largest_No = lambda No1,No2,No3 : No1 if (No1 >= No2 and No1 >= No3) else (No2 if No2 >= No3 else No3)
def main():
    a= int(input("enter first number: "))
    b= int(input("enter second number: "))
    c= int(input("enter third number: "))
    ret= Largest_No(a,b,c)
    print("Largest No is: ",ret)
if __name__ == "__main__":
    main()    