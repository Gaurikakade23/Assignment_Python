MaxNum= lambda No1,No2 : No1>No2
def main():
    
    n1=int(input("Enter first number: "))
    n2=int(input("Enter first number: "))
    if MaxNum(n1,n2):
        print("Maximum number is: ",n1)
    else:
        print("Maximum number is: ",n2)    

if __name__ == "__main__":
    main()    